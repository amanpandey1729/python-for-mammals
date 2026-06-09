"""
Python for Mammals - Day 8 Exercise File
Topic: For Loops

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
By the end of these exercises, you should be comfortable using for loops,
range(), loop variables, strings, and lists to automate repetition in
reports, monitoring, daily checks, cleanup, and operational summaries.
"""

print("=" * 70)
print("DAY 8 EXERCISES - FOR LOOPS")
print("=" * 70)


# ---------------------------------------------------------------------
# EXERCISE 1: Print Server Names
# ---------------------------------------------------------------------

"""
Given:
servers = ["app01", "db01", "web01"]

TODO:
- Use a for loop
- Print each server name

Expected style:
Server: app01
Server: db01
Server: web01

Concept focus:
basic for loop with list
"""

servers = ["app01", "db01", "web01"]

# Write your code below this line





# ---------------------------------------------------------------------
# EXERCISE 2: Numbered Health Checks
# ---------------------------------------------------------------------

"""
TODO:
- Use range()
- Print health check numbers from 1 to 5

Expected style:
Health check number: 1
Health check number: 2
...
Health check number: 5

Concept focus:
range(start, stop)
"""

# Write your code below this line





# ---------------------------------------------------------------------
# EXERCISE 3: Repeat a Message
# ---------------------------------------------------------------------

"""
TODO:
- Ask the user how many reminders to print
- Convert the input to integer
- Use range() to print the message that many times

Message:
Reminder: Complete daily checklist

Concept focus:
range() with user input
"""

# Write your code below this line





# ---------------------------------------------------------------------
# EXERCISE 4: Iterate Through a String
# ---------------------------------------------------------------------

"""
Given:
ticket_id = "INC12345"

TODO:
- Use a for loop to print each character from ticket_id

Expected style:
Character: I
Character: N
Character: C
...

Concept focus:
iterating through strings
"""

ticket_id = "INC12345"

# Write your code below this line





# ---------------------------------------------------------------------
# EXERCISE 5: Service Checklist
# ---------------------------------------------------------------------

"""
Given:
services = ["ssh", "httpd", "database", "backup-agent"]

TODO:
- Loop through services
- Print Checking service: <service>
- Print Result: Pending validation

Concept focus:
loop body with multiple print statements
"""

services = ["ssh", "httpd", "database", "backup-agent"]

# Write your code below this line





# ---------------------------------------------------------------------
# EXERCISE 6: Disk Usage Status
# ---------------------------------------------------------------------

"""
Given:
disk_usages = [65, 82, 91, 76]

TODO:
- Loop through disk_usages
- If usage >= 90, print CRITICAL
- Else if usage >= 80, print WARNING
- Else print OK

Concept focus:
for loop with if / elif / else
"""

disk_usages = [65, 82, 91, 76]

# Write your code below this line





# ---------------------------------------------------------------------
# EXERCISE 7: Count Backup Results
# ---------------------------------------------------------------------

"""
Given:
backup_statuses = ["SUCCESS", "FAILED", "SUCCESS", "FAILED", "SUCCESS"]

TODO:
- Create successful_backups = 0
- Create failed_backups = 0
- Loop through backup_statuses
- Increase successful_backups for SUCCESS
- Increase failed_backups for anything else
- Print both counters

Concept focus:
loop with counters
"""

backup_statuses = ["SUCCESS", "FAILED", "SUCCESS", "FAILED", "SUCCESS"]

# Write your code below this line





# ---------------------------------------------------------------------
# EXERCISE 8: Clean Server Names
# ---------------------------------------------------------------------

"""
Given:
raw_server_names = [" app01 ", " DB01", "backup01  "]

TODO:
- Loop through raw_server_names
- Clean each value using strip()
- Convert each value to lowercase using lower()
- Print raw value and clean value

Concept focus:
loop with string cleanup
"""

raw_server_names = [" app01 ", " DB01", "backup01  "]

# Write your code below this line





# ---------------------------------------------------------------------
# EXERCISE 9: Progress Generator
# ---------------------------------------------------------------------

"""
TODO:
- Use range(10, 101, 10)
- Print progress from 10% to 100%

Expected style:
Progress: 10 %
Progress: 20 %
...
Progress: 100 %

Concept focus:
range(start, stop, step)
"""

# Write your code below this line





# ---------------------------------------------------------------------
# EXERCISE 10: Alert Keyword Checker
# ---------------------------------------------------------------------

"""
Given:
alerts = ["CPU high", "Backup failed", "Disk warning", "Login failed"]

TODO:
- Loop through alerts
- Convert each alert to lowercase
- If the alert contains "failed", print Needs immediate review
- Otherwise, print Normal review

Concept focus:
loop with string search
"""

alerts = ["CPU high", "Backup failed", "Disk warning", "Login failed"]

# Write your code below this line





# ---------------------------------------------------------------------
# EXERCISE 11: Generate Report Rows
# ---------------------------------------------------------------------

"""
Given:
servers = ["app01", "db01", "web01"]
environment = "PROD"

TODO:
- Loop through servers
- Print a small report row for each server:
    Server      : <server>
    Environment : PROD
    Status      : Pending

Concept focus:
loop-based report generation
"""

servers = ["app01", "db01", "web01"]
environment = "PROD"

# Write your code below this line





# ---------------------------------------------------------------------
# EXERCISE 12: Count Critical Alerts
# ---------------------------------------------------------------------

"""
Given:
alert_levels = ["INFO", "CRITICAL", "WARNING", "CRITICAL", "INFO"]

TODO:
- Create critical_count = 0
- Loop through alert_levels
- Count how many alerts are CRITICAL
- Print the final count

Concept focus:
counting selected items
"""

alert_levels = ["INFO", "CRITICAL", "WARNING", "CRITICAL", "INFO"]

# Write your code below this line





# ---------------------------------------------------------------------
# EXERCISE 13: User-driven Checklist Generator
# ---------------------------------------------------------------------

"""
Ask the user for:
1. Checklist name
2. Number of items

TODO:
- Clean checklist name using strip()
- Convert number of items to integer
- Print checklist heading
- Use a for loop to print:
    Item 1 : Pending
    Item 2 : Pending
    ...

Concept focus:
input + range() + formatted operational output
"""

# Write your code below this line





# ---------------------------------------------------------------------
# EXERCISE 14: Mini Project - Multi Server Disk Review
# ---------------------------------------------------------------------

"""
Build a mini Multi Server Disk Review.

Collect all required inputs once at the beginning:
1. Server 1 name
2. Server 1 disk usage percentage
3. Server 2 name
4. Server 2 disk usage percentage
5. Server 3 name
6. Server 3 disk usage percentage
7. Warning threshold
8. Critical threshold

TODO:
- Clean server names using strip()
- Convert disk usage and threshold inputs to float
- Store server names in a list
- Store disk usages in a list
- Create counters:
    ok_count = 0
    warning_count = 0
    critical_count = 0
- Use a for loop with range(3)
- For each server:
    - Print server name
    - Print disk usage
    - Decide status using warning and critical thresholds
    - Increase the correct counter
- Print a final summary

Expected output style:
========================================
Multi Server Disk Review
========================================
Server : app01
Usage  : 72.0 %
Status : OK
----------------------------------------
Server : db01
Usage  : 86.0 %
Status : WARNING
----------------------------------------
Server : backup01
Usage  : 94.0 %
Status : CRITICAL
----------------------------------------
OK Count       : 1
WARNING Count  : 1
CRITICAL Count : 1
========================================

Important:
Ask each input only once at the beginning of the mini project.
Reuse those variables throughout the project.
"""

# Write your mini project code below this line





print("\nExercise file loaded successfully. Complete the tasks one by one.")
