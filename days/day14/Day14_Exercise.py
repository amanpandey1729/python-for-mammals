"""
Python for Mammals - Day 14 Exercise File
Topic: Dictionaries

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
By the end of these exercises, you should be able to create dictionaries,
access values using keys, update values, add new key-value pairs, and loop
through dictionaries for practical automation workflows.
"""

print("=" * 70)
print("DAY 14 EXERCISES - DICTIONARIES")
print("KEY-VALUE PAIRS, ACCESS, UPDATE, LOOPING")
print("=" * 70)

# ---------------------------------------------------------------------
# EXERCISE 1: Create a Server Dictionary
# ---------------------------------------------------------------------

"""
TODO:
- Create a dictionary named server with these keys:
  name, environment, os
- Use any practical values such as app01, production, linux
- Print the dictionary
- Print the type of the dictionary

Concept focus:
dictionary creation
"""

# Write your code below this line




# ---------------------------------------------------------------------
# EXERCISE 2: Access Dictionary Values
# ---------------------------------------------------------------------

"""
Given:
server = {
    "name": "app01",
    "environment": "production",
    "os": "linux"
}

TODO:
- Print the server name using the name key
- Print the environment using the environment key
- Print the OS type using the os key

Concept focus:
accessing values using keys
"""

server = {
    "name": "app01",
    "environment": "production",
    "os": "linux"
}

# Write your code below this line




# ---------------------------------------------------------------------
# EXERCISE 3: Create a Backup Job Dictionary
# ---------------------------------------------------------------------

"""
TODO:
- Create a dictionary named backup_job with these keys:
  database, backup_type, status
- Print each value in a readable format

Example style:
Database    : PRODDB
Backup Type : FULL
Status      : SUCCESS

Concept focus:
key-value pairs for operational records
"""

# Write your code below this line




# ---------------------------------------------------------------------
# EXERCISE 4: Update a Server Status
# ---------------------------------------------------------------------

"""
Given:
server_health = {
    "server": "web01",
    "cpu_percent": 65,
    "status": "OK"
}

TODO:
- Print the dictionary before update
- Update cpu_percent to 92
- Update status to CRITICAL
- Print the dictionary after update

Concept focus:
updating dictionary values
"""

server_health = {
    "server": "web01",
    "cpu_percent": 65,
    "status": "OK"
}

# Write your code below this line




# ---------------------------------------------------------------------
# EXERCISE 5: Add New Keys to a Dictionary
# ---------------------------------------------------------------------

"""
Given:
server = {
    "name": "db01",
    "environment": "production"
}

TODO:
- Add a new key owner with value platform-team
- Add a new key status with value active
- Print the updated dictionary

Concept focus:
adding new key-value pairs
"""

server = {
    "name": "db01",
    "environment": "production"
}

# Write your code below this line




# ---------------------------------------------------------------------
# EXERCISE 6: Use get() for Optional Data
# ---------------------------------------------------------------------

"""
Given:
server = {
    "name": "app01",
    "environment": "uat"
}

TODO:
- Print the name using get()
- Print the owner using get()
- For owner, provide default value not assigned

Concept focus:
safe dictionary access using get()
"""

server = {
    "name": "app01",
    "environment": "uat"
}

# Write your code below this line




# ---------------------------------------------------------------------
# EXERCISE 7: Check If a Key Exists
# ---------------------------------------------------------------------

"""
Given:
ticket = {
    "ticket_id": "INC1001",
    "priority": "P2",
    "status": "open"
}

TODO:
- Check if priority exists in the dictionary
- If it exists, print Priority key found
- Check if owner does not exist in the dictionary
- If it does not exist, print Owner key missing

Concept focus:
in and not in with dictionary keys
"""

ticket = {
    "ticket_id": "INC1001",
    "priority": "P2",
    "status": "open"
}

# Write your code below this line




# ---------------------------------------------------------------------
# EXERCISE 8: Loop Through Dictionary Keys
# ---------------------------------------------------------------------

"""
Given:
server = {
    "name": "app01",
    "environment": "production",
    "os": "linux"
}

TODO:
- Loop through the dictionary
- Print each key

Concept focus:
looping through dictionary keys
"""

server = {
    "name": "app01",
    "environment": "production",
    "os": "linux"
}

# Write your code below this line




# ---------------------------------------------------------------------
# EXERCISE 9: Loop Through Dictionary Values
# ---------------------------------------------------------------------

"""
Given:
server = {
    "name": "app01",
    "environment": "production",
    "os": "linux"
}

TODO:
- Loop through server.values()
- Print each value

Concept focus:
looping through dictionary values
"""

server = {
    "name": "app01",
    "environment": "production",
    "os": "linux"
}

# Write your code below this line




# ---------------------------------------------------------------------
# EXERCISE 10: Loop Through Keys and Values
# ---------------------------------------------------------------------

"""
Given:
server = {
    "name": "app01",
    "environment": "production",
    "os": "linux"
}

TODO:
- Loop through server.items()
- Print each key and value in readable format

Example style:
name : app01
environment : production
os : linux

Concept focus:
looping through dictionary items
"""

server = {
    "name": "app01",
    "environment": "production",
    "os": "linux"
}

# Write your code below this line




# ---------------------------------------------------------------------
# EXERCISE 11: Build a Ticket Summary
# ---------------------------------------------------------------------

"""
TODO:
- Create a dictionary named ticket with these keys:
  ticket_id, priority, owner, status
- Print a clean ticket summary by looping through items()

Concept focus:
dictionary report generation
"""

# Write your code below this line




# ---------------------------------------------------------------------
# EXERCISE 12: Add Calculated Disk Usage
# ---------------------------------------------------------------------

"""
Given:
disk_check = {
    "server": "db01",
    "mount_point": "/u01",
    "total_gb": 500,
    "used_gb": 425
}

TODO:
- Calculate usage percentage
- Add it to the dictionary using key usage_percent
- Round the percentage to 2 decimal places
- Print the updated dictionary

Concept focus:
adding calculated values to dictionaries
"""

disk_check = {
    "server": "db01",
    "mount_point": "/u01",
    "total_gb": 500,
    "used_gb": 425
}

# Write your code below this line




# ---------------------------------------------------------------------
# EXERCISE 13: Determine Disk Status
# ---------------------------------------------------------------------

"""
Given:
disk_check = {
    "server": "db01",
    "mount_point": "/u01",
    "usage_percent": 85
}

TODO:
- If usage_percent is greater than or equal to 90, add status CRITICAL
- Else if usage_percent is greater than or equal to 80, add status WARNING
- Else add status OK
- Print the updated dictionary

Concept focus:
conditions with dictionary values
"""

disk_check = {
    "server": "db01",
    "mount_point": "/u01",
    "usage_percent": 85
}

# Write your code below this line




# ---------------------------------------------------------------------
# EXERCISE 14: Mini Project - Server Health Dictionary Report
# ---------------------------------------------------------------------

"""
Build a small Server Health Dictionary Report script.

Collect all required inputs once at the beginning:
1. Server name
2. Environment
3. CPU usage percentage
4. Memory usage percentage
5. Disk usage percentage
6. Owner/team name

TODO:
- Store all collected values in a dictionary named server_health
- Convert CPU, memory, and disk inputs into numbers
- Calculate the highest usage among CPU, memory, and disk
- Add highest_usage to the dictionary
- Determine final status:
  - CRITICAL if highest usage is greater than or equal to 90
  - WARNING if highest usage is greater than or equal to 80
  - OK otherwise
- Add the final status to the dictionary
- Add an action message:
  - Immediate review required for CRITICAL
  - Monitor closely for WARNING
  - No action required for OK
- Print a clean final report by looping through server_health.items()

Expected output style:
========================================
Server Health Dictionary Report
========================================
server : app01
environment : production
cpu_percent : 88.0
memory_percent : 76.0
disk_percent : 91.0
owner : app-team
highest_usage : 91.0
status : CRITICAL
action : Immediate review required
========================================

Important:
Collect each required input once at the beginning.
Reuse those variables throughout the mini project.
Do not ask for the same input multiple times.
This should feel like one complete automation workflow.
"""

# Write your mini project code below this line




print("\nExercise file loaded successfully. Complete the tasks one by one.")
