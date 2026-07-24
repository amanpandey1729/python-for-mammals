"""
Python for Mammals - Day 29 Exercise File
Topic: Directories - Creating Folders, Renaming Folders, and Moving Files

Instructions:
1. Do not look for solutions immediately.
2. Read each task carefully.
3. Write your code below each exercise.
4. Run the file after completing each exercise.
5. Use only harmless practice folders and files.

Important:
This file contains exercises only.
No complete solutions are provided here.

Goal:
By the end of these exercises, you should be able to create directories,
rename folders, move files safely, validate paths, prevent overwrites, preview
changes, route selected files, and build a practical file-routing workflow.
"""

print("=" * 70)
print("DAY 29 EXERCISES - DIRECTORIES")
print("Creating folders, renaming folders, and moving files")
print("=" * 70)

# ---------------------------------------------------------------------
# EXERCISE 1: Import Required Tools
# ---------------------------------------------------------------------

"""
TODO:
- Import Path from pathlib
- Import shutil
- Print a short confirmation message

Concept focus:
imports
"""

# Write your code below this line




# ---------------------------------------------------------------------
# EXERCISE 2: Create a Practice Root
# ---------------------------------------------------------------------

"""
TODO:
- Create an independent Path named day29_exercise_output
- Create it with mkdir()
- Make the operation repeatable
- Print whether the path is now a directory

Concept focus:
mkdir() + exist_ok
"""

# Write your code below this line




# ---------------------------------------------------------------------
# EXERCISE 3: Create One Report Folder
# ---------------------------------------------------------------------

"""
TODO:
- Create an independent folder path:
  day29_exercise_output/reports
- Create the folder safely
- Print the path and readiness result

Concept focus:
single-directory creation
"""

# Write your code below this line




# ---------------------------------------------------------------------
# EXERCISE 4: Create Nested Environment Folders
# ---------------------------------------------------------------------

"""
TODO:
- Independently create:
  day29_exercise_output/output/test/daily
- Use parents=True and exist_ok=True
- Print whether the final directory exists

Concept focus:
nested-directory creation
"""

# Write your code below this line




# ---------------------------------------------------------------------
# EXERCISE 5: Create a Standard Workspace
# ---------------------------------------------------------------------

"""
TODO:
- Create an independent list containing:
  incoming, processed, archive, failed
- Create each folder under day29_exercise_output/workspace
- Use a loop
- Print one readiness line per folder

Concept focus:
repeatable workspace preparation
"""

# Write your code below this line




# ---------------------------------------------------------------------
# EXERCISE 6: Rename an Empty Folder
# ---------------------------------------------------------------------

"""
TODO:
- Work only inside day29_exercise_output/exercise6
- Create a folder named pending
- Rename it to completed
- Print whether the old path exists
- Print whether the new path exists
- Make your practice repeatable without deleting non-empty folders

Concept focus:
Path.rename()
"""

# Write your code below this line




# ---------------------------------------------------------------------
# EXERCISE 7: Validate a Rename Request
# ---------------------------------------------------------------------

"""
TODO:
- Ask the user for:
  parent directory path
  current folder name
  new folder name
- Build both paths once
- Print one decision:
  SOURCE MISSING
  SOURCE IS NOT A DIRECTORY
  DESTINATION EXISTS
  READY TO RENAME
- Do not perform the rename

Concept focus:
pre-change validation
"""

# Write your code below this line




# ---------------------------------------------------------------------
# EXERCISE 8: Move One Practice File
# ---------------------------------------------------------------------

"""
TODO:
- Work only inside day29_exercise_output/exercise8
- Create source and destination folders
- Create a small source file named status.txt
- Move it into the destination folder with shutil.move()
- Print source existence after the move
- Print destination existence after the move
- Prevent accidental overwrite when the exercise is run again

Concept focus:
shutil.move()
"""

# Write your code below this line




# ---------------------------------------------------------------------
# EXERCISE 9: Move and Rename a File
# ---------------------------------------------------------------------

"""
TODO:
- Work only inside day29_exercise_output/exercise9
- Create a source file named raw_capacity.tmp
- Move it to an archive folder
- Rename it to capacity_report.txt during the move
- Print the final file name and final path
- Prevent accidental overwrite

Concept focus:
move + rename
"""

# Write your code below this line




# ---------------------------------------------------------------------
# EXERCISE 10: Build a Move Readiness Check
# ---------------------------------------------------------------------

"""
TODO:
- Independently ask for:
  source file path
  destination directory path
- Build the final destination file using the source file name
- Print one status:
  SOURCE MISSING
  SOURCE IS NOT A FILE
  DESTINATION DIRECTORY MISSING
  DESTINATION ALREADY EXISTS
  READY TO MOVE
- Do not move anything

Concept focus:
safe operational decision logic
"""

# Write your code below this line




# ---------------------------------------------------------------------
# EXERCISE 11: Add Preview Mode
# ---------------------------------------------------------------------

"""
TODO:
- Independently ask for:
  source file path
  destination directory path
  execution mode: preview or move
- Validate the paths
- In preview mode, print the planned source and destination only
- In move mode, perform the move only when validation passes
- Reject unsupported mode values
- Handle PermissionError and OSError

Concept focus:
dry-run / preview design
"""

# Write your code below this line




# ---------------------------------------------------------------------
# EXERCISE 12: Move Files by Extension
# ---------------------------------------------------------------------

"""
TODO:
- Work only inside day29_exercise_output/exercise12
- Create source and destination directories
- Create harmless sample files:
  app.log, inventory.csv, alert.LOG, notes.txt
- Move only .log files, case-insensitively
- Print each moved file name
- Print the final moved count
- Avoid overwriting an existing destination file

Concept focus:
extension-based routing
"""

# Write your code below this line




# ---------------------------------------------------------------------
# EXERCISE 13: Route Reports by Environment
# ---------------------------------------------------------------------

"""
TODO:
- Independently ask for:
  base directory path
  environment name
  report file path
- Normalize the environment name with strip() and lower()
- Allow only dev, test, and prod
- Build <base>/reports/<environment>
- Create the destination directory safely
- Validate that the report source is a file
- Print the planned destination
- Do not move the file

Concept focus:
input-driven destination construction
"""

# Write your code below this line




# ---------------------------------------------------------------------
# EXERCISE 14: Prevent Duplicate Deliveries
# ---------------------------------------------------------------------

"""
TODO:
- Independently ask for:
  source file path
  destination directory path
- Build the final destination path
- Print:
  READY when the source is a file and destination does not exist
  SKIP when the destination already exists
  ATTENTION for invalid source or destination
- Do not overwrite or delete anything

Concept focus:
duplicate prevention
"""

# Write your code below this line




# ---------------------------------------------------------------------
# EXERCISE 15: Produce a Routing Summary
# ---------------------------------------------------------------------

"""
TODO:
- Work inside an independent harmless practice folder
- Create source and destination directories
- Create at least four sample files with mixed extensions
- Select one required extension
- Count:
  total files discovered
  matching files
  files ready to move
  files skipped because destination exists
- Print a compact report
- Do not perform moves

Concept focus:
planning and reporting
"""

# Write your code below this line




# ---------------------------------------------------------------------
# EXERCISE 16: Mini Project - File Routing Assistant
# ---------------------------------------------------------------------

"""
Build a complete File Routing Assistant.

Collect all required user inputs once at the beginning:
1. Base directory path
2. Source folder name
3. Destination folder name
4. Required file extension
5. Execution mode: preview or move

TODO:
- Convert the base directory input to a Path object
- Normalize folder names and the required extension appropriately
- Add a leading dot to the extension when the user omits it
- Build reusable source and destination Path objects
- Reuse the same variables throughout the workflow
- Validate that the base path exists and is a directory
- Validate that the source path exists and is a directory
- Create the destination directory safely only after base validation
- Inspect direct child items of the source directory
- Select regular files matching the required extension case-insensitively
- Sort selected files by name
- Build a move plan for every selected file
- For each planned file:
    destination = destination directory / source file name
- Never overwrite an existing destination file
- In preview mode:
    print the move plan
    do not move any file
- In move mode:
    move only validated, non-duplicate files
- Count:
    total direct-child items
    regular files discovered
    extension matches
    files planned
    files moved
    files skipped
    files failed
- Generate a clean final report containing:
    base directory
    source directory
    destination directory
    required extension
    execution mode
    all counts
    final status
    sorted move-plan entries
- Choose a meaningful final status such as:
    PREVIEW COMPLETE
    MOVE COMPLETE
    PARTIAL
    NOTHING TO PROCESS
    ATTENTION
- Handle at least:
    PermissionError
    OSError

Important:
- Collect every input only once.
- Do not ask for the same value again.
- Preview mode must make no file-system move.
- Do not delete or overwrite files.
- The final result should feel like one complete automation workflow.
"""

# Write your code below this line




print("\nEnd of Day 29 exercises. Complete the TODO sections one by one.")
