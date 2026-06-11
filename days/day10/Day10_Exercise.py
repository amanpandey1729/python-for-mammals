"""
Python for Mammals - Day 10 Exercise File
Topic: Mini Project #1 - Server Health Message Generator

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
By the end of these exercises, you should be able to combine variables,
input, conditions, strings, and loops to build a small practical automation
workflow: a Server Health Message Generator.
"""

print("=" * 70)
print("DAY 10 EXERCISES - MINI PROJECT #1")
print("SERVER HEALTH MESSAGE GENERATOR")
print("=" * 70)

# ---------------------------------------------------------------------
# EXERCISE 1: Store Basic Server Details
# ---------------------------------------------------------------------

"""
TODO:
- Create a variable server_name with value app01
- Create a variable environment with value PROD
- Print both values in a readable format

Concept focus:
variables and print formatting
"""

# Write your code below this line




# ---------------------------------------------------------------------
# EXERCISE 2: Create a Simple Health Message
# ---------------------------------------------------------------------

"""
TODO:
- Create server_name = "web01"
- Create environment = "TEST"
- Create status = "OK"
- Print a message like:
  Server web01 in TEST is OK

Concept focus:
string joining or f-string formatting
"""

# Write your code below this line




# ---------------------------------------------------------------------
# EXERCISE 3: Decide CPU Status
# ---------------------------------------------------------------------

"""
Given:
cpu_usage = 85

TODO:
- If cpu_usage >= 90, status should be CRITICAL
- Else if cpu_usage >= 80, status should be WARNING
- Otherwise status should be OK
- Print CPU usage and CPU status

Concept focus:
if / elif / else decision
"""

cpu_usage = 85

# Write your code below this line




# ---------------------------------------------------------------------
# EXERCISE 4: Decide Disk Status
# ---------------------------------------------------------------------

"""
Given:
disk_usage = 93

TODO:
- Decide disk status using the same rule:
    CRITICAL if usage >= 90
    WARNING if usage >= 80
    OK otherwise
- Print disk usage and disk status

Concept focus:
condition practice with another metric
"""

disk_usage = 93

# Write your code below this line




# ---------------------------------------------------------------------
# EXERCISE 5: Decide Overall Status from Three Metrics
# ---------------------------------------------------------------------

"""
Given:
cpu_usage = 75
memory_usage = 84
disk_usage = 70

TODO:
- Overall status should be CRITICAL if any metric is >= 90
- Overall status should be WARNING if any metric is >= 80
- Otherwise overall status should be OK
- Print the final overall status

Concept focus:
or operator with multiple conditions
"""

cpu_usage = 75
memory_usage = 84
disk_usage = 70

# Write your code below this line




# ---------------------------------------------------------------------
# EXERCISE 6: Create Action Message
# ---------------------------------------------------------------------

"""
Given:
status = "WARNING"

TODO:
- If status is CRITICAL, action should be Immediate action required
- If status is WARNING, action should be Review during current shift
- If status is OK, action should be No action required
- Print status and action

Concept focus:
turning status into an operational message
"""

status = "WARNING"

# Write your code below this line




# ---------------------------------------------------------------------
# EXERCISE 7: Ask for Server Name
# ---------------------------------------------------------------------

"""
TODO:
- Ask the user to enter server name
- Clean extra spaces using strip()
- Convert it to lowercase
- Print accepted server name

Concept focus:
input and string cleanup
"""

# Write your code below this line




# ---------------------------------------------------------------------
# EXERCISE 8: Validate Non-Blank Server Name
# ---------------------------------------------------------------------

"""
TODO:
- Ask the user to enter server name
- Keep asking while the cleaned value is blank
- Convert accepted server name to lowercase
- Print accepted server name

Concept focus:
while loop validation
"""

# Write your code below this line




# ---------------------------------------------------------------------
# EXERCISE 9: Validate Environment
# ---------------------------------------------------------------------

"""
TODO:
- Ask the user to enter environment
- Clean input using strip()
- Convert input to uppercase
- Keep asking while environment is not DEV, TEST, or PROD
- Print accepted environment

Concept focus:
controlled validation loop
"""

# Write your code below this line




# ---------------------------------------------------------------------
# EXERCISE 10: Validate Usage Percentage
# ---------------------------------------------------------------------

"""
TODO:
- Ask the user for CPU usage percentage
- Convert it to float
- Keep asking while the value is less than 0 or greater than 100
- Print accepted CPU usage

Assume the user enters numeric input for now.
Exception handling will come later.

Concept focus:
numeric validation
"""

# Write your code below this line




# ---------------------------------------------------------------------
# EXERCISE 11: Print Repeated Health Check Steps
# ---------------------------------------------------------------------

"""
TODO:
- Create check_count = 3
- Use a while loop to print:
    Running health check step: 1
    Running health check step: 2
    Running health check step: 3

Concept focus:
using loops inside a workflow
"""

# Write your code below this line




# ---------------------------------------------------------------------
# EXERCISE 12: Generate a Clean Final Report with Fixed Values
# ---------------------------------------------------------------------

"""
Given:
server_name = "app01"
environment = "PROD"
cpu_usage = 72
memory_usage = 83
disk_usage = 67

TODO:
- Decide overall status using the rule:
    CRITICAL if any metric is >= 90
    WARNING if any metric is >= 80
    OK otherwise
- Decide action message using the status
- Print a clean final report

Expected style:
========================================
Server Health Message
========================================
Server      : app01
Environment : PROD
CPU Usage   : 72
Memory      : 83
Disk Usage  : 67
Status      : WARNING
Action      : Review during current shift
========================================

Concept focus:
complete report formatting with fixed values
"""

server_name = "app01"
environment = "PROD"
cpu_usage = 72
memory_usage = 83
disk_usage = 67

# Write your code below this line




# ---------------------------------------------------------------------
# EXERCISE 13: Mini Project - Server Health Message Generator
# ---------------------------------------------------------------------

"""
Build a complete Server Health Message Generator.

Collect all required inputs once at the beginning using validation loops:
1. Server name
2. Environment
3. CPU usage percentage
4. Memory usage percentage
5. Disk usage percentage

TODO:
- Keep asking for server name until it is not blank
- Keep asking for environment until it is DEV, TEST, or PROD
- Keep asking for CPU usage until it is between 0 and 100
- Keep asking for memory usage until it is between 0 and 100
- Keep asking for disk usage until it is between 0 and 100
- Decide final status:
    CRITICAL if any metric is >= 90
    WARNING if any metric is >= 80
    OK otherwise
- Decide action:
    Immediate action required for CRITICAL
    Review during current shift for WARNING
    No action required for OK
- Generate a final health message
- Print a clean final report

Expected output style:
========================================
Server Health Message Generator
========================================
Server      : app01
Environment : PROD
CPU Usage   : 82.0
Memory      : 74.0
Disk Usage  : 69.0
Status      : WARNING
Action      : Review during current shift
Message     : app01 in PROD is WARNING. Review during current shift.
========================================

Important:
Ask each input only once in its own validation section.
Reuse those variables throughout the project.
This should feel like one complete automation workflow.
"""

# Write your mini project code below this line




print("\nExercise file loaded successfully. Complete the tasks one by one.")
