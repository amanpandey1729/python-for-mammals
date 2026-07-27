"""
Python for Mammals - Day 32
Topic: Configuration Files - Storing Settings and Reading Configuration

Audience:
- Complete beginners
- DBAs, Sysadmins, Support Engineers, Cloud Engineers, Monitoring Teams
- Anyone who wants Python for practical automation

Goal of Day 32:
By the end of today, you should be able to:
1. Explain why settings should be separated from program logic
2. Store settings in an INI configuration file
3. Read configuration files with configparser
4. Access sections, keys, and default values
5. Convert text settings into integers, floats, and booleans
6. Validate required configuration values
7. Handle missing files, sections, keys, and invalid values
8. use pathlib.Path for predictable configuration paths
9. Avoid placing secrets directly in source code
10. Build a configuration-driven operational report

Why this matters:
Operational scripts often change between servers, teams, or environments.
Thresholds, paths, report names, feature switches, and connection labels should
not require source-code edits every time. A configuration file lets the same
Python program behave differently by changing data instead of changing logic.

Automation pattern:

    configuration file -> read settings -> validate -> run logic -> report

Safety note:
Configuration files are useful for ordinary settings, but plain-text files are
not secure secret stores. Do not commit passwords, tokens, private keys, or
production credentials to Git repositories. Use environment variables or a
proper secret manager for sensitive values.
"""

from configparser import (
    ConfigParser,
    Error as ConfigParserError,
    NoOptionError,
    NoSectionError,
)
from pathlib import Path
import tempfile

print("=" * 70)
print("DAY 32 - CONFIGURATION FILES")
print("Storing settings and reading configuration")
print("=" * 70)

# ---------------------------------------------------------------------
# SECTION 1: Why Configuration Files Matter
# ---------------------------------------------------------------------

print("\nSECTION 1: Why Configuration Files Matter")

"""
Without configuration:
    disk_threshold = 80
    report_folder = "reports"
    environment = "production"

Every change requires editing the Python file.

With configuration:
    [monitoring]
    disk_threshold = 80

    [report]
    folder = reports

The Python logic stays stable while settings can change independently.
"""

print("Configuration separates changing settings from stable program logic.")

# ---------------------------------------------------------------------
# SECTION 2: Meet the INI Format
# ---------------------------------------------------------------------

print("\nSECTION 2: Meet the INI Format")

sample_ini = """[application]
name = Daily Operations Reporter
environment = test

[monitoring]
disk_threshold = 80
memory_threshold = 85
alerts_enabled = yes

[report]
folder = reports
filename = daily_summary.txt
"""

print(sample_ini)

"""
INI vocabulary:
- [application] is a section
- name is a key
- Daily Operations Reporter is a value
- key = value is one setting

configparser reads values as text first. Typed getters can convert values later.
"""

# ---------------------------------------------------------------------
# SECTION 3: Create a Practice Configuration File
# ---------------------------------------------------------------------

print("\nSECTION 3: Create a Practice Configuration File")

practice_folder = Path(tempfile.mkdtemp(prefix="python_for_mammals_day32_"))
config_path = practice_folder / "operations.ini"
config_path.write_text(sample_ini, encoding="utf-8")

print("Configuration created:", config_path.name)
print("File exists          :", config_path.exists())

"""
A temporary practice folder keeps this lesson self-contained.
In a real project, the file might be:
    project/config/operations.ini
"""

# ---------------------------------------------------------------------
# SECTION 4: Read Configuration with ConfigParser
# ---------------------------------------------------------------------

print("\nSECTION 4: Read Configuration with ConfigParser")

config = ConfigParser()
files_read = config.read(config_path, encoding="utf-8")

print("Files read:", len(files_read))
print("Sections  :", config.sections())

"""
config.read() does not raise FileNotFoundError for a missing path.
It returns a list containing the files that were successfully read.
Always check the returned list when the file is required.
"""

# ---------------------------------------------------------------------
# SECTION 5: Access Sections and Values
# ---------------------------------------------------------------------

print("\nSECTION 5: Access Sections and Values")

application_name = config["application"]["name"]
environment = config.get("application", "environment")
report_folder = config.get("report", "folder")

print("Application :", application_name)
print("Environment :", environment)
print("Report folder:", report_folder)

"""
Two common access styles:
    config["section"]["key"]
    config.get("section", "key")

Direct indexing is concise but raises an error when data is missing.
get() supports a fallback for optional values.
"""

# ---------------------------------------------------------------------
# SECTION 6: Use Fallback Values
# ---------------------------------------------------------------------

print("\nSECTION 6: Use Fallback Values")

report_format = config.get("report", "format", fallback="text")
retry_count_text = config.get("runtime", "retry_count", fallback="3")

print("Report format:", report_format)
print("Retry count  :", retry_count_text)

"""
Fallback values are useful for optional settings.
Do not use a fallback for a truly required setting because it can hide a
configuration mistake.
"""

# ---------------------------------------------------------------------
# SECTION 7: Read Integers, Floats, and Booleans
# ---------------------------------------------------------------------

print("\nSECTION 7: Read Integers, Floats, and Booleans")

disk_threshold = config.getint("monitoring", "disk_threshold")
memory_threshold = config.getfloat("monitoring", "memory_threshold")
alerts_enabled = config.getboolean("monitoring", "alerts_enabled")

print("Disk threshold  :", disk_threshold, type(disk_threshold).__name__)
print("Memory threshold:", memory_threshold, type(memory_threshold).__name__)
print("Alerts enabled  :", alerts_enabled, type(alerts_enabled).__name__)

"""
Useful typed getters:
- getint()
- getfloat()
- getboolean()

getboolean() recognises common values such as yes/no, true/false, and on/off.
An invalid value raises ValueError.
"""

# ---------------------------------------------------------------------
# SECTION 8: Inspect Sections Safely
# ---------------------------------------------------------------------

print("\nSECTION 8: Inspect Sections Safely")

required_sections = ["application", "monitoring", "report"]

for section_name in required_sections:
    status = "FOUND" if config.has_section(section_name) else "MISSING"
    print(f"{section_name:<12}: {status}")

print("Has report filename:", config.has_option("report", "filename"))

"""
Use has_section() and has_option() when you want to inspect configuration
before reading values.
"""

# ---------------------------------------------------------------------
# SECTION 9: Convert a Section into a Dictionary
# ---------------------------------------------------------------------

print("\nSECTION 9: Convert a Section into a Dictionary")

monitoring_settings = dict(config["monitoring"])

print("Monitoring keys:", len(monitoring_settings))

for key, value in monitoring_settings.items():
    print(f"{key:<18}: {value}")

"""
A section behaves like a mapping.
Converting it to a dictionary can help with reporting, iteration, or passing
settings to another function. Values remain strings in this dictionary.
"""

# ---------------------------------------------------------------------
# SECTION 10: DEFAULT Values Shared by Sections
# ---------------------------------------------------------------------

print("\nSECTION 10: DEFAULT Values Shared by Sections")

default_ini = """[DEFAULT]
team = Operations
timeout_seconds = 10

[linux_check]
command = uptime

[database_check]
command = connectivity_test
"""

default_config = ConfigParser()
default_config.read_string(default_ini)

print("Linux team      :", default_config.get("linux_check", "team"))
print("Database timeout:", default_config.getint("database_check", "timeout_seconds"))

"""
Values in [DEFAULT] are inherited by normal sections.
Use defaults for genuinely shared settings, not unrelated values.
"""

# ---------------------------------------------------------------------
# SECTION 11: Write Configuration with ConfigParser
# ---------------------------------------------------------------------

print("\nSECTION 11: Write Configuration with ConfigParser")

generated_config = ConfigParser()
generated_config["application"] = {
    "name": "Inventory Reporter",
    "environment": "development",
}
generated_config["report"] = {
    "folder": "output",
    "include_header": "yes",
}

generated_path = practice_folder / "generated.ini"

with generated_path.open("w", encoding="utf-8") as config_file:
    generated_config.write(config_file)

print("Generated file:", generated_path.name)
print("Generated size:", generated_path.stat().st_size, "bytes")

"""
ConfigParser can create files too.
Be careful: writing replaces the target file content. Keep backups or write to
a new file when preserving an existing configuration matters.
"""

# ---------------------------------------------------------------------
# SECTION 12: Validate Required Settings
# ---------------------------------------------------------------------

print("\nSECTION 12: Validate Required Settings")


def validate_configuration(parser, required_options):
    """Return a list of readable validation errors."""
    errors = []

    for section_name, option_names in required_options.items():
        if not parser.has_section(section_name):
            errors.append(f"Missing section: [{section_name}]")
            continue

        for option_name in option_names:
            value = parser.get(section_name, option_name, fallback="").strip()

            if not value:
                errors.append(
                    f"Missing value: [{section_name}] {option_name}"
                )

    return errors


requirements = {
    "application": ["name", "environment"],
    "monitoring": ["disk_threshold", "memory_threshold"],
    "report": ["folder", "filename"],
}

validation_errors = validate_configuration(config, requirements)

print("Validation errors:", len(validation_errors))

for error_message in validation_errors:
    print("-", error_message)

# ---------------------------------------------------------------------
# SECTION 13: Validate Ranges and Allowed Values
# ---------------------------------------------------------------------

print("\nSECTION 13: Validate Ranges and Allowed Values")


def validate_operational_values(parser):
    """Validate typed values and return errors without stopping the script."""
    errors = []

    try:
        disk_limit = parser.getint("monitoring", "disk_threshold")
        if not 0 <= disk_limit <= 100:
            errors.append("disk_threshold must be between 0 and 100")
    except (NoSectionError, NoOptionError, ValueError) as error:
        errors.append(f"Invalid disk_threshold: {error}")

    environment_value = parser.get(
        "application",
        "environment",
        fallback="",
    ).strip().lower()

    allowed_environments = {"development", "test", "staging", "production"}

    if environment_value not in allowed_environments:
        errors.append(
            "environment must be development, test, staging, or production"
        )

    return errors


operational_errors = validate_operational_values(config)

print("Operational errors:", len(operational_errors))

for error_message in operational_errors:
    print("-", error_message)

# ---------------------------------------------------------------------
# SECTION 14: Load Configuration Through a Function
# ---------------------------------------------------------------------

print("\nSECTION 14: Load Configuration Through a Function")


def load_configuration(path):
    """Load one required INI file and return its parser."""
    parser = ConfigParser()

    try:
        files_loaded = parser.read(path, encoding="utf-8")
    except ConfigParserError as error:
        raise ValueError(f"Invalid configuration syntax: {error}") from error

    if not files_loaded:
        raise FileNotFoundError(f"Configuration file not found: {path}")

    return parser


try:
    loaded_config = load_configuration(config_path)
    loaded_name = loaded_config.get("application", "name")
    print("Loaded application:", loaded_name)
except (FileNotFoundError, ValueError) as error:
    print("Configuration error:", error)

"""
A loader function keeps file checks and parser errors in one place.
The main workflow can then focus on using validated settings.
"""

# ---------------------------------------------------------------------
# SECTION 15: Guided Practice - Configuration-Driven Report
# ---------------------------------------------------------------------

print("\nSECTION 15: Guided Practice - Configuration-Driven Report")

server_inventory = [
    {"name": "app-01", "environment": "production", "usage_percent": 72},
    {"name": "app-02", "environment": "production", "usage_percent": 88},
    {"name": "test-01", "environment": "test", "usage_percent": 64},
]

target_environment = config.get("application", "environment")
warning_threshold = config.getint("monitoring", "disk_threshold")

matching_servers = [
    server
    for server in server_inventory
    if server["environment"] == target_environment
]

alert_servers = [
    server
    for server in matching_servers
    if server["usage_percent"] >= warning_threshold
]

print("Target environment:", target_environment)
print("Servers checked   :", len(matching_servers))
print("Alerts found      :", len(alert_servers))

for server in alert_servers:
    print(f"{server['name']}: {server['usage_percent']}%")

"""
Change environment or disk_threshold in operations.ini and run the workflow
again. The Python decision logic does not need to change.
"""

# ---------------------------------------------------------------------
# SECTION 16: Mini Challenge
# ---------------------------------------------------------------------

print("\nSECTION 16: Mini Challenge")

"""
Build a Configuration-Driven Daily Operations Reporter.

Create an operations.ini file containing:
- [application]
    name
    environment
    owner
- [monitoring]
    disk_threshold
    memory_threshold
    alerts_enabled
- [report]
    folder
    filename
    include_timestamp

Your Python workflow should:
1. Determine the configuration path with pathlib.Path.
2. Read the file once.
3. Confirm that the required file was loaded.
4. Validate required sections and keys.
5. Read typed values with getint() and getboolean().
6. Reject thresholds outside 0 to 100.
7. Reject unsupported environment values.
8. Use fallback only for optional settings.
9. Process a small in-memory list of operational observations.
10. Filter observations for the configured environment.
11. Identify disk and memory threshold breaches.
12. Respect alerts_enabled when deciding whether to list alerts.
13. Create the report folder when configuration is valid.
14. Produce a clean report with settings, counts, alerts, and final status.
15. Handle missing files, malformed INI syntax, missing settings, and invalid
    typed values without showing an uncontrolled traceback.

Do not store passwords or tokens in the practice configuration.
"""

print("Mini challenge: build one reusable script controlled by operations.ini.")

# ---------------------------------------------------------------------
# SECTION 17: Day 32 Summary
# ---------------------------------------------------------------------

print("\nSECTION 17: Day 32 Summary")
print("Today you separated changing settings from stable Python logic.")
print("You read, converted, validated, and used values from INI files.")
print("Day 32 complete. Change configuration, not working code.")
