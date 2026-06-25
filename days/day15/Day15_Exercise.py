"""
Python for Mammals - Day 15 Exercise File
Topic: Nested Data Structure

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
By the end of these exercises, you should be able to create a list of dictionaries,
loop through nested records, access values inside nested data, create a dictionary
of lists, and build practical structured reports.
"""

print("=" * 70)
print("DAY 15 EXERCISES - NESTED DATA STRUCTURE")
print("LIST OF DICTIONARIES, DICTIONARY OF LISTS, REAL-WORLD DATA")
print("=" * 70)

# ---------------------------------------------------------------------
# EXERCISE 1: Create a List of Server Dictionaries
# ---------------------------------------------------------------------

"""
TODO:
- Create a list named servers
- Add 3 dictionaries inside the list
- Each dictionary should have these keys:
  name, environment, status
- Print the full servers list
- Print the type of servers

Concept focus:
list of dictionaries
"""

# Write your code below this line




# ---------------------------------------------------------------------
# EXERCISE 2: Access One Dictionary from the List
# ---------------------------------------------------------------------

"""
Given:
servers = [
    {"name": "app01", "environment": "production", "status": "active"},
    {"name": "web01", "environment": "uat", "status": "active"},
    {"name": "batch01", "environment": "test", "status": "maintenance"}
]

TODO:
- Print the first dictionary from the list
- Print the second dictionary from the list
- Print the name of the first server
- Print the status of the third server

Concept focus:
accessing nested data step by step
"""

servers = [
    {"name": "app01", "environment": "production", "status": "active"},
    {"name": "web01", "environment": "uat", "status": "active"},
    {"name": "batch01", "environment": "test", "status": "maintenance"}
]

# Write your code below this line




# ---------------------------------------------------------------------
# EXERCISE 3: Loop Through Server Records
# ---------------------------------------------------------------------

"""
Given:
servers = [
    {"name": "app01", "environment": "production", "status": "active"},
    {"name": "web01", "environment": "uat", "status": "active"},
    {"name": "batch01", "environment": "test", "status": "maintenance"}
]

TODO:
- Loop through the list
- Print server name, environment, and status in one readable line

Example style:
app01 - production - active

Concept focus:
looping through a list of dictionaries
"""

servers = [
    {"name": "app01", "environment": "production", "status": "active"},
    {"name": "web01", "environment": "uat", "status": "active"},
    {"name": "batch01", "environment": "test", "status": "maintenance"}
]

# Write your code below this line




# ---------------------------------------------------------------------
# EXERCISE 4: Create a Clean Inventory Report
# ---------------------------------------------------------------------

"""
Given:
inventory = [
    {"server": "app01", "os": "linux", "owner": "app-team"},
    {"server": "db01", "os": "linux", "owner": "database-team"},
    {"server": "win01", "os": "windows", "owner": "infra-team"}
]

TODO:
- Print a report title
- Loop through the inventory list
- For each record, print server, os, and owner in readable format
- Print a separator line after each record

Concept focus:
report generation from nested data
"""

inventory = [
    {"server": "app01", "os": "linux", "owner": "app-team"},
    {"server": "db01", "os": "linux", "owner": "database-team"},
    {"server": "win01", "os": "windows", "owner": "infra-team"}
]

# Write your code below this line




# ---------------------------------------------------------------------
# EXERCISE 5: Count Production Servers
# ---------------------------------------------------------------------

"""
Given:
servers = [
    {"name": "app01", "environment": "production"},
    {"name": "db01", "environment": "production"},
    {"name": "web01", "environment": "uat"},
    {"name": "test01", "environment": "test"}
]

TODO:
- Create a counter variable named production_count
- Loop through the list
- Increase the counter when environment is production
- Print the final production_count

Concept focus:
counting records based on nested dictionary values
"""

servers = [
    {"name": "app01", "environment": "production"},
    {"name": "db01", "environment": "production"},
    {"name": "web01", "environment": "uat"},
    {"name": "test01", "environment": "test"}
]

# Write your code below this line




# ---------------------------------------------------------------------
# EXERCISE 6: Print Non-Active Servers
# ---------------------------------------------------------------------

"""
Given:
servers = [
    {"name": "app01", "status": "active"},
    {"name": "batch01", "status": "maintenance"},
    {"name": "oldweb01", "status": "retired"},
    {"name": "db01", "status": "active"}
]

TODO:
- Loop through the list
- Print only servers where status is not active

Concept focus:
filtering records from nested data
"""

servers = [
    {"name": "app01", "status": "active"},
    {"name": "batch01", "status": "maintenance"},
    {"name": "oldweb01", "status": "retired"},
    {"name": "db01", "status": "active"}
]

# Write your code below this line




# ---------------------------------------------------------------------
# EXERCISE 7: Add Usage Percentage to Disk Records
# ---------------------------------------------------------------------

"""
Given:
disks = [
    {"server": "app01", "total_gb": 100, "used_gb": 72},
    {"server": "db01", "total_gb": 500, "used_gb": 455},
    {"server": "web01", "total_gb": 200, "used_gb": 88}
]

TODO:
- Loop through the list
- Calculate usage percentage for each dictionary
- Add usage_percent to each dictionary
- Round usage_percent to 2 decimal places
- Print each updated dictionary

Concept focus:
adding calculated values to each nested record
"""

disks = [
    {"server": "app01", "total_gb": 100, "used_gb": 72},
    {"server": "db01", "total_gb": 500, "used_gb": 455},
    {"server": "web01", "total_gb": 200, "used_gb": 88}
]

# Write your code below this line




# ---------------------------------------------------------------------
# EXERCISE 8: Add Disk Status to Each Record
# ---------------------------------------------------------------------

"""
Given:
disks = [
    {"server": "app01", "usage_percent": 72},
    {"server": "db01", "usage_percent": 91},
    {"server": "web01", "usage_percent": 84}
]

TODO:
- Loop through the list
- Add status CRITICAL if usage_percent is greater than or equal to 90
- Add status WARNING if usage_percent is greater than or equal to 80
- Add status OK otherwise
- Print server, usage_percent, and status for every record

Concept focus:
conditions inside loops with nested data
"""

disks = [
    {"server": "app01", "usage_percent": 72},
    {"server": "db01", "usage_percent": 91},
    {"server": "web01", "usage_percent": 84}
]

# Write your code below this line




# ---------------------------------------------------------------------
# EXERCISE 9: Create a Dictionary of Lists
# ---------------------------------------------------------------------

"""
TODO:
- Create a dictionary named monitoring_data
- Add these keys:
  servers, cpu_percent, memory_percent
- servers should contain 3 server names
- cpu_percent should contain 3 CPU numbers
- memory_percent should contain 3 memory numbers
- Print the dictionary
- Print only the servers list

Concept focus:
dictionary of lists
"""

# Write your code below this line




# ---------------------------------------------------------------------
# EXERCISE 10: Loop Through Dictionary of Lists
# ---------------------------------------------------------------------

"""
Given:
monitoring_data = {
    "servers": ["app01", "db01", "web01"],
    "cpu_percent": [65, 82, 91],
    "memory_percent": [70, 76, 88]
}

TODO:
- Use range() and len() to loop through the indexes
- Print server name, CPU percentage, and memory percentage for each index

Concept focus:
reading related list values by index
"""

monitoring_data = {
    "servers": ["app01", "db01", "web01"],
    "cpu_percent": [65, 82, 91],
    "memory_percent": [70, 76, 88]
}

# Write your code below this line




# ---------------------------------------------------------------------
# EXERCISE 11: Alert Filtering
# ---------------------------------------------------------------------

"""
Given:
alerts = [
    {"alert_id": "A1001", "server": "app01", "severity": "HIGH"},
    {"alert_id": "A1002", "server": "db01", "severity": "CRITICAL"},
    {"alert_id": "A1003", "server": "web01", "severity": "LOW"}
]

TODO:
- Loop through the alerts
- Print only alerts where severity is HIGH or CRITICAL

Concept focus:
filtering alert records
"""

alerts = [
    {"alert_id": "A1001", "server": "app01", "severity": "HIGH"},
    {"alert_id": "A1002", "server": "db01", "severity": "CRITICAL"},
    {"alert_id": "A1003", "server": "web01", "severity": "LOW"}
]

# Write your code below this line




# ---------------------------------------------------------------------
# EXERCISE 12: Backup Job Summary
# ---------------------------------------------------------------------

"""
Given:
backup_jobs = [
    {"database": "PRODDB", "type": "FULL", "status": "SUCCESS"},
    {"database": "APPDB", "type": "ARCHIVELOG", "status": "SUCCESS"},
    {"database": "TESTDB", "type": "FULL", "status": "FAILED"}
]

TODO:
- Count successful backups
- Count failed backups
- Print both counts

Concept focus:
summarizing operational records
"""

backup_jobs = [
    {"database": "PRODDB", "type": "FULL", "status": "SUCCESS"},
    {"database": "APPDB", "type": "ARCHIVELOG", "status": "SUCCESS"},
    {"database": "TESTDB", "type": "FULL", "status": "FAILED"}
]

# Write your code below this line




# ---------------------------------------------------------------------
# EXERCISE 13: Build a Ticket List from User Inputs
# ---------------------------------------------------------------------

"""
TODO:
- Collect details for 2 tickets using input()
- For each ticket collect:
  ticket_id, priority, owner, status
- Store each ticket as a dictionary
- Add both dictionaries to a list named tickets
- Print the final tickets list

Concept focus:
building nested data from user input
"""

# Write your code below this line




# ---------------------------------------------------------------------
# EXERCISE 14: Mini Project - Daily Operations Nested Report
# ---------------------------------------------------------------------

"""
Build a small Daily Operations Nested Report script.

Collect all required inputs once at the beginning:
1. Server 1 name
2. Server 1 environment
3. Server 1 CPU usage percentage
4. Server 1 memory usage percentage
5. Server 1 disk usage percentage
6. Server 2 name
7. Server 2 environment
8. Server 2 CPU usage percentage
9. Server 2 memory usage percentage
10. Server 2 disk usage percentage
11. Server 3 name
12. Server 3 environment
13. Server 3 CPU usage percentage
14. Server 3 memory usage percentage
15. Server 3 disk usage percentage

TODO:
- Store all three servers as dictionaries inside a list named daily_checks
- Convert CPU, memory, and disk inputs into numbers
- For each server dictionary:
  - Calculate highest usage among CPU, memory, and disk
  - Add highest_usage to that dictionary
  - Add status:
    - CRITICAL if highest usage is greater than or equal to 90
    - WARNING if highest usage is greater than or equal to 80
    - OK otherwise
  - Add action:
    - Immediate review required for CRITICAL
    - Monitor closely for WARNING
    - No action required for OK
- Count how many servers are CRITICAL, WARNING, and OK
- Print a clean final report for all servers
- Print the final summary counts

Expected output style:
==================================================
Daily Operations Nested Report
==================================================
Server        : app01
Environment   : production
CPU           : 88.0
Memory        : 76.0
Disk          : 91.0
Highest Usage : 91.0
Status        : CRITICAL
Action        : Immediate review required
--------------------------------------------------
Summary
Critical: 1
Warning : 1
OK      : 1
==================================================

Important:
Collect each required input once at the beginning.
Reuse those variables throughout the mini project.
Do not ask for the same input multiple times.
This should feel like one complete automation workflow.
"""

# Write your mini project code below this line




print("\nExercise file loaded successfully. Complete the tasks one by one.")
