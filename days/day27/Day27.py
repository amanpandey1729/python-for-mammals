"""
Python for Mammals - Day 27
Topic: OS Module - Current Directory, Directory Listing, and Environment Basics

Audience:
- Complete beginners
- DBAs, Sysadmins, Support Engineers, Cloud Engineers, Monitoring Teams
- Anyone who wants Python for practical automation

Goal of Day 27:
By the end of today, you should be able to:
1. Import and use Python's built-in os module
2. Find the current working directory with os.getcwd()
3. Understand why the working directory affects relative file paths
4. List directory contents with os.listdir()
5. Inspect a specific directory without changing into it
6. Understand basic environment variables
7. Read environment variables safely with os.getenv()
8. Build a small environment and folder inspection workflow

Why this matters:
Automation scripts run inside an operating-system environment. Before a
script can read logs, create reports, or inspect files, it should know:
- where it is currently running
- which files and folders are available
- which environment settings are available to it

These checks are useful in scheduled jobs, support tools, deployment
scripts, inventory collection, health checks, and troubleshooting.

Important safety note:
Environment variables can contain passwords, tokens, and other secrets.
Never print every environment variable in a production script. Read only
specific, non-sensitive values that your automation genuinely needs.
"""

import os

print("=" * 70)
print("DAY 27 - OS MODULE")
print("os.getcwd(), os.listdir(), environment basics")
print("=" * 70)

# ---------------------------------------------------------------------
# SECTION 1: What Is the os Module?
# ---------------------------------------------------------------------

print("\nSECTION 1: What Is the os Module?")

"""
The os module is part of Python's standard library.
You do not need to install it separately.

It helps Python interact with the operating system. For example, it can:
- report the current working directory
- list files and folders
- read environment variables
- create, rename, and remove directories
- work with operating-system paths

Today we focus only on safe inspection operations.
"""

print("The os module helps Python inspect and interact with its environment.")

# ---------------------------------------------------------------------
# SECTION 2: Current Working Directory with os.getcwd()
# ---------------------------------------------------------------------

print("\nSECTION 2: Current Working Directory")

current_directory = os.getcwd()

print("Current working directory:", current_directory)

"""
The current working directory is the folder Python treats as its starting
location for relative paths.

A script file and its working directory are not always the same folder.
This matters when a scheduled task, IDE, terminal, or automation platform
starts the script from a different location.
"""

# ---------------------------------------------------------------------
# SECTION 3: Why the Working Directory Matters
# ---------------------------------------------------------------------

print("\nSECTION 3: Why the Working Directory Matters")

report_name = "daily_report.txt"
report_location = os.path.join(current_directory, report_name)

print("Relative file name :", report_name)
print("Resolved location  :", report_location)

"""
When Python opens "daily_report.txt" using a relative path, it normally
looks for that file inside the current working directory.

os.path.join() safely combines path parts using the separator expected by
the operating system.
"""

# ---------------------------------------------------------------------
# SECTION 4: List the Current Directory with os.listdir()
# ---------------------------------------------------------------------

print("\nSECTION 4: List the Current Directory")

items = os.listdir()

print("Total items found:", len(items))

for item_number, item_name in enumerate(sorted(items), start=1):
    print(f"{item_number}. {item_name}")

"""
os.listdir() without an argument lists the current working directory.
It returns names, not full paths.

sorted() is optional, but predictable ordering makes reports easier to read.
"""

# ---------------------------------------------------------------------
# SECTION 5: List a Specific Directory
# ---------------------------------------------------------------------

print("\nSECTION 5: List a Specific Directory")

selected_directory = current_directory
selected_items = os.listdir(selected_directory)

print("Directory inspected:", selected_directory)
print("Items found        :", len(selected_items))

"""
os.listdir(path) inspects the requested directory without changing the
current working directory.

This is safer than changing folders when a script only needs to inspect
another location.
"""

# ---------------------------------------------------------------------
# SECTION 6: Separate Files and Directories
# ---------------------------------------------------------------------

print("\nSECTION 6: Separate Files and Directories")

file_names = []
directory_names = []

for item_name in os.listdir(current_directory):
    item_path = os.path.join(current_directory, item_name)

    if os.path.isfile(item_path):
        file_names.append(item_name)
    elif os.path.isdir(item_path):
        directory_names.append(item_name)

print("File count     :", len(file_names))
print("Directory count:", len(directory_names))

"""
os.listdir() returns both files and directories.
os.path.isfile() and os.path.isdir() help classify each item.

This pattern is useful for inventory reports and folder validation.
"""

# ---------------------------------------------------------------------
# SECTION 7: Environment Variable Basics
# ---------------------------------------------------------------------

print("\nSECTION 7: Environment Variable Basics")

"""
An environment variable is a name-value setting supplied by the operating
system or the process that starts Python.

Common uses include:
- application mode such as DEVELOPMENT or PRODUCTION
- configuration directory locations
- user home directories
- executable search paths
- temporary directory locations

Environment variables differ across Windows, Linux, macOS, containers,
cloud services, and individual machines.
"""

print("Environment variables provide external settings to a running program.")

# ---------------------------------------------------------------------
# SECTION 8: Read One Variable Safely with os.getenv()
# ---------------------------------------------------------------------

print("\nSECTION 8: Read One Environment Variable")

user_name = os.getenv("USERNAME") or os.getenv("USER") or "UNKNOWN"
home_directory = os.getenv("HOME") or os.getenv("USERPROFILE") or "NOT SET"

print("Current user     :", user_name)
print("Home directory   :", home_directory)

"""
os.getenv("NAME") returns the variable's value when it exists.
It returns None when the variable is missing.

The or expressions above handle common Windows and Linux/macOS names
without crashing when one of them is unavailable.
"""

# ---------------------------------------------------------------------
# SECTION 9: Use a Default Value
# ---------------------------------------------------------------------

print("\nSECTION 9: Use a Default Environment Value")

environment_name = os.getenv("APP_ENV", "DEVELOPMENT")

print("Application environment:", environment_name)

"""
The second argument to os.getenv() is a default value.

Using a sensible default prevents None from spreading into later logic.
For production automation, choose defaults carefully and validate critical
settings before continuing.
"""

# ---------------------------------------------------------------------
# SECTION 10: Make a Simple Environment Decision
# ---------------------------------------------------------------------

print("\nSECTION 10: Make an Environment Decision")

normalized_environment = environment_name.strip().upper()

if normalized_environment == "PRODUCTION":
    execution_mode = "CAUTIOUS"
elif normalized_environment in ("TEST", "UAT", "STAGING"):
    execution_mode = "VALIDATION"
else:
    execution_mode = "DEVELOPMENT"

print("Normalized environment:", normalized_environment)
print("Execution mode        :", execution_mode)

"""
Real automation often changes behavior by environment.
For example, a cleanup script may run in preview mode outside production.

Do not depend only on a label for safety. Important scripts should still
validate targets, paths, permissions, and user confirmation where needed.
"""

# ---------------------------------------------------------------------
# SECTION 11: Inspect Only Selected Environment Variables
# ---------------------------------------------------------------------

print("\nSECTION 11: Inspect Selected Environment Variables")

safe_variable_names = ["APP_ENV", "HOME", "USERPROFILE", "TEMP", "TMP"]

for variable_name in safe_variable_names:
    variable_value = os.getenv(variable_name, "NOT SET")
    print(f"{variable_name}: {variable_value}")

"""
Avoid printing os.environ in full because it may expose credentials,
tokens, connection details, or internal paths.

Use an allow-list: explicitly name only the safe values needed in a report.
"""

# ---------------------------------------------------------------------
# SECTION 12: Build a Directory Summary
# ---------------------------------------------------------------------

print("\nSECTION 12: Build a Directory Summary")

summary_lines = [
    "=" * 60,
    "OS ENVIRONMENT SUMMARY",
    "=" * 60,
    f"Working directory : {current_directory}",
    f"Total items       : {len(items)}",
    f"Files             : {len(file_names)}",
    f"Directories       : {len(directory_names)}",
    f"Application env   : {normalized_environment}",
    f"Execution mode    : {execution_mode}",
    "=" * 60,
]

summary_text = "\n".join(summary_lines)
print(summary_text)

# ---------------------------------------------------------------------
# SECTION 13: Practical Validation Pattern
# ---------------------------------------------------------------------

print("\nSECTION 13: Practical Validation Pattern")

required_file_name = "config.txt"
required_file_path = os.path.join(current_directory, required_file_name)

if required_file_name in os.listdir(current_directory):
    validation_status = "FOUND"
else:
    validation_status = "MISSING"

print("Required file:", required_file_path)
print("Status       :", validation_status)

"""
This simple membership check is useful for beginner practice.
Later, pathlib or os.path.exists() can provide more direct path validation.
"""

# ---------------------------------------------------------------------
# SECTION 14: Guided Practice
# ---------------------------------------------------------------------

print("\nSECTION 14: Guided Practice")

"""
Guided practice:
1. Run this file from VS Code and note the working directory.
2. Run it from a terminal opened in a different folder.
3. Compare the os.getcwd() results.
4. Create a few harmless test files and rerun the directory listing.
5. Set APP_ENV to TEST in your terminal, then run the script again.
6. Observe how the normalized environment and execution mode change.

Windows Command Prompt example:
set APP_ENV=TEST
python Day27.py

PowerShell example:
$env:APP_ENV="TEST"
python Day27.py

Linux/macOS example:
APP_ENV=TEST python Day27.py
"""

print("Guided practice: change the launch folder and APP_ENV, then compare output.")

# ---------------------------------------------------------------------
# SECTION 15: Mini Challenge
# ---------------------------------------------------------------------

print("\nSECTION 15: Mini Challenge")

"""
Build an OS Environment Inspector.

Collect these inputs once:
1. directory path to inspect
2. expected file name
3. environment-variable name to read

Then:
- display the current working directory
- validate that the requested directory exists
- list its contents in sorted order
- count files and directories
- check whether the expected file is present
- read the requested environment variable using a safe default
- decide a simple READY or ATTENTION status
- print a compact final report
- handle FileNotFoundError and PermissionError

Do not ask for the same input repeatedly.
Reuse the collected values throughout the workflow.
"""

print("Mini challenge: build an input-driven OS Environment Inspector.")

# ---------------------------------------------------------------------
# SECTION 16: Day 27 Summary
# ---------------------------------------------------------------------

print("\nSECTION 16: Day 27 Summary")
print("Today you used os.getcwd(), os.listdir(), os.getenv(), and safe OS checks.")
print("Next step: use stronger path tools to navigate and manage files safely.")
print("Day 27 complete. Keep automating one practical task at a time.")
