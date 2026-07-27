"""
Python for Mammals - Day 31
Topic: Linux Commands from Python - df, free, uptime, ps, and Output Processing

Audience:
- Complete beginners
- DBAs, Sysadmins, Support Engineers, Cloud Engineers, Monitoring Teams
- Anyone who wants Python for practical automation

Goal of Day 31:
By the end of today, you should be able to:
1. Run common Linux commands from Python
2. Capture output from df, free, uptime, and ps
3. Check whether a command exists before running it
4. Inspect return codes, stdout, and stderr
5. Split command output into lines and columns
6. Extract disk usage from df output
7. Extract memory values from free output
8. Read load information from uptime output
9. Inspect process rows from ps output
10. Build a compact Linux health summary

Why this matters:
Linux administrators, DBAs, cloud engineers, support teams, and monitoring
teams frequently rely on commands such as df, free, uptime, and ps. Python can
run these commands, capture their output, extract only the important values,
apply thresholds, and combine multiple checks into one operational report.

Platform note:
These commands are Linux-specific. The file checks whether each command is
available before running it. On Windows or restricted systems, the script
prints a clear SKIPPED message instead of failing.

Safety note:
Today's commands are read-only. Continue to pass command arguments as a list,
avoid shell=True, set reasonable timeouts, and verify command availability
before execution.
"""

import shutil
import subprocess

print("=" * 70)
print("DAY 31 - LINUX COMMANDS FROM PYTHON")
print("df, free, uptime, ps, and output processing")
print("=" * 70)

# ---------------------------------------------------------------------
# SECTION 1: Why Run Linux Commands from Python?
# ---------------------------------------------------------------------

print("\nSECTION 1: Why Run Linux Commands from Python?")

"""
Linux commands already expose valuable system information.
Python adds automation around them:

    command -> captured text -> parsed values -> decision -> report

Examples:
- identify a filesystem above a disk threshold
- calculate memory usage from free
- collect load averages from uptime
- count or filter process rows from ps
"""

print("Python can turn familiar Linux command output into automation data.")

# ---------------------------------------------------------------------
# SECTION 2: Check Command Availability
# ---------------------------------------------------------------------

print("\nSECTION 2: Check Command Availability")

linux_commands = ["df", "free", "uptime", "ps"]

for command_name in linux_commands:
    command_path = shutil.which(command_name)
    status = "AVAILABLE" if command_path else "MISSING"
    print(f"{command_name:<8}: {status}")

"""
shutil.which() searches the executable path.
Use it before running a platform-specific command.
"""

# ---------------------------------------------------------------------
# SECTION 3: Reusable Command Runner
# ---------------------------------------------------------------------

print("\nSECTION 3: Reusable Command Runner")


def run_linux_command(command, timeout=10):
    """Run one read-only Linux command and return a result dictionary."""
    executable = command[0]

    if shutil.which(executable) is None:
        return {
            "status": "SKIPPED",
            "return_code": None,
            "stdout": "",
            "stderr": f"{executable} is not available",
        }

    try:
        result = subprocess.run(
            command,
            capture_output=True,
            text=True,
            timeout=timeout,
        )
        return {
            "status": "SUCCESS" if result.returncode == 0 else "ATTENTION",
            "return_code": result.returncode,
            "stdout": result.stdout.strip(),
            "stderr": result.stderr.strip(),
        }
    except subprocess.TimeoutExpired:
        return {
            "status": "TIMEOUT",
            "return_code": None,
            "stdout": "",
            "stderr": f"Command exceeded {timeout} seconds",
        }
    except OSError as error:
        return {
            "status": "ERROR",
            "return_code": None,
            "stdout": "",
            "stderr": str(error),
        }


print("Reusable Linux command runner is ready.")

# ---------------------------------------------------------------------
# SECTION 4: Run df
# ---------------------------------------------------------------------

print("\nSECTION 4: Run df")

df_result = run_linux_command(["df", "-P"])

print("Status     :", df_result["status"])
print("Return code:", df_result["return_code"])

if df_result["stdout"]:
    df_lines = df_result["stdout"].splitlines()
    print("Output lines:", len(df_lines))
    print("Header      :", df_lines[0])
else:
    print("Message     :", df_result["stderr"])

"""
df -P requests portable, one-line-per-filesystem output on Linux.
The exact devices and sizes differ between systems.
"""

# ---------------------------------------------------------------------
# SECTION 5: Process df Output
# ---------------------------------------------------------------------

print("\nSECTION 5: Process df Output")

df_alerts = []

if df_result["status"] == "SUCCESS":
    for line in df_result["stdout"].splitlines()[1:]:
        columns = line.split()

        if len(columns) < 6:
            continue

        filesystem = columns[0]
        usage_text = columns[4]
        mount_point = columns[5]

        if usage_text.endswith("%"):
            usage_percent = int(usage_text.rstrip("%"))

            if usage_percent >= 80:
                df_alerts.append(
                    {
                        "filesystem": filesystem,
                        "usage_percent": usage_percent,
                        "mount_point": mount_point,
                    }
                )

print("Filesystems at or above 80%:", len(df_alerts))

for alert in df_alerts:
    print(
        f"{alert['mount_point']}: "
        f"{alert['usage_percent']}% "
        f"({alert['filesystem']})"
    )

"""
split() handles variable whitespace in command output.
The percentage sign is removed before converting the value to int.
"""

# ---------------------------------------------------------------------
# SECTION 6: Run free
# ---------------------------------------------------------------------

print("\nSECTION 6: Run free")

free_result = run_linux_command(["free", "-m"])

print("Status     :", free_result["status"])
print("Return code:", free_result["return_code"])

if free_result["stdout"]:
    free_lines = free_result["stdout"].splitlines()
    print("Output lines:", len(free_lines))
    print("Header      :", free_lines[0])
else:
    print("Message     :", free_result["stderr"])

# ---------------------------------------------------------------------
# SECTION 7: Process free Output
# ---------------------------------------------------------------------

print("\nSECTION 7: Process free Output")

memory_summary = {
    "total_mb": None,
    "used_mb": None,
    "available_mb": None,
    "usage_percent": None,
}

if free_result["status"] == "SUCCESS":
    memory_line = next(
        (
            line
            for line in free_result["stdout"].splitlines()
            if line.lower().startswith("mem:")
        ),
        None,
    )

    if memory_line:
        columns = memory_line.split()

        if len(columns) >= 7:
            total_mb = int(columns[1])
            used_mb = int(columns[2])
            available_mb = int(columns[6])
            usage_percent = round((used_mb / total_mb) * 100, 2)

            memory_summary = {
                "total_mb": total_mb,
                "used_mb": used_mb,
                "available_mb": available_mb,
                "usage_percent": usage_percent,
            }

print("Total memory MB    :", memory_summary["total_mb"])
print("Used memory MB     :", memory_summary["used_mb"])
print("Available memory MB:", memory_summary["available_mb"])
print("Usage percent      :", memory_summary["usage_percent"])

"""
free -m reports memory values in MiB on common Linux systems.
The Mem: row is selected, split into columns, and converted into integers.
"""

# ---------------------------------------------------------------------
# SECTION 8: Run uptime
# ---------------------------------------------------------------------

print("\nSECTION 8: Run uptime")

uptime_result = run_linux_command(["uptime"])

print("Status     :", uptime_result["status"])
print("Return code:", uptime_result["return_code"])

if uptime_result["stdout"]:
    print("Output     :", uptime_result["stdout"])
else:
    print("Message    :", uptime_result["stderr"])

# ---------------------------------------------------------------------
# SECTION 9: Process uptime Output
# ---------------------------------------------------------------------

print("\nSECTION 9: Process uptime Output")

load_averages = []

if uptime_result["status"] == "SUCCESS":
    uptime_text = uptime_result["stdout"]

    if "load average:" in uptime_text:
        load_text = uptime_text.split("load average:", 1)[1].strip()
    elif "load averages:" in uptime_text:
        load_text = uptime_text.split("load averages:", 1)[1].strip()
    else:
        load_text = ""

    if load_text:
        load_averages = [
            float(value.strip().replace(",", "."))
            for value in load_text.split(",")[:3]
        ]

print("Load values found:", len(load_averages))
print("Load averages     :", load_averages)

"""
uptime output varies slightly across Unix-like systems.
This example recognises both load average: and load averages: labels.
"""

# ---------------------------------------------------------------------
# SECTION 10: Run ps
# ---------------------------------------------------------------------

print("\nSECTION 10: Run ps")

ps_result = run_linux_command(
    ["ps", "-eo", "pid,comm,%cpu,%mem", "--sort=-%cpu"]
)

print("Status     :", ps_result["status"])
print("Return code:", ps_result["return_code"])

if ps_result["stdout"]:
    ps_lines = ps_result["stdout"].splitlines()
    print("Process rows:", max(len(ps_lines) - 1, 0))
    print("Header      :", ps_lines[0])
else:
    print("Message     :", ps_result["stderr"])

# ---------------------------------------------------------------------
# SECTION 11: Process ps Output
# ---------------------------------------------------------------------

print("\nSECTION 11: Process ps Output")

top_processes = []

if ps_result["status"] == "SUCCESS":
    for line in ps_result["stdout"].splitlines()[1:6]:
        columns = line.split(None, 3)

        if len(columns) == 4:
            pid, command_name, cpu_text, memory_text = columns
            top_processes.append(
                {
                    "pid": int(pid),
                    "command": command_name,
                    "cpu_percent": float(cpu_text),
                    "memory_percent": float(memory_text),
                }
            )

print("Top process entries:", len(top_processes))

for process in top_processes:
    print(
        f"PID {process['pid']} | "
        f"{process['command']} | "
        f"CPU {process['cpu_percent']}% | "
        f"MEM {process['memory_percent']}%"
    )

"""
ps output is converted into dictionaries.
That makes the data easier to sort, filter, report, or export later.
"""

# ---------------------------------------------------------------------
# SECTION 12: Filter Processes by CPU
# ---------------------------------------------------------------------

print("\nSECTION 12: Filter Processes by CPU")

cpu_threshold = 10.0
high_cpu_processes = [
    process
    for process in top_processes
    if process["cpu_percent"] >= cpu_threshold
]

print("CPU threshold      :", cpu_threshold)
print("Processes above it :", len(high_cpu_processes))

for process in high_cpu_processes:
    print(
        f"{process['command']} "
        f"(PID {process['pid']}) "
        f"{process['cpu_percent']}%"
    )

# ---------------------------------------------------------------------
# SECTION 13: Build a Linux Health Summary
# ---------------------------------------------------------------------

print("\nSECTION 13: Build a Linux Health Summary")

check_statuses = {
    "df": df_result["status"],
    "free": free_result["status"],
    "uptime": uptime_result["status"],
    "ps": ps_result["status"],
}

successful_checks = sum(
    1 for status in check_statuses.values() if status == "SUCCESS"
)

if successful_checks == len(check_statuses) and not df_alerts:
    overall_status = "HEALTHY"
elif successful_checks == 0:
    overall_status = "UNAVAILABLE"
else:
    overall_status = "ATTENTION"

summary_lines = [
    "=" * 60,
    "LINUX HEALTH SUMMARY",
    "=" * 60,
    f"df status          : {check_statuses['df']}",
    f"free status        : {check_statuses['free']}",
    f"uptime status      : {check_statuses['uptime']}",
    f"ps status          : {check_statuses['ps']}",
    f"Disk alerts        : {len(df_alerts)}",
    f"Memory usage       : {memory_summary['usage_percent']}",
    f"Load averages      : {load_averages}",
    f"Top process entries: {len(top_processes)}",
    f"Overall status     : {overall_status}",
    "=" * 60,
]

print("\n".join(summary_lines))

# ---------------------------------------------------------------------
# SECTION 14: Guided Practice
# ---------------------------------------------------------------------

print("\nSECTION 14: Guided Practice")

"""
Guided practice:
1. Run df -P and print only the first two output lines.
2. Change the disk threshold from 80 to 70.
3. Capture free -m and locate the Mem: line.
4. Calculate memory usage from total and used values.
5. Capture uptime and isolate the load-average section.
6. Run ps with a different sort field such as -%mem.
7. Print only processes above a CPU threshold.
8. Store parsed process details in dictionaries.
9. Combine command statuses into one compact report.
"""

print("Guided practice: collect, split, convert, filter, and report.")

# ---------------------------------------------------------------------
# SECTION 15: Mini Challenge
# ---------------------------------------------------------------------

print("\nSECTION 15: Mini Challenge")

"""
Build a Linux Health Snapshot.

Collect these inputs once:
1. Server label
2. Disk warning threshold
3. Memory warning threshold
4. Process CPU threshold
5. Number of top processes to display

Then:
- validate all threshold values
- check whether df, free, uptime, and ps are available
- run each available command once
- capture stdout, stderr, and return codes
- parse disk usage from df -P
- identify filesystems at or above the disk threshold
- parse memory values from free -m
- calculate memory usage percentage
- parse load averages from uptime
- parse process rows from ps
- keep the requested number of top processes
- identify processes at or above the CPU threshold
- decide HEALTHY, ATTENTION, PARTIAL, or UNAVAILABLE
- generate a clean final report
- handle TimeoutExpired, OSError, and ValueError

Do not ask for the same input more than once.
Do not use shell=True.
Do not run destructive commands.
"""

print("Mini challenge: build an input-driven Linux Health Snapshot.")

# ---------------------------------------------------------------------
# SECTION 16: Day 31 Summary
# ---------------------------------------------------------------------

print("\nSECTION 16: Day 31 Summary")
print("Today you ran df, free, uptime, and ps from Python.")
print("You converted command output into values, lists, and dictionaries.")
print("Day 31 complete. Useful automation begins where command output becomes data.")
