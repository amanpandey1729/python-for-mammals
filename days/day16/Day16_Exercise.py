"""
Python for Mammals - Day 16 Exercise File
Topic: Functions

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
By the end of these exercises, you should be able to define functions,
call functions, pass values using parameters, and reuse function blocks
for practical automation-style reports and checks.
"""

print("=" * 70)
print("DAY 16 EXERCISES - FUNCTIONS")
print("DEFINE FUNCTIONS, CALL FUNCTIONS, PARAMETERS")
print("=" * 70)

# ---------------------------------------------------------------------
# EXERCISE 1: Create and Call a Simple Function
# ---------------------------------------------------------------------

"""
TODO:
- Create a function named show_welcome
- Inside the function, print a welcome message for a daily automation script
- Call the function once

Concept focus:
defining and calling a basic function
"""

# Write your code below this line




# ---------------------------------------------------------------------
# EXERCISE 2: Call the Same Function Multiple Times
# ---------------------------------------------------------------------

"""
TODO:
- Create a function named print_separator
- Inside the function, print 40 hyphens
- Call the function 3 times

Concept focus:
reusing the same function multiple times
"""

# Write your code below this line




# ---------------------------------------------------------------------
# EXERCISE 3: Function for Report Title
# ---------------------------------------------------------------------

"""
TODO:
- Create a function named show_report_title
- Inside the function, print:
  Daily Operations Report
  followed by 50 equal signs
- Call the function once

Concept focus:
using a function to keep report formatting reusable
"""

# Write your code below this line




# ---------------------------------------------------------------------
# EXERCISE 4: Function with One Parameter
# ---------------------------------------------------------------------

"""
TODO:
- Create a function named greet_user
- The function should accept one parameter named user_name
- Print a message like:
  Hello Aman, your automation script is ready.
- Call the function with any name

Concept focus:
one parameter
"""

# Write your code below this line




# ---------------------------------------------------------------------
# EXERCISE 5: Report Title with Parameter
# ---------------------------------------------------------------------

"""
TODO:
- Create a function named print_report_header
- The function should accept one parameter named report_name
- It should print the report name
- It should print a separator line below it
- Call the function for:
  Server Health Report
  Backup Summary Report
  Ticket Aging Report

Concept focus:
using one function with different values
"""

# Write your code below this line




# ---------------------------------------------------------------------
# EXERCISE 6: Function with Two Parameters
# ---------------------------------------------------------------------

"""
TODO:
- Create a function named show_server_environment
- The function should accept:
  server_name, environment
- Print a readable line like:
  app01 belongs to production environment
- Call the function at least 2 times with different values

Concept focus:
multiple parameters
"""

# Write your code below this line




# ---------------------------------------------------------------------
# EXERCISE 7: Function with Three Parameters
# ---------------------------------------------------------------------

"""
TODO:
- Create a function named show_ticket_summary
- The function should accept:
  ticket_id, priority, owner
- Print the ticket details in one readable line
- Call the function for 3 different tickets

Concept focus:
parameter order and readable output
"""

# Write your code below this line




# ---------------------------------------------------------------------
# EXERCISE 8: Disk Usage Function
# ---------------------------------------------------------------------

"""
TODO:
- Create a function named calculate_disk_usage
- The function should accept:
  total_gb, used_gb
- Calculate usage percentage
- Print the usage percentage rounded to 2 decimal places
- Call the function for at least 2 disk examples

Concept focus:
calculation inside function
"""

# Write your code below this line




# ---------------------------------------------------------------------
# EXERCISE 9: CPU Status Function
# ---------------------------------------------------------------------

"""
TODO:
- Create a function named check_cpu_status
- The function should accept:
  server_name, cpu_percent
- Print:
  CRITICAL if cpu_percent is greater than or equal to 90
  WARNING if cpu_percent is greater than or equal to 80
  OK otherwise
- Call the function for 3 different servers

Concept focus:
conditions inside function
"""

# Write your code below this line




# ---------------------------------------------------------------------
# EXERCISE 10: Backup Message Function
# ---------------------------------------------------------------------

"""
TODO:
- Create a function named show_backup_message
- The function should accept:
  database_name, backup_type, backup_status
- Print a clean backup message
- Call the function for at least 3 backup jobs

Concept focus:
function parameters for operational messages
"""

# Write your code below this line




# ---------------------------------------------------------------------
# EXERCISE 11: Function Used Inside a Loop
# ---------------------------------------------------------------------

"""
Given:
servers = [
    {"name": "app01", "environment": "production", "status": "active"},
    {"name": "db01", "environment": "production", "status": "maintenance"},
    {"name": "web01", "environment": "uat", "status": "active"}
]

TODO:
- Create a function named print_server_line
- The function should accept server_name, environment, status
- Loop through the servers list
- Call the function for each dictionary

Concept focus:
using functions with list of dictionaries
"""

servers = [
    {"name": "app01", "environment": "production", "status": "active"},
    {"name": "db01", "environment": "production", "status": "maintenance"},
    {"name": "web01", "environment": "uat", "status": "active"}
]

# Write your code below this line




# ---------------------------------------------------------------------
# EXERCISE 12: Function for Alert Formatting
# ---------------------------------------------------------------------

"""
Given:
alerts = [
    {"alert_id": "A1001", "server": "app01", "severity": "HIGH"},
    {"alert_id": "A1002", "server": "db01", "severity": "CRITICAL"},
    {"alert_id": "A1003", "server": "web01", "severity": "LOW"}
]

TODO:
- Create a function named print_alert
- The function should accept alert_id, server, severity
- Loop through alerts
- Print only HIGH or CRITICAL alerts by calling the function

Concept focus:
filtering records and using function for output
"""

alerts = [
    {"alert_id": "A1001", "server": "app01", "severity": "HIGH"},
    {"alert_id": "A1002", "server": "db01", "severity": "CRITICAL"},
    {"alert_id": "A1003", "server": "web01", "severity": "LOW"}
]

# Write your code below this line




# ---------------------------------------------------------------------
# EXERCISE 13: Function-Based Mini Report from User Input
# ---------------------------------------------------------------------

"""
TODO:
- Collect these inputs:
  server_name
  environment
  status
- Create a function named show_server_report
- The function should accept server_name, environment, status
- The function should print a clean mini report
- Call the function using the values collected from input()

Concept focus:
collect input once and pass values to a function
"""

# Write your code below this line




# ---------------------------------------------------------------------
# EXERCISE 14: Mini Project - Function-Based Daily Health Reporter
# ---------------------------------------------------------------------

"""
Build a small Function-Based Daily Health Reporter script.

Collect all required inputs once at the beginning:
1. Server Name
2. Environment
3. CPU usage percentage
4. Memory usage percentage
5. Disk usage percentage
6. Backup status
7. Open critical ticket count

TODO:
- Convert CPU, memory, disk, and ticket count values into numbers
- Create a function named print_header
  - It should accept report_name
  - It should print a clean report title and separator

- Create a function named print_metric
  - It should accept metric_name and metric_value
  - It should print one clean metric line

- Create a function named print_usage_status
  - It should accept metric_name and usage_percent
  - It should print:
    CRITICAL if usage_percent is greater than or equal to 90
    WARNING if usage_percent is greater than or equal to 80
    OK otherwise

- Create a function named print_backup_status
  - It should accept backup_status
  - It should print backup status clearly

- Create a function named print_ticket_status
  - It should accept critical_ticket_count
  - It should print:
    ACTION REQUIRED if critical_ticket_count is greater than 0
    NO CRITICAL TICKETS otherwise

- Use the functions to generate one final report containing:
  - Server name
  - Environment
  - CPU usage and status
  - Memory usage and status
  - Disk usage and status
  - Backup status
  - Critical ticket status

Important:
- Collect each input only once.
- Reuse the variables throughout the project.
- Do not ask for the same input repeatedly.
- The mini project should look like one complete automation workflow.

Concept focus:
real-world function-based automation structure
"""

# Write your code below this line




print("\nEnd of Day 16 exercises. Complete the TODO sections one by one.")
