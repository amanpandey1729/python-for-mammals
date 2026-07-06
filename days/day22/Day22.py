"""
Python for Mammals - Day 22
Topic: CSV Files

Audience:
- Complete beginners
- DBAs, Sysadmins, Support Engineers, Cloud Engineers, Monitoring Teams
- Anyone who wants Python for practical automation

Goal of Day 22:
By the end of today, you should be able to:
1. Understand why CSV files are heavily used in operational automation
2. Import and use Python's built-in csv module
3. Write CSV files using csv.writer
4. Read CSV files using csv.reader
5. Work with headers and rows
6. Write dictionary data using csv.DictWriter
7. Read dictionary-style CSV data using csv.DictReader
8. Build small CSV reports for inventory, monitoring, and daily checks

Why this matters:
CSV files are everywhere in IT operations.

You will see CSV files in:
- server inventory exports
- database inventory reports
- disk usage reports
- backup status reports
- monitoring exports
- user access reviews
- capacity reports
- incident analysis files

CSV is simple, portable, and opens easily in Excel, Google Sheets,
LibreOffice, text editors, and automation scripts.
Today you learn how Python can read and write CSV files safely and clearly.
"""

import csv

print("=" * 70)
print("DAY 22 - CSV FILES")
print("csv module, reading CSV, writing CSV")
print("=" * 70)

# ---------------------------------------------------------------------
# SECTION 1: Project Introduction
# ---------------------------------------------------------------------

print("\nSECTION 1: Project Introduction")

"""
A CSV file is a Comma-Separated Values file.
It stores tabular data as plain text.

Example:
server,environment,status
app01,production,running
db01,production,running
web01,uat,stopped

Each line is a row.
Each value separated by comma is a column.
"""

print("Today we will use CSV files to create and read simple operational reports.")

# ---------------------------------------------------------------------
# SECTION 2: Why CSV Matters in Automation
# ---------------------------------------------------------------------

print("\nSECTION 2: Why CSV Matters in Automation")

"""
CSV is useful because many tools can export or import it.

Common examples:
- Monitoring tool exports alerts as CSV
- Database script writes tablespace usage as CSV
- Linux script writes server health output as CSV
- Cloud portal exports resource inventory as CSV
- Excel users can open CSV reports easily
"""

print("CSV files help Python talk to spreadsheets, reports, and other tools.")

# ---------------------------------------------------------------------
# SECTION 3: Importing the csv Module
# ---------------------------------------------------------------------

print("\nSECTION 3: Importing the csv Module")

"""
Python has a built-in csv module.
You do not need to install anything.

We imported it at the top of this file:
import csv
"""

print("csv module imported successfully.")

# ---------------------------------------------------------------------
# SECTION 4: Writing a Simple CSV File
# ---------------------------------------------------------------------

print("\nSECTION 4: Writing a Simple CSV File")

with open("day22_servers.csv", "w", newline="") as file_object:
    writer = csv.writer(file_object)
    writer.writerow(["server", "environment", "status"])
    writer.writerow(["app01", "production", "running"])
    writer.writerow(["db01", "production", "running"])
    writer.writerow(["web01", "uat", "stopped"])

print("Created file: day22_servers.csv")

"""
Important details:
- open(..., "w") creates or overwrites the file
- newline="" is recommended when writing CSV files
- csv.writer() creates a writer object
- writerow() writes one row at a time
"""

# ---------------------------------------------------------------------
# SECTION 5: Reading a Simple CSV File
# ---------------------------------------------------------------------

print("\nSECTION 5: Reading a Simple CSV File")

with open("day22_servers.csv", "r", newline="") as file_object:
    reader = csv.reader(file_object)

    for row in reader:
        print(row)

"""
csv.reader() reads each row as a list.

The first row is usually the header row.
Each next row contains actual data.
"""

# ---------------------------------------------------------------------
# SECTION 6: Skipping the Header Row
# ---------------------------------------------------------------------

print("\nSECTION 6: Skipping the Header Row")

with open("day22_servers.csv", "r", newline="") as file_object:
    reader = csv.reader(file_object)

    header = next(reader)
    print("Header:", header)

    for row in reader:
        print("Server:", row[0], "| Environment:", row[1], "| Status:", row[2])

"""
next(reader) reads the first row and moves the reader forward.
After that, the for loop starts from the second row.
"""

# ---------------------------------------------------------------------
# SECTION 7: Writing Multiple Rows with writerows()
# ---------------------------------------------------------------------

print("\nSECTION 7: Writing Multiple Rows with writerows()")

backup_rows = [
    ["database", "backup_type", "status"],
    ["salesdb", "full", "success"],
    ["hrdb", "archive", "success"],
    ["testdb", "full", "failed"]
]

with open("day22_backup_report.csv", "w", newline="") as file_object:
    writer = csv.writer(file_object)
    writer.writerows(backup_rows)

print("Created file: day22_backup_report.csv")

"""
writerows() writes many rows from a list of lists.
This is useful when your script prepares all report rows first.
"""

# ---------------------------------------------------------------------
# SECTION 8: Reading CSV and Counting Rows
# ---------------------------------------------------------------------

print("\nSECTION 8: Reading CSV and Counting Rows")

success_count = 0
failed_count = 0

with open("day22_backup_report.csv", "r", newline="") as file_object:
    reader = csv.reader(file_object)
    header = next(reader)

    for row in reader:
        status = row[2]

        if status == "success":
            success_count += 1
        elif status == "failed":
            failed_count += 1

print("Successful backups:", success_count)
print("Failed backups    :", failed_count)

"""
This is the beginning of report analysis.
Read rows, check values, count what matters.
"""

# ---------------------------------------------------------------------
# SECTION 9: Writing Dictionary Data with DictWriter
# ---------------------------------------------------------------------

print("\nSECTION 9: Writing Dictionary Data with DictWriter")

server_inventory = [
    {"server": "app01", "environment": "production", "cpu_percent": 45},
    {"server": "db01", "environment": "production", "cpu_percent": 72},
    {"server": "web01", "environment": "uat", "cpu_percent": 31}
]

with open("day22_inventory.csv", "w", newline="") as file_object:
    fieldnames = ["server", "environment", "cpu_percent"]
    writer = csv.DictWriter(file_object, fieldnames=fieldnames)

    writer.writeheader()
    writer.writerows(server_inventory)

print("Created file: day22_inventory.csv")

"""
DictWriter is useful when your data is stored as dictionaries.
Dictionary keys become column names.
"""

# ---------------------------------------------------------------------
# SECTION 10: Reading Dictionary Data with DictReader
# ---------------------------------------------------------------------

print("\nSECTION 10: Reading Dictionary Data with DictReader")

with open("day22_inventory.csv", "r", newline="") as file_object:
    reader = csv.DictReader(file_object)

    for row in reader:
        print(row["server"], "is in", row["environment"], "with CPU", row["cpu_percent"] + "%")

"""
DictReader reads each row as a dictionary.
This is easier to understand than using row[0], row[1], row[2].
"""

# ---------------------------------------------------------------------
# SECTION 11: Converting CSV Values into Numbers
# ---------------------------------------------------------------------

print("\nSECTION 11: Converting CSV Values into Numbers")

total_cpu = 0
server_count = 0

with open("day22_inventory.csv", "r", newline="") as file_object:
    reader = csv.DictReader(file_object)

    for row in reader:
        cpu_percent = int(row["cpu_percent"])
        total_cpu += cpu_percent
        server_count += 1

average_cpu = total_cpu / server_count
print("Average CPU %:", round(average_cpu, 2))

"""
CSV values are read as strings.
If you need calculation, convert values using int() or float().
"""

# ---------------------------------------------------------------------
# SECTION 12: Creating a Disk Usage CSV Report
# ---------------------------------------------------------------------

print("\nSECTION 12: Creating a Disk Usage CSV Report")

disk_rows = [
    ["server", "mount", "total_gb", "used_gb", "usage_percent", "status"],
    ["app01", "/", 100, 65, 65.0, "HEALTHY"],
    ["db01", "/u01", 500, 430, 86.0, "WARNING"],
    ["web01", "/var", 80, 75, 93.75, "CRITICAL"]
]

with open("day22_disk_usage.csv", "w", newline="") as file_object:
    writer = csv.writer(file_object)
    writer.writerows(disk_rows)

print("Created file: day22_disk_usage.csv")

# ---------------------------------------------------------------------
# SECTION 13: Reading CSV and Filtering Critical Rows
# ---------------------------------------------------------------------

print("\nSECTION 13: Reading CSV and Filtering Critical Rows")

with open("day22_disk_usage.csv", "r", newline="") as file_object:
    reader = csv.DictReader(file_object)

    for row in reader:
        if row["status"] == "CRITICAL":
            print("Critical disk found:", row["server"], row["mount"], row["usage_percent"] + "%")

"""
This is a practical pattern:
- read CSV
- check one column
- print or report only matching rows
"""

# ---------------------------------------------------------------------
# SECTION 14: Appending a Row to an Existing CSV
# ---------------------------------------------------------------------

print("\nSECTION 14: Appending a Row to an Existing CSV")

with open("day22_disk_usage.csv", "a", newline="") as file_object:
    writer = csv.writer(file_object)
    writer.writerow(["batch01", "/data", 200, 120, 60.0, "HEALTHY"])

print("Added one more row to day22_disk_usage.csv")

"""
Append mode "a" adds data at the end of an existing file.
Be careful not to write the header again unless you are creating a new file.
"""

# ---------------------------------------------------------------------
# SECTION 15: CSV + Exception Handling
# ---------------------------------------------------------------------

print("\nSECTION 15: CSV + Exception Handling")

try:
    with open("day22_disk_usage.csv", "r", newline="") as file_object:
        reader = csv.DictReader(file_object)
        for row in reader:
            usage_percent = float(row["usage_percent"])
            if usage_percent >= 90:
                print("Needs attention:", row["server"], row["mount"])
except FileNotFoundError:
    print("CSV file not found.")
except ValueError:
    print("CSV contains a non-numeric usage value.")

"""
Day 21 and Day 22 work together.
File automation becomes safer when CSV handling is combined with exceptions.
"""

# ---------------------------------------------------------------------
# SECTION 16: Guided Practice - Write Your Own CSV
# ---------------------------------------------------------------------

print("\nSECTION 16: Guided Practice - Write Your Own CSV")

"""
Uncomment this block and run it.
It collects one service record and writes it to a CSV file.
"""

# service_name = input("Enter service name: ")
# service_status = input("Enter service status: ")
# owner_team = input("Enter owner team: ")
#
# with open("service_status.csv", "w", newline="") as file_object:
#     writer = csv.writer(file_object)
#     writer.writerow(["service", "status", "owner_team"])
#     writer.writerow([service_name, service_status, owner_team])
#
# print("Created service_status.csv")

print("Guided practice: uncomment the service_status.csv block.")

# ---------------------------------------------------------------------
# SECTION 17: Mini Challenge Preview
# ---------------------------------------------------------------------

print("\nSECTION 17: Mini Challenge Preview")

"""
Mini Challenge:
Build a Disk Usage CSV Reporter.

Your script should:
1. Collect server name, environment, mount point, total GB, and used GB once
2. Calculate free GB and usage percentage
3. Decide status as HEALTHY, WARNING, or CRITICAL
4. Write the result into a CSV file
5. Read the CSV file back and print the report

This mirrors real automation:
- collect operational data
- calculate useful values
- store data in a reusable report format
- read the report for validation
"""

print("Mini challenge: build a Disk Usage CSV Reporter.")

# ---------------------------------------------------------------------
# SECTION 18: Closing Message
# ---------------------------------------------------------------------

print("\nSECTION 18: Closing Message")

print("You have completed Day 22.")
print("You can now read and write CSV files for simple automation reports.")
print("Next, you will keep improving how scripts exchange data with real-world tools.")
