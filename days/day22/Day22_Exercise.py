"""
Python for Mammals - Day 22 Exercise File
Topic: CSV Files

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
By the end of these exercises, you should be able to use Python's csv module
to read CSV files, write CSV files, append rows, use headers, and create
small operational reports that can be opened in spreadsheet tools.
"""

print("=" * 70)
print("DAY 22 EXERCISES - CSV FILES")
print("csv module, reading CSV, writing CSV")
print("=" * 70)

# ---------------------------------------------------------------------
# EXERCISE 1: Import the csv Module
# ---------------------------------------------------------------------

"""
TODO:
- Import the csv module
- Print a message that says:
  CSV module imported successfully

Concept focus:
importing built-in modules
"""

# Write your code below this line




# ---------------------------------------------------------------------
# EXERCISE 2: Write a Simple Server CSV
# ---------------------------------------------------------------------

"""
TODO:
- Create a file named exercise22_servers.csv
- Write a header row:
  server, environment, status
- Write at least 3 server rows
- Print a success message after creating the file

Concept focus:
csv.writer, writerow
"""

# Write your code below this line




# ---------------------------------------------------------------------
# EXERCISE 3: Read a Simple Server CSV
# ---------------------------------------------------------------------

"""
TODO:
- Open exercise22_servers.csv in read mode
- Use csv.reader to read the file
- Print every row

Concept focus:
csv.reader, reading rows
"""

# Write your code below this line




# ---------------------------------------------------------------------
# EXERCISE 4: Skip Header and Print Clean Output
# ---------------------------------------------------------------------

"""
TODO:
- Open exercise22_servers.csv
- Use next(reader) to skip or capture the header row
- For each data row, print output like:
  Server app01 is running in production

Concept focus:
headers, row indexes
"""

# Write your code below this line




# ---------------------------------------------------------------------
# EXERCISE 5: Write Multiple Rows with writerows()
# ---------------------------------------------------------------------

"""
TODO:
- Create a list of lists for backup report data
- Include a header row:
  database, backup_type, status
- Include at least 4 database backup rows
- Write all rows into exercise22_backups.csv using writerows()

Concept focus:
writerows, list of lists
"""

# Write your code below this line




# ---------------------------------------------------------------------
# EXERCISE 6: Count Success and Failed Backups
# ---------------------------------------------------------------------

"""
TODO:
- Read exercise22_backups.csv
- Skip the header row
- Count how many backups have status success
- Count how many backups have status failed
- Print both counts

Concept focus:
reading CSV + conditions + counters
"""

# Write your code below this line




# ---------------------------------------------------------------------
# EXERCISE 7: Write CSV from User Input
# ---------------------------------------------------------------------

"""
TODO:
- Ask the user for:
  1. Server name
  2. Environment
  3. Service name
  4. Service status
- Write this data into exercise22_service_status.csv
- Include a header row
- Print a success message

Concept focus:
input + csv writing
"""

# Write your code below this line




# ---------------------------------------------------------------------
# EXERCISE 8: Append a Row to an Existing CSV
# ---------------------------------------------------------------------

"""
TODO:
- Ask the user for one more service record:
  1. Server name
  2. Environment
  3. Service name
  4. Service status
- Append the row to exercise22_service_status.csv
- Do not write the header again

Concept focus:
append mode "a"
"""

# Write your code below this line




# ---------------------------------------------------------------------
# EXERCISE 9: Use DictWriter for Inventory
# ---------------------------------------------------------------------

"""
TODO:
- Create a list of dictionaries for at least 3 servers
- Each dictionary should have:
  server, environment, cpu_percent
- Use csv.DictWriter to write the data into exercise22_inventory.csv
- Write the header using writeheader()

Concept focus:
DictWriter, dictionary rows
"""

# Write your code below this line




# ---------------------------------------------------------------------
# EXERCISE 10: Use DictReader for Inventory
# ---------------------------------------------------------------------

"""
TODO:
- Read exercise22_inventory.csv using csv.DictReader
- Print each row in this style:
  app01 | production | CPU: 45%

Concept focus:
DictReader, column names
"""

# Write your code below this line




# ---------------------------------------------------------------------
# EXERCISE 11: Calculate Average CPU from CSV
# ---------------------------------------------------------------------

"""
TODO:
- Read exercise22_inventory.csv using DictReader
- Convert cpu_percent into an integer or float
- Calculate average CPU usage
- Print the average CPU usage

Concept focus:
CSV values as strings, numeric conversion
"""

# Write your code below this line




# ---------------------------------------------------------------------
# EXERCISE 12: Find High CPU Servers
# ---------------------------------------------------------------------

"""
TODO:
- Read exercise22_inventory.csv
- Convert cpu_percent into a number
- Print only servers where CPU is greater than or equal to 80
- If no server is high CPU, print a clear message

Concept focus:
filtering CSV records
"""

# Write your code below this line




# ---------------------------------------------------------------------
# EXERCISE 13: Create Disk Usage CSV
# ---------------------------------------------------------------------

"""
TODO:
- Create exercise22_disk_usage.csv
- Header columns should be:
  server, mount, total_gb, used_gb, usage_percent, status
- Add at least 4 disk rows
- Use status values such as HEALTHY, WARNING, CRITICAL

Concept focus:
CSV report structure
"""

# Write your code below this line




# ---------------------------------------------------------------------
# EXERCISE 14: Read Critical Disk Rows
# ---------------------------------------------------------------------

"""
TODO:
- Read exercise22_disk_usage.csv using DictReader
- Print only rows where status is CRITICAL
- Output should show server, mount, and usage_percent

Concept focus:
operational filtering from CSV
"""

# Write your code below this line




# ---------------------------------------------------------------------
# EXERCISE 15: CSV with Basic Exception Handling
# ---------------------------------------------------------------------

"""
TODO:
- Ask the user for a CSV file name
- Try to open and read the file using csv.reader
- Print each row if the file exists
- Handle FileNotFoundError with a friendly message

Concept focus:
CSV reading + exception handling
"""

# Write your code below this line




# ---------------------------------------------------------------------
# EXERCISE 16: Mini Project - Disk Usage CSV Reporter
# ---------------------------------------------------------------------

"""
Build a small Disk Usage CSV Reporter.

Collect all required user inputs once at the beginning:
1. Server name
2. Environment name
3. Mount point or disk name
4. Disk total GB
5. Disk used GB
6. CSV report file name

Then reuse those variables throughout the mini project.

TODO:
- Import csv if not already imported
- Collect all required inputs once
- Convert disk total and disk used into numbers
- Calculate free GB
- Calculate usage percentage
- Decide health status:
    CRITICAL if usage is greater than or equal to 90
    WARNING if usage is greater than or equal to 80 and less than 90
    HEALTHY if usage is less than 80
- Write one CSV report with columns:
    server, environment, mount, total_gb, used_gb, free_gb, usage_percent, status
- Read the same CSV file back
- Print a clean report on screen

Important:
- Collect each input only once.
- Reuse those variables throughout the project.
- Do not ask for the same input repeatedly.
- The mini project should feel like one complete CSV reporting workflow.

Concept focus:
real-world CSV report generation workflow
"""

# Write your code below this line




print("\nEnd of Day 22 exercises. Complete the TODO sections one by one.")
