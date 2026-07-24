"""
Python for Mammals - Day 29
Topic: Directories - Creating Folders, Renaming Folders, and Moving Files

Audience:
- Complete beginners
- DBAs, Sysadmins, Support Engineers, Cloud Engineers, Monitoring Teams
- Anyone who wants Python for practical automation

Goal of Day 29:
By the end of today, you should be able to:
1. Create one directory with pathlib
2. Create nested directory structures safely
3. Understand parents=True and exist_ok=True
4. Rename directories with Path.rename()
5. Move files between directories with shutil.move()
6. Validate source and destination paths before acting
7. Avoid accidental overwrites
8. Preview file operations before executing them
9. Handle common file-system errors
10. Build a small report-routing workflow

Why this matters:
Operational automation often creates dated report folders, prepares archive
locations, renames completed work areas, and routes files to the correct
destination. These tasks appear in backup handling, log collection, inventory
processing, report delivery, deployment preparation, and daily cleanup jobs.

Safety note:
Creating, renaming, and moving items changes the file system. Practise only
inside the dedicated day29_practice directory created by this file. Never test
automation against production folders until paths, permissions, naming rules,
and overwrite behaviour have been verified.
"""

from pathlib import Path
import shutil

print("=" * 70)
print("DAY 29 - DIRECTORIES")
print("Creating folders, renaming folders, and moving files")
print("=" * 70)

# ---------------------------------------------------------------------
# SECTION 1: Why Directory Automation Matters
# ---------------------------------------------------------------------

print("\nSECTION 1: Why Directory Automation Matters")

"""
Many repeatable workflows follow the same pattern:

    create destination -> validate source -> move item -> confirm result

Examples:
- create a folder for today's reports
- rename an incoming folder after processing
- move completed files into an archive
- route logs according to environment or status
"""

print("Directory automation helps organize repeatable operational workflows.")

# ---------------------------------------------------------------------
# SECTION 2: Prepare a Safe Practice Area
# ---------------------------------------------------------------------

print("\nSECTION 2: Prepare a Safe Practice Area")

practice_root = Path("day29_practice")
practice_root.mkdir(exist_ok=True)

print("Practice root :", practice_root)
print("Exists        :", practice_root.exists())
print("Is directory  :", practice_root.is_dir())

"""
exist_ok=True makes this example repeatable. If day29_practice already exists
as a directory, Python continues without raising FileExistsError.
"""

# ---------------------------------------------------------------------
# SECTION 3: Create One Folder
# ---------------------------------------------------------------------

print("\nSECTION 3: Create One Folder")

reports_directory = practice_root / "reports"
reports_directory.mkdir(exist_ok=True)

print("Created or available:", reports_directory)
print("Directory ready     :", reports_directory.is_dir())

# ---------------------------------------------------------------------
# SECTION 4: Create Nested Folders
# ---------------------------------------------------------------------

print("\nSECTION 4: Create Nested Folders")

nested_directory = practice_root / "output" / "test" / "daily"
nested_directory.mkdir(parents=True, exist_ok=True)

print("Nested directory:", nested_directory)
print("Directory ready :", nested_directory.is_dir())

"""
parents=True creates missing parent directories.
exist_ok=True allows the same script to run again safely.
This pattern is useful for environment-based and date-based report folders.
"""

# ---------------------------------------------------------------------
# SECTION 5: Create Multiple Operational Folders
# ---------------------------------------------------------------------

print("\nSECTION 5: Create Multiple Operational Folders")

folder_names = ["incoming", "processed", "archive"]

for folder_name in folder_names:
    folder_path = practice_root / folder_name
    folder_path.mkdir(exist_ok=True)
    print("Ready:", folder_path)

"""
A loop can prepare a standard workspace consistently.
Each Path object is built from the same trusted practice root.
"""

# ---------------------------------------------------------------------
# SECTION 6: Rename a Folder
# ---------------------------------------------------------------------

print("\nSECTION 6: Rename a Folder")

old_directory = practice_root / "pending_review"
new_directory = practice_root / "review_complete"

# Reset only these harmless practice folders so the example stays repeatable.
if new_directory.exists() and new_directory.is_dir():
    new_directory.rmdir()
if not old_directory.exists():
    old_directory.mkdir()

renamed_path = old_directory.rename(new_directory)

print("Old path exists:", old_directory.exists())
print("New path exists:", renamed_path.exists())
print("New folder name:", renamed_path.name)

"""
Path.rename() changes the directory name and returns a Path for the new
location. The source must exist, and the destination must not contain an item
that would make the operation unsafe or invalid.
"""

# ---------------------------------------------------------------------
# SECTION 7: Create a Practice File
# ---------------------------------------------------------------------

print("\nSECTION 7: Create a Practice File")

incoming_directory = practice_root / "incoming"
source_file = incoming_directory / "daily_health.txt"
source_file.write_text("Status: READY\n", encoding="utf-8")

print("Source file :", source_file)
print("File exists :", source_file.is_file())

# ---------------------------------------------------------------------
# SECTION 8: Move a File with shutil.move()
# ---------------------------------------------------------------------

print("\nSECTION 8: Move a File")

processed_directory = practice_root / "processed"
destination_file = processed_directory / source_file.name

# Remove only the previous practice destination to keep the lesson repeatable.
if destination_file.exists():
    destination_file.unlink()

moved_location = Path(shutil.move(str(source_file), str(destination_file)))

print("Source exists      :", source_file.exists())
print("Destination exists :", moved_location.is_file())
print("Moved file         :", moved_location)

"""
shutil.move() can move files between directories.
Converting Path objects with str() keeps the intent clear and works with the
function on supported Python versions.
"""

# ---------------------------------------------------------------------
# SECTION 9: Move and Rename in One Operation
# ---------------------------------------------------------------------

print("\nSECTION 9: Move and Rename Together")

second_source = incoming_directory / "capacity.tmp"
second_source.write_text("Usage: 64%\n", encoding="utf-8")
renamed_destination = processed_directory / "capacity_report.txt"

if renamed_destination.exists():
    renamed_destination.unlink()

final_location = Path(shutil.move(str(second_source), str(renamed_destination)))

print("Original name exists:", second_source.exists())
print("Final file exists   :", final_location.is_file())
print("Final file name     :", final_location.name)

"""
The destination may include a different file name.
This allows one operation to move and rename a file.
"""

# ---------------------------------------------------------------------
# SECTION 10: Validate Before Moving
# ---------------------------------------------------------------------

print("\nSECTION 10: Validate Before Moving")

candidate_source = processed_directory / "daily_health.txt"
candidate_destination = practice_root / "archive" / candidate_source.name

if not candidate_source.is_file():
    move_status = "SOURCE MISSING"
elif not candidate_destination.parent.is_dir():
    move_status = "DESTINATION DIRECTORY MISSING"
elif candidate_destination.exists():
    move_status = "DESTINATION ALREADY EXISTS"
else:
    move_status = "READY TO MOVE"

print("Source      :", candidate_source)
print("Destination :", candidate_destination)
print("Move status :", move_status)

"""
Validation reduces accidental overwrites and makes failures easier to explain.
A production script should still handle exceptions because file-system state
can change after validation.
"""

# ---------------------------------------------------------------------
# SECTION 11: Preview Before Execution
# ---------------------------------------------------------------------

print("\nSECTION 11: Preview Before Execution")

preview_source = processed_directory / "capacity_report.txt"
preview_destination = practice_root / "archive" / preview_source.name
execute_move = False

print("Planned source      :", preview_source)
print("Planned destination :", preview_destination)
print("Execute move        :", execute_move)

if execute_move:
    shutil.move(str(preview_source), str(preview_destination))
    print("Result              : MOVED")
else:
    print("Result              : PREVIEW ONLY")

"""
A preview or dry-run option is valuable in operational scripts.
It lets users verify planned changes before modifying the file system.
"""

# ---------------------------------------------------------------------
# SECTION 12: Move Files by Extension
# ---------------------------------------------------------------------

print("\nSECTION 12: Move Files by Extension")

routing_source = practice_root / "routing_source"
routing_target = practice_root / "routing_target"
routing_source.mkdir(exist_ok=True)
routing_target.mkdir(exist_ok=True)

for old_item in routing_source.iterdir():
    if old_item.is_file():
        old_item.unlink()
for old_item in routing_target.iterdir():
    if old_item.is_file():
        old_item.unlink()

sample_files = ["alert.log", "inventory.csv", "health.log", "notes.txt"]

for file_name in sample_files:
    (routing_source / file_name).touch()

moved_names = []

for item in sorted(routing_source.iterdir(), key=lambda path: path.name.lower()):
    if item.is_file() and item.suffix.lower() == ".log":
        destination = routing_target / item.name
        shutil.move(str(item), str(destination))
        moved_names.append(item.name)

print("Moved log files:", moved_names)
print("Moved count    :", len(moved_names))

# ---------------------------------------------------------------------
# SECTION 13: Handle Common Errors
# ---------------------------------------------------------------------

print("\nSECTION 13: Handle Common Errors")

missing_source = practice_root / "incoming" / "missing_report.txt"
safe_destination = practice_root / "archive" / missing_source.name

try:
    if not missing_source.is_file():
        raise FileNotFoundError(f"Source file not found: {missing_source}")
    shutil.move(str(missing_source), str(safe_destination))
except FileNotFoundError as error:
    print("Move skipped:", error)
except PermissionError:
    print("Move skipped: permission denied")
except OSError as error:
    print("Move skipped:", error)

# ---------------------------------------------------------------------
# SECTION 14: Guided Practice
# ---------------------------------------------------------------------

print("\nSECTION 14: Guided Practice")

"""
Guided practice:
1. Create a harmless folder named reports inside day29_practice.
2. Create nested folders for output/prod/daily.
3. Create an empty folder and rename it.
4. Create a small test file and move it into archive.
5. Move another file while changing its name.
6. Add a destination-exists check before moving.
7. Add a preview flag that prevents the real move.
8. Route only .csv or .log files into a matching folder.
9. Run the script twice and observe which safeguards make it repeatable.
"""

print("Guided practice: create, validate, rename, preview, and move safely.")

# ---------------------------------------------------------------------
# SECTION 15: Mini Challenge
# ---------------------------------------------------------------------

print("\nSECTION 15: Mini Challenge")

"""
Build a File Routing Assistant.

Collect these inputs once:
1. base directory path
2. source folder name
3. destination folder name
4. required file extension
5. execution mode: preview or move

Then:
- build reusable Path objects
- validate the base and source directories
- create the destination directory safely when appropriate
- inspect only direct child files
- select files matching the required extension
- show a move plan
- prevent overwriting existing destination files
- move files only when execution mode is move
- count discovered, matched, moved, skipped, and failed files
- print a clean final report
- handle PermissionError and OSError

Do not collect the same input more than once.
Do not delete files.
Preview mode must make no move.
"""

print("Mini challenge: build a safe, input-driven File Routing Assistant.")

# ---------------------------------------------------------------------
# SECTION 16: Day 29 Summary
# ---------------------------------------------------------------------

print("\nSECTION 16: Day 29 Summary")
print("Today you created nested folders, renamed folders, and moved files.")
print("You also validated paths, prevented overwrites, and used preview mode.")
print("Day 29 complete. Safe automation plans first and changes second.")
