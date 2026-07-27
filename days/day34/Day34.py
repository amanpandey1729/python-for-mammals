"""
Python for Mammals - Day 34
Topic: Logging - Recording What an Automation Did

Audience:
- Complete beginners
- DBAs, Sysadmins, Support Engineers, Cloud Engineers, Monitoring Teams
- Anyone who wants Python for practical automation

Goal of Day 34:
By the end of today, you should be able to:
1. Explain why operational scripts need logs
2. Use Python's built-in logging module
3. Recognise DEBUG, INFO, WARNING, ERROR, and CRITICAL levels
4. Configure readable log messages with timestamps and logger names
5. Write logs to a file
6. Send different levels to the console and a log file
7. Record exception details with logger.exception()
8. Create reusable named loggers without duplicate handlers
9. Choose useful messages without exposing secrets
10. Build a logged operational-check workflow

Why this matters:
A script may run from Task Scheduler, cron, an automation server, or a remote
terminal when nobody is watching. print() can show what is happening now, but
logging creates a durable operational trail that answers:

    When did the script run?
    Which step completed?
    What was skipped?
    What warning occurred?
    Why did the workflow fail?

Automation pattern:

    start -> log context -> perform work -> log decisions -> log result
                              | failure
                              v
                    record exception details

Safety note:
Logs often remain on disk and may be forwarded to monitoring platforms. Never
log passwords, tokens, private keys, full connection strings, or unnecessary
personal information.
"""

import logging
from pathlib import Path
import tempfile

print("=" * 70)
print("DAY 34 - LOGGING")
print("Recording what an automation did")
print("=" * 70)

# ---------------------------------------------------------------------
# SECTION 1: Why Logging Matters
# ---------------------------------------------------------------------

print("\nSECTION 1: Why Logging Matters")

print("print() is useful for immediate output.")
print("logging adds severity, timestamps, destinations, and history.")

"""
Use print() for intentional user-facing results.
Use logging for operational evidence and troubleshooting information.

A script can use both:
- print(): final report shown to the operator
- logging: detailed execution trail stored for later investigation
"""

# ---------------------------------------------------------------------
# SECTION 2: Create a Logger
# ---------------------------------------------------------------------

print("\nSECTION 2: Create a Logger")

logger = logging.getLogger("day34.basics")
logger.setLevel(logging.DEBUG)
logger.handlers.clear()
logger.propagate = False

console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)
console_handler.setFormatter(logging.Formatter("%(levelname)s - %(message)s"))
logger.addHandler(console_handler)

logger.info("Inventory collection started")
logger.warning("One host did not return a response")
logger.error("Report file could not be copied")

"""
getLogger(name) returns a named logger.
setLevel() controls the lowest level the logger accepts.
A handler decides where accepted records go, such as the console or a file.
propagate = False prevents this practice logger from also reaching the root
logger and appearing twice.
"""

# ---------------------------------------------------------------------
# SECTION 3: Understand Log Levels
# ---------------------------------------------------------------------

print("\nSECTION 3: Understand Log Levels")

levels = [
    ("DEBUG", "Detailed diagnostic information for troubleshooting"),
    ("INFO", "Normal progress and successful milestones"),
    ("WARNING", "Unexpected condition; workflow can still continue"),
    ("ERROR", "A task failed; part of the workflow could not complete"),
    ("CRITICAL", "Severe failure requiring immediate attention"),
]

for level_name, purpose in levels:
    print(f"{level_name:<8} : {purpose}")

"""
Typical operational choices:
DEBUG    parsed 214 records; candidate path=/data/input
INFO     health check started; report created successfully
WARNING  disk usage is 82%, above warning threshold
ERROR    backup metadata file could not be read
CRITICAL all configured targets failed; no report was produced

A warning is not merely a colourful INFO message. The level should describe
impact and urgency.
"""

# ---------------------------------------------------------------------
# SECTION 4: Filtering by Level
# ---------------------------------------------------------------------

print("\nSECTION 4: Filtering by Level")

filter_logger = logging.getLogger("day34.filter")
filter_logger.setLevel(logging.DEBUG)
filter_logger.handlers.clear()
filter_logger.propagate = False

filter_handler = logging.StreamHandler()
filter_handler.setLevel(logging.WARNING)
filter_handler.setFormatter(logging.Formatter("%(levelname)s - %(message)s"))
filter_logger.addHandler(filter_handler)

filter_logger.debug("Detailed value: disk_used=72")
filter_logger.info("Disk check completed")
filter_logger.warning("Disk usage is approaching the limit")
filter_logger.error("Disk information is unavailable")

print("The handler displayed WARNING and above.")

"""
Both logger and handler levels matter.
A record must pass the logger level and then the handler level.
This allows one logger to send detailed records to a file while keeping the
console quieter.
"""

# ---------------------------------------------------------------------
# SECTION 5: Add Useful Context with a Formatter
# ---------------------------------------------------------------------

print("\nSECTION 5: Add Useful Context with a Formatter")

formatter = logging.Formatter(
    "%(asctime)s | %(levelname)-8s | %(name)s | %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)

print("Formatter fields:")
print("%(asctime)s  -> date and time")
print("%(levelname)s -> severity")
print("%(name)s      -> logger name")
print("%(message)s   -> message supplied by the script")

"""
Other useful fields include:
- %(filename)s
- %(funcName)s
- %(lineno)d

Do not add every possible field merely because it exists. Keep production logs
readable and include context that helps an operator investigate.
"""

# ---------------------------------------------------------------------
# SECTION 6: Write Logs to a File
# ---------------------------------------------------------------------

print("\nSECTION 6: Write Logs to a File")

practice_folder = Path(tempfile.mkdtemp(prefix="python_for_mammals_day34_"))
log_path = practice_folder / "operations.log"

file_logger = logging.getLogger("day34.file")
file_logger.setLevel(logging.DEBUG)
file_logger.handlers.clear()
file_logger.propagate = False

file_handler = logging.FileHandler(log_path, mode="w", encoding="utf-8")
file_handler.setLevel(logging.DEBUG)
file_handler.setFormatter(formatter)
file_logger.addHandler(file_handler)

file_logger.debug("Loaded 3 inventory records")
file_logger.info("Inventory report created")
file_logger.warning("One optional field was blank")

for handler in file_logger.handlers:
    handler.flush()

print("Log file created:", log_path.name)
print("Log file exists :", log_path.exists())
print("Log records     :", len(log_path.read_text(encoding="utf-8").splitlines()))

"""
FileHandler appends by default. mode="w" is used here only to make the lesson
repeatable. For operational history, append mode is often more appropriate.
Use encoding="utf-8" for predictable text handling.
"""

# ---------------------------------------------------------------------
# SECTION 7: Console and File with Different Levels
# ---------------------------------------------------------------------

print("\nSECTION 7: Console and File with Different Levels")

combined_path = practice_folder / "combined.log"
combined_logger = logging.getLogger("day34.combined")
combined_logger.setLevel(logging.DEBUG)
combined_logger.handlers.clear()
combined_logger.propagate = False

combined_console = logging.StreamHandler()
combined_console.setLevel(logging.WARNING)
combined_console.setFormatter(logging.Formatter("%(levelname)s - %(message)s"))

combined_file = logging.FileHandler(combined_path, mode="w", encoding="utf-8")
combined_file.setLevel(logging.DEBUG)
combined_file.setFormatter(formatter)

combined_logger.addHandler(combined_console)
combined_logger.addHandler(combined_file)

combined_logger.debug("Raw usage value received: 78")
combined_logger.info("Disk check completed")
combined_logger.warning("Disk usage is close to threshold")

for handler in combined_logger.handlers:
    handler.flush()

print("Console minimum level: WARNING")
print("File minimum level   : DEBUG")
print("Records in file      :", len(combined_path.read_text(encoding="utf-8").splitlines()))

# ---------------------------------------------------------------------
# SECTION 8: Build Messages with Values
# ---------------------------------------------------------------------

print("\nSECTION 8: Build Messages with Values")

message_logger = logging.getLogger("day34.values")
message_logger.setLevel(logging.INFO)
message_logger.handlers.clear()
message_logger.propagate = False

message_handler = logging.StreamHandler()
message_handler.setFormatter(logging.Formatter("%(levelname)s - %(message)s"))
message_logger.addHandler(message_handler)

server_name = "app-01"
disk_usage = 84
threshold = 80

message_logger.info("Checking server %s", server_name)

if disk_usage >= threshold:
    message_logger.warning(
        "Disk usage is %s%% on %s; threshold is %s%%",
        disk_usage,
        server_name,
        threshold,
    )
else:
    message_logger.info("Disk usage is within threshold on %s", server_name)

"""
The logging module supports placeholder arguments:
    logger.info("Checked %s records", record_count)

This delays final string formatting until the record is actually needed and is
the conventional logging style.
"""

# ---------------------------------------------------------------------
# SECTION 9: Log Exceptions Correctly
# ---------------------------------------------------------------------

print("\nSECTION 9: Log Exceptions Correctly")

exception_path = practice_folder / "exceptions.log"
exception_logger = logging.getLogger("day34.exceptions")
exception_logger.setLevel(logging.DEBUG)
exception_logger.handlers.clear()
exception_logger.propagate = False

exception_handler = logging.FileHandler(exception_path, mode="w", encoding="utf-8")
exception_handler.setFormatter(formatter)
exception_logger.addHandler(exception_handler)

try:
    raw_value = "unknown"
    usage_percent = float(raw_value)
except ValueError:
    exception_logger.exception("Could not convert usage value to a number")

for handler in exception_logger.handlers:
    handler.flush()

exception_text = exception_path.read_text(encoding="utf-8")
print("Exception logged    :", "ValueError" in exception_text)
print("Traceback recorded  :", "Traceback" in exception_text)

"""
Use logger.exception() inside an except block. It writes an ERROR record and
includes traceback information. Use logger.error() when a traceback is not
needed or no active exception exists.
"""

# ---------------------------------------------------------------------
# SECTION 10: Create a Reusable Logger Function
# ---------------------------------------------------------------------

print("\nSECTION 10: Create a Reusable Logger Function")


def create_logger(name, destination):
    """Return one configured logger without adding duplicate handlers."""
    reusable_logger = logging.getLogger(name)
    reusable_logger.setLevel(logging.DEBUG)
    reusable_logger.propagate = False

    if reusable_logger.handlers:
        return reusable_logger

    destination.parent.mkdir(parents=True, exist_ok=True)

    reusable_file_handler = logging.FileHandler(
        destination,
        encoding="utf-8",
    )
    reusable_file_handler.setLevel(logging.DEBUG)
    reusable_file_handler.setFormatter(formatter)
    reusable_logger.addHandler(reusable_file_handler)

    return reusable_logger


reusable_path = practice_folder / "reusable.log"
first_logger = create_logger("operations.health", reusable_path)
second_logger = create_logger("operations.health", reusable_path)

first_logger.info("Reusable logger is ready")

for handler in first_logger.handlers:
    handler.flush()

print("Same logger object :", first_logger is second_logger)
print("Handler count      :", len(first_logger.handlers))

"""
Calling setup code repeatedly can accidentally attach duplicate handlers and
write every record multiple times. Check existing handlers or configure logging
once at application startup.
"""

# ---------------------------------------------------------------------
# SECTION 11: Logger Names for Workflow Components
# ---------------------------------------------------------------------

print("\nSECTION 11: Logger Names for Workflow Components")

component_names = [
    "operations.inventory",
    "operations.disk",
    "operations.report",
]

for component_name in component_names:
    print(component_name)

"""
Hierarchical names make records searchable and show where they came from.
Larger scripts often use:
    logger = logging.getLogger(__name__)

Each module then records its own dotted Python module name.
"""

# ---------------------------------------------------------------------
# SECTION 12: What Should and Should Not Be Logged
# ---------------------------------------------------------------------

print("\nSECTION 12: What Should and Should Not Be Logged")

safe_examples = [
    "workflow start and finish",
    "target name and environment",
    "record counts and durations",
    "threshold decisions",
    "handled failures and retry results",
]

unsafe_examples = [
    "passwords or authentication tokens",
    "private keys",
    "complete secret-bearing connection strings",
    "unnecessary personal or confidential data",
]

print("Useful to log:")
for item in safe_examples:
    print("-", item)

print("Do not log:")
for item in unsafe_examples:
    print("-", item)

# ---------------------------------------------------------------------
# SECTION 13: Guided Practice - Logged Health Check
# ---------------------------------------------------------------------

print("\nSECTION 13: Guided Practice - Logged Health Check")

health_log_path = practice_folder / "health_check.log"
health_logger = create_logger("operations.guided_health", health_log_path)

observations = [
    {"server": "app-01", "disk_usage": 72},
    {"server": "app-02", "disk_usage": 88},
    {"server": "batch-01", "disk_usage": None},
]
health_threshold = 80
healthy_count = 0
warning_count = 0
error_count = 0

health_logger.info("Health check started for %s servers", len(observations))

for observation in observations:
    server = observation["server"]
    usage = observation["disk_usage"]
    health_logger.debug("Processing server=%s usage=%s", server, usage)

    if usage is None:
        error_count += 1
        health_logger.error("Usage data is missing for %s", server)
    elif usage >= health_threshold:
        warning_count += 1
        health_logger.warning(
            "Disk usage is %s%% on %s; threshold is %s%%",
            usage,
            server,
            health_threshold,
        )
    else:
        healthy_count += 1
        health_logger.info("Disk usage is healthy on %s: %s%%", server, usage)

health_logger.info(
    "Health check finished: healthy=%s warning=%s error=%s",
    healthy_count,
    warning_count,
    error_count,
)

for handler in health_logger.handlers:
    handler.flush()

print("Servers checked:", len(observations))
print("Healthy        :", healthy_count)
print("Warnings       :", warning_count)
print("Errors         :", error_count)
print("Log destination:", health_log_path.name)

# ---------------------------------------------------------------------
# SECTION 14: A Small Logged File Workflow
# ---------------------------------------------------------------------

print("\nSECTION 14: A Small Logged File Workflow")

report_path = practice_folder / "reports" / "summary.txt"
workflow_logger = create_logger("operations.report_workflow", practice_folder / "report_workflow.log")

try:
    workflow_logger.info("Report workflow started")
    report_path.parent.mkdir(parents=True, exist_ok=True)
    workflow_logger.debug("Report directory ready: %s", report_path.parent)

    report_text = (
        "DAILY HEALTH SUMMARY\n"
        f"Healthy: {healthy_count}\n"
        f"Warnings: {warning_count}\n"
        f"Errors: {error_count}\n"
    )
    report_path.write_text(report_text, encoding="utf-8")
    workflow_logger.info("Report created successfully: %s", report_path)
except OSError:
    workflow_logger.exception("Report workflow failed")

for handler in workflow_logger.handlers:
    handler.flush()

print("Report created:", report_path.exists())
print("Report name   :", report_path.name)

# ---------------------------------------------------------------------
# SECTION 15: Common Logging Mistakes
# ---------------------------------------------------------------------

print("\nSECTION 15: Common Logging Mistakes")

mistakes = [
    "using ERROR for normal progress",
    "writing vague messages such as 'something failed'",
    "logging the same exception repeatedly at every layer",
    "adding handlers more than once",
    "recording secrets or excessive raw data",
    "keeping DEBUG logging permanently without retention planning",
]

for number, mistake in enumerate(mistakes, start=1):
    print(f"{number}. {mistake}")

# ---------------------------------------------------------------------
# SECTION 16: Mini Challenge
# ---------------------------------------------------------------------

print("\nSECTION 16: Mini Challenge")

"""
Build a Logged Daily Operations Checker.

Collect once:
- server name
- environment
- disk usage percentage
- memory usage percentage
- disk warning threshold
- memory warning threshold
- log filename

Your workflow should:
1. Validate all inputs before evaluating health.
2. Create a named logger and a UTF-8 FileHandler.
3. Record the workflow start and safe context at INFO.
4. Record converted values and decision details at DEBUG.
5. Record each threshold breach at WARNING.
6. Record invalid or unavailable data at ERROR.
7. Use logger.exception() for handled file or conversion failures where useful.
8. Produce HEALTHY, ATTENTION, or INVALID as the final status.
9. Print a concise operator-facing summary.
10. Write a detailed execution trail to the selected log file.
11. Avoid duplicate handlers when setup is called more than once.
12. Never write credentials or secrets to the log.

Test at least these scenarios:
- both metrics healthy
- disk threshold breached
- both thresholds breached
- invalid numeric input
- log destination cannot be created
"""

print("Mini challenge: build one health workflow with a trustworthy audit trail.")

# ---------------------------------------------------------------------
# SECTION 17: Day 34 Summary
# ---------------------------------------------------------------------

print("\nSECTION 17: Day 34 Summary")
print("Today you replaced invisible automation with an execution trail.")
print("You used levels, formatters, console handlers, file handlers, and exception logs.")
print("Day 34 complete. Useful automation should explain what it did.")
