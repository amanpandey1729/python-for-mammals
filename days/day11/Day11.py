"""
Python for Mammals - Day 11
Topic: Lists

Audience:
- Complete beginners
- DBAs, Sysadmins, Support Engineers, Cloud Engineers, Monitoring Teams
- Anyone who wants Python for practical automation

Goal of Day 11:
By the end of today, you should be able to:
1. Create lists to store multiple related values
2. Access list values using indexes
3. Understand that indexing starts from 0
4. Access the first, second, last, and specific values from a list
5. Update values inside a list
6. Use lists for practical operational data like servers, alerts, files, checks, and statuses
7. Understand why lists are important for automation scripts

Why this matters:
A real automation script rarely works with only one value.

Examples:
- A list of servers to check
- A list of log files to scan
- A list of failed backup jobs
- A list of disk usage values
- A list of alerts collected during a shift

Lists help us keep multiple related values together.
This makes automation cleaner and easier to expand.
"""

print("=" * 70)
print("DAY 11 - LISTS")
print("CREATING LISTS, INDEXING, ACCESSING VALUES, UPDATING VALUES")
print("=" * 70)

# ---------------------------------------------------------------------
# SECTION 1: Why Lists Matter
# ---------------------------------------------------------------------

print("\nSECTION 1: Why Lists Matter")

"""
Until now, we mostly stored one value in one variable.

Example:
server_name = "app01"

But in real operations work, we usually deal with many values:
- many servers
- many users
- many files
- many alerts
- many backup jobs
- many database names

A list allows us to store multiple values in one variable.
"""

print("A list helps us store multiple related values in one place.")

# ---------------------------------------------------------------------
# SECTION 2: Creating a Simple List
# ---------------------------------------------------------------------

print("\nSECTION 2: Creating a Simple List")

servers = ["app01", "db01", "web01"]

print("Servers:", servers)

"""
A list is created using square brackets: []
Each value is separated by a comma.

This list contains three server names.
"""

# ---------------------------------------------------------------------
# SECTION 3: Lists Can Store Different Operational Values
# ---------------------------------------------------------------------

print("\nSECTION 3: Lists Can Store Different Operational Values")

environments = ["DEV", "TEST", "PROD"]
backup_statuses = ["SUCCESS", "FAILED", "RUNNING"]
disk_usages = [65.5, 82.0, 91.2]

print("Environments    :", environments)
print("Backup statuses :", backup_statuses)
print("Disk usages     :", disk_usages)

"""
Lists can store strings, numbers, or other data types.
For today, keep lists simple: one list should contain related values.
"""

# ---------------------------------------------------------------------
# SECTION 4: Accessing Values Using Index Numbers
# ---------------------------------------------------------------------

print("\nSECTION 4: Accessing Values Using Index Numbers")

servers = ["app01", "db01", "web01"]

print("Full list     :", servers)
print("First server  :", servers[0])
print("Second server :", servers[1])
print("Third server  :", servers[2])

"""
Important:
Python list indexing starts from 0.

servers[0] means the first item.
servers[1] means the second item.
servers[2] means the third item.

This may feel strange at first, but it becomes natural with practice.
"""

# ---------------------------------------------------------------------
# SECTION 5: Accessing the Last Value
# ---------------------------------------------------------------------

print("\nSECTION 5: Accessing the Last Value")

servers = ["app01", "db01", "web01"]

print("Last server using positive index:", servers[2])
print("Last server using negative index:", servers[-1])
print("Second last server:", servers[-2])

"""
Negative indexes count from the end.

-1 means last item.
-2 means second last item.

This is useful when you want the latest alert, latest file name,
or last processed item from a list.
"""

# ---------------------------------------------------------------------
# SECTION 6: Updating Values in a List
# ---------------------------------------------------------------------

print("\nSECTION 6: Updating Values in a List")

statuses = ["OK", "OK", "WARNING"]

print("Before update:", statuses)

statuses[1] = "CRITICAL"

print("After update :", statuses)

"""
Lists are changeable.
The technical word is mutable, but for now remember this:

You can update an item inside a list by using its index.
"""

# ---------------------------------------------------------------------
# SECTION 7: Practical Example - Server Inventory List
# ---------------------------------------------------------------------

print("\nSECTION 7: Practical Example - Server Inventory List")

server_inventory = ["linux01", "linux02", "windows01", "dbprod01"]

print("Inventory:", server_inventory)
print("Primary Linux server:", server_inventory[0])
print("Database server:", server_inventory[3])

"""
A server inventory script can start with a simple list.
Later in the challenge, we will read these values from files,
CSV reports, command outputs, or APIs.
"""

# ---------------------------------------------------------------------
# SECTION 8: Practical Example - Alert Queue
# ---------------------------------------------------------------------

print("\nSECTION 8: Practical Example - Alert Queue")

alerts = ["CPU high", "Disk warning", "Backup failed"]

print("All alerts:", alerts)
print("First alert to review:", alerts[0])
print("Latest alert:", alerts[-1])

"""
Lists are useful when alerts come in sequence.
You can access the first alert, latest alert, or a specific alert.
"""

# ---------------------------------------------------------------------
# SECTION 9: Practical Example - Updating a Backup Status
# ---------------------------------------------------------------------

print("\nSECTION 9: Practical Example - Updating a Backup Status")

backup_jobs = ["SUCCESS", "RUNNING", "SUCCESS"]

print("Before validation:", backup_jobs)

backup_jobs[1] = "FAILED"

print("After validation :", backup_jobs)

"""
Imagine the second backup job was still RUNNING when the first report was created.
After checking the final status, we updated it to FAILED.
"""

# ---------------------------------------------------------------------
# SECTION 10: Lists and len()
# ---------------------------------------------------------------------

print("\nSECTION 10: Lists and len()")

servers = ["app01", "db01", "web01", "batch01"]

print("Servers:", servers)
print("Total servers:", len(servers))

"""
len() tells us how many items are present in a list.
This is useful for reports:
- total servers checked
- total alerts found
- total failed jobs
- total files processed
"""

# ---------------------------------------------------------------------
# SECTION 11: Guided Practice - Create a List
# ---------------------------------------------------------------------

print("\nSECTION 11: Guided Practice - Create a List")

"""
Uncomment this block and run it.

Create your own list of server names.
"""

# my_servers = ["server01", "server02", "server03"]
# print("My servers:", my_servers)

print("Guided practice: uncomment the list creation block.")

# ---------------------------------------------------------------------
# SECTION 12: Guided Practice - Access Values
# ---------------------------------------------------------------------

print("\nSECTION 12: Guided Practice - Access Values")

"""
Uncomment this block and run it.

Practice accessing values using indexes.
"""

# checks = ["CPU", "Memory", "Disk"]
# print("First check:", checks[0])
# print("Second check:", checks[1])
# print("Last check:", checks[-1])

print("Guided practice: uncomment the indexing block.")

# ---------------------------------------------------------------------
# SECTION 13: Guided Practice - Update Values
# ---------------------------------------------------------------------

print("\nSECTION 13: Guided Practice - Update Values")

"""
Uncomment this block and run it.

Practice updating one value inside a list.
"""

# statuses = ["OK", "OK", "OK"]
# statuses[2] = "WARNING"
# print("Updated statuses:", statuses)

print("Guided practice: uncomment the update block.")

# ---------------------------------------------------------------------
# SECTION 14: Practical Program 1 - Server List Summary
# ---------------------------------------------------------------------

print("\nSECTION 14: Practical Program 1 - Server List Summary")

servers = ["app01", "app02", "db01"]

print("Server List Summary")
print("-" * 35)
print("First server :", servers[0])
print("Second server:", servers[1])
print("Third server :", servers[2])
print("Total servers:", len(servers))

# ---------------------------------------------------------------------
# SECTION 15: Practical Program 2 - Update Maintenance Status
# ---------------------------------------------------------------------

print("\nSECTION 15: Practical Program 2 - Update Maintenance Status")

maintenance_status = ["PENDING", "PENDING", "PENDING"]

print("Before maintenance:", maintenance_status)

maintenance_status[0] = "DONE"
maintenance_status[1] = "DONE"

print("After maintenance :", maintenance_status)

# ---------------------------------------------------------------------
# SECTION 16: Practical Program 3 - Access Related Lists
# ---------------------------------------------------------------------

print("\nSECTION 16: Practical Program 3 - Access Related Lists")

servers = ["app01", "db01", "web01"]
statuses = ["OK", "WARNING", "OK"]

print("Server Health Snapshot")
print("-" * 35)
print(servers[0], "status is", statuses[0])
print(servers[1], "status is", statuses[1])
print(servers[2], "status is", statuses[2])

"""
For today, we are manually accessing list items.
In the next steps of the challenge, loops will make this cleaner.
"""

# ---------------------------------------------------------------------
# SECTION 17: Mini Project - Shift Handover List Summary
# ---------------------------------------------------------------------

print("\nSECTION 17: Mini Project - Shift Handover List Summary")

"""
This mini project uses fixed values so the file can run without stopping
for user input.

In Day11_Exercise.py, you will build your own version using lists.
"""

servers = ["app01", "db01", "web01"]
checks = ["CPU", "Memory", "Disk"]
statuses = ["OK", "WARNING", "OK"]

print("Shift Handover List Summary")
print("-" * 45)
print("Servers checked:", len(servers))
print("First server   :", servers[0])
print("Latest server  :", servers[-1])
print("Primary check  :", checks[0])
print("Latest check   :", checks[-1])
print("Before update  :", statuses)

statuses[1] = "CRITICAL"

print("After update   :", statuses)
print("Important item :", servers[1], "needs", checks[1], "review. Status:", statuses[1])
print("-" * 45)

# ---------------------------------------------------------------------
# SECTION 18: Mini Challenge
# ---------------------------------------------------------------------

print("\nSECTION 18: Mini Challenge")

"""
Create a Shift Handover List Summary.

It should:
1. Create a list of three server names
2. Create a list of three check names
3. Create a list of three status values
4. Print the full lists
5. Print the first and last server
6. Print the first and last check
7. Update one status value
8. Print a clean handover summary

Use:
- lists
- indexes
- negative indexes
- value updates
- len()
- print()
"""

print("Mini challenge: Build a Shift Handover List Summary using lists.")

# ---------------------------------------------------------------------
# CLOSING MESSAGE
# ---------------------------------------------------------------------

print("\nDay 11 complete. You can now store and update multiple related values using lists.")
print("Lists are one of the most important foundations for practical automation.")
