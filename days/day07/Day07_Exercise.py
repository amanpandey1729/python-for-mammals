"""
Python for Mammals - Day 7 Exercise File
Topic: Conditions Deep Dive

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
By the end of these exercises, you should be comfortable using nested if,
multiple conditions, and/or/not, and validation logic for practical scripts
used in reports, monitoring, daily checks, cleanup, and operational decisions.
"""

print("=" * 70)
print("DAY 7 EXERCISES - CONDITIONS DEEP DIVE")
print("=" * 70)


# ---------------------------------------------------------------------
# EXERCISE 1: Production Disk Alert
# ---------------------------------------------------------------------

"""
Given:
environment = "PROD"
disk_usage = 92

TODO:
- If environment is PROD and disk usage is >= 90, print CRITICAL PROD DISK ALERT
- Otherwise, print No critical production disk alert

Concept focus:
and
"""

environment = "PROD"
disk_usage = 92

# Write your code below this line





# ---------------------------------------------------------------------
# EXERCISE 2: Backup Review Rule
# ---------------------------------------------------------------------

"""
Given:
backup_status = "SUCCESS"
backup_duration_minutes = 145

TODO:
- If backup status is FAILED OR backup duration is greater than 120, print Backup needs review
- Otherwise, print Backup is normal

Concept focus:
or
"""

backup_status = "SUCCESS"
backup_duration_minutes = 145

# Write your code below this line





# ---------------------------------------------------------------------
# EXERCISE 3: Server Reachability Stop Check
# ---------------------------------------------------------------------

"""
Given:
server_reachable = False

TODO:
- Use not
- If server is not reachable, print Stop script and notify support
- Otherwise, print Continue health check

Concept focus:
not
"""

server_reachable = False

# Write your code below this line





# ---------------------------------------------------------------------
# EXERCISE 4: Nested Disk Check
# ---------------------------------------------------------------------

"""
Given:
server_reachable = True
disk_usage = 87

TODO:
- First check whether the server is reachable
- If reachable:
    - If disk usage is >= 90, print Disk CRITICAL
    - Else if disk usage is >= 80, print Disk WARNING
    - Else print Disk OK
- If not reachable:
    - Print Server unreachable. Disk not checked.

Concept focus:
nested if
"""

server_reachable = True
disk_usage = 87

# Write your code below this line





# ---------------------------------------------------------------------
# EXERCISE 5: Environment Validator
# ---------------------------------------------------------------------

"""
Ask the user for environment name.

TODO:
- Clean the input using strip()
- Convert it to uppercase using upper()
- If environment is PROD, DEV, or TEST, print Environment accepted
- Otherwise, print Invalid environment

Concept focus:
or, input validation
"""

# Write your code below this line





# ---------------------------------------------------------------------
# EXERCISE 6: Missing Server Name Validator
# ---------------------------------------------------------------------

"""
Ask the user for server name.

TODO:
- Clean the input using strip()
- If server name is empty, print Server name is required
- Otherwise, print Server name accepted

Concept focus:
real-world validation
"""

# Write your code below this line





# ---------------------------------------------------------------------
# EXERCISE 7: Percentage Range Validator
# ---------------------------------------------------------------------

"""
Ask the user for disk usage percentage.

TODO:
- Convert input to float
- If value is less than 0 OR greater than 100, print Invalid percentage
- Otherwise, print Percentage accepted

Test with:
-5
45
104

Concept focus:
or, numeric validation
"""

# Write your code below this line





# ---------------------------------------------------------------------
# EXERCISE 8: Login and Server Access Check
# ---------------------------------------------------------------------

"""
Given:
server_reachable = True
login_successful = False

TODO:
- If server is reachable AND login is successful, print Ready to collect report
- Otherwise, print Cannot collect report

Concept focus:
and
"""

server_reachable = True
login_successful = False

# Write your code below this line





# ---------------------------------------------------------------------
# EXERCISE 9: Backup Validation With Reasons
# ---------------------------------------------------------------------

"""
Given:
backup_status = "FAILED"
backup_duration_minutes = 80
backup_size_gb = 12

TODO:
- If backup status is SUCCESS AND duration <= 120 AND size > 0:
    - Print Backup is valid
- Otherwise:
    - Print Backup needs review
    - If backup status is not SUCCESS, print reason
    - If duration > 120, print reason
    - If size <= 0, print reason

Concept focus:
and, nested independent checks, not equal
"""

backup_status = "FAILED"
backup_duration_minutes = 80
backup_size_gb = 12

# Write your code below this line





# ---------------------------------------------------------------------
# EXERCISE 10: CPU or Memory Alert
# ---------------------------------------------------------------------

"""
Given:
environment = "PROD"
cpu_usage = 78
memory_usage = 93

TODO:
- If environment is PROD and either CPU OR memory is >= 90, print Production performance alert
- Otherwise, print No production performance alert

Concept focus:
and + or with brackets
"""

environment = "PROD"
cpu_usage = 78
memory_usage = 93

# Write your code below this line





# ---------------------------------------------------------------------
# EXERCISE 11: Change Window Validator
# ---------------------------------------------------------------------

"""
Ask the user for:
1. Environment
2. Approval available? YES/NO
3. Current hour in 24-hour format

TODO:
- Clean environment and approval inputs
- Convert current hour to integer
- If environment is PROD:
    - Allow change only if approval is YES and current hour is >= 22 OR <= 5
    - Otherwise print Change not allowed
- If environment is not PROD:
    - Print Follow non-prod change process

Concept focus:
nested if, and, or
"""

# Write your code below this line





# ---------------------------------------------------------------------
# EXERCISE 12: Health Status From Multiple Checks
# ---------------------------------------------------------------------

"""
Ask the user for:
1. Server reachable? YES/NO
2. CPU usage
3. Memory usage
4. Disk usage

TODO:
- Convert YES/NO input into a boolean variable
- Convert usage values to float
- If server is not reachable, print CRITICAL
- Else if CPU, memory, or disk is >= 90, print WARNING
- Else print OK

Concept focus:
not, or, multiple checks
"""

# Write your code below this line





# ---------------------------------------------------------------------
# EXERCISE 13: Report Readiness Validator
# ---------------------------------------------------------------------

"""
Ask the user for:
1. Report name
2. Successful checks count
3. Failed checks count
4. Report approved? YES/NO

TODO:
- Clean report name
- Convert counts to integers
- Calculate total checks
- If report name is empty, print Report name required
- Else if total checks is 0, print No checks found
- Else if failed checks is 0 AND approved is YES, print Report ready to send
- Else print Report not ready

Concept focus:
validation, and, nested decisions
"""

# Write your code below this line





# ---------------------------------------------------------------------
# EXERCISE 14: Mini Project - Operational Health Validator
# ---------------------------------------------------------------------

"""
Build a mini Operational Health Validator.

Collect all inputs once at the beginning:
1. Server name
2. Environment
3. Server reachable? YES/NO
4. CPU usage percentage
5. Memory usage percentage
6. Disk usage percentage
7. Backup status SUCCESS/FAILED
8. Backup age in hours

TODO:
- Clean all text inputs using strip()
- Convert text inputs to uppercase where useful
- Convert numeric inputs to float
- Convert reachable input into a boolean variable
- Validate server name is not empty
- Validate environment is PROD, DEV, or TEST
- Validate CPU, memory, and disk values are between 0 and 100
- Print a clean operational health report
- Decide final status:
    - INVALID if required inputs are missing or invalid
    - CRITICAL if server is not reachable
    - CRITICAL if environment is PROD and disk usage >= 90
    - WARNING if CPU, memory, or disk usage >= 90
    - WARNING if backup status is not SUCCESS or backup age > 24
    - OK otherwise

Expected output style:
========================================
Operational Health Report
========================================
Server Name      : app-server-01
Environment      : PROD
Server Reachable : True
CPU Usage        : 74.0 %
Memory Usage     : 82.0 %
Disk Usage       : 91.0 %
Backup Status    : SUCCESS
Backup Age       : 18.0 hours
Final Status     : CRITICAL
Action           : Cleanup or extend production capacity urgently
========================================

Important:
Ask each input only once at the beginning of the mini project.
Reuse those variables throughout the project.
"""

# Write your mini project code below this line





print("\nExercise file loaded successfully. Complete the tasks one by one.")
