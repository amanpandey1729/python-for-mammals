"""
Python for Mammals - Day 28
Topic: pathlib - Paths, File Existence, and Path Operations

Audience:
- Complete beginners
- DBAs, Sysadmins, Support Engineers, Cloud Engineers, Monitoring Teams
- Anyone who wants Python for practical automation

Goal of Day 28:
By the end of today, you should be able to:
1. Import and use Path from Python's pathlib module
2. Represent file and directory locations as Path objects
3. Build paths with the / operator
4. Check whether a path exists with exists()
5. Distinguish files and directories with is_file() and is_dir()
6. Inspect path components such as name, stem, suffix, and parent
7. Convert relative paths to absolute paths with resolve()
8. Create directories safely with mkdir()
9. List folder contents with iterdir()
10. Build a small path-readiness inspection workflow

Why this matters:
Most automation eventually works with files or folders. Scripts may need to
find a configuration file, validate a backup location, create a report folder,
inspect logs, or build output file names. pathlib provides a readable,
object-oriented, and cross-platform way to perform these tasks.

Safety note:
Today focuses on inspection and safe directory creation. Avoid deleting,
renaming, or overwriting important files while practising. Use dedicated test
folders and verify every target path before performing destructive operations.
"""

from pathlib import Path

print("=" * 70)
print("DAY 28 - PATHLIB")
print("Paths, file existence, and path operations")
print("=" * 70)

# ---------------------------------------------------------------------
# SECTION 1: Why Use pathlib?
# ---------------------------------------------------------------------

print("\nSECTION 1: Why Use pathlib?")

"""
pathlib is part of Python's standard library.
You do not need to install it separately.

Instead of treating a path as only a text string, pathlib represents it as a
Path object. That object provides useful methods and properties for building,
checking, inspecting, and navigating file-system paths.
"""

print("pathlib gives Python a readable way to work with files and folders.")

# ---------------------------------------------------------------------
# SECTION 2: Create Path Objects
# ---------------------------------------------------------------------

print("\nSECTION 2: Create Path Objects")

current_path = Path.cwd()
report_path = Path("reports") / "daily_status.txt"

print("Current path object:", current_path)
print("Report path object :", report_path)
print("Object type        :", type(report_path).__name__)

"""
Path.cwd() returns the current working directory as a Path object.
Path("reports") creates a relative path.

The / operator joins path parts. pathlib automatically uses the correct path
separator for Windows, Linux, or macOS.
"""

# ---------------------------------------------------------------------
# SECTION 3: Relative and Absolute Paths
# ---------------------------------------------------------------------

print("\nSECTION 3: Relative and Absolute Paths")

relative_path = Path("reports") / "health_check.txt"
absolute_path = relative_path.resolve()

print("Relative path:", relative_path)
print("Is absolute? :", relative_path.is_absolute())
print("Resolved path:", absolute_path)
print("Is absolute? :", absolute_path.is_absolute())

"""
A relative path is interpreted from the current working directory.
resolve() converts it into an absolute path. The final file does not need to
exist for this basic resolution example.
"""

# ---------------------------------------------------------------------
# SECTION 4: Inspect Path Components
# ---------------------------------------------------------------------

print("\nSECTION 4: Inspect Path Components")

sample_path = Path("reports") / "server_health.csv"

print("Full path:", sample_path)
print("Name     :", sample_path.name)
print("Stem     :", sample_path.stem)
print("Suffix   :", sample_path.suffix)
print("Parent   :", sample_path.parent)

"""
Useful properties:
- name   -> final file or directory name
- stem   -> file name without the final extension
- suffix -> final extension, including the dot
- parent -> directory containing the path

These are useful for report naming, extension checks, and routing files.
"""

# ---------------------------------------------------------------------
# SECTION 5: Check Whether Paths Exist
# ---------------------------------------------------------------------

print("\nSECTION 5: Check Whether Paths Exist")

existing_path = Path.cwd()
missing_path = Path("pathlib_practice_missing_item.tmp")

print("Current path exists:", existing_path.exists())
print("Practice item exists:", missing_path.exists())

"""
exists() returns True when the file or directory is present.
It returns False when the path is missing.

Checking existence before reading a file can prevent avoidable errors, but a
production script should still use exception handling because files can change
between the check and the actual operation.
"""

# ---------------------------------------------------------------------
# SECTION 6: Distinguish Files and Directories
# ---------------------------------------------------------------------

print("\nSECTION 6: Distinguish Files and Directories")

script_candidate = Path(__file__) if "__file__" in globals() else Path.cwd()

print("Candidate path:", script_candidate)
print("Is a file?    :", script_candidate.is_file())
print("Is directory? :", script_candidate.is_dir())

"""
is_file() is True only for an existing regular file.
is_dir() is True only for an existing directory.
A missing path normally returns False for both methods.
"""

# ---------------------------------------------------------------------
# SECTION 7: Build Paths with the / Operator
# ---------------------------------------------------------------------

print("\nSECTION 7: Build Paths with the / Operator")

base_directory = Path.cwd()
environment_name = "test"
report_name = "capacity_report.csv"
final_report_path = base_directory / "output" / environment_name / report_name

print("Base directory   :", base_directory)
print("Environment      :", environment_name)
print("Final report path:", final_report_path)

"""
The / operator keeps path construction readable.
It avoids manually adding \\ or / separators and reduces cross-platform bugs.
"""

# ---------------------------------------------------------------------
# SECTION 8: Create Directories Safely
# ---------------------------------------------------------------------

print("\nSECTION 8: Create Directories Safely")

practice_directory = Path("day28_practice") / "reports"
practice_directory.mkdir(parents=True, exist_ok=True)

print("Directory created or already present:", practice_directory)
print("Directory exists:", practice_directory.exists())
print("Is directory    :", practice_directory.is_dir())

"""
mkdir() creates a directory.
- parents=True creates missing parent directories
- exist_ok=True avoids an error when the directory already exists

Use this pattern for output folders, archive folders, and report locations.
"""

# ---------------------------------------------------------------------
# SECTION 9: List Folder Contents with iterdir()
# ---------------------------------------------------------------------

print("\nSECTION 9: List Folder Contents")

practice_file = practice_directory / "readiness.txt"
practice_file.write_text("READY\n", encoding="utf-8")

items = sorted(practice_directory.iterdir(), key=lambda item: item.name.lower())

print("Directory inspected:", practice_directory)
print("Total items        :", len(items))

for item_number, item in enumerate(items, start=1):
    print(f"{item_number}. {item.name}")

"""
iterdir() returns Path objects for the direct children of a directory.
Because each item is already a Path object, you can immediately use .name,
.is_file(), .is_dir(), .suffix, and other pathlib features.
"""

# ---------------------------------------------------------------------
# SECTION 10: Filter Files by Extension
# ---------------------------------------------------------------------

print("\nSECTION 10: Filter Files by Extension")

sample_names = ["alerts.log", "inventory.csv", "health.log", "notes.txt"]
log_paths = [Path(name) for name in sample_names if Path(name).suffix.lower() == ".log"]

print("All names:", sample_names)
print("Log files:", [path.name for path in log_paths])
print("Log count:", len(log_paths))

"""
The suffix property makes extension filtering clear.
lower() allows .LOG and .log to be treated consistently.
"""

# ---------------------------------------------------------------------
# SECTION 11: Change a File Name or Extension Safely in Memory
# ---------------------------------------------------------------------

print("\nSECTION 11: Build a New Name")

original_report = Path("daily_status.txt")
csv_report = original_report.with_suffix(".csv")
archived_report = original_report.with_name("daily_status_archive.txt")

print("Original path :", original_report)
print("CSV path      :", csv_report)
print("Archived path :", archived_report)

"""
with_suffix() and with_name() return new Path objects.
They do not rename a real file by themselves.
This makes them useful for planning output or archive names safely.
"""

# ---------------------------------------------------------------------
# SECTION 12: Build a Path Readiness Summary
# ---------------------------------------------------------------------

print("\nSECTION 12: Build a Path Readiness Summary")

required_path = practice_directory / "readiness.txt"

if required_path.is_file():
    readiness_status = "READY"
else:
    readiness_status = "ATTENTION"

summary_lines = [
    "=" * 60,
    "PATH READINESS SUMMARY",
    "=" * 60,
    f"Working directory : {Path.cwd()}",
    f"Target directory  : {practice_directory.resolve()}",
    f"Required file     : {required_path.name}",
    f"File exists       : {required_path.exists()}",
    f"Is regular file   : {required_path.is_file()}",
    f"Final status      : {readiness_status}",
    "=" * 60,
]

print("\n".join(summary_lines))

# ---------------------------------------------------------------------
# SECTION 13: Practical Validation Pattern
# ---------------------------------------------------------------------

print("\nSECTION 13: Practical Validation Pattern")

candidate_directory = Path("day28_practice")

if not candidate_directory.exists():
    validation_message = "MISSING"
elif not candidate_directory.is_dir():
    validation_message = "NOT A DIRECTORY"
else:
    validation_message = "AVAILABLE"

print("Candidate path:", candidate_directory)
print("Validation    :", validation_message)

"""
This sequence checks three different situations:
1. the path is missing
2. the path exists but is not a directory
3. the directory is available

Clear validation messages make operational scripts easier to troubleshoot.
"""

# ---------------------------------------------------------------------
# SECTION 14: Guided Practice
# ---------------------------------------------------------------------

print("\nSECTION 14: Guided Practice")

"""
Guided practice:
1. Change sample_path to a .log, .json, or .csv file and inspect its parts.
2. Build a path containing an environment folder such as prod or test.
3. Check an existing file and a missing file with exists().
4. Create a harmless nested output folder using mkdir().
5. Add two test files and inspect them using iterdir().
6. Filter the results by suffix.
7. Use resolve() to print the complete target location.
8. Remove the day28_practice folder manually after practice if desired.
"""

print("Guided practice: build, inspect, validate, and list safe test paths.")

# ---------------------------------------------------------------------
# SECTION 15: Mini Challenge
# ---------------------------------------------------------------------

print("\nSECTION 15: Mini Challenge")

"""
Build a Path Readiness Inspector.

Collect these inputs once:
1. base directory path
2. subdirectory name
3. expected file name
4. required file extension

Then:
- create Path objects from the inputs
- build the target directory with the / operator
- resolve and display the target directory
- check whether the target exists
- verify that it is a directory
- list direct child items when available
- count files and directories
- check whether the expected file exists and is a regular file
- compare its suffix with the required extension
- decide READY or ATTENTION
- print a clean final report
- handle PermissionError and OSError

Do not collect the same value more than once.
Reuse the Path objects throughout the workflow.
"""

print("Mini challenge: build an input-driven Path Readiness Inspector.")

# ---------------------------------------------------------------------
# SECTION 16: Day 28 Summary
# ---------------------------------------------------------------------

print("\nSECTION 16: Day 28 Summary")
print("Today you used Path objects, exists(), is_file(), is_dir(), and path operations.")
print("You also created directories, listed contents, and built a readiness report.")
print("Day 28 complete. Reliable automation starts with reliable paths.")
