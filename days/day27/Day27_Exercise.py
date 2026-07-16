"""
Python for Mammals - Day 27 Exercise File
Topic: OS Module - os.getcwd(), os.listdir(), Environment Basics

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
By the end of these exercises, you should be able to inspect the current
working directory, list files and folders, read selected environment
variables safely, and build a small OS environment inspection workflow.
"""

print("=" * 70)
print("DAY 27 EXERCISES - OS MODULE")
print("os.getcwd(), os.listdir(), environment basics")
print("=" * 70)

# ---------------------------------------------------------------------
# EXERCISE 1: Import the OS Module
# ---------------------------------------------------------------------

"""
TODO:
- Import the os module
- Print a message confirming that the module is ready

Concept focus:
module import
"""

# Write your code below this line




# ---------------------------------------------------------------------
# EXERCISE 2: Display the Current Working Directory
# ---------------------------------------------------------------------

"""
TODO:
- Use os.getcwd()
- Store the result in a variable
- Print a clear label and the directory

Concept focus:
os.getcwd()
"""

# Write your code below this line




# ---------------------------------------------------------------------
# EXERCISE 3: Build a Report Location
# ---------------------------------------------------------------------

"""
TODO:
- Get the current working directory
- Create an independent report file name such as daily_status.txt
- Use os.path.join() to combine them
- Print the complete report location

Concept focus:
working directory + path joining
"""

# Write your code below this line




# ---------------------------------------------------------------------
# EXERCISE 4: List the Current Directory
# ---------------------------------------------------------------------

"""
TODO:
- Use os.listdir() without an argument
- Store the returned names in a list
- Print the complete list
- Print the total number of items

Concept focus:
os.listdir()
"""

# Write your code below this line




# ---------------------------------------------------------------------
# EXERCISE 5: Print One Item per Line
# ---------------------------------------------------------------------

"""
TODO:
- List the current directory
- Sort the names
- Print each item on a separate line with a sequence number

Concept focus:
list directory + loop + enumerate
"""

# Write your code below this line




# ---------------------------------------------------------------------
# EXERCISE 6: Inspect a User-Selected Directory
# ---------------------------------------------------------------------

"""
TODO:
- Ask the user for one directory path
- Use os.listdir(path) to inspect it
- Print every item in sorted order
- Handle FileNotFoundError
- Handle PermissionError

Concept focus:
listing a specific directory safely
"""

# Write your code below this line




# ---------------------------------------------------------------------
# EXERCISE 7: Count Files and Directories
# ---------------------------------------------------------------------

"""
TODO:
- Use the current working directory
- Loop through its items
- Build each complete item path with os.path.join()
- Count files with os.path.isfile()
- Count directories with os.path.isdir()
- Print both counts

Concept focus:
classifying directory contents
"""

# Write your code below this line




# ---------------------------------------------------------------------
# EXERCISE 8: Search for an Expected File Name
# ---------------------------------------------------------------------

"""
TODO:
- Ask the user for one expected file name
- List the current directory
- Check whether the exact name is present
- Print FOUND or MISSING

Concept focus:
membership validation
"""

# Write your code below this line




# ---------------------------------------------------------------------
# EXERCISE 9: Read a Common Environment Variable
# ---------------------------------------------------------------------

"""
TODO:
- Read USERNAME using os.getenv()
- If it is unavailable, try USER
- If both are unavailable, use UNKNOWN
- Print the final value

Concept focus:
os.getenv() + fallback values
"""

# Write your code below this line




# ---------------------------------------------------------------------
# EXERCISE 10: Read an Application Environment
# ---------------------------------------------------------------------

"""
TODO:
- Read APP_ENV using os.getenv()
- Use DEVELOPMENT as the default
- Normalize it with strip() and upper()
- Print the normalized environment

Concept focus:
environment variables + defaults
"""

# Write your code below this line




# ---------------------------------------------------------------------
# EXERCISE 11: Decide an Execution Mode
# ---------------------------------------------------------------------

"""
TODO:
- Independently read APP_ENV with DEVELOPMENT as the default
- Normalize the value
- Decide:
    CAUTIOUS for PRODUCTION
    VALIDATION for TEST, UAT, or STAGING
    DEVELOPMENT for every other value
- Print the execution mode

Concept focus:
environment-aware conditions
"""

# Write your code below this line




# ---------------------------------------------------------------------
# EXERCISE 12: Inspect Only Approved Variables
# ---------------------------------------------------------------------

"""
TODO:
- Create a list containing these names:
  APP_ENV, HOME, USERPROFILE, TEMP, TMP
- Loop through the list
- Read each value with os.getenv()
- Use NOT SET as the default
- Print name and value

Important:
Do not print the complete os.environ mapping.

Concept focus:
safe allow-list inspection
"""

# Write your code below this line




# ---------------------------------------------------------------------
# EXERCISE 13: Build a Compact Folder Summary
# ---------------------------------------------------------------------

"""
TODO:
- Independently inspect the current working directory
- Calculate total items, file count, and directory count
- Build a clear multi-line summary
- Print the summary

Concept focus:
operational report formatting
"""

# Write your code below this line




# ---------------------------------------------------------------------
# EXERCISE 14: Validate Required Operational Files
# ---------------------------------------------------------------------

"""
TODO:
- Create an independent list of required names such as:
  config.ini, inventory.csv, runbook.txt
- List the current directory once
- For each required name, print FOUND or MISSING
- Count how many required files are missing
- Print the final missing count

Concept focus:
folder validation checklist
"""

# Write your code below this line




# ---------------------------------------------------------------------
# EXERCISE 15: Create a Readiness Decision
# ---------------------------------------------------------------------

"""
TODO:
- Ask for:
  total required files
  missing required files
  environment name
- Normalize the environment name
- Decide ATTENTION when any file is missing
- Otherwise decide READY
- Print a compact readiness summary

Concept focus:
combining environment and validation data
"""

# Write your code below this line




# ---------------------------------------------------------------------
# EXERCISE 16: Mini Project - OS Environment Inspector
# ---------------------------------------------------------------------

"""
Build a complete OS Environment Inspector.

Collect all required user inputs once at the beginning:
1. Directory path to inspect
2. Expected file name
3. Environment-variable name to inspect

TODO:
- Store all three inputs in variables and reuse them
- Display the script's current working directory using os.getcwd()
- Validate that the requested directory exists
- List the requested directory using os.listdir(path)
- Sort the returned names
- Count total items
- Count files using os.path.isfile()
- Count directories using os.path.isdir()
- Check whether the expected file name is present
- Read only the requested environment variable with os.getenv()
- Use NOT SET as its default value
- Decide final status:
    ATTENTION when the expected file is missing
    READY when the expected file is present
- Generate a clean report containing:
    current working directory
    inspected directory
    total item count
    file count
    directory count
    expected file name
    expected file status
    requested environment-variable name
    requested environment-variable value
    final status
    sorted item list
- Print the complete report
- Handle at least:
    FileNotFoundError
    PermissionError
    NotADirectoryError

Important:
- Collect each input only once.
- Reuse the same variables throughout the workflow.
- Do not ask for the same value again.
- Do not print all environment variables.
- The final result should feel like one complete automation workflow.
"""

# Write your code below this line




print("\nEnd of Day 27 exercises. Complete the TODO sections one by one.")
