"""
Python for Mammals - Day 33
Mini Project #4: Linux Health Check Script

Checks:
- CPU
- Memory
- Disk

Audience:
- Complete beginners
- DBAs, Linux Administrators, Cloud Engineers, Support Engineers
- Monitoring Teams and non-developer IT professionals

Project goal:
Build one complete Linux health-check workflow that:
1. Collects CPU, memory, and disk information
2. Converts command output into structured Python data
3. Applies configurable warning thresholds
4. Handles unavailable commands and command failures safely
5. Produces one compact operational report
6. Keeps data collection separate from analysis and reporting

Why this matters:
Operations teams repeatedly answer the same questions:

    Is CPU pressure high?
    Is memory usage approaching a limit?
    Is any filesystem becoming full?

A health-check script standardises those checks and produces the same report
every time. This mini project combines subprocess, pathlib, functions,
exceptions, dictionaries, lists, calculations, conditions, and configuration.

Platform note:
The live commands used today are Linux-specific:
- uptime
- free -m
- df -P

The guided examples use fixed sample output so the lesson runs safely on any
platform. The final live check verifies command availability before execution.

Safety note:
All commands are read-only. Arguments are passed as lists. shell=True is not
used. Every command has a timeout.
"""

from configparser import ConfigParser
from pathlib import Path
import shutil
import subprocess
import tempfile

print("=" * 70)
print("DAY 33 - MINI PROJECT #4")
print("LINUX HEALTH CHECK SCRIPT")
print("CPU, memory, and disk")
print("=" * 70)

# ---------------------------------------------------------------------
# SECTION 1: Project Blueprint
# ---------------------------------------------------------------------

print("\nSECTION 1: Project Blueprint")

"""
A reliable health check is easier to build in stages:

    settings
       |
       v
    collect raw data
       |
       v
    parse useful values
       |
       v
    compare with thresholds
       |
       v
    create final report

Keeping these responsibilities separate makes the script easier to test,
debug, and extend.
"""

project_steps = [
    "Load thresholds",
    "Collect CPU information",
    "Collect memory information",
    "Collect disk information",
    "Apply health rules",
    "Generate one report",
]

for step_number, step_name in enumerate(project_steps, start=1):
    print(f"{step_number}. {step_name}")

# ---------------------------------------------------------------------
# SECTION 2: Project Configuration
# ---------------------------------------------------------------------

print("\nSECTION 2: Project Configuration")

config_text = """[health_check]
server_label = demo-linux-01
cpu_threshold = 75
memory_threshold = 80
disk_threshold = 85
command_timeout = 5
"""

practice_folder = Path(tempfile.mkdtemp(prefix="python_for_mammals_day33_"))
config_path = practice_folder / "health_check.ini"
config_path.write_text(config_text, encoding="utf-8")

config = ConfigParser()
files_read = config.read(config_path, encoding="utf-8")

server_label = config.get("health_check", "server_label")
cpu_threshold = config.getfloat("health_check", "cpu_threshold")
memory_threshold = config.getfloat("health_check", "memory_threshold")
disk_threshold = config.getfloat("health_check", "disk_threshold")
command_timeout = config.getint("health_check", "command_timeout")

print("Configuration files read:", len(files_read))
print("Server label            :", server_label)
print("CPU threshold           :", cpu_threshold)
print("Memory threshold        :", memory_threshold)
print("Disk threshold          :", disk_threshold)
print("Command timeout         :", command_timeout)

# ---------------------------------------------------------------------
# SECTION 3: Sample Linux Output
# ---------------------------------------------------------------------

print("\nSECTION 3: Sample Linux Output")

"""
The project first uses deterministic sample output.
This allows every learner to practise parsing even when they are using
Windows, macOS, or an online Python environment.
"""

sample_uptime = (
    " 10:42:11 up 12 days,  3:18,  2 users,  "
    "load average: 1.25, 0.95, 0.70"
)

sample_free = """               total        used        free      shared  buff/cache   available
Mem:           16000       11200        1200         300        3600        4300
Swap:           4096         256        3840
"""

sample_df = """Filesystem     1024-blocks      Used Available Capacity Mounted on
/dev/root         104857600  73400320  31457280      70% /
/dev/data         209715200 188743680  20971520      90% /data
tmpfs               8192000    409600   7782400       5% /run
"""

print("Sample uptime lines:", len(sample_uptime.splitlines()))
print("Sample free lines  :", len(sample_free.splitlines()))
print("Sample df lines    :", len(sample_df.splitlines()))

# ---------------------------------------------------------------------
# SECTION 4: Parse CPU Load
# ---------------------------------------------------------------------

print("\nSECTION 4: Parse CPU Load")


def parse_load_averages(uptime_output):
    """Extract up to three load averages from uptime output."""
    for label in ("load average:", "load averages:"):
        if label in uptime_output:
            load_text = uptime_output.split(label, 1)[1].strip()
            return [
                float(value.strip().replace(",", "."))
                for value in load_text.split(",")[:3]
            ]

    return []


load_averages = parse_load_averages(sample_uptime)

print("Load averages:", load_averages)
print("One-minute load:", load_averages[0] if load_averages else None)

"""
Load average is not a direct CPU percentage.
For a simple beginner project, we compare one-minute load with logical CPU
count and convert it into an estimated pressure percentage:

    estimated pressure % = one-minute load / CPU count * 100

This is a useful operational indicator, not a replacement for detailed tools.
"""

logical_cpu_count = 4
one_minute_load = load_averages[0]
cpu_pressure_percent = round(
    (one_minute_load / logical_cpu_count) * 100,
    2,
)

print("Logical CPUs       :", logical_cpu_count)
print("CPU pressure       :", cpu_pressure_percent)

# ---------------------------------------------------------------------
# SECTION 5: Parse Memory Usage
# ---------------------------------------------------------------------

print("\nSECTION 5: Parse Memory Usage")


def parse_memory(free_output):
    """Return memory values from the Mem: row."""
    for line in free_output.splitlines():
        if line.strip().lower().startswith("mem:"):
            columns = line.split()

            if len(columns) >= 7:
                total_mb = int(columns[1])
                used_mb = int(columns[2])
                available_mb = int(columns[6])
                usage_percent = round((used_mb / total_mb) * 100, 2)

                return {
                    "total_mb": total_mb,
                    "used_mb": used_mb,
                    "available_mb": available_mb,
                    "usage_percent": usage_percent,
                }

    return {
        "total_mb": None,
        "used_mb": None,
        "available_mb": None,
        "usage_percent": None,
    }


memory = parse_memory(sample_free)

print("Total memory MB    :", memory["total_mb"])
print("Used memory MB     :", memory["used_mb"])
print("Available memory MB:", memory["available_mb"])
print("Memory usage       :", memory["usage_percent"])

# ---------------------------------------------------------------------
# SECTION 6: Parse Disk Usage
# ---------------------------------------------------------------------

print("\nSECTION 6: Parse Disk Usage")


def parse_disk(df_output):
    """Convert df -P rows into filesystem dictionaries."""
    filesystems = []

    for line in df_output.splitlines()[1:]:
        columns = line.split()

        if len(columns) < 6:
            continue

        usage_text = columns[4]

        if not usage_text.endswith("%"):
            continue

        filesystems.append(
            {
                "filesystem": columns[0],
                "usage_percent": int(usage_text.rstrip("%")),
                "mount_point": columns[5],
            }
        )

    return filesystems


filesystems = parse_disk(sample_df)

print("Filesystems parsed:", len(filesystems))

for filesystem in filesystems:
    print(
        f"{filesystem['mount_point']:<8} "
        f"{filesystem['usage_percent']:>3}% "
        f"{filesystem['filesystem']}"
    )

# ---------------------------------------------------------------------
# SECTION 7: Apply Health Rules
# ---------------------------------------------------------------------

print("\nSECTION 7: Apply Health Rules")


def status_for(value, threshold):
    """Return HEALTHY or ATTENTION for one numeric metric."""
    return "ATTENTION" if value >= threshold else "HEALTHY"


cpu_status = status_for(cpu_pressure_percent, cpu_threshold)
memory_status = status_for(memory["usage_percent"], memory_threshold)

disk_alerts = [
    filesystem
    for filesystem in filesystems
    if filesystem["usage_percent"] >= disk_threshold
]

disk_status = "ATTENTION" if disk_alerts else "HEALTHY"

print("CPU status   :", cpu_status)
print("Memory status:", memory_status)
print("Disk status  :", disk_status)
print("Disk alerts  :", len(disk_alerts))

# ---------------------------------------------------------------------
# SECTION 8: Decide Overall Health
# ---------------------------------------------------------------------

print("\nSECTION 8: Decide Overall Health")

component_statuses = {
    "CPU": cpu_status,
    "Memory": memory_status,
    "Disk": disk_status,
}

attention_components = [
    component
    for component, status in component_statuses.items()
    if status == "ATTENTION"
]

overall_status = "ATTENTION" if attention_components else "HEALTHY"

print("Components checked :", len(component_statuses))
print("Attention components:", attention_components)
print("Overall status     :", overall_status)

# ---------------------------------------------------------------------
# SECTION 9: Build the Final Report
# ---------------------------------------------------------------------

print("\nSECTION 9: Build the Final Report")


def build_report(
    label,
    cpu_value,
    cpu_limit,
    cpu_health,
    memory_data,
    memory_limit,
    memory_health,
    disk_rows,
    disk_limit,
    disk_health,
    disk_breaches,
    final_status,
):
    """Return a compact multiline health report."""
    lines = [
        "=" * 66,
        "LINUX HEALTH CHECK REPORT",
        "=" * 66,
        f"Server label       : {label}",
        f"CPU pressure       : {cpu_value}% (threshold {cpu_limit}%)",
        f"CPU status         : {cpu_health}",
        f"Memory usage       : {memory_data['usage_percent']}% "
        f"(threshold {memory_limit}%)",
        f"Memory status      : {memory_health}",
        f"Filesystems checked: {len(disk_rows)}",
        f"Disk threshold     : {disk_limit}%",
        f"Disk status        : {disk_health}",
        f"Disk alerts        : {len(disk_breaches)}",
    ]

    for breach in disk_breaches:
        lines.append(
            f"  - {breach['mount_point']}: "
            f"{breach['usage_percent']}% "
            f"({breach['filesystem']})"
        )

    lines.extend(
        [
            f"Overall status     : {final_status}",
            "=" * 66,
        ]
    )

    return "\n".join(lines)


health_report = build_report(
    server_label,
    cpu_pressure_percent,
    cpu_threshold,
    cpu_status,
    memory,
    memory_threshold,
    memory_status,
    filesystems,
    disk_threshold,
    disk_status,
    disk_alerts,
    overall_status,
)

print(health_report)

# ---------------------------------------------------------------------
# SECTION 10: Reusable Safe Command Runner
# ---------------------------------------------------------------------

print("\nSECTION 10: Reusable Safe Command Runner")


def run_read_only_command(command, timeout=5):
    """Run one command safely and return a predictable dictionary."""
    executable = command[0]

    if shutil.which(executable) is None:
        return {
            "status": "UNAVAILABLE",
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
            check=False,
        )
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

    return {
        "status": "SUCCESS" if result.returncode == 0 else "FAILED",
        "return_code": result.returncode,
        "stdout": result.stdout.strip(),
        "stderr": result.stderr.strip(),
    }


print("Safe command runner is ready.")

# ---------------------------------------------------------------------
# SECTION 11: Live Linux Collection
# ---------------------------------------------------------------------

print("\nSECTION 11: Live Linux Collection")

live_commands = {
    "uptime": ["uptime"],
    "memory": ["free", "-m"],
    "disk": ["df", "-P"],
}

live_results = {
    name: run_read_only_command(command, command_timeout)
    for name, command in live_commands.items()
}

for check_name, result in live_results.items():
    print(
        f"{check_name:<8}: "
        f"{result['status']} "
        f"(return code {result['return_code']})"
    )

"""
On Linux, successful stdout can now be passed to the same parsing functions.
On systems where a command is unavailable, the result stays predictable and
the script continues instead of crashing.
"""

# ---------------------------------------------------------------------
# SECTION 12: Guided Practice - One Complete Workflow
# ---------------------------------------------------------------------

print("\nSECTION 12: Guided Practice - One Complete Workflow")


def analyse_health(
    label,
    uptime_output,
    free_output,
    df_output,
    cpu_count,
    cpu_limit,
    memory_limit,
    disk_limit,
):
    """Parse, analyse, and return a structured health summary."""
    loads = parse_load_averages(uptime_output)

    if not loads or cpu_count <= 0:
        raise ValueError("CPU load data and a positive CPU count are required")

    cpu_value = round((loads[0] / cpu_count) * 100, 2)
    memory_data = parse_memory(free_output)
    disk_data = parse_disk(df_output)

    if memory_data["usage_percent"] is None:
        raise ValueError("Memory data could not be parsed")

    cpu_health = status_for(cpu_value, cpu_limit)
    memory_health = status_for(memory_data["usage_percent"], memory_limit)
    breaches = [
        row
        for row in disk_data
        if row["usage_percent"] >= disk_limit
    ]
    disk_health = "ATTENTION" if breaches else "HEALTHY"

    overall = (
        "ATTENTION"
        if "ATTENTION" in (cpu_health, memory_health, disk_health)
        else "HEALTHY"
    )

    return {
        "server": label,
        "cpu_pressure_percent": cpu_value,
        "cpu_status": cpu_health,
        "memory": memory_data,
        "memory_status": memory_health,
        "filesystems": disk_data,
        "disk_alerts": breaches,
        "disk_status": disk_health,
        "overall_status": overall,
    }


guided_result = analyse_health(
    "guided-linux-01",
    sample_uptime,
    sample_free,
    sample_df,
    logical_cpu_count,
    cpu_threshold,
    memory_threshold,
    disk_threshold,
)

print("Server         :", guided_result["server"])
print("CPU status     :", guided_result["cpu_status"])
print("Memory status  :", guided_result["memory_status"])
print("Disk status    :", guided_result["disk_status"])
print("Overall status :", guided_result["overall_status"])

# ---------------------------------------------------------------------
# SECTION 13: Mini Challenge
# ---------------------------------------------------------------------

print("\nSECTION 13: Mini Challenge")

"""
Extend the Linux Health Check Script.

Requirements:
1. Read thresholds and server label from health_check.ini.
2. Validate all thresholds are between 0 and 100.
3. Discover logical CPU count with os.cpu_count().
4. Run uptime, free -m, and df -P only once each.
5. Keep command execution inside one reusable function.
6. Keep parsing inside separate functions.
7. Represent parsed information with dictionaries and lists.
8. Report unavailable, failed, and timed-out commands clearly.
9. Decide final status:
       HEALTHY    - all checks available and below thresholds
       ATTENTION  - one or more available metrics breach thresholds
       PARTIAL    - at least one command is unavailable or failed
       UNAVAILABLE- no health command can run
10. Add a timestamp to the final report.
11. Save the report to a configured output folder.
12. Never use shell=True.
13. Do not run administrative or destructive commands.
14. Do not place passwords or private keys in the configuration file.
"""

print("Mini challenge: turn the guided workflow into a reusable live tool.")

# ---------------------------------------------------------------------
# SECTION 14: Project Review
# ---------------------------------------------------------------------

print("\nSECTION 14: Project Review")

project_skills = [
    "configuration files",
    "subprocess",
    "command availability",
    "timeouts",
    "functions",
    "string parsing",
    "lists and dictionaries",
    "calculations and thresholds",
    "exception handling",
    "report generation",
]

for skill in project_skills:
    print("-", skill)

# ---------------------------------------------------------------------
# SECTION 15: Closing Message
# ---------------------------------------------------------------------

print("\nSECTION 15: Closing Message")
print("Mini Project #4 complete.")
print("You combined multiple Python concepts into one operational workflow.")
print("A useful automation tool is not one long command.")
print("It is a clear pipeline: collect, parse, decide, and report.")
