"""
Python for Mammals - Day 11 Exercise File
Topic: Lists

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
By the end of these exercises, you should be able to create lists,
access values using indexes, update values, and use lists for small
operational automation-style summaries.
"""

print("=" * 70)
print("DAY 11 EXERCISES - LISTS")
print("CREATING LISTS, INDEXING, ACCESSING VALUES, UPDATING VALUES")
print("=" * 70)

# ---------------------------------------------------------------------
# EXERCISE 1: Create a Server List
# ---------------------------------------------------------------------

"""
TODO:
- Create a list named servers with three server names
- Print the full list

Example values you may use:
app01, db01, web01

Concept focus:
creating a list
"""

# Write your code below this line




# ---------------------------------------------------------------------
# EXERCISE 2: Create a List of Environments
# ---------------------------------------------------------------------

"""
TODO:
- Create a list named environments with DEV, TEST, and PROD
- Print the full list

Concept focus:
storing related text values in one list
"""

# Write your code below this line




# ---------------------------------------------------------------------
# EXERCISE 3: Create a List of Usage Percentages
# ---------------------------------------------------------------------

"""
TODO:
- Create a list named disk_usages with three numeric values
- Print the full list

Example values:
65.5, 82.0, 91.2

Concept focus:
storing related numeric values in one list
"""

# Write your code below this line




# ---------------------------------------------------------------------
# EXERCISE 4: Access the First Server
# ---------------------------------------------------------------------

"""
Given:
servers = ["app01", "db01", "web01"]

TODO:
- Print the first server using index 0

Concept focus:
list indexing starts from 0
"""

servers = ["app01", "db01", "web01"]

# Write your code below this line




# ---------------------------------------------------------------------
# EXERCISE 5: Access the Second and Third Server
# ---------------------------------------------------------------------

"""
Given:
servers = ["app01", "db01", "web01"]

TODO:
- Print the second server
- Print the third server

Concept focus:
accessing specific list values by index
"""

servers = ["app01", "db01", "web01"]

# Write your code below this line




# ---------------------------------------------------------------------
# EXERCISE 6: Access the Last Alert
# ---------------------------------------------------------------------

"""
Given:
alerts = ["CPU high", "Disk warning", "Backup failed"]

TODO:
- Print the last alert using a negative index

Concept focus:
negative indexing
"""

alerts = ["CPU high", "Disk warning", "Backup failed"]

# Write your code below this line




# ---------------------------------------------------------------------
# EXERCISE 7: Count Items in a List
# ---------------------------------------------------------------------

"""
Given:
servers = ["app01", "app02", "db01", "web01"]

TODO:
- Print the total number of servers using len()

Concept focus:
counting list items
"""

servers = ["app01", "app02", "db01", "web01"]

# Write your code below this line




# ---------------------------------------------------------------------
# EXERCISE 8: Update a Server Status
# ---------------------------------------------------------------------

"""
Given:
statuses = ["OK", "OK", "WARNING"]

TODO:
- Print the list before update
- Update the second status to CRITICAL
- Print the list after update

Concept focus:
updating list values by index
"""

statuses = ["OK", "OK", "WARNING"]

# Write your code below this line




# ---------------------------------------------------------------------
# EXERCISE 9: Update a Backup Job Status
# ---------------------------------------------------------------------

"""
Given:
backup_jobs = ["SUCCESS", "RUNNING", "SUCCESS"]

TODO:
- Update the second item from RUNNING to FAILED
- Print the updated list

Concept focus:
changing operational status values
"""

backup_jobs = ["SUCCESS", "RUNNING", "SUCCESS"]

# Write your code below this line




# ---------------------------------------------------------------------
# EXERCISE 10: Access Related Lists
# ---------------------------------------------------------------------

"""
Given:
servers = ["app01", "db01", "web01"]
statuses = ["OK", "WARNING", "OK"]

TODO:
- Print the first server with its first status
- Print the second server with its second status
- Print the third server with its third status

Expected style:
app01 status is OK

Concept focus:
using matching indexes across related lists
"""

servers = ["app01", "db01", "web01"]
statuses = ["OK", "WARNING", "OK"]

# Write your code below this line




# ---------------------------------------------------------------------
# EXERCISE 11: Create a File Processing List
# ---------------------------------------------------------------------

"""
TODO:
- Create a list named log_files with three file names
- Print the first file to process
- Print the latest file to process using a negative index
- Print the total number of files

Example file names:
alert.log, listener.log, backup.log

Concept focus:
lists for file automation thinking
"""

# Write your code below this line




# ---------------------------------------------------------------------
# EXERCISE 12: Maintenance Checklist Status
# ---------------------------------------------------------------------

"""
Given:
checks = ["CPU", "Memory", "Disk"]
statuses = ["PENDING", "PENDING", "PENDING"]

TODO:
- Mark CPU check as DONE
- Mark Memory check as DONE
- Keep Disk check as PENDING
- Print a clean checklist summary using indexes

Expected style:
CPU    : DONE
Memory : DONE
Disk   : PENDING

Concept focus:
updating and accessing list values
"""

checks = ["CPU", "Memory", "Disk"]
statuses = ["PENDING", "PENDING", "PENDING"]

# Write your code below this line




# ---------------------------------------------------------------------
# EXERCISE 13: Mini Project - Shift Handover List Summary
# ---------------------------------------------------------------------

"""
Build a small Shift Handover List Summary.

Collect all required user inputs once at the beginning:
1. First server name
2. Second server name
3. Third server name
4. First check name
5. Second check name
6. Third check name
7. First status
8. Second status
9. Third status

TODO:
- Store the three server names in a list named servers
- Store the three check names in a list named checks
- Store the three statuses in a list named statuses
- Print the full server list
- Print the full check list
- Print the full status list
- Print total servers using len()
- Print first server using index 0
- Print latest server using negative index
- Update the second status to REVIEW_REQUIRED
- Print the updated statuses list
- Print a clean final handover report

Expected output style:
========================================
Shift Handover List Summary
========================================
Servers Checked : 3
First Server    : app01
Latest Server   : web01
Primary Check   : CPU
Latest Check    : Disk
Updated Statuses: ['OK', 'REVIEW_REQUIRED', 'OK']
Important Item  : db01 needs Memory review. Status: REVIEW_REQUIRED
========================================

Important:
Collect each required input once at the beginning.
Reuse those list values throughout the mini project.
Do not ask for the same input multiple times.
This should feel like one complete automation workflow.
"""

# Write your mini project code below this line




print("\nExercise file loaded successfully. Complete the tasks one by one.")
