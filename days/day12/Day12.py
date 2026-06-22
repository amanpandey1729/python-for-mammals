"""
Python for Mammals - Day 12
Topic: List Operations

Audience:
- Complete beginners
- DBAs, Sysadmins, Support Engineers, Cloud Engineers, Monitoring Teams
- Anyone who wants Python for practical automation

Goal of Day 12:
By the end of today, you should be able to:
1. Add values to a list using append()
2. Insert values at a specific position using insert()
3. Remove known values using remove()
4. Remove and capture values using pop()
5. Sort list values using sort()
6. Reverse list order using reverse()
7. Loop through lists to process many items
8. Use list operations for practical operational workflows

Why this matters:
Day 11 taught us how to store multiple related values.
Day 12 teaches us how to manage those values.

Real automation scripts often need to:
- add newly discovered servers
- insert priority tasks
- remove completed alerts
- pop the latest file from a queue
- sort report values
- reverse processing order
- loop through every item in an inventory

This is where lists start becoming genuinely useful for automation.
"""

print("=" * 70)
print("DAY 12 - LIST OPERATIONS")
print("APPEND, INSERT, REMOVE, POP, SORT, REVERSE, LOOPING")
print("=" * 70)

# ---------------------------------------------------------------------
# SECTION 1: Why List Operations Matter
# ---------------------------------------------------------------------

print("\nSECTION 1: Why List Operations Matter")

"""
Creating a list is useful.
But real automation needs more than storing values.

In operations work, values keep changing:
- a new server is added
- an alert is closed
- a failed job is removed from a pending queue
- a list of files needs sorting
- every server needs to be checked one by one

List operations help us manage these changing values.
"""

print("List operations help us add, remove, reorder, and process values.")

# ---------------------------------------------------------------------
# SECTION 2: append() - Add an Item at the End
# ---------------------------------------------------------------------

print("\nSECTION 2: append() - Add an Item at the End")

servers = ["app01", "db01", "web01"]

print("Before append:", servers)

servers.append("batch01")

print("After append :", servers)

"""
append() adds one item at the end of a list.

This is useful when your script discovers a new server, file,
alert, user, backup job, or task and you want to add it to the list.
"""

# ---------------------------------------------------------------------
# SECTION 3: insert() - Add an Item at a Specific Position
# ---------------------------------------------------------------------

print("\nSECTION 3: insert() - Add an Item at a Specific Position")

tasks = ["Check CPU", "Check Disk", "Send Report"]

print("Before insert:", tasks)

tasks.insert(1, "Check Memory")

print("After insert :", tasks)

"""
insert(index, value) places a value at a specific position.

Here, "Check Memory" is inserted at index 1.
The old item at index 1 moves to the right.
"""

# ---------------------------------------------------------------------
# SECTION 4: remove() - Remove a Known Value
# ---------------------------------------------------------------------

print("\nSECTION 4: remove() - Remove a Known Value")

alerts = ["CPU high", "Disk warning", "Backup failed", "Login failed"]

print("Before remove:", alerts)

alerts.remove("Disk warning")

print("After remove :", alerts)

"""
remove(value) removes the first matching value from a list.

This is useful when an alert is closed or a completed task should
no longer appear in the pending list.
"""

# ---------------------------------------------------------------------
# SECTION 5: pop() - Remove and Capture an Item
# ---------------------------------------------------------------------

print("\nSECTION 5: pop() - Remove and Capture an Item")

log_files = ["alert.log", "listener.log", "backup.log"]

print("Before pop:", log_files)

latest_file = log_files.pop()

print("Popped file:", latest_file)
print("After pop  :", log_files)

"""
pop() removes an item and returns it.
Without an index, pop() removes the last item.

This is useful when you want to pick the latest file, latest alert,
or next item from a processing queue.
"""

# ---------------------------------------------------------------------
# SECTION 6: pop() with an Index
# ---------------------------------------------------------------------

print("\nSECTION 6: pop() with an Index")

files_to_process = ["01_alert.log", "02_listener.log", "03_backup.log"]

print("Before pop:", files_to_process)

first_file = files_to_process.pop(0)

print("First file processed:", first_file)
print("Remaining files      :", files_to_process)

"""
pop(0) removes the first item.
This can be used when you want to process items in first-in, first-out order.
"""

# ---------------------------------------------------------------------
# SECTION 7: sort() - Sort Values
# ---------------------------------------------------------------------

print("\nSECTION 7: sort() - Sort Values")

servers = ["web01", "app01", "db01", "batch01"]

print("Before sort:", servers)

servers.sort()

print("After sort :", servers)

"""
sort() changes the list and arranges values in ascending order.

This is useful for clean reports because sorted output is easier to read.
"""

# ---------------------------------------------------------------------
# SECTION 8: Sorting Numbers
# ---------------------------------------------------------------------

print("\nSECTION 8: Sorting Numbers")

disk_usages = [91.5, 62.0, 84.2, 73.8]

print("Before sort:", disk_usages)

disk_usages.sort()

print("After sort :", disk_usages)

"""
Numbers are sorted from smallest to largest.
Later, this will help when creating capacity reports and finding high usage values.
"""

# ---------------------------------------------------------------------
# SECTION 9: reverse() - Reverse the Order
# ---------------------------------------------------------------------

print("\nSECTION 9: reverse() - Reverse the Order")

deployment_steps = ["Stop service", "Deploy package", "Start service", "Validate"]

print("Original order:", deployment_steps)

deployment_steps.reverse()

print("Reverse order :", deployment_steps)

"""
reverse() changes the order of the list.

This can be useful when rollback steps need to be performed in the opposite order.
"""

# ---------------------------------------------------------------------
# SECTION 10: Looping Through Lists
# ---------------------------------------------------------------------

print("\nSECTION 10: Looping Through Lists")

servers = ["app01", "db01", "web01"]

for server in servers:
    print("Checking server:", server)

"""
This is one of the most important automation patterns:

for item in list:
    do something with item

Instead of writing the same code again and again, we loop through the list.
"""

# ---------------------------------------------------------------------
# SECTION 11: Practical Example - Server Inventory Update
# ---------------------------------------------------------------------

print("\nSECTION 11: Practical Example - Server Inventory Update")

inventory = ["app01", "db01"]

print("Initial inventory:", inventory)

inventory.append("web01")
inventory.append("batch01")
inventory.sort()

print("Updated inventory:", inventory)
print("Total servers    :", len(inventory))

# ---------------------------------------------------------------------
# SECTION 12: Practical Example - Alert Queue Cleanup
# ---------------------------------------------------------------------

print("\nSECTION 12: Practical Example - Alert Queue Cleanup")

alerts = ["CPU high", "Disk warning", "Backup failed", "Service down"]

print("Before cleanup:", alerts)

alerts.remove("Disk warning")
latest_alert = alerts.pop()

print("Latest alert picked:", latest_alert)
print("Pending alerts     :", alerts)

# ---------------------------------------------------------------------
# SECTION 13: Practical Example - Loop Through Backup Jobs
# ---------------------------------------------------------------------

print("\nSECTION 13: Practical Example - Loop Through Backup Jobs")

backup_jobs = ["DB_FULL_BACKUP", "ARCHIVE_BACKUP", "CONFIG_BACKUP"]

for job in backup_jobs:
    print("Validating backup job:", job)

print("Backup job validation loop completed.")

# ---------------------------------------------------------------------
# SECTION 14: Guided Practice - append()
# ---------------------------------------------------------------------

print("\nSECTION 14: Guided Practice - append()")

"""
Uncomment this block and run it.
Add your own task to the list.
"""

# tasks = ["Check CPU", "Check Memory"]
# tasks.append("Check Disk")
# print("Tasks:", tasks)

print("Guided practice: uncomment the append() block.")

# ---------------------------------------------------------------------
# SECTION 15: Guided Practice - remove()
# ---------------------------------------------------------------------

print("\nSECTION 15: Guided Practice - remove()")

"""
Uncomment this block and run it.
Remove a completed task from the list.
"""

# pending_tasks = ["Check backup", "Send report", "Close ticket"]
# pending_tasks.remove("Send report")
# print("Pending tasks:", pending_tasks)

print("Guided practice: uncomment the remove() block.")

# ---------------------------------------------------------------------
# SECTION 16: Guided Practice - Loop Through a List
# ---------------------------------------------------------------------

print("\nSECTION 16: Guided Practice - Loop Through a List")

"""
Uncomment this block and run it.
Loop through each server and print a check message.
"""

# servers = ["app01", "db01", "web01"]
# for server in servers:
#     print("Running health check for:", server)

print("Guided practice: uncomment the loop block.")

# ---------------------------------------------------------------------
# SECTION 17: Practical Program 1 - Clean Server Report
# ---------------------------------------------------------------------

print("\nSECTION 17: Practical Program 1 - Clean Server Report")

servers = ["web01", "app01", "db01"]
servers.append("batch01")
servers.sort()

print("Server Report")
print("-" * 35)
print("Total servers:", len(servers))

for server in servers:
    print("Server:", server)

# ---------------------------------------------------------------------
# SECTION 18: Practical Program 2 - Operations Task Tracker
# ---------------------------------------------------------------------

print("\nSECTION 18: Practical Program 2 - Operations Task Tracker")

tasks = ["Check CPU", "Check Disk", "Send Report"]

print("Initial tasks:", tasks)

tasks.insert(1, "Check Memory")
tasks.remove("Check CPU")
completed_task = tasks.pop()

print("Completed task:", completed_task)
print("Remaining tasks:", tasks)

# ---------------------------------------------------------------------
# SECTION 19: Mini Project - Daily Operations Tracker
# ---------------------------------------------------------------------

print("\nSECTION 19: Mini Project - Daily Operations Tracker")

"""
This mini project uses fixed values so the file can run without stopping
for user input.

In Day12_Exercise.py, you will build your own version using input().
"""

team_name = "Morning Shift"
servers = ["app01", "db01", "web01"]
tasks = ["Check CPU", "Check Disk", "Validate Backup"]

print("Daily Operations Tracker")
print("-" * 45)
print("Team:", team_name)
print("Initial servers:", servers)
print("Initial tasks  :", tasks)

servers.append("batch01")
tasks.insert(1, "Check Memory")
tasks.remove("Check CPU")
completed_task = tasks.pop()
servers.sort()
tasks.reverse()

print("Completed task :", completed_task)
print("Final servers  :", servers)
print("Pending tasks  :", tasks)
print("Server count   :", len(servers))

for server in servers:
    print("Ready for check:", server)

print("-" * 45)

# ---------------------------------------------------------------------
# SECTION 20: Mini Challenge
# ---------------------------------------------------------------------

print("\nSECTION 20: Mini Challenge")

"""
Create a Daily Operations Tracker.

It should:
1. Create a list of servers
2. Create a list of pending tasks
3. Add one new server using append()
4. Insert one priority task using insert()
5. Remove one completed task using remove()
6. Pop one task and store it as completed_task
7. Sort the server list
8. Reverse the task list
9. Loop through servers and print a check message
10. Print a clean final report

Use:
- append()
- insert()
- remove()
- pop()
- sort()
- reverse()
- for loop
- len()
- print()
"""

print("Mini challenge: Build a Daily Operations Tracker using list operations.")

# ---------------------------------------------------------------------
# CLOSING MESSAGE
# ---------------------------------------------------------------------

print("\nDay 12 complete. You can now manage list data using common list operations.")
print("This is a major step toward processing inventories, alerts, files, and tasks automatically.")
