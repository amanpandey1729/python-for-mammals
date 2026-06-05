"""
Python for Mammals - Day 4 Exercise File
Topic: Strings

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
By the end of these exercises, you should be comfortable cleaning,
checking, formatting, and extracting useful information from text.
"""

print("=" * 70)
print("DAY 4 EXERCISES - STRINGS")
print("=" * 70)


# ---------------------------------------------------------------------
# EXERCISE 1: Clean Introduction Text
# ---------------------------------------------------------------------

"""
Ask the user for:
1. Name
2. Profession
3. City

The user may enter extra spaces.

TODO:
- Remove extra spaces using strip()
- Print name and city in title case
- Print profession in uppercase

Expected style:
Hello Aman!
Profession : DBA
City       : Delhi
"""

# Write your code below this line





# ---------------------------------------------------------------------
# EXERCISE 2: Backup Status Normalizer
# ---------------------------------------------------------------------

"""
Ask the user for backup status.

The user may enter:
success
 SUCCESS
Success
failed
 FAILED

TODO:
- Clean extra spaces
- Convert status to uppercase
- If status is SUCCESS, print "Backup completed successfully"
- If status is FAILED, print "Backup failed"
- Otherwise, print "Unknown backup status"
"""

# Write your code below this line





# ---------------------------------------------------------------------
# EXERCISE 3: File Extension Checker
# ---------------------------------------------------------------------

"""
Ask the user for a file name.

TODO:
- Clean extra spaces
- Check if the file ends with .log
- Check if the file ends with .csv
- Print a suitable message

Examples:
backup.log  -> Log file detected
report.csv  -> CSV report detected
notes.txt   -> Unsupported file type

Bonus:
Handle uppercase extensions like REPORT.CSV or ALERT.LOG.
"""

# Write your code below this line





# ---------------------------------------------------------------------
# EXERCISE 4: Server Naming Standard Checker
# ---------------------------------------------------------------------

"""
Ask the user for a server name.

Standard:
- Production server names should start with prod-
- Development server names should start with dev-
- Test server names should start with test-

TODO:
- Clean extra spaces
- Convert to lowercase
- Print the environment based on the prefix

Examples:
prod-db-01  -> Production server
dev-app-02  -> Development server
test-web-01 -> Test server
abc-01      -> Unknown naming standard
"""

# Write your code below this line





# ---------------------------------------------------------------------
# EXERCISE 5: Extract Environment from Server Name
# ---------------------------------------------------------------------

"""
Given this server name:
server_name = "prod-db-server-01"

TODO:
- Extract first 4 characters using slicing
- Extract last 2 characters using slicing
- Print both values

Expected output:
Environment Code : prod
Server Number    : 01
"""

server_name = "prod-db-server-01"

# Write your code below this line





# ---------------------------------------------------------------------
# EXERCISE 6: Alert Message Classifier
# ---------------------------------------------------------------------

"""
Ask the user for an alert message.

TODO:
- Clean extra spaces
- Convert it to uppercase
- If it contains ERROR or FAILED, print CRITICAL
- Else if it contains WARNING, print WARNING
- Else if it contains SUCCESS, print OK
- Otherwise, print UNKNOWN

Example:
"backup failed on server app-01" -> CRITICAL
"disk warning on server app-01"  -> WARNING
"backup success"                 -> OK
"job started"                    -> UNKNOWN
"""

# Write your code below this line





# ---------------------------------------------------------------------
# EXERCISE 7: Create a File-Friendly Name
# ---------------------------------------------------------------------

"""
Ask the user for a report title.

TODO:
- Clean extra spaces
- Convert to lowercase
- Replace spaces with underscores
- Add .txt at the end while printing

Example:
Input : Daily Backup Report
Output: daily_backup_report.txt
"""

# Write your code below this line





# ---------------------------------------------------------------------
# EXERCISE 8: Split a Simple Monitoring Line
# ---------------------------------------------------------------------

"""
Given this monitoring line:
line = "app-server-01 CPU 86 WARNING"

TODO:
- Split the line using split()
- Print server name
- Print metric name
- Print metric value
- Print status

Expected output:
Server : app-server-01
Metric : CPU
Value  : 86
Status : WARNING
"""

line = "app-server-01 CPU 86 WARNING"

# Write your code below this line





# ---------------------------------------------------------------------
# EXERCISE 9: Split a CSV-like Report Row
# ---------------------------------------------------------------------

"""
Given this CSV-like row:
row = "db-server-01,DISK,92,CRITICAL"

TODO:
- Split the row using comma as separator
- Store each part in a separate variable
- Print a clean report using f-strings

Expected style:
Server : db-server-01
Metric : DISK
Value  : 92%
Status : CRITICAL
"""

row = "db-server-01,DISK,92,CRITICAL"

# Write your code below this line





# ---------------------------------------------------------------------
# EXERCISE 10: Log Line Keyword Search
# ---------------------------------------------------------------------

"""
Ask the user for a log line.

TODO:
- Normalize the line to uppercase
- Check whether the log contains any of these words:
  ERROR
  ORA-
  FAILED
  TIMEOUT
  WARNING

Print a useful message based on what you find.

Example:
Input : ORA-00060 deadlock detected
Output: Oracle error found in log line

Input : connection timeout for app
Output: Timeout issue found
"""

# Write your code below this line





# ---------------------------------------------------------------------
# EXERCISE 11: Username Validator
# ---------------------------------------------------------------------

"""
Ask the user for a username.

TODO:
- Remove extra spaces
- Check length using len()
- If username length is 0, print "Username cannot be empty"
- If username length is less than 5, print "Username too short"
- Otherwise, print "Username accepted"

Bonus:
Convert username to lowercase before printing final accepted username.
"""

# Write your code below this line





# ---------------------------------------------------------------------
# EXERCISE 12: Mini Project - Daily Text Cleanup Assistant
# ---------------------------------------------------------------------

"""
Create a small text cleanup assistant.

Ask the user for:
1. Server name
2. Backup status
3. Log line
4. Report file name

TODO:
- Clean all inputs using strip()
- Normalize backup status using upper()
- Normalize log line for searching using upper()
- Check if report file name ends with .csv or .log
- Print a clean operational summary

Decision rules:
- If backup status is FAILED, final status should be CRITICAL
- If log line contains ERROR, FAILED, ORA-, or TIMEOUT, final status should be CRITICAL
- If log line contains WARNING, final status should be WARNING
- If backup status is SUCCESS and file name is valid, final status should be OK
- Otherwise, final status should be UNKNOWN

Expected output style:
========================================
Daily Text Cleanup Summary
========================================
Server Name   : app-server-01
Backup Status : SUCCESS
File Name     : daily_report.csv
File Type     : Valid report/log file
Final Status  : OK
Reason        : Backup success and file name looks valid
========================================

Important:
Focus on string cleaning and searching first.
Formatting can be improved after the logic works.
"""

# Write your mini project code below this line





print("\nExercise file loaded successfully. Complete the tasks one by one.")
