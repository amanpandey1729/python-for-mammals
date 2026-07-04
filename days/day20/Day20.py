"""
Python for Mammals - Day 20
Topic: Writing Files

Audience:
- Complete beginners
- DBAs, Sysadmins, Support Engineers, Cloud Engineers, Monitoring Teams
- Anyone who wants Python for practical automation

Goal of Day 20:
By the end of today, you should be able to:
1. Create a new text file using write mode
2. Write text into a file using write()
3. Add new content to an existing file using append mode
4. Use \n correctly to create multiple lines
5. Generate simple text reports from Python
6. Start thinking like an automation engineer who produces reusable output files

Why this matters:
Reading files helps Python consume information.
Writing files helps Python produce useful results.

In real automation, your script may generate:
- daily health-check reports
- backup verification summaries
- server inventory files
- alert validation reports
- cleanup logs
- deployment notes
- capacity tracking summaries

Today you move from only seeing output on screen to saving output in files.
"""

print("=" * 70)
print("DAY 20 - WRITING FILES")
print("write(), append mode, creating reports")
print("=" * 70)

# ---------------------------------------------------------------------
# SECTION 1: Project Introduction
# ---------------------------------------------------------------------

print("\nSECTION 1: Project Introduction")

"""
Yesterday you learned how to read files.
Today you will learn how to write files.

This is important because printing output is temporary.
A written report can be shared, stored, attached, compared, or reviewed later.
"""

print("Today we will create files and generate simple automation reports.")

# ---------------------------------------------------------------------
# SECTION 2: write() - Create a Simple File
# ---------------------------------------------------------------------

print("\nSECTION 2: write() - Create a Simple File")

file_object = open("day20_notes.txt", "w")
file_object.write("Python can write text into files.\n")
file_object.write("Reports are useful automation outputs.\n")
file_object.close()

print("day20_notes.txt created successfully.")

"""
"w" means write mode.

Important:
If the file does not exist, Python creates it.
If the file already exists, write mode replaces the old content.
"""

# ---------------------------------------------------------------------
# SECTION 3: Read Back the Written File
# ---------------------------------------------------------------------

print("\nSECTION 3: Read Back the Written File")

with open("day20_notes.txt", "r") as file_object:
    content = file_object.read()

print(content)

"""
After writing a file, it is common to read it back during practice.
This confirms that the file was created correctly.
"""

# ---------------------------------------------------------------------
# SECTION 4: Use with open() for Writing
# ---------------------------------------------------------------------

print("\nSECTION 4: Use with open() for Writing")

with open("day20_server_report.txt", "w") as report_file:
    report_file.write("Server Report\n")
    report_file.write("-------------\n")
    report_file.write("app01 production running\n")
    report_file.write("db01 production running\n")
    report_file.write("web01 uat maintenance\n")

print("day20_server_report.txt created using with open().")

"""
The with statement automatically closes the file.
This is the recommended pattern for file writing.
"""

# ---------------------------------------------------------------------
# SECTION 5: New Line Character \n
# ---------------------------------------------------------------------

print("\nSECTION 5: New Line Character")

with open("day20_lines.txt", "w") as file_object:
    file_object.write("Line 1\n")
    file_object.write("Line 2\n")
    file_object.write("Line 3\n")

with open("day20_lines.txt", "r") as file_object:
    lines_content = file_object.read()

print(lines_content)

"""
\n means new line.

Without \n, multiple write() calls may appear on the same line.
This matters when creating readable reports.
"""

# ---------------------------------------------------------------------
# SECTION 6: Write Variables into a File
# ---------------------------------------------------------------------

print("\nSECTION 6: Write Variables into a File")

server_name = "db01"
environment = "production"
status = "running"

with open("day20_status.txt", "w") as file_object:
    file_object.write("Server Name: " + server_name + "\n")
    file_object.write("Environment: " + environment + "\n")
    file_object.write("Status: " + status + "\n")

print("Status file created from variables.")

"""
Most real reports are created from variables.
Values may come from user input, command output, database query output, or another file.
"""

# ---------------------------------------------------------------------
# SECTION 7: Write Calculated Values into a Report
# ---------------------------------------------------------------------

print("\nSECTION 7: Write Calculated Values into a Report")

disk_total_gb = 500
disk_used_gb = 390
disk_usage_percent = (disk_used_gb / disk_total_gb) * 100

with open("day20_disk_report.txt", "w") as report_file:
    report_file.write("Disk Usage Report\n")
    report_file.write("-----------------\n")
    report_file.write("Total GB: " + str(disk_total_gb) + "\n")
    report_file.write("Used GB : " + str(disk_used_gb) + "\n")
    report_file.write("Usage % : " + str(round(disk_usage_percent, 2)) + "\n")

print("Disk report created.")

"""
This is where file writing becomes powerful.
Python can calculate values and save the final summary into a report file.
"""

# ---------------------------------------------------------------------
# SECTION 8: Append Mode
# ---------------------------------------------------------------------

print("\nSECTION 8: Append Mode")

with open("day20_activity.log", "w") as log_file:
    log_file.write("INFO script started\n")

with open("day20_activity.log", "a") as log_file:
    log_file.write("INFO health check completed\n")
    log_file.write("WARNING disk usage crossed threshold\n")

with open("day20_activity.log", "r") as log_file:
    activity_content = log_file.read()

print(activity_content)

"""
"a" means append mode.

Append mode adds new content at the end of the file.
It does not remove the existing content.
This is useful for activity logs and audit-style output.
"""

# ---------------------------------------------------------------------
# SECTION 9: Write Lines from a List
# ---------------------------------------------------------------------

print("\nSECTION 9: Write Lines from a List")

services = ["listener", "database", "monitoring", "backup"]

with open("day20_services.txt", "w") as file_object:
    for service in services:
        file_object.write(service + "\n")

print("Service list written to day20_services.txt.")

"""
A common pattern is:
1. Store values in a list
2. Loop through the list
3. Write each item into a file
"""

# ---------------------------------------------------------------------
# SECTION 10: Create a Simple Health Report
# ---------------------------------------------------------------------

print("\nSECTION 10: Create a Simple Health Report")

cpu_status = "OK"
memory_status = "OK"
disk_status = "WARNING"

with open("day20_health_report.txt", "w") as report_file:
    report_file.write("Health Check Report\n")
    report_file.write("===================\n")
    report_file.write("CPU    : " + cpu_status + "\n")
    report_file.write("Memory : " + memory_status + "\n")
    report_file.write("Disk   : " + disk_status + "\n")

print("Health report created.")

"""
A report does not need to be complex.
A clear text file with labels and values is already useful in operations.
"""

# ---------------------------------------------------------------------
# SECTION 11: Add Final Health Status
# ---------------------------------------------------------------------

print("\nSECTION 11: Add Final Health Status")

error_count = 0
warning_count = 1

if error_count > 0:
    final_status = "CRITICAL"
elif warning_count > 0:
    final_status = "WARNING"
else:
    final_status = "HEALTHY"

with open("day20_final_status_report.txt", "w") as report_file:
    report_file.write("Final Status Report\n")
    report_file.write("-------------------\n")
    report_file.write("Errors  : " + str(error_count) + "\n")
    report_file.write("Warnings: " + str(warning_count) + "\n")
    report_file.write("Status  : " + final_status + "\n")

print("Final status report created with status:", final_status)

# ---------------------------------------------------------------------
# SECTION 12: Creating Report Headers and Separators
# ---------------------------------------------------------------------

print("\nSECTION 12: Creating Report Headers and Separators")

report_title = "Daily Operations Summary"
separator = "=" * len(report_title)

with open("day20_operations_summary.txt", "w") as report_file:
    report_file.write(report_title + "\n")
    report_file.write(separator + "\n")
    report_file.write("Servers checked : 3\n")
    report_file.write("Errors found    : 0\n")
    report_file.write("Warnings found  : 1\n")

print("Operations summary report created.")

"""
Formatting matters.
A readable report saves time for the person who will review it later.
"""

# ---------------------------------------------------------------------
# SECTION 13: Guided Practice - Create Backup Summary
# ---------------------------------------------------------------------

print("\nSECTION 13: Guided Practice - Create Backup Summary")

"""
Uncomment this block and run it.
It creates a small backup report.
"""

# backup_name = "daily_backup_01"
# backup_status = "SUCCESS"
# backup_size_gb = 120
#
# with open("backup_summary.txt", "w") as report_file:
#     report_file.write("Backup Summary\n")
#     report_file.write("--------------\n")
#     report_file.write("Backup Name: " + backup_name + "\n")
#     report_file.write("Status     : " + backup_status + "\n")
#     report_file.write("Size GB    : " + str(backup_size_gb) + "\n")
#
# print("Backup summary created.")

print("Guided practice: uncomment the backup summary block.")

# ---------------------------------------------------------------------
# SECTION 14: Guided Practice - Append Activity Entries
# ---------------------------------------------------------------------

print("\nSECTION 14: Guided Practice - Append Activity Entries")

"""
Uncomment this block and run it.
It appends multiple activity messages into a log file.
"""

# with open("activity_history.log", "a") as log_file:
#     log_file.write("INFO login check completed\n")
#     log_file.write("INFO service check completed\n")
#     log_file.write("WARNING cleanup pending\n")
#
# print("Activity entries appended.")

print("Guided practice: uncomment the append activity block.")

# ---------------------------------------------------------------------
# SECTION 15: Guided Practice - Write List Records
# ---------------------------------------------------------------------

print("\nSECTION 15: Guided Practice - Write List Records")

"""
Uncomment this block and run it.
It writes each server from a list into a file.
"""

# servers = ["app01", "db01", "web01"]
#
# with open("server_list.txt", "w") as file_object:
#     for server in servers:
#         file_object.write(server + "\n")
#
# print("Server list file created.")

print("Guided practice: uncomment the server list block.")

# ---------------------------------------------------------------------
# SECTION 16: Mini Challenge Preview
# ---------------------------------------------------------------------

print("\nSECTION 16: Mini Challenge Preview")

"""
Mini Challenge:
Build a Disk Usage Report Generator.

Your script should:
1. Collect server name, environment, disk total, and disk used once
2. Calculate disk usage percentage
3. Decide health status based on usage
4. Write a clean report into a text file
5. Append one activity line into an activity log
6. Read the report back and print it on screen

This mirrors real automation:
- collect input
- calculate result
- decide status
- generate report
- maintain activity history
"""

print("Mini challenge: build a Disk Usage Report Generator using file writing.")

# ---------------------------------------------------------------------
# SECTION 17: Closing Message
# ---------------------------------------------------------------------

print("\nSECTION 17: Closing Message")

print("You have completed Day 20.")
print("You can now create files, append logs, and generate simple text reports.")
print("Next, you will keep building toward stronger file-based automation workflows.")
