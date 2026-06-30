"""
Python for Mammals - Day 19
Topic: Reading Files

Audience:
- Complete beginners
- DBAs, Sysadmins, Support Engineers, Cloud Engineers, Monitoring Teams
- Anyone who wants Python for practical automation

Goal of Day 19:
By the end of today, you should be able to:
1. Open a text file using open()
2. Read complete file content using read()
3. Read one line at a time using readline()
4. Read all lines as a list using readlines()
5. Use the with statement to open and close files safely
6. Start thinking about log files, reports, inventories, and health-check outputs as automation input

Why this matters:
Most operational automation starts with files.

You may need to read:
- alert logs
- application logs
- backup reports
- server inventory files
- health-check output files
- monitoring exports
- deployment checklists

Before Python can analyze a log or generate a report, it must first read the file.
Today is the entry point into real file-based automation.
"""

print("=" * 70)
print("DAY 19 - READING FILES")
print("open(), read(), readline(), readlines(), with")
print("=" * 70)

# ---------------------------------------------------------------------
# SECTION 1: Project Introduction
# ---------------------------------------------------------------------

print("\nSECTION 1: Project Introduction")

"""
Today we will read text files using Python.

To keep this lesson easy to run, this file first creates a few small
sample files. In real work, these files may already exist as logs,
reports, exports, or command outputs.
"""

print("Today we will learn how Python reads text files for automation.")

# ---------------------------------------------------------------------
# SECTION 2: Create Sample Files for Practice
# ---------------------------------------------------------------------

print("\nSECTION 2: Create Sample Files for Practice")

sample_file = open("day19_server_status.txt", "w")
sample_file.write("app01 production running\n")
sample_file.write("db01 production running\n")
sample_file.write("web01 uat maintenance\n")
sample_file.close()

log_file = open("day19_app_log.txt", "w")
log_file.write("INFO application started\n")
log_file.write("WARNING disk usage above 80 percent\n")
log_file.write("ERROR backup job failed\n")
log_file.write("INFO monitoring completed\n")
log_file.close()

print("Sample files created for today's practice.")

"""
We are using write mode only to prepare practice files.
Today's main focus is reading files.
"""

# ---------------------------------------------------------------------
# SECTION 3: open() and close()
# ---------------------------------------------------------------------

print("\nSECTION 3: open() and close()")

file_object = open("day19_server_status.txt", "r")
content = file_object.read()
file_object.close()

print(content)

"""
open() connects Python to a file.

"r" means read mode.
close() disconnects Python from the file.

If you open files manually, you should close them manually.
"""

# ---------------------------------------------------------------------
# SECTION 4: read() - Read the Complete File
# ---------------------------------------------------------------------

print("\nSECTION 4: read() - Read the Complete File")

with open("day19_app_log.txt", "r") as file_object:
    log_content = file_object.read()

print(log_content)

"""
read() reads the complete file as one string.

This is useful when:
- the file is small
- you want to search the full content
- you want to print or store the entire file text
"""

# ---------------------------------------------------------------------
# SECTION 5: readline() - Read One Line
# ---------------------------------------------------------------------

print("\nSECTION 5: readline() - Read One Line")

with open("day19_server_status.txt", "r") as file_object:
    first_line = file_object.readline()
    second_line = file_object.readline()

print("First line :", first_line.strip())
print("Second line:", second_line.strip())

"""
readline() reads one line at a time.

Each call moves to the next line.
strip() removes extra newline characters from the beginning or end.
"""

# ---------------------------------------------------------------------
# SECTION 6: readlines() - Read All Lines as a List
# ---------------------------------------------------------------------

print("\nSECTION 6: readlines() - Read All Lines as a List")

with open("day19_server_status.txt", "r") as file_object:
    lines = file_object.readlines()

print("Total lines:", len(lines))
print("First item from list:", lines[0].strip())

"""
readlines() reads all lines and returns a list.

Each line becomes one item in the list.
This is useful when you want to loop, count, filter, or process line by line.
"""

# ---------------------------------------------------------------------
# SECTION 7: Loop Through File Lines
# ---------------------------------------------------------------------

print("\nSECTION 7: Loop Through File Lines")

with open("day19_server_status.txt", "r") as file_object:
    for line in file_object:
        clean_line = line.strip()
        print("Record:", clean_line)

"""
Looping directly through the file is a common professional pattern.

It is useful for logs because you can process one line at a time.
"""

# ---------------------------------------------------------------------
# SECTION 8: Search Text Inside a File
# ---------------------------------------------------------------------

print("\nSECTION 8: Search Text Inside a File")

with open("day19_app_log.txt", "r") as file_object:
    for line in file_object:
        if "ERROR" in line:
            print("Error found:", line.strip())

"""
This is the beginning of log analysis.

You read each line and check whether it contains a keyword such as:
- ERROR
- WARNING
- FAILED
- ORA-
- timeout
- denied
"""

# ---------------------------------------------------------------------
# SECTION 9: Count Warning and Error Lines
# ---------------------------------------------------------------------

print("\nSECTION 9: Count Warning and Error Lines")

warning_count = 0
error_count = 0

with open("day19_app_log.txt", "r") as file_object:
    for line in file_object:
        if "WARNING" in line:
            warning_count = warning_count + 1
        if "ERROR" in line:
            error_count = error_count + 1

print("Warnings:", warning_count)
print("Errors  :", error_count)

"""
Counting matching lines is useful for daily summaries.

Example:
- 2 backup failures
- 5 warning messages
- 1 ORA error
- 0 failed logins
"""

# ---------------------------------------------------------------------
# SECTION 10: Convert File Lines into a List of Clean Records
# ---------------------------------------------------------------------

print("\nSECTION 10: Convert File Lines into a List of Clean Records")

server_records = []

with open("day19_server_status.txt", "r") as file_object:
    for line in file_object:
        clean_line = line.strip()
        server_records.append(clean_line)

print(server_records)

"""
After reading a file, you often store useful lines inside a list.
Later you can filter, summarize, or convert them into dictionaries.
"""

# ---------------------------------------------------------------------
# SECTION 11: Split File Lines into Columns
# ---------------------------------------------------------------------

print("\nSECTION 11: Split File Lines into Columns")

with open("day19_server_status.txt", "r") as file_object:
    for line in file_object:
        clean_line = line.strip()
        parts = clean_line.split()
        server_name = parts[0]
        environment = parts[1]
        status = parts[2]
        print(server_name, "|", environment, "|", status)

"""
split() breaks one text line into smaller pieces.

This is useful when file lines have predictable columns.
Example:
app01 production running
"""

# ---------------------------------------------------------------------
# SECTION 12: The with Statement
# ---------------------------------------------------------------------

print("\nSECTION 12: The with Statement")

with open("day19_app_log.txt", "r") as file_object:
    one_line = file_object.readline()

print("Read safely:", one_line.strip())

"""
The with statement is the recommended way to work with files.

It automatically closes the file when the block ends.
This is safer and cleaner than manually calling close().
"""

# ---------------------------------------------------------------------
# SECTION 13: Guided Practice - Read a Health Check File
# ---------------------------------------------------------------------

print("\nSECTION 13: Guided Practice - Read a Health Check File")

"""
Uncomment this block and run it.
It creates a small health-check file and reads it back.
"""

# with open("health_check.txt", "w") as file_object:
#     file_object.write("CPU OK\n")
#     file_object.write("MEMORY OK\n")
#     file_object.write("DISK WARNING\n")
#
# with open("health_check.txt", "r") as file_object:
#     for line in file_object:
#         print(line.strip())

print("Guided practice: uncomment the health-check file block.")

# ---------------------------------------------------------------------
# SECTION 14: Guided Practice - Count Failed Lines
# ---------------------------------------------------------------------

print("\nSECTION 14: Guided Practice - Count Failed Lines")

"""
Uncomment this block and run it.
It counts lines that contain FAILED.
"""

# failed_count = 0
#
# with open("backup_report.txt", "w") as file_object:
#     file_object.write("backup01 SUCCESS\n")
#     file_object.write("backup02 FAILED\n")
#     file_object.write("backup03 SUCCESS\n")
#
# with open("backup_report.txt", "r") as file_object:
#     for line in file_object:
#         if "FAILED" in line:
#             failed_count = failed_count + 1
#
# print("Failed backups:", failed_count)

print("Guided practice: uncomment the failed backup count block.")

# ---------------------------------------------------------------------
# SECTION 15: Guided Practice - Build Clean List from File
# ---------------------------------------------------------------------

print("\nSECTION 15: Guided Practice - Build Clean List from File")

"""
Uncomment this block and run it.
It reads file lines and stores clean values in a list.
"""

# clean_services = []
#
# with open("services.txt", "w") as file_object:
#     file_object.write("listener\n")
#     file_object.write("database\n")
#     file_object.write("monitoring\n")
#
# with open("services.txt", "r") as file_object:
#     for line in file_object:
#         clean_services.append(line.strip())
#
# print(clean_services)

print("Guided practice: uncomment the clean services list block.")

# ---------------------------------------------------------------------
# SECTION 16: Mini Challenge Preview
# ---------------------------------------------------------------------

print("\nSECTION 16: Mini Challenge Preview")

"""
Mini Challenge:
Build a Log Reader Summary script.

Your script should:
1. Create or read a text file containing operational log lines
2. Read the file using with open()
3. Count INFO, WARNING, and ERROR lines
4. Print each ERROR line clearly
5. Generate a final summary report

This mirrors real automation:
- read a file
- scan each line
- count useful patterns
- produce a clear operational report
"""

print("Mini challenge: build a Log Reader Summary using file reading methods.")

# ---------------------------------------------------------------------
# SECTION 17: Closing Message
# ---------------------------------------------------------------------

print("\nSECTION 17: Closing Message")

print("You have completed Day 19.")
print("You can now read text files, which is the foundation of log analysis and report automation.")
print("Next, you will learn how to write files and generate your own output reports.")
