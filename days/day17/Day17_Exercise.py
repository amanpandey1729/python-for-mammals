"""
Python for Mammals - Day 17 Exercise File
Topic: Return Values & Scope

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
By the end of these exercises, you should be able to return values from
functions, store returned values in variables, understand local/global
scope, and build reusable function-based automation workflows.
"""

print("=" * 70)
print("DAY 17 EXERCISES - RETURN VALUES & SCOPE")
print("RETURN, LOCAL VARIABLES, GLOBAL VARIABLES, REUSABLE FUNCTIONS")
print("=" * 70)

# ---------------------------------------------------------------------
# EXERCISE 1: Return a Simple Message
# ---------------------------------------------------------------------

"""
TODO:
- Create a function named get_welcome_message
- The function should return this text:
  Daily automation script started
- Store the returned value in a variable
- Print the variable

Concept focus:
basic return value
"""

# Write your code below this line




# ---------------------------------------------------------------------
# EXERCISE 2: Return a Report Title
# ---------------------------------------------------------------------

"""
TODO:
- Create a function named build_report_title
- The function should accept one parameter named report_name
- It should return a string like:
  Report: Server Health Report
- Call the function with any report name
- Store and print the returned title

Concept focus:
returning formatted text
"""

# Write your code below this line




# ---------------------------------------------------------------------
# EXERCISE 3: Return Disk Usage Percentage
# ---------------------------------------------------------------------

"""
TODO:
- Create a function named calculate_disk_usage
- The function should accept total_gb and used_gb
- Calculate usage percentage
- Return the usage percentage
- Store the returned value in a variable
- Print the value rounded to 2 decimal places

Concept focus:
returning calculated numbers
"""

# Write your code below this line




# ---------------------------------------------------------------------
# EXERCISE 4: Return Free Space
# ---------------------------------------------------------------------

"""
TODO:
- Create a function named calculate_free_space
- The function should accept total_gb and used_gb
- Return free space in GB
- Call the function for one server disk example
- Print the returned free space

Concept focus:
small calculation function
"""

# Write your code below this line




# ---------------------------------------------------------------------
# EXERCISE 5: Return Health Status
# ---------------------------------------------------------------------

"""
TODO:
- Create a function named get_usage_status
- The function should accept usage_percent
- Return:
  CRITICAL if usage_percent is greater than or equal to 90
  WARNING if usage_percent is greater than or equal to 80
  OK otherwise
- Call the function for at least 3 usage values
- Print the returned statuses

Concept focus:
return with if / elif / else
"""

# Write your code below this line




# ---------------------------------------------------------------------
# EXERCISE 6: Use Returned Value in a Condition
# ---------------------------------------------------------------------

"""
TODO:
- Create a function named get_backup_health
- The function should accept backup_status
- Return OK if backup_status is SUCCESS
- Return ACTION REQUIRED otherwise
- Store the returned value in a variable
- If returned value is ACTION REQUIRED, print:
  Backup needs investigation
- Otherwise print:
  Backup is healthy

Concept focus:
using a returned value in decision logic
"""

# Write your code below this line




# ---------------------------------------------------------------------
# EXERCISE 7: Return Multiple Values
# ---------------------------------------------------------------------

"""
TODO:
- Create a function named calculate_storage_summary
- The function should accept total_gb and used_gb
- Return two values:
  free_gb
  usage_percent
- Capture both returned values in two variables
- Print both values clearly

Concept focus:
returning multiple values
"""

# Write your code below this line




# ---------------------------------------------------------------------
# EXERCISE 8: Local Variable Practice
# ---------------------------------------------------------------------

"""
TODO:
- Create a function named calculate_ticket_age
- The function should accept opened_day and current_day
- Inside the function, create a local variable named ticket_age
- Return ticket_age
- Call the function and print the returned age

Concept focus:
local variable inside a function
"""

# Write your code below this line




# ---------------------------------------------------------------------
# EXERCISE 9: Global Variable Read Practice
# ---------------------------------------------------------------------

"""
TODO:
- Create a global variable named team_name with any team value
- Create a function named build_team_report_title
- The function should accept report_name
- Inside the function, use team_name and report_name to return a title
- Call the function and print the returned title

Concept focus:
reading a global variable inside a function
"""

# Write your code below this line




# ---------------------------------------------------------------------
# EXERCISE 10: Prefer Parameters Over Globals
# ---------------------------------------------------------------------

"""
TODO:
- Create a function named build_report_owner_line
- The function should accept team_name and owner_name
- It should return a line like:
  Team: Infra | Owner: Ravi
- Call the function twice with different values
- Print both returned lines

Concept focus:
passing values as parameters instead of depending on globals
"""

# Write your code below this line




# ---------------------------------------------------------------------
# EXERCISE 11: Function Calling Another Function
# ---------------------------------------------------------------------

"""
TODO:
- Create a function named calculate_usage_percent
- It should accept total and used
- It should return usage percentage

- Create another function named build_usage_line
- It should accept resource_name, total, used
- It should call calculate_usage_percent internally
- It should return a line like:
  Disk usage is 75.0%

- Call build_usage_line for CPU, Memory, or Disk style examples

Concept focus:
reusable function calling another reusable function
"""

# Write your code below this line




# ---------------------------------------------------------------------
# EXERCISE 12: Return Alert Priority
# ---------------------------------------------------------------------

"""
TODO:
- Create a function named get_alert_priority
- The function should accept severity
- Return:
  P1 if severity is CRITICAL
  P2 if severity is HIGH
  P3 otherwise
- Use the function for at least 3 alert severities
- Print the returned priorities

Concept focus:
returning normalized values for reports
"""

# Write your code below this line




# ---------------------------------------------------------------------
# EXERCISE 13: Return Values with a List of Dictionaries
# ---------------------------------------------------------------------

"""
Given:
servers = [
    {"name": "app01", "disk_total": 500, "disk_used": 350},
    {"name": "db01", "disk_total": 1000, "disk_used": 920},
    {"name": "web01", "disk_total": 200, "disk_used": 120}
]

TODO:
- Create a function named calculate_usage
- It should accept total and used
- It should return usage percentage
- Loop through the servers list
- For each server, call calculate_usage
- Print server name and returned usage percentage

Concept focus:
using returned values while processing records
"""

servers = [
    {"name": "app01", "disk_total": 500, "disk_used": 350},
    {"name": "db01", "disk_total": 1000, "disk_used": 920},
    {"name": "web01", "disk_total": 200, "disk_used": 120}
]

# Write your code below this line




# ---------------------------------------------------------------------
# EXERCISE 14: Mini Project - Return-Based Server Health Reporter
# ---------------------------------------------------------------------

"""
Build a small Return-Based Server Health Reporter script.

Collect all required inputs once at the beginning:
1. Server Name
2. Environment
3. CPU usage percentage
4. Memory usage percentage
5. Disk total GB
6. Disk used GB
7. Backup status
8. Open critical ticket count

TODO:
- Convert CPU, memory, disk total, disk used, and ticket count into numbers

- Create a function named calculate_usage_percent
  - It should accept total and used
  - It should return usage percentage
  - For CPU and memory, you may pass 100 as total and the usage value as used

- Create a function named get_usage_status
  - It should accept usage_percent
  - It should return:
    CRITICAL if usage_percent is greater than or equal to 90
    WARNING if usage_percent is greater than or equal to 80
    OK otherwise

- Create a function named get_backup_health
  - It should accept backup_status
  - It should return OK if backup_status is SUCCESS
  - It should return ACTION REQUIRED otherwise

- Create a function named get_ticket_health
  - It should accept critical_ticket_count
  - It should return ACTION REQUIRED if critical_ticket_count is greater than 0
  - It should return OK otherwise

- Create a function named build_report_line
  - It should accept label and value
  - It should return a clean report line like:
    CPU Status: WARNING

- Use returned values to calculate:
  - CPU status
  - Memory status
  - Disk usage percentage
  - Disk status
  - Backup health
  - Ticket health

- Generate one final report containing:
  - Server name
  - Environment
  - CPU usage and status
  - Memory usage and status
  - Disk usage and status
  - Backup health
  - Ticket health

Important:
- Collect each input only once.
- Reuse the variables throughout the project.
- Do not ask for the same input repeatedly.
- Functions should return values where possible.
- The mini project should look like one complete automation workflow.

Concept focus:
return-based reusable automation design
"""

# Write your code below this line




print("\nEnd of Day 17 exercises. Complete the TODO sections one by one.")
