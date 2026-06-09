"""
Python for Mammals - Day 8
Topic: For Loops

Audience:
- Complete beginners
- DBAs, Sysadmins, Support Engineers, Cloud Engineers, Monitoring Teams
- Anyone who wants Python for practical automation

Goal of Day 8:
By the end of today, you should be able to:
1. Understand what iteration means
2. Use for loops to repeat actions
3. Use range() for controlled repetition
4. Understand loop variables
5. Iterate through strings
6. Iterate through lists
7. Automate repeated checks instead of writing the same code again and again

Why this matters:
Automation becomes useful when Python can repeat work for you.

Examples:
- Print a checklist for multiple servers
- Check multiple services one by one
- Read multiple alert messages
- Process multiple filenames
- Validate multiple report names
- Generate repeated daily task summaries

Day 7 helped us make smarter decisions.
Day 8 helps us repeat those decisions across many items.
"""

print("=" * 70)
print("DAY 8 - FOR LOOPS")
print("=" * 70)


# ---------------------------------------------------------------------
# SECTION 1: Why Repetition Matters in Automation
# ---------------------------------------------------------------------

print("\nSECTION 1: Why Repetition Matters in Automation")

"""
Without loops, you repeat code manually.

Example:
print("Check server 1")
print("Check server 2")
print("Check server 3")

This is fine for 3 items.
But what about 30 servers, 300 files, or 3000 log lines?

A loop helps Python repeat a task automatically.
"""

print("Manual approach:")
print("Check server 1")
print("Check server 2")
print("Check server 3")


# ---------------------------------------------------------------------
# SECTION 2: What is Iteration?
# ---------------------------------------------------------------------

print("\nSECTION 2: What is Iteration?")

"""
Iteration means going through items one by one.

In real work, iteration can mean:
- going through servers one by one
- going through filenames one by one
- going through alert messages one by one
- going through report rows one by one

A for loop is one of the most common ways to iterate in Python.
"""

print("Iteration means repeating a task item by item.")


# ---------------------------------------------------------------------
# SECTION 3: First for Loop
# ---------------------------------------------------------------------

print("\nSECTION 3: First for Loop")

"""
Basic structure:

for variable in collection:
    code to repeat

The indented code runs once for each item.
"""

servers = ["server-01", "server-02", "server-03"]

for server in servers:
    print("Checking server:", server)


# ---------------------------------------------------------------------
# SECTION 4: Understanding the Loop Variable
# ---------------------------------------------------------------------

print("\nSECTION 4: Understanding the Loop Variable")

"""
The loop variable temporarily stores the current item.

In this example:
- first run: service = "web"
- second run: service = "database"
- third run: service = "backup"

The name can be anything meaningful.
"""

services = ["web", "database", "backup"]

for service in services:
    print("Service being checked:", service)


# ---------------------------------------------------------------------
# SECTION 5: range() for Repeating a Fixed Number of Times
# ---------------------------------------------------------------------

print("\nSECTION 5: range() for Repeating a Fixed Number of Times")

"""
range() helps you repeat something a fixed number of times.

range(5) produces:
0, 1, 2, 3, 4

Important:
Python starts counting from 0 by default.
"""

for number in range(5):
    print("Run number:", number)


# ---------------------------------------------------------------------
# SECTION 6: range() with Start and Stop
# ---------------------------------------------------------------------

print("\nSECTION 6: range() with Start and Stop")

"""
range(1, 6) produces:
1, 2, 3, 4, 5

The start value is included.
The stop value is not included.
"""

for check_number in range(1, 6):
    print("Health check number:", check_number)


# ---------------------------------------------------------------------
# SECTION 7: range() with Step
# ---------------------------------------------------------------------

print("\nSECTION 7: range() with Step")

"""
range(start, stop, step)

Example:
range(10, 51, 10) gives:
10, 20, 30, 40, 50
"""

for percent in range(10, 51, 10):
    print("Progress:", percent, "%")


# ---------------------------------------------------------------------
# SECTION 8: Iterating Through a String
# ---------------------------------------------------------------------

print("\nSECTION 8: Iterating Through a String")

"""
A string is also a sequence.

That means Python can go through it character by character.

This is useful when later we parse codes, filenames, IDs, and log text.
"""

ticket_id = "INC123"

for character in ticket_id:
    print("Character:", character)


# ---------------------------------------------------------------------
# SECTION 9: Iterating Through a List
# ---------------------------------------------------------------------

print("\nSECTION 9: Iterating Through a List")

"""
A list stores multiple values.

A for loop can process each value in the list.
"""

alert_messages = [
    "CPU high",
    "Memory high",
    "Disk warning"
]

for alert in alert_messages:
    print("Alert found:", alert)


# ---------------------------------------------------------------------
# SECTION 10: Practical Loop - Server Inventory
# ---------------------------------------------------------------------

print("\nSECTION 10: Practical Loop - Server Inventory")

server_list = ["app01", "db01", "backup01", "monitor01"]

print("Server Inventory")
print("-" * 40)

for server in server_list:
    print("Server:", server)


# ---------------------------------------------------------------------
# SECTION 11: Practical Loop - Service Check
# ---------------------------------------------------------------------

print("\nSECTION 11: Practical Loop - Service Check")

services = ["ssh", "httpd", "database", "backup-agent"]

for service in services:
    print("Checking service:", service)
    print("Result          : Pending manual validation")


# ---------------------------------------------------------------------
# SECTION 12: Loop with Conditions
# ---------------------------------------------------------------------

print("\nSECTION 12: Loop with Conditions")

"""
Loops become powerful when combined with conditions.

Example:
Go through multiple disk usages and print status for each one.
"""

disk_usages = [65, 82, 91, 76]

for usage in disk_usages:
    print("Disk usage:", usage, "%")

    if usage >= 90:
        print("Status    : CRITICAL")
    elif usage >= 80:
        print("Status    : WARNING")
    else:
        print("Status    : OK")


# ---------------------------------------------------------------------
# SECTION 13: Counting Items with a Loop
# ---------------------------------------------------------------------

print("\nSECTION 13: Counting Items with a Loop")

"""
You can use a counter variable with a loop.

This is useful for counting:
- failed checks
- successful backups
- critical alerts
- invalid rows
"""

backup_statuses = ["SUCCESS", "FAILED", "SUCCESS", "FAILED", "SUCCESS"]

successful_backups = 0
failed_backups = 0

for status in backup_statuses:
    if status == "SUCCESS":
        successful_backups += 1
    else:
        failed_backups += 1

print("Successful backups:", successful_backups)
print("Failed backups    :", failed_backups)


# ---------------------------------------------------------------------
# SECTION 14: Cleaning Multiple Text Values
# ---------------------------------------------------------------------

print("\nSECTION 14: Cleaning Multiple Text Values")

"""
Loops are useful for cleaning repeated text values.

Later this will help with:
- CSV cleanup
- report cleanup
- file name cleanup
- alert normalization
"""

raw_server_names = [" app01 ", " DB01", "backup01  "]

for raw_name in raw_server_names:
    clean_name = raw_name.strip().lower()
    print("Raw name  :", repr(raw_name))
    print("Clean name:", clean_name)


# ---------------------------------------------------------------------
# SECTION 15: Practical Program 1 - Daily Checklist Generator
# ---------------------------------------------------------------------

print("\nSECTION 15: Practical Program 1 - Daily Checklist Generator")

checks = [
    "CPU check",
    "Memory check",
    "Disk check",
    "Backup check",
    "Log check"
]

print("Daily Operations Checklist")
print("-" * 40)

for check in checks:
    print("TODO:", check)


# ---------------------------------------------------------------------
# SECTION 16: Practical Program 2 - Alert Classifier
# ---------------------------------------------------------------------

print("\nSECTION 16: Practical Program 2 - Alert Classifier")

alerts = [
    "CPU usage 91",
    "Disk usage 76",
    "Memory usage 88",
    "Backup failed"
]

for alert in alerts:
    clean_alert = alert.lower()

    print("Alert:", alert)

    if "failed" in clean_alert:
        print("Status: Needs immediate review")
    elif "91" in clean_alert:
        print("Status: High usage alert")
    else:
        print("Status: Review during normal check")


# ---------------------------------------------------------------------
# SECTION 17: Practical Program 3 - Simple Report Builder
# ---------------------------------------------------------------------

print("\nSECTION 17: Practical Program 3 - Simple Report Builder")

servers = ["app01", "db01", "web01"]
environment = "PROD"

print("Simple Server Report")
print("-" * 40)

for server in servers:
    print("Server      :", server)
    print("Environment :", environment)
    print("Status      : Pending detailed check")


# ---------------------------------------------------------------------
# SECTION 18: Mini Project - Multi Server Disk Review
# ---------------------------------------------------------------------

print("\nSECTION 18: Mini Project - Multi Server Disk Review")

"""
This mini project reviews disk usage for multiple servers.

Input values used today:
- Server names
- Disk usage values

Output:
- Status for each server
- Count of OK, WARNING, and CRITICAL servers

Today we use fixed lists.
You can later collect this data from files, commands, CSV, APIs, or databases.
"""

servers = ["app01", "db01", "backup01", "monitor01"]
disk_usages = [72, 86, 94, 61]

ok_count = 0
warning_count = 0
critical_count = 0

print("Multi Server Disk Review")
print("-" * 40)

for index in range(4):
    server = servers[index]
    usage = disk_usages[index]

    print("Server:", server)
    print("Usage :", usage, "%")

    if usage >= 90:
        print("Status: CRITICAL")
        critical_count += 1
    elif usage >= 80:
        print("Status: WARNING")
        warning_count += 1
    else:
        print("Status: OK")
        ok_count += 1

print("-" * 40)
print("OK count      :", ok_count)
print("WARNING count :", warning_count)
print("CRITICAL count:", critical_count)


# ---------------------------------------------------------------------
# SECTION 19: Guided Practice - Input-based Repetition
# ---------------------------------------------------------------------

print("\nSECTION 19: Guided Practice - Input-based Repetition")

"""
Uncomment this block and run it.

This program asks how many checks you want to generate,
then prints a numbered checklist.

Try:
3
5
8
"""

# total_checks = int(input("How many checks do you want to generate? "))
#
# print("\nGenerated Checklist")
# print("-" * 40)
#
# for check_number in range(1, total_checks + 1):
#     print("Check", check_number, ": Pending")


# ---------------------------------------------------------------------
# SECTION 20: Mini Challenge
# ---------------------------------------------------------------------

print("\nSECTION 20: Mini Challenge")

"""
Create a Multi-Item Health Summary.

It should:
1. Create a list of at least 5 resource names
2. Create a list of matching usage percentages
3. Loop through each resource
4. Print resource name, usage, and status
5. Count how many resources are OK, WARNING, and CRITICAL
6. Print a final summary

Use:
- lists
- for loop
- range()
- loop variables
- if / elif / else
- counters
- print()
"""

print("Mini challenge: Build a Multi-Item Health Summary using for loops.")


# ---------------------------------------------------------------------
# SECTION 21: Homework
# ---------------------------------------------------------------------

print("\nSECTION 21: Homework")

"""
Homework:
1. Complete Day08_Exercise.py
2. Practice range() with different start, stop, and step values
3. Create a list of 5 tasks from your daily work and print them using a loop
4. Create a list of 5 alert messages and classify them using a loop
5. Share one repetitive task from your work that can be automated using for loops

Community discussion question:
What is one daily task where you repeat the same action for many servers,
files, reports, alerts, or rows?
"""

print("Homework: Complete Day08_Exercise.py and share one repetition use case.")


print("\nDay 8 completed. You can now automate repetition using for loops.")
