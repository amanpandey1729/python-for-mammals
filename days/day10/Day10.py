"""
Python for Mammals - Day 10
Topic: Mini Project #1 - Server Health Message Generator

Audience:
- Complete beginners
- DBAs, Sysadmins, Support Engineers, Cloud Engineers, Monitoring Teams
- Anyone who wants Python for practical automation

Goal of Day 10:
By the end of today, you should be able to:
1. Combine variables, input, conditions, strings, and loops
2. Collect required values for a small operational workflow
3. Clean and validate user input
4. Calculate simple health indicators
5. Decide health status using if / elif / else
6. Generate a readable server health message
7. Understand how small scripts become real automation tools

Why this matters:
Real automation is rarely one isolated concept.
A useful script usually combines many small skills.

Examples:
- Ask for a server name
- Ask for CPU, memory, and disk usage
- Validate environment name
- Decide if the server is OK, WARNING, or CRITICAL
- Print a clean message that can be shared in a ticket, email, or chat

Day 10 is your first mini project.
Today we connect the basics into one complete workflow.
"""

print("=" * 70)
print("DAY 10 - MINI PROJECT #1")
print("SERVER HEALTH MESSAGE GENERATOR")
print("=" * 70)

# ---------------------------------------------------------------------
# SECTION 1: Why Mini Projects Matter
# ---------------------------------------------------------------------

print("\nSECTION 1: Why Mini Projects Matter")

"""
So far, we practiced individual concepts:
- variables
- input
- strings
- conditions
- for loops
- while loops

A mini project helps us combine these concepts.
This is closer to how real automation scripts are written.
"""

print("A useful automation script combines multiple small Python concepts.")

# ---------------------------------------------------------------------
# SECTION 2: Project Goal
# ---------------------------------------------------------------------

print("\nSECTION 2: Project Goal")

"""
Project:
Server Health Message Generator

The script will:
1. Store server details
2. Store CPU, memory, and disk usage
3. Decide the server health status
4. Generate a readable message
5. Print a small final report
"""

print("Goal: Generate a clean server health message from basic input values.")

# ---------------------------------------------------------------------
# SECTION 3: Fixed Values First
# ---------------------------------------------------------------------

print("\nSECTION 3: Fixed Values First")

server_name = "app01"
environment = "PROD"
cpu_usage = 72.5
memory_usage = 68.0
disk_usage = 81.0

print("Server     :", server_name)
print("Environment:", environment)
print("CPU Usage  :", cpu_usage)
print("Memory     :", memory_usage)
print("Disk Usage :", disk_usage)

"""
Before using input(), it is good to test the logic with fixed values.
This keeps the first version simple and easier to debug.
"""

# ---------------------------------------------------------------------
# SECTION 4: Decide Status from One Metric
# ---------------------------------------------------------------------

print("\nSECTION 4: Decide Status from One Metric")

disk_usage = 86.0

if disk_usage >= 90:
    disk_status = "CRITICAL"
elif disk_usage >= 80:
    disk_status = "WARNING"
else:
    disk_status = "OK"

print("Disk usage:", disk_usage)
print("Disk status:", disk_status)

# ---------------------------------------------------------------------
# SECTION 5: Decide Overall Health
# ---------------------------------------------------------------------

print("\nSECTION 5: Decide Overall Health")

cpu_usage = 65.0
memory_usage = 91.0
disk_usage = 75.0

if cpu_usage >= 90 or memory_usage >= 90 or disk_usage >= 90:
    overall_status = "CRITICAL"
elif cpu_usage >= 80 or memory_usage >= 80 or disk_usage >= 80:
    overall_status = "WARNING"
else:
    overall_status = "OK"

print("CPU Usage    :", cpu_usage)
print("Memory Usage :", memory_usage)
print("Disk Usage   :", disk_usage)
print("Overall      :", overall_status)

# ---------------------------------------------------------------------
# SECTION 6: Create a Human-Friendly Message
# ---------------------------------------------------------------------

print("\nSECTION 6: Create a Human-Friendly Message")

server_name = "dbserver01"
environment = "PROD"
overall_status = "WARNING"

message = "Server " + server_name + " in " + environment + " is currently " + overall_status

print(message)

"""
This kind of message can later be used in:
- ticket comments
- daily health reports
- email body
- Slack or Teams notifications
- monitoring summaries
"""

# ---------------------------------------------------------------------
# SECTION 7: Cleaner Formatting with f-strings
# ---------------------------------------------------------------------

print("\nSECTION 7: Cleaner Formatting with f-strings")

server_name = "web02"
environment = "TEST"
cpu_usage = 78.25
memory_usage = 65.50
disk_usage = 49.75

summary = f"{server_name} | {environment} | CPU: {cpu_usage}% | Memory: {memory_usage}% | Disk: {disk_usage}%"

print(summary)

# ---------------------------------------------------------------------
# SECTION 8: Repeat a Message for Multiple Checks
# ---------------------------------------------------------------------

print("\nSECTION 8: Repeat a Message for Multiple Checks")

checks = 3
counter = 1

while counter <= checks:
    print("Collecting health metric number:", counter)
    counter += 1

print("Metric collection completed.")

# ---------------------------------------------------------------------
# SECTION 9: Use a Loop to Print Report Lines
# ---------------------------------------------------------------------

print("\nSECTION 9: Use a Loop to Print Report Lines")

report_lines = [
    "Server      : app01",
    "Environment : PROD",
    "CPU Usage   : 72.5%",
    "Memory      : 68.0%",
    "Disk Usage  : 81.0%",
    "Status      : WARNING"
]

for line in report_lines:
    print(line)

"""
A list is shown here only as a preview.
We will properly learn lists from Day 11.
For now, notice that a loop can print repeated report lines cleanly.
"""

# ---------------------------------------------------------------------
# SECTION 10: Input Collection Concept
# ---------------------------------------------------------------------

print("\nSECTION 10: Input Collection Concept")

"""
Real scripts usually collect input from:
- user input
- command output
- files
- monitoring tools
- database queries
- APIs

For today, we use input() because it is beginner-friendly.
"""

print("In real automation, values may come from commands, files, APIs, or database queries.")

# ---------------------------------------------------------------------
# SECTION 11: Guided Practice - Collect Server Name
# ---------------------------------------------------------------------

print("\nSECTION 11: Guided Practice - Collect Server Name")

"""
Uncomment this block and run it.

This asks for a server name and cleans extra spaces.
"""

# server_name = input("Enter server name: ").strip().lower()
# print("Accepted server:", server_name)

print("Guided practice: uncomment the server name input block.")

# ---------------------------------------------------------------------
# SECTION 12: Guided Practice - Validate Environment
# ---------------------------------------------------------------------

print("\nSECTION 12: Guided Practice - Validate Environment")

"""
Uncomment this block and run it.

This keeps asking until the user enters DEV, TEST, or PROD.
"""

# environment = input("Enter environment DEV, TEST, or PROD: ").strip().upper()
#
# while environment not in ["DEV", "TEST", "PROD"]:
#     print("Invalid environment. Please enter DEV, TEST, or PROD.")
#     environment = input("Enter environment DEV, TEST, or PROD: ").strip().upper()
#
# print("Accepted environment:", environment)

print("Guided practice: uncomment the environment validation block.")

# ---------------------------------------------------------------------
# SECTION 13: Guided Practice - Decide Status from Input
# ---------------------------------------------------------------------

print("\nSECTION 13: Guided Practice - Decide Status from Input")

"""
Uncomment this block and run it.

Assume numeric input for now.
Exception handling will come later in the challenge.
"""

# cpu_usage = float(input("Enter CPU usage percentage: "))
#
# if cpu_usage >= 90:
#     cpu_status = "CRITICAL"
# elif cpu_usage >= 80:
#     cpu_status = "WARNING"
# else:
#     cpu_status = "OK"
#
# print("CPU status:", cpu_status)

print("Guided practice: uncomment the CPU status block.")

# ---------------------------------------------------------------------
# SECTION 14: Practical Program 1 - Simple Health Message
# ---------------------------------------------------------------------

print("\nSECTION 14: Practical Program 1 - Simple Health Message")

server_name = "linuxapp01"
environment = "DEV"
cpu_usage = 55.0
memory_usage = 62.0
disk_usage = 58.0

if cpu_usage >= 90 or memory_usage >= 90 or disk_usage >= 90:
    status = "CRITICAL"
elif cpu_usage >= 80 or memory_usage >= 80 or disk_usage >= 80:
    status = "WARNING"
else:
    status = "OK"

print(f"Health message: {server_name} in {environment} is {status}.")

# ---------------------------------------------------------------------
# SECTION 15: Practical Program 2 - Action Message
# ---------------------------------------------------------------------

print("\nSECTION 15: Practical Program 2 - Action Message")

status = "WARNING"

if status == "CRITICAL":
    action = "Immediate action required"
elif status == "WARNING":
    action = "Review during current shift"
else:
    action = "No action required"

print("Status:", status)
print("Action:", action)

# ---------------------------------------------------------------------
# SECTION 16: Practical Program 3 - Clean Final Report
# ---------------------------------------------------------------------

print("\nSECTION 16: Practical Program 3 - Clean Final Report")

server_name = "dbprod01"
environment = "PROD"
cpu_usage = 88.0
memory_usage = 76.0
disk_usage = 91.0

if cpu_usage >= 90 or memory_usage >= 90 or disk_usage >= 90:
    status = "CRITICAL"
elif cpu_usage >= 80 or memory_usage >= 80 or disk_usage >= 80:
    status = "WARNING"
else:
    status = "OK"

if status == "CRITICAL":
    action = "Immediate action required"
elif status == "WARNING":
    action = "Review during current shift"
else:
    action = "No action required"

print("=" * 45)
print("Server Health Message")
print("=" * 45)
print("Server      :", server_name)
print("Environment :", environment)
print("CPU Usage   :", cpu_usage)
print("Memory      :", memory_usage)
print("Disk Usage  :", disk_usage)
print("Status      :", status)
print("Action      :", action)
print("=" * 45)

# ---------------------------------------------------------------------
# SECTION 17: Mini Project - Server Health Message Generator
# ---------------------------------------------------------------------

print("\nSECTION 17: Mini Project - Server Health Message Generator")

"""
This mini project uses fixed values so the file can run without stopping
for user input.

In Day10_Exercise.py, you will build the interactive version using input().
"""

server_name = "appserver01"
environment = "PROD"
cpu_usage = 82.0
memory_usage = 74.0
disk_usage = 69.0
check_count = 3

if cpu_usage >= 90 or memory_usage >= 90 or disk_usage >= 90:
    status = "CRITICAL"
elif cpu_usage >= 80 or memory_usage >= 80 or disk_usage >= 80:
    status = "WARNING"
else:
    status = "OK"

if status == "CRITICAL":
    action = "Immediate action required"
elif status == "WARNING":
    action = "Review during current shift"
else:
    action = "No action required"

print("Server Health Message Generator")
print("-" * 45)
print("Server      :", server_name)
print("Environment :", environment)

counter = 1
while counter <= check_count:
    print("Health check step:", counter)
    counter += 1

print("CPU Usage   :", cpu_usage)
print("Memory      :", memory_usage)
print("Disk Usage  :", disk_usage)
print("Status      :", status)
print("Message     :", f"{server_name} in {environment} is {status}. {action}.")
print("-" * 45)

# ---------------------------------------------------------------------
# SECTION 18: Mini Challenge
# ---------------------------------------------------------------------

print("\nSECTION 18: Mini Challenge")

"""
Create an interactive Server Health Message Generator.

It should:
1. Ask for server name until it is not blank
2. Ask for environment until it is DEV, TEST, or PROD
3. Ask for CPU usage between 0 and 100
4. Ask for memory usage between 0 and 100
5. Ask for disk usage between 0 and 100
6. Decide final status:
   - CRITICAL if any metric is >= 90
   - WARNING if any metric is >= 80
   - OK otherwise
7. Decide action message
8. Print a clean final health report

Use:
- variables
- input()
- strip(), upper(), lower()
- while loops
- if / elif / else
- strings
- print()
"""

print("Mini challenge: Build the interactive Server Health Message Generator.")

# ---------------------------------------------------------------------
# SECTION 19: Homework
# ---------------------------------------------------------------------

print("\nSECTION 19: Homework")

"""
Homework:
1. Complete Day10_Exercise.py
2. Build the mini project using real input()
3. Test with OK, WARNING, and CRITICAL values
4. Try blank server names and invalid environments
5. Write one final health message that you would be comfortable sharing in a ticket
6. Share your output screenshot with the community

Community discussion question:
Which daily operational message can you generate automatically using Python?
"""

print("Homework: Complete Day10_Exercise.py and share one generated health message.")

print("\nDay 10 completed. You have built your first project-style automation workflow.")
