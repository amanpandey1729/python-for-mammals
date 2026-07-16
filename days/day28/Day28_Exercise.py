"""
Python for Mammals - Day 28 Exercise File
Topic: pathlib - Paths, File Existence, and Path Operations

Instructions:
1. Do not look for solutions immediately.
2. Read each task carefully.
3. Write your code below each exercise.
4. Run the file after completing each exercise.
5. Fix errors patiently. Errors are part of learning.

Important:
This file contains exercises only.
No complete solutions are provided here.

Goal:
By the end of these exercises, you should be able to create Path objects,
build cross-platform paths, validate files and directories, inspect path
components, list folder contents, and build a practical readiness workflow.
"""

print("=" * 70)
print("DAY 28 EXERCISES - PATHLIB")
print("Paths, file existence, and path operations")
print("=" * 70)

# ---------------------------------------------------------------------
# EXERCISE 1: Import Path
# ---------------------------------------------------------------------

"""
TODO:
- Import Path from pathlib
- Print a message confirming that pathlib is ready

Concept focus:
module import
"""

# Write your code below this line




# ---------------------------------------------------------------------
# EXERCISE 2: Display the Current Path
# ---------------------------------------------------------------------

"""
TODO:
- Use Path.cwd()
- Store the result in a variable
- Print a clear label and the path
- Print the object's type name

Concept focus:
Path.cwd() + Path objects
"""

# Write your code below this line




# ---------------------------------------------------------------------
# EXERCISE 3: Build a Report Path
# ---------------------------------------------------------------------

"""
TODO:
- Create an independent Path for a folder named reports
- Create a file name such as daily_status.txt
- Join them with the / operator
- Print the complete relative path

Concept focus:
path construction
"""

# Write your code below this line




# ---------------------------------------------------------------------
# EXERCISE 4: Inspect Path Components
# ---------------------------------------------------------------------

"""
TODO:
- Create a Path such as output/server_inventory.csv
- Print its name
- Print its stem
- Print its suffix
- Print its parent

Concept focus:
name, stem, suffix, parent
"""

# Write your code below this line




# ---------------------------------------------------------------------
# EXERCISE 5: Resolve an Absolute Path
# ---------------------------------------------------------------------

"""
TODO:
- Create a relative path for reports/health.txt
- Print whether it is absolute
- Resolve it to an absolute path
- Print the resolved path
- Print whether the resolved path is absolute

Concept focus:
relative paths + resolve()
"""

# Write your code below this line




# ---------------------------------------------------------------------
# EXERCISE 6: Check Path Existence
# ---------------------------------------------------------------------

"""
TODO:
- Ask the user for one file or directory path
- Convert the input to a Path object
- Use exists()
- Print EXISTS or MISSING

Concept focus:
exists()
"""

# Write your code below this line




# ---------------------------------------------------------------------
# EXERCISE 7: Classify a User-Selected Path
# ---------------------------------------------------------------------

"""
TODO:
- Ask the user for one path
- Convert it to a Path object
- Print FILE when is_file() is true
- Print DIRECTORY when is_dir() is true
- Otherwise print MISSING OR UNSUPPORTED

Concept focus:
is_file() + is_dir()
"""

# Write your code below this line




# ---------------------------------------------------------------------
# EXERCISE 8: Build an Environment Report Location
# ---------------------------------------------------------------------

"""
TODO:
- Ask independently for:
  environment name
  report file name
- Start from Path.cwd()
- Build output/<environment>/<report file name>
- Normalize the environment name with strip() and lower()
- Print the final path

Concept focus:
input-driven path construction
"""

# Write your code below this line




# ---------------------------------------------------------------------
# EXERCISE 9: Create a Safe Output Directory
# ---------------------------------------------------------------------

"""
TODO:
- Create a Path for day28_output/reports
- Use mkdir() with parents=True and exist_ok=True
- Print whether it now exists
- Print whether it is a directory

Concept focus:
mkdir()
"""

# Write your code below this line




# ---------------------------------------------------------------------
# EXERCISE 10: List Direct Children
# ---------------------------------------------------------------------

"""
TODO:
- Ask the user for one directory path
- Validate that it exists and is a directory
- Use iterdir() to get its direct children
- Sort the children by name
- Print one item per line
- Handle PermissionError

Concept focus:
iterdir() + validation
"""

# Write your code below this line




# ---------------------------------------------------------------------
# EXERCISE 11: Count Files and Directories
# ---------------------------------------------------------------------

"""
TODO:
- Independently ask for one directory path
- Validate it
- Loop through direct children using iterdir()
- Count regular files
- Count directories
- Print both counts and the total item count

Concept focus:
folder inventory
"""

# Write your code below this line




# ---------------------------------------------------------------------
# EXERCISE 12: Filter by Extension
# ---------------------------------------------------------------------

"""
TODO:
- Create an independent list of names such as:
  alerts.log, inventory.csv, health.log, notes.txt
- Convert each name to a Path object
- Keep only paths whose suffix is .log
- Print the matching names and final count
- Make the comparison case-insensitive

Concept focus:
suffix filtering
"""

# Write your code below this line




# ---------------------------------------------------------------------
# EXERCISE 13: Build New File Names
# ---------------------------------------------------------------------

"""
TODO:
- Create a Path for daily_report.txt
- Use with_suffix() to build daily_report.csv
- Use with_name() to build daily_report_archive.txt
- Print all three paths
- Do not rename or create any real file

Concept focus:
with_suffix() + with_name()
"""

# Write your code below this line




# ---------------------------------------------------------------------
# EXERCISE 14: Validate Required Operational Files
# ---------------------------------------------------------------------

"""
TODO:
- Ask for one directory path
- Create an independent list of required names such as:
  config.ini, inventory.csv, runbook.txt
- Build each required path with the / operator
- Print FOUND when it is a file
- Otherwise print MISSING
- Print the final missing count

Concept focus:
path-based checklist validation
"""

# Write your code below this line




# ---------------------------------------------------------------------
# EXERCISE 15: Produce a Readiness Decision
# ---------------------------------------------------------------------

"""
TODO:
- Ask independently for:
  target directory path
  expected file name
  required extension such as .csv
- Build the expected file path
- Decide ATTENTION when:
  the directory is missing, or
  the target is not a directory, or
  the expected file is missing, or
  the suffix does not match
- Otherwise decide READY
- Print a compact readiness summary

Concept focus:
combining path validation checks
"""

# Write your code below this line




# ---------------------------------------------------------------------
# EXERCISE 16: Mini Project - Path Readiness Inspector
# ---------------------------------------------------------------------

"""
Build a complete Path Readiness Inspector.

Collect all required user inputs once at the beginning:
1. Base directory path
2. Subdirectory name
3. Expected file name
4. Required file extension

TODO:
- Convert the base directory input to a Path object
- Normalize the subdirectory name and extension appropriately
- Build the target directory with the / operator
- Build the expected file path from the target directory
- Reuse these Path objects throughout the workflow
- Display:
    base directory
    target directory
    resolved target directory
    expected file path
- Validate whether the base directory exists
- Validate whether the target directory exists
- Validate whether the target is a directory
- When available, list direct child items with iterdir()
- Sort items by name
- Count total items
- Count regular files
- Count directories
- Check whether the expected file exists
- Check whether it is a regular file
- Compare its suffix with the required extension case-insensitively
- Decide final status:
    READY only when the target directory is valid, the expected file is a
    regular file, and the extension matches
    ATTENTION for every other result
- Generate a clean report containing:
    base directory
    target directory
    resolved target directory
    total item count
    file count
    directory count
    expected file name
    expected file existence
    expected file type result
    expected suffix
    required suffix
    suffix match result
    final status
    sorted direct-child item list
- Handle at least:
    PermissionError
    OSError

Important:
- Collect each input only once.
- Reuse the same variables and Path objects throughout the workflow.
- Do not ask for the same value again.
- Do not delete, rename, or overwrite files.
- The final result should feel like one complete automation workflow.
"""

# Write your code below this line




print("\nEnd of Day 28 exercises. Complete the TODO sections one by one.")
