"""
Python for Mammals - Day 12 Exercise File
Topic: List Operations

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
By the end of these exercises, you should be able to add, insert,
remove, pop, sort, reverse, and loop through list values for practical
operations-style automation workflows.
"""

print("=" * 70)
print("DAY 12 EXERCISES - LIST OPERATIONS")
print("APPEND, INSERT, REMOVE, POP, SORT, REVERSE, LOOPING THROUGH LISTS")
print("=" * 70)

# ---------------------------------------------------------------------
# EXERCISE 1: Add Server to Inventory
# ---------------------------------------------------------------------

"""
TODO:
- Create a list named servers with app01 and db01
- Add web01 using append()
- Print the final list

Concept focus:
append()
"""

# Write your code below this line




# ---------------------------------------------------------------------
# EXERCISE 2: Add a Log File to Processing List
# ---------------------------------------------------------------------

"""
TODO:
- Create a list named log_files with alert.log and listener.log
- Add backup.log using append()
- Print the final list

Concept focus:
adding a new item at the end
"""

# Write your code below this line




# ---------------------------------------------------------------------
# EXERCISE 3: Insert a Priority Task
# ---------------------------------------------------------------------

"""
Given:
tasks = ["Check CPU", "Check Disk", "Send Report"]

TODO:
- Insert "Check Memory" at index 1
- Print the updated task list

Concept focus:
insert()
"""

tasks = ["Check CPU", "Check Disk", "Send Report"]

# Write your code below this line




# ---------------------------------------------------------------------
# EXERCISE 4: Insert Priority Alert at the Beginning
# ---------------------------------------------------------------------

"""
Given:
alerts = ["Disk warning", "Backup failed", "Login failed"]

TODO:
- Insert "CPU critical" at the beginning of the list
- Print the updated alert list

Concept focus:
insert at index 0
"""

alerts = ["Disk warning", "Backup failed", "Login failed"]

# Write your code below this line




# ---------------------------------------------------------------------
# EXERCISE 5: Remove a Closed Alert
# ---------------------------------------------------------------------

"""
Given:
alerts = ["CPU high", "Disk warning", "Backup failed"]

TODO:
- Remove "Disk warning" from the list
- Print remaining alerts

Concept focus:
remove()
"""

alerts = ["CPU high", "Disk warning", "Backup failed"]

# Write your code below this line




# ---------------------------------------------------------------------
# EXERCISE 6: Remove a Completed Task
# ---------------------------------------------------------------------

"""
Given:
pending_tasks = ["Check CPU", "Check Memory", "Check Disk"]

TODO:
- Remove "Check CPU"
- Print the pending task list

Concept focus:
cleaning a task list
"""

pending_tasks = ["Check CPU", "Check Memory", "Check Disk"]

# Write your code below this line




# ---------------------------------------------------------------------
# EXERCISE 7: Pop Latest Log File
# ---------------------------------------------------------------------

"""
Given:
log_files = ["alert.log", "listener.log", "backup.log"]

TODO:
- Use pop() to remove the latest file
- Store it in a variable named latest_file
- Print latest_file
- Print the remaining list

Concept focus:
pop() without index
"""

log_files = ["alert.log", "listener.log", "backup.log"]

# Write your code below this line




# ---------------------------------------------------------------------
# EXERCISE 8: Pop First Item from Queue
# ---------------------------------------------------------------------

"""
Given:
queue = ["ticket001", "ticket002", "ticket003"]

TODO:
- Use pop(0) to remove the first ticket
- Store it in a variable named current_ticket
- Print current_ticket
- Print the remaining queue

Concept focus:
pop() with index
"""

queue = ["ticket001", "ticket002", "ticket003"]

# Write your code below this line




# ---------------------------------------------------------------------
# EXERCISE 9: Sort Server Names
# ---------------------------------------------------------------------

"""
Given:
servers = ["web01", "app01", "db01", "batch01"]

TODO:
- Sort the list
- Print the sorted list

Concept focus:
sort()
"""

servers = ["web01", "app01", "db01", "batch01"]

# Write your code below this line




# ---------------------------------------------------------------------
# EXERCISE 10: Sort Disk Usage Values
# ---------------------------------------------------------------------

"""
Given:
disk_usages = [91.5, 62.0, 84.2, 73.8]

TODO:
- Sort the numeric values
- Print the sorted list
- Print the lowest usage using index 0
- Print the highest usage using negative index

Concept focus:
sorting numbers and accessing values
"""

disk_usages = [91.5, 62.0, 84.2, 73.8]

# Write your code below this line




# ---------------------------------------------------------------------
# EXERCISE 11: Reverse Deployment Steps
# ---------------------------------------------------------------------

"""
Given:
deployment_steps = ["Stop service", "Deploy package", "Start service", "Validate"]

TODO:
- Reverse the list
- Print the reversed list

Concept focus:
reverse()
"""

deployment_steps = ["Stop service", "Deploy package", "Start service", "Validate"]

# Write your code below this line




# ---------------------------------------------------------------------
# EXERCISE 12: Loop Through Servers
# ---------------------------------------------------------------------

"""
Given:
servers = ["app01", "db01", "web01"]

TODO:
- Use a for loop to print a health check message for each server

Expected style:
Running health check for app01

Concept focus:
looping through lists
"""

servers = ["app01", "db01", "web01"]

# Write your code below this line




# ---------------------------------------------------------------------
# EXERCISE 13: Loop Through Alert List
# ---------------------------------------------------------------------

"""
Given:
alerts = ["CPU high", "Disk warning", "Backup failed"]

TODO:
- Use a for loop to print each alert in a readable format

Expected style:
Alert found: CPU high

Concept focus:
processing each item in a list
"""

alerts = ["CPU high", "Disk warning", "Backup failed"]

# Write your code below this line




# ---------------------------------------------------------------------
# EXERCISE 14: Mini Project - Daily Operations Tracker
# ---------------------------------------------------------------------

"""
Build a small Daily Operations Tracker.

Collect all required inputs once at the beginning:
1. Team name
2. First server name
3. Second server name
4. Third server name
5. First task
6. Second task
7. Third task
8. New server to add
9. Priority task to insert
10. Completed task to remove

TODO:
- Store the three server names in a list named servers
- Store the three task names in a list named tasks
- Add the new server using append()
- Insert the priority task at index 0 using insert()
- Remove the completed task using remove()
- Pop the latest task and store it in completed_latest_task
- Sort the server list
- Reverse the task list
- Print total servers using len()
- Loop through servers and print a check message
- Print a clean final operations report

Expected output style:
========================================
Daily Operations Tracker
========================================
Team              : Morning Shift
Total Servers     : 4
Completed Latest  : Send Report
Final Servers     : ['app01', 'batch01', 'db01', 'web01']
Pending Tasks     : ['Check Disk', 'Check Memory']
Servers to Check:
- app01
- batch01
- db01
- web01
========================================

Important:
Collect each required input once at the beginning.
Reuse those variables throughout the mini project.
Do not ask for the same input multiple times.
This should feel like one complete automation workflow.
"""

# Write your mini project code below this line




print("\nExercise file loaded successfully. Complete the tasks one by one.")
