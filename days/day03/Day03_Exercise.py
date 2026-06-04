"""
Python for Mammals - Day 3 Exercise File
Topic: Input, Type Conversion, f-Strings, Comparisons, and Conditions

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
By the end of these exercises, you should be comfortable writing small
automation-style decision programs.
"""

print("=" * 70)
print("DAY 3 EXERCISES - INPUT, TYPE CONVERSION, AND CONDITIONS")
print("=" * 70)


# ---------------------------------------------------------------------
# EXERCISE 1: User Introduction
# ---------------------------------------------------------------------

"""
Ask the user for:
1. Name
2. Profession
3. City

Print a clean message using an f-string.

Expected style:
Hello Aman!
You are a DBA from Delhi.
Welcome to Python for Mammals.
"""

# Write your code below this line





# ---------------------------------------------------------------------
# EXERCISE 2: Age Calculator
# ---------------------------------------------------------------------

"""
Ask the user for:
1. Name
2. Age

Print:
Hi <name>, next year you will be <age + 1> years old.

Important:
input() returns string.
You must convert age into int before adding 1.
"""

# Write your code below this line





# ---------------------------------------------------------------------
# EXERCISE 3: Disk Free Space Calculator
# ---------------------------------------------------------------------

"""
Ask the user for:
1. Total disk size in GB
2. Used disk size in GB

Calculate:
1. Free disk size
2. Used percentage

Print output like:
Total Disk : 500 GB
Used Disk  : 375 GB
Free Disk  : 125 GB
Used %     : 75.00%
"""

# Write your code below this line





# ---------------------------------------------------------------------
# EXERCISE 4: Disk Usage Status
# ---------------------------------------------------------------------

"""
Ask the user for disk usage percentage.

Decision:
- If disk usage is greater than or equal to 90, print CRITICAL
- Else if disk usage is greater than or equal to 75, print WARNING
- Else print HEALTHY
"""

# Write your code below this line





# ---------------------------------------------------------------------
# EXERCISE 5: Backup Status Checker
# ---------------------------------------------------------------------

"""
Ask the user for:
1. Backup name
2. Backup status

Backup status can be:
SUCCESS
FAILED

Decision:
- If status is SUCCESS, print "Backup completed successfully"
- Otherwise, print "Backup failed. Please check logs"

Bonus:
Use .upper() on the status so that success, Success, SUCCESS all work.
Example:
backup_status = backup_status.upper()
"""

# Write your code below this line





# ---------------------------------------------------------------------
# EXERCISE 6: Login Attempt Checker
# ---------------------------------------------------------------------

"""
Ask the user for number of failed login attempts.

Decision:
- 0 to 2 attempts     -> Normal
- 3 to 5 attempts     -> Suspicious
- More than 5 attempts -> Security Alert

Example:
Failed Attempts: 6
Output: Security Alert
"""

# Write your code below this line





# ---------------------------------------------------------------------
# EXERCISE 7: Service Status Checker
# ---------------------------------------------------------------------

"""
Ask the user for:
1. Service name
2. Service status

Possible service status:
RUNNING
STOPPED

Decision:
- If service is RUNNING, print "<service_name> is healthy"
- Else print "<service_name> needs attention"

Bonus:
Handle lowercase input using .upper()
"""

# Write your code below this line





# ---------------------------------------------------------------------
# EXERCISE 8: CPU and Memory Combined Alert
# ---------------------------------------------------------------------

"""
Ask the user for:
1. CPU usage percentage
2. Memory usage percentage

Decision:
- If both CPU and memory are above 80, print "High load on system"
- If only CPU is above 80, print "CPU is high"
- If only memory is above 80, print "Memory is high"
- Otherwise, print "System load is normal"

Hint:
Use and / elif / else
"""

# Write your code below this line





# ---------------------------------------------------------------------
# EXERCISE 9: Ticket Priority Classifier
# ---------------------------------------------------------------------

"""
Ask the user for:
1. Impact level
2. Urgency level

Both values should be numbers from 1 to 3.

Simple rule:
- If impact is 1 and urgency is 1, print P1
- Else if impact is 1 or urgency is 1, print P2
- Else if impact is 2 or urgency is 2, print P3
- Otherwise, print P4

This is similar to how operational tickets are classified.
"""

# Write your code below this line





# ---------------------------------------------------------------------
# EXERCISE 10: Mini Project - Interactive Health Report
# ---------------------------------------------------------------------

"""
Create a small interactive health report.

Ask the user for:
1. Server name
2. CPU usage
3. Memory usage
4. Disk usage

Print a clean report:
----------------------------------------
Health Report for <server_name>
CPU Usage    : xx.xx%
Memory Usage : xx.xx%
Disk Usage   : xx.xx%
----------------------------------------

Final decision:
- If any value is >= 90, print CRITICAL
- Else if any value is >= 75, print WARNING
- Else print HEALTHY

Bonus:
Also print the reason.

Example:
Final Status: WARNING
Reason: Disk usage is high
"""

# Write your code below this line





# ---------------------------------------------------------------------
# HOMEWORK CHALLENGE
# ---------------------------------------------------------------------

"""
Homework Challenge: Daily Operations Decision Assistant

Create a program that asks the user for:

1. Server name
2. CPU usage
3. Memory usage
4. Disk usage
5. Backup status
6. Number of failed login attempts

Then print a final operational summary.

Rules:
- If backup failed, final status should be CRITICAL
- If disk usage >= 90, final status should be CRITICAL
- If failed login attempts > 5, final status should be SECURITY ALERT
- If CPU or memory >= 80, final status should be WARNING
- Otherwise, final status should be HEALTHY

Expected output style:
========================================
Daily Operations Summary
========================================
Server Name           : app-server-01
CPU Usage             : 76.00%
Memory Usage          : 82.00%
Disk Usage            : 68.00%
Backup Status         : SUCCESS
Failed Login Attempts : 2
Final Status          : WARNING
Reason                : Memory usage is high
========================================

Important:
Focus on logic first.
Formatting can be improved after the logic works.
"""

# Write your homework code below this line





print("\nExercise file loaded successfully. Complete the tasks one by one.")
