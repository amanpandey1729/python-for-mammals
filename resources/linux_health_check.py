#!/usr/bin/env python3
"""
Linux OS Health Check
=====================

A production-oriented, standard-library-only Linux health-check utility.

Outputs:
    - Human-readable text report
    - Optional HTML report
    - Optional JSON report
    - Optional email through the local sendmail-compatible MTA

Exit codes:
    0 = Healthy
    1 = Warning
    2 = Critical
    3 = Script/runtime error

Examples:
    python3 linux_health_check.py
    python3 linux_health_check.py --output-dir /var/log/os-health
    python3 linux_health_check.py --format text html json
    python3 linux_health_check.py --email dba-team@example.com
    python3 linux_health_check.py --brief
"""

from __future__ import annotations

import argparse
import html
import json
import os
import platform
import re
import shutil
import socket
import subprocess
import sys
import time
from dataclasses import asdict, dataclass
from datetime import datetime
from pathlib import Path
from typing import Any, Iterable


STATUS_RANK = {"OK": 0, "INFO": 0, "WARNING": 1, "CRITICAL": 2, "UNKNOWN": 1}
STATUS_ICON = {"OK": "[OK]", "INFO": "[INFO]", "WARNING": "[WARN]", "CRITICAL": "[CRIT]", "UNKNOWN": "[UNKN]"}


@dataclass
class CheckResult:
    section: str
    name: str
    status: str
    value: str
    detail: str = ""


@dataclass
class Thresholds:
    cpu_warning: float = 75.0
    cpu_critical: float = 90.0
    memory_warning: float = 80.0
    memory_critical: float = 90.0
    swap_warning: float = 40.0
    swap_critical: float = 70.0
    filesystem_warning: float = 80.0
    filesystem_critical: float = 90.0
    inode_warning: float = 80.0
    inode_critical: float = 90.0
    load_warning_per_cpu: float = 1.0
    load_critical_per_cpu: float = 1.5


def run_command(command: list[str], timeout: int = 10) -> tuple[int, str, str]:
    """Run a command safely without invoking a shell."""
    try:
        completed = subprocess.run(
            command,
            text=True,
            capture_output=True,
            timeout=timeout,
            check=False,
        )
        return completed.returncode, completed.stdout.strip(), completed.stderr.strip()
    except FileNotFoundError:
        return 127, "", f"Command not found: {command[0]}"
    except subprocess.TimeoutExpired:
        return 124, "", f"Command timed out after {timeout}s: {' '.join(command)}"
    except OSError as exc:
        return 126, "", str(exc)


def read_text(path: str | Path, default: str = "") -> str:
    try:
        return Path(path).read_text(encoding="utf-8", errors="replace").strip()
    except (OSError, PermissionError):
        return default


def human_bytes(value: int | float) -> str:
    units = ("B", "KiB", "MiB", "GiB", "TiB", "PiB")
    size = float(value)
    for unit in units:
        if abs(size) < 1024.0 or unit == units[-1]:
            return f"{size:.1f} {unit}"
        size /= 1024.0
    return f"{size:.1f} PiB"


def classify(value: float, warning: float, critical: float) -> str:
    if value >= critical:
        return "CRITICAL"
    if value >= warning:
        return "WARNING"
    return "OK"


def parse_os_release() -> str:
    candidates = ("/etc/os-release", "/usr/lib/os-release")
    for file_name in candidates:
        text = read_text(file_name)
        if not text:
            continue
        values: dict[str, str] = {}
        for line in text.splitlines():
            if "=" in line:
                key, value = line.split("=", 1)
                values[key] = value.strip().strip('"')
        return values.get("PRETTY_NAME") or values.get("NAME") or platform.platform()
    return platform.platform()


def hostname_fqdn() -> str:
    fqdn = socket.getfqdn()
    return fqdn if fqdn else platform.node()


def ip_addresses() -> list[str]:
    addresses: set[str] = set()

    if shutil.which("hostname"):
        code, stdout, _ = run_command(["hostname", "-I"])
        if code == 0:
            addresses.update(item for item in stdout.split() if item)

    if not addresses:
        try:
            for info in socket.getaddrinfo(hostname_fqdn(), None):
                address = info[4][0]
                if not address.startswith("127.") and address != "::1":
                    addresses.add(address)
        except socket.gaierror:
            pass

    return sorted(addresses)


def boot_time_and_uptime() -> tuple[str, str]:
    uptime_seconds = 0.0
    try:
        uptime_seconds = float(read_text("/proc/uptime").split()[0])
    except (ValueError, IndexError):
        pass

    boot_epoch = time.time() - uptime_seconds
    boot_time = datetime.fromtimestamp(boot_epoch).astimezone().strftime("%Y-%m-%d %H:%M:%S %Z")

    days, remainder = divmod(int(uptime_seconds), 86400)
    hours, remainder = divmod(remainder, 3600)
    minutes, seconds = divmod(remainder, 60)
    uptime = f"{days}d {hours}h {minutes}m {seconds}s"
    return boot_time, uptime


def virtualization() -> str:
    if shutil.which("systemd-detect-virt"):
        code, stdout, _ = run_command(["systemd-detect-virt"])
        if code == 0 and stdout and stdout != "none":
            return f"Virtual ({stdout})"
        if stdout == "none":
            return "Physical or undetected"

    product = read_text("/sys/class/dmi/id/product_name")
    vendor = read_text("/sys/class/dmi/id/sys_vendor")
    combined = f"{vendor} {product}".lower()
    virtual_markers = ("vmware", "virtualbox", "kvm", "qemu", "xen", "hyper-v", "amazon ec2", "google")
    if any(marker in combined for marker in virtual_markers):
        return f"Virtual ({vendor} {product})".strip()
    return "Physical or undetected"


def cpu_model() -> str:
    for line in read_text("/proc/cpuinfo").splitlines():
        if line.lower().startswith(("model name", "hardware", "processor")) and ":" in line:
            value = line.split(":", 1)[1].strip()
            if value:
                return value
    return platform.processor() or "Unknown"


def read_cpu_times() -> tuple[int, int]:
    first_line = read_text("/proc/stat").splitlines()[0]
    values = [int(item) for item in first_line.split()[1:]]
    idle = values[3] + (values[4] if len(values) > 4 else 0)
    total = sum(values)
    return idle, total


def cpu_usage(interval: float = 1.0) -> float:
    idle1, total1 = read_cpu_times()
    time.sleep(interval)
    idle2, total2 = read_cpu_times()
    total_delta = total2 - total1
    idle_delta = idle2 - idle1
    if total_delta <= 0:
        return 0.0
    return max(0.0, min(100.0, 100.0 * (1.0 - idle_delta / total_delta)))


def memory_info() -> dict[str, int]:
    values: dict[str, int] = {}
    for line in read_text("/proc/meminfo").splitlines():
        if ":" not in line:
            continue
        key, rest = line.split(":", 1)
        match = re.search(r"(\d+)", rest)
        if match:
            values[key] = int(match.group(1)) * 1024
    return values


def memory_metrics() -> tuple[float, str, float, str]:
    mem = memory_info()
    total = mem.get("MemTotal", 0)
    available = mem.get("MemAvailable", mem.get("MemFree", 0))
    used = max(0, total - available)
    memory_pct = (used / total * 100.0) if total else 0.0

    swap_total = mem.get("SwapTotal", 0)
    swap_free = mem.get("SwapFree", 0)
    swap_used = max(0, swap_total - swap_free)
    swap_pct = (swap_used / swap_total * 100.0) if swap_total else 0.0

    memory_text = f"{human_bytes(used)} used / {human_bytes(total)} total ({memory_pct:.1f}%)"
    swap_text = (
        f"{human_bytes(swap_used)} used / {human_bytes(swap_total)} total ({swap_pct:.1f}%)"
        if swap_total
        else "No swap configured"
    )
    return memory_pct, memory_text, swap_pct, swap_text


def load_average() -> tuple[float, float, float]:
    try:
        values = os.getloadavg()
        return float(values[0]), float(values[1]), float(values[2])
    except (AttributeError, OSError):
        return 0.0, 0.0, 0.0


def filesystem_rows() -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    mounts_seen: set[str] = set()

    try:
        mounts = read_text("/proc/self/mounts").splitlines()
        for line in mounts:
            parts = line.split()
            if len(parts) < 3:
                continue
            device, mountpoint, fs_type = parts[:3]
            mountpoint = mountpoint.replace(r"\040", " ")

            if mountpoint in mounts_seen:
                continue
            mounts_seen.add(mountpoint)

            if fs_type in {
                "proc", "sysfs", "devtmpfs", "devpts", "tmpfs", "cgroup", "cgroup2",
                "securityfs", "pstore", "debugfs", "tracefs", "configfs", "fusectl",
                "mqueue", "hugetlbfs", "rpc_pipefs", "autofs", "overlay", "squashfs"
            }:
                continue

            try:
                usage = shutil.disk_usage(mountpoint)
                pct = (usage.used / usage.total * 100.0) if usage.total else 0.0
            except OSError:
                continue

            inode_total = inode_free = inode_used = 0
            inode_pct = 0.0
            try:
                stats = os.statvfs(mountpoint)
                inode_total = stats.f_files
                inode_free = stats.f_ffree
                inode_used = max(0, inode_total - inode_free)
                inode_pct = (inode_used / inode_total * 100.0) if inode_total else 0.0
            except OSError:
                pass

            rows.append(
                {
                    "device": device,
                    "mountpoint": mountpoint,
                    "filesystem": fs_type,
                    "total": usage.total,
                    "used": usage.used,
                    "free": usage.free,
                    "used_pct": pct,
                    "inode_used_pct": inode_pct,
                }
            )
    except OSError:
        pass

    return sorted(rows, key=lambda row: row["mountpoint"])


def top_processes(sort_key: str, limit: int = 5) -> str:
    if not shutil.which("ps"):
        return "ps command is unavailable"

    sort_option = "-%cpu" if sort_key == "cpu" else "-%mem"
    code, stdout, stderr = run_command(
        ["ps", "-eo", "pid,ppid,user,stat,%cpu,%mem,etimes,comm,args", f"--sort={sort_option}"],
        timeout=10,
    )
    if code != 0:
        return stderr or "Unable to query processes"

    lines = stdout.splitlines()
    return "\n".join(lines[: limit + 1])


def zombie_processes() -> tuple[int, str]:
    if not shutil.which("ps"):
        return 0, "ps command is unavailable"

    code, stdout, stderr = run_command(["ps", "-eo", "pid,ppid,user,stat,comm,args"])
    if code != 0:
        return 0, stderr or "Unable to query processes"

    lines = stdout.splitlines()
    header = lines[0] if lines else ""
    zombies = []
    for line in lines[1:]:
        fields = line.split(None, 4)
        if len(fields) >= 4 and "Z" in fields[3]:
            zombies.append(line)

    detail = "\n".join([header] + zombies) if zombies else "No zombie processes found"
    return len(zombies), detail


def failed_systemd_units() -> tuple[int, str]:
    if not shutil.which("systemctl"):
        return 0, "systemctl is unavailable"

    code, stdout, stderr = run_command(
        ["systemctl", "--failed", "--no-legend", "--no-pager"],
        timeout=15,
    )
    # systemctl can return non-zero in containers/non-systemd systems.
    if code != 0 and not stdout:
        return 0, stderr or "Unable to query systemd"

    lines = [line for line in stdout.splitlines() if line.strip()]
    return len(lines), "\n".join(lines) if lines else "No failed systemd units"


def network_summary() -> str:
    if shutil.which("ip"):
        code, stdout, stderr = run_command(["ip", "-brief", "address"])
        if code == 0:
            return stdout
        return stderr or "Unable to query network interfaces"
    return "ip command is unavailable"


def socket_summary() -> tuple[int, int, str]:
    if shutil.which("ss"):
        code, stdout, stderr = run_command(["ss", "-H", "-tan"])
        if code != 0:
            return 0, 0, stderr or "Unable to query sockets"
        established = 0
        listening = 0
        for line in stdout.splitlines():
            state = line.split(None, 1)[0] if line.split() else ""
            if state == "ESTAB":
                established += 1
            elif state == "LISTEN":
                listening += 1

        code2, listen_out, _ = run_command(["ss", "-lntup"])
        detail = listen_out if code2 == 0 else stdout[:5000]
        return established, listening, detail

    if shutil.which("netstat"):
        code, stdout, stderr = run_command(["netstat", "-ant"])
        if code != 0:
            return 0, 0, stderr or "Unable to query sockets"
        established = sum(1 for line in stdout.splitlines() if "ESTABLISHED" in line)
        listening = sum(1 for line in stdout.splitlines() if "LISTEN" in line)
        return established, listening, stdout[:5000]

    return 0, 0, "Neither ss nor netstat is available"


def disk_io_summary() -> str:
    if shutil.which("iostat"):
        code, stdout, stderr = run_command(["iostat", "-xz", "1", "2"], timeout=15)
        if code == 0:
            return stdout
        return stderr or "iostat failed"
    return "iostat is unavailable. Install the sysstat package for disk I/O statistics."


def vmstat_summary() -> str:
    if shutil.which("vmstat"):
        code, stdout, stderr = run_command(["vmstat", "1", "3"], timeout=10)
        if code == 0:
            return stdout
        return stderr or "vmstat failed"
    return "vmstat is unavailable"


def collect_checks(thresholds: Thresholds, brief: bool = False) -> tuple[list[CheckResult], dict[str, Any]]:
    results: list[CheckResult] = []
    boot_time, uptime = boot_time_and_uptime()
    cpu_count = os.cpu_count() or 1

    metadata = {
        "generated_at": datetime.now().astimezone().isoformat(timespec="seconds"),
        "hostname": hostname_fqdn(),
        "ip_addresses": ip_addresses(),
        "os": parse_os_release(),
        "kernel": platform.release(),
        "architecture": platform.machine(),
        "virtualization": virtualization(),
        "product_name": read_text("/sys/class/dmi/id/product_name", "Unknown"),
        "cpu_model": cpu_model(),
        "cpu_count": cpu_count,
        "boot_time": boot_time,
        "uptime": uptime,
    }

    for name, value in (
        ("Hostname", metadata["hostname"]),
        ("IP addresses", ", ".join(metadata["ip_addresses"]) or "Unavailable"),
        ("Operating system", metadata["os"]),
        ("Kernel", metadata["kernel"]),
        ("Architecture", metadata["architecture"]),
        ("Machine type", metadata["virtualization"]),
        ("Product name", metadata["product_name"]),
        ("Processor", metadata["cpu_model"]),
        ("Logical CPUs", str(metadata["cpu_count"])),
        ("Boot time", metadata["boot_time"]),
        ("Uptime", metadata["uptime"]),
    ):
        results.append(CheckResult("System Information", name, "INFO", value))

    cpu_pct = cpu_usage()
    results.append(
        CheckResult(
            "Resource Usage",
            "CPU utilisation",
            classify(cpu_pct, thresholds.cpu_warning, thresholds.cpu_critical),
            f"{cpu_pct:.1f}%",
            f"Warning >= {thresholds.cpu_warning:.0f}%, critical >= {thresholds.cpu_critical:.0f}%",
        )
    )

    load1, load5, load15 = load_average()
    normalized_load = load1 / cpu_count
    results.append(
        CheckResult(
            "Resource Usage",
            "Load average",
            classify(
                normalized_load,
                thresholds.load_warning_per_cpu,
                thresholds.load_critical_per_cpu,
            ),
            f"{load1:.2f}, {load5:.2f}, {load15:.2f}",
            f"1-minute load per CPU: {normalized_load:.2f}; logical CPUs: {cpu_count}",
        )
    )

    memory_pct, memory_text, swap_pct, swap_text = memory_metrics()
    results.append(
        CheckResult(
            "Resource Usage",
            "Memory utilisation",
            classify(memory_pct, thresholds.memory_warning, thresholds.memory_critical),
            memory_text,
        )
    )
    swap_status = "OK" if "No swap" in swap_text else classify(
        swap_pct, thresholds.swap_warning, thresholds.swap_critical
    )
    results.append(CheckResult("Resource Usage", "Swap utilisation", swap_status, swap_text))

    filesystems = filesystem_rows()
    if not filesystems:
        results.append(CheckResult("Storage", "Filesystem usage", "UNKNOWN", "No filesystem data collected"))
    else:
        for row in filesystems:
            results.append(
                CheckResult(
                    "Storage",
                    f"Filesystem {row['mountpoint']}",
                    classify(
                        row["used_pct"],
                        thresholds.filesystem_warning,
                        thresholds.filesystem_critical,
                    ),
                    f"{row['used_pct']:.1f}% used ({human_bytes(row['used'])} / {human_bytes(row['total'])})",
                    f"Device={row['device']}; type={row['filesystem']}; free={human_bytes(row['free'])}",
                )
            )
            if row["inode_used_pct"] > 0:
                results.append(
                    CheckResult(
                        "Storage",
                        f"Inodes {row['mountpoint']}",
                        classify(
                            row["inode_used_pct"],
                            thresholds.inode_warning,
                            thresholds.inode_critical,
                        ),
                        f"{row['inode_used_pct']:.1f}% used",
                        f"Warning >= {thresholds.inode_warning:.0f}%, critical >= {thresholds.inode_critical:.0f}%",
                    )
                )

    zombie_count, zombie_detail = zombie_processes()
    results.append(
        CheckResult(
            "Processes and Services",
            "Zombie processes",
            "WARNING" if zombie_count else "OK",
            str(zombie_count),
            zombie_detail,
        )
    )

    failed_count, failed_detail = failed_systemd_units()
    failed_status = "CRITICAL" if failed_count else ("OK" if "No failed" in failed_detail else "INFO")
    results.append(
        CheckResult(
            "Processes and Services",
            "Failed systemd units",
            failed_status,
            str(failed_count),
            failed_detail,
        )
    )

    established, listening, socket_detail = socket_summary()
    results.append(
        CheckResult(
            "Network",
            "TCP socket summary",
            "INFO",
            f"{established} established, {listening} listening",
            socket_detail,
        )
    )
    results.append(CheckResult("Network", "Network interfaces", "INFO", "", network_summary()))

    if not brief:
        results.append(CheckResult("Process Detail", "Top 5 by CPU", "INFO", "", top_processes("cpu")))
        results.append(CheckResult("Process Detail", "Top 5 by memory", "INFO", "", top_processes("memory")))
        results.append(CheckResult("Performance Detail", "Disk I/O", "INFO", "", disk_io_summary()))
        results.append(CheckResult("Performance Detail", "vmstat samples", "INFO", "", vmstat_summary()))

    return results, metadata


def overall_status(results: Iterable[CheckResult]) -> str:
    ranked = max((STATUS_RANK.get(result.status, 1) for result in results), default=0)
    return {0: "OK", 1: "WARNING", 2: "CRITICAL"}.get(ranked, "WARNING")


def render_text(results: list[CheckResult], metadata: dict[str, Any]) -> str:
    status = overall_status(results)
    width = 112
    lines = [
        "=" * width,
        "LINUX OS HEALTH CHECK REPORT".center(width),
        "=" * width,
        f"Generated : {metadata['generated_at']}",
        f"Host      : {metadata['hostname']}",
        f"Overall   : {STATUS_ICON[status]} {status}",
        "=" * width,
    ]

    current_section = ""
    for result in results:
        if result.section != current_section:
            current_section = result.section
            lines.extend(["", f"--- {current_section} " + "-" * max(1, width - len(current_section) - 5)])

        label = f"{STATUS_ICON.get(result.status, '[?]')} {result.name}"
        lines.append(f"{label:<43} {result.value}")
        if result.detail:
            for detail_line in result.detail.splitlines():
                lines.append(f"    {detail_line}")

    alerts = [r for r in results if r.status in {"WARNING", "CRITICAL", "UNKNOWN"}]
    lines.extend(["", "=" * width, "ACTION SUMMARY", "=" * width])
    if alerts:
        for item in alerts:
            lines.append(f"{STATUS_ICON.get(item.status)} {item.section} -> {item.name}: {item.value}")
    else:
        lines.append("[OK] No warning or critical condition was detected.")

    lines.extend(["=" * width, ""])
    return "\n".join(lines)


def render_html(results: list[CheckResult], metadata: dict[str, Any]) -> str:
    status = overall_status(results)
    rows = []
    for result in results:
        detail = f"<pre>{html.escape(result.detail)}</pre>" if result.detail else ""
        rows.append(
            "<tr>"
            f"<td>{html.escape(result.section)}</td>"
            f"<td>{html.escape(result.name)}</td>"
            f"<td class='{result.status.lower()}'>{html.escape(result.status)}</td>"
            f"<td>{html.escape(result.value)}{detail}</td>"
            "</tr>"
        )

    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>Linux OS Health Check - {html.escape(metadata['hostname'])}</title>
<style>
body {{ font-family: Arial, sans-serif; margin: 24px; color: #202124; }}
h1 {{ margin-bottom: 4px; }}
.meta {{ margin-bottom: 20px; }}
table {{ border-collapse: collapse; width: 100%; }}
th, td {{ border: 1px solid #d0d7de; padding: 8px; text-align: left; vertical-align: top; }}
th {{ background: #f6f8fa; }}
.ok, .info {{ font-weight: bold; }}
.warning {{ background: #fff3cd; font-weight: bold; }}
.critical {{ background: #f8d7da; font-weight: bold; }}
.unknown {{ background: #e2e3e5; font-weight: bold; }}
pre {{ white-space: pre-wrap; margin: 8px 0 0; font-size: 12px; }}
</style>
</head>
<body>
<h1>Linux OS Health Check</h1>
<div class="meta">
Host: <strong>{html.escape(metadata['hostname'])}</strong><br>
Generated: {html.escape(metadata['generated_at'])}<br>
Overall status: <strong class="{status.lower()}">{status}</strong>
</div>
<table>
<thead><tr><th>Section</th><th>Check</th><th>Status</th><th>Value / Detail</th></tr></thead>
<tbody>
{''.join(rows)}
</tbody>
</table>
</body>
</html>
"""


def send_email_via_sendmail(recipient: str, subject: str, body: str, html_body: str | None = None) -> None:
    sendmail = shutil.which("sendmail")
    if not sendmail:
        raise RuntimeError(
            "sendmail-compatible command not found. Configure Postfix/Sendmail, "
            "or use cron with mailx as documented in the deployment guide."
        )

    boundary = "OS_HEALTH_BOUNDARY_2026"
    if html_body:
        message = (
            f"To: {recipient}\n"
            f"Subject: {subject}\n"
            "MIME-Version: 1.0\n"
            f"Content-Type: multipart/alternative; boundary={boundary}\n\n"
            f"--{boundary}\nContent-Type: text/plain; charset=UTF-8\n\n{body}\n"
            f"--{boundary}\nContent-Type: text/html; charset=UTF-8\n\n{html_body}\n"
            f"--{boundary}--\n"
        )
    else:
        message = (
            f"To: {recipient}\n"
            f"Subject: {subject}\n"
            "Content-Type: text/plain; charset=UTF-8\n\n"
            f"{body}\n"
        )

    process = subprocess.run(
        [sendmail, "-t", "-oi"],
        input=message,
        text=True,
        capture_output=True,
        check=False,
    )
    if process.returncode != 0:
        raise RuntimeError(process.stderr.strip() or "sendmail returned a non-zero exit code")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Generate a Linux OS health-check report.")
    parser.add_argument(
        "--output-dir",
        default="./health_reports",
        help="Directory for generated reports (default: ./health_reports)",
    )
    parser.add_argument(
        "--format",
        nargs="+",
        choices=("text", "html", "json"),
        default=("text", "html", "json"),
        help="Report formats to generate",
    )
    parser.add_argument("--brief", action="store_true", help="Skip command-heavy diagnostic sections")
    parser.add_argument("--email", help="Email recipient; requires a local sendmail-compatible MTA")
    parser.add_argument("--cpu-warning", type=float, default=75.0)
    parser.add_argument("--cpu-critical", type=float, default=90.0)
    parser.add_argument("--memory-warning", type=float, default=80.0)
    parser.add_argument("--memory-critical", type=float, default=90.0)
    parser.add_argument("--swap-warning", type=float, default=40.0)
    parser.add_argument("--swap-critical", type=float, default=70.0)
    parser.add_argument("--filesystem-warning", type=float, default=80.0)
    parser.add_argument("--filesystem-critical", type=float, default=90.0)
    parser.add_argument("--inode-warning", type=float, default=80.0)
    parser.add_argument("--inode-critical", type=float, default=90.0)
    return parser.parse_args()


def validate_thresholds(thresholds: Thresholds) -> None:
    pairs = (
        ("CPU", thresholds.cpu_warning, thresholds.cpu_critical),
        ("Memory", thresholds.memory_warning, thresholds.memory_critical),
        ("Swap", thresholds.swap_warning, thresholds.swap_critical),
        ("Filesystem", thresholds.filesystem_warning, thresholds.filesystem_critical),
        ("Inode", thresholds.inode_warning, thresholds.inode_critical),
        ("Load", thresholds.load_warning_per_cpu, thresholds.load_critical_per_cpu),
    )
    for name, warning, critical in pairs:
        if warning < 0 or critical < 0 or warning >= critical:
            raise ValueError(f"{name} thresholds must satisfy: 0 <= warning < critical")


def main() -> int:
    args = parse_args()
    thresholds = Thresholds(
        cpu_warning=args.cpu_warning,
        cpu_critical=args.cpu_critical,
        memory_warning=args.memory_warning,
        memory_critical=args.memory_critical,
        swap_warning=args.swap_warning,
        swap_critical=args.swap_critical,
        filesystem_warning=args.filesystem_warning,
        filesystem_critical=args.filesystem_critical,
        inode_warning=args.inode_warning,
        inode_critical=args.inode_critical,
    )

    try:
        validate_thresholds(thresholds)
        output_dir = Path(args.output_dir).expanduser().resolve()
        output_dir.mkdir(parents=True, exist_ok=True)

        results, metadata = collect_checks(thresholds, brief=args.brief)
        status = overall_status(results)
        timestamp = datetime.now().astimezone().strftime("%Y%m%d_%H%M%S")
        safe_host = re.sub(r"[^A-Za-z0-9_.-]+", "_", metadata["hostname"])
        base_name = f"os_health_{safe_host}_{timestamp}"

        text_report = render_text(results, metadata)
        html_report = render_html(results, metadata)

        generated_files: list[Path] = []
        if "text" in args.format:
            path = output_dir / f"{base_name}.txt"
            path.write_text(text_report, encoding="utf-8")
            generated_files.append(path)

        if "html" in args.format:
            path = output_dir / f"{base_name}.html"
            path.write_text(html_report, encoding="utf-8")
            generated_files.append(path)

        if "json" in args.format:
            path = output_dir / f"{base_name}.json"
            payload = {
                "metadata": metadata,
                "thresholds": asdict(thresholds),
                "overall_status": status,
                "checks": [asdict(item) for item in results],
            }
            path.write_text(json.dumps(payload, indent=2), encoding="utf-8")
            generated_files.append(path)

        print(text_report)
        print("Generated files:")
        for path in generated_files:
            print(f"  {path}")

        if args.email:
            subject = f"[{status}] Linux OS Health Check - {metadata['hostname']}"
            send_email_via_sendmail(args.email, subject, text_report, html_report)
            print(f"Email submitted to local MTA for: {args.email}")

        return STATUS_RANK.get(status, 1)

    except Exception as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 3


if __name__ == "__main__":
    sys.exit(main())
