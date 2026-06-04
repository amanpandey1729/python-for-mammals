"""
Python for Mammals - Day 3
Topic: Taking Input, Type Conversion, f-Strings, and First Decisions

Audience:
- Complete beginners
- DBAs, Sysadmins, Support Engineers, Cloud Engineers, Monitoring Teams
- Anyone who wants Python for practical automation

Goal of Day 3:
By the end of today, you should be able to:
1. Ask the user for input
2. Convert input into numbers when needed
3. Format output using f-strings
4. Compare values
5. Use if / elif / else to make your program take decisions

Why this matters:
Automation scripts are useful only when they can react.

Example:
- Disk usage is 92 percent
  Python should say: CRITICAL

- Backup status is SUCCESS
  Python should say: Backup completed

- CPU usage is 45 percent
  Python should say: Normal

This is where Python starts behaving like a small automation assistant.
"""

print("=" * 70)
print("DAY 3 - INPUT, TYPE CONVERSION, F-STRINGS, AND CONDITIONS")
print("=" * 70)

# ---------------------------------------------------------------------
# SECTION 1: Quick Revision from Day 2
# ---------------------------------------------------------------------

print("\nSECTION 1: Quick Revision")

server_name = "app-server-01"
cpu_usage = 67.5
is_server_up = True

print("Server Name:", server_name)
print("CPU Usage:", cpu_usage)
print("Is Server Up:", is_server_up)

print("Type of server_name:", type(server_name))
print("Type of cpu_usage:", type(cpu_usage))
print("Type of is_server_up:", type(is_server_up))


# ---------------------------------------------------------------------
# SECTION 2: Taking Input from User
# ---------------------------------------------------------------------

print("\nSECTION 2: Taking Input from User")

"""
input() is used to take information from the user.

Important:
input() always returns text/string.

Even if the user types 90, Python receives it as "90".
"""

# Uncomment and run this section manually.
# name = input("Enter your name: ")
# print("Welcome,", name)


# ---------------------------------------------------------------------
# SECTION 3: input() Always Returns String
# ---------------------------------------------------------------------

print("\nSECTION 3: input() Always Returns String")

"""
Let us understand this carefully.

If you ask the user for disk usage and they type 85,
Python stores it as text unless we convert it.
"""

# Uncomment to test.
# disk_usage = input("Enter disk usage percentage: ")
# print("You entered:", disk_usage)
# print("Data type of disk_usage:", type(disk_usage))


# ---------------------------------------------------------------------
# SECTION 4: Type Conversion
# ---------------------------------------------------------------------

print("\nSECTION 4: Type Conversion")

"""
Type conversion means changing one data type into another.

Common conversions:
str()   -> converts to string
int()   -> converts to integer
float() -> converts to decimal number

Why needed?
Because input() gives string, but calculations need numbers.
"""

text_number = "90"
converted_number = int(text_number)

print("Before conversion:", text_number, type(text_number))
print("After conversion:", converted_number, type(converted_number))

used_space_gb = "450.5"
used_space_gb = float(used_space_gb)

print("Used space in GB:", used_space_gb)
print("Type after float conversion:", type(used_space_gb))


# ---------------------------------------------------------------------
# SECTION 5: Small Practical Example - Disk Usage Calculator
# ---------------------------------------------------------------------

print("\nSECTION 5: Disk Usage Calculator")

total_space_gb = 500
used_space_gb = 375

used_percent = (used_space_gb / total_space_gb) * 100
free_space_gb = total_space_gb - used_space_gb

print("Total Space GB:", total_space_gb)
print("Used Space GB:", used_space_gb)
print("Free Space GB:", free_space_gb)
print("Used Percent:", used_percent)


# ---------------------------------------------------------------------
# SECTION 6: f-Strings for Clean Output
# ---------------------------------------------------------------------

print("\nSECTION 6: f-Strings")

"""
f-strings help us print variables inside text cleanly.

Syntax:
f"Some text {variable_name}"

This is very useful for reports, alerts, logs, and summaries.
"""

server_name = "db-server-01"
cpu_usage = 72.3456

print(f"Server {server_name} has CPU usage of {cpu_usage}%")

# Formatting decimal places
print(f"Server {server_name} has CPU usage of {cpu_usage:.2f}%")

# Practical report line
total_space_gb = 500
used_space_gb = 375
free_space_gb = total_space_gb - used_space_gb
used_percent = (used_space_gb / total_space_gb) * 100

print(f"Disk Report: Total={total_space_gb}GB, Used={used_space_gb}GB, Free={free_space_gb}GB, Used%={used_percent:.2f}%")


# ---------------------------------------------------------------------
# SECTION 7: Comparison Operators
# ---------------------------------------------------------------------

print("\nSECTION 7: Comparison Operators")

"""
Comparison operators help Python compare values.

Operator    Meaning
==          equal to
!=          not equal to
>           greater than
<           less than
>=          greater than or equal to
<=          less than or equal to

The result is always True or False.
"""

disk_usage = 82

print("disk_usage == 82:", disk_usage == 82)
print("disk_usage > 80:", disk_usage > 80)
print("disk_usage < 50:", disk_usage < 50)
print("disk_usage != 90:", disk_usage != 90)


# ---------------------------------------------------------------------
# SECTION 8: Boolean Values
# ---------------------------------------------------------------------

print("\nSECTION 8: Boolean Values")

"""
Boolean has only two values:
True
False

In automation, Boolean answers questions like:
- Is the server up?
- Is backup completed?
- Is disk usage above threshold?
"""

is_backup_successful = True
is_disk_full = False

print("Backup successful:", is_backup_successful)
print("Disk full:", is_disk_full)


# ---------------------------------------------------------------------
# SECTION 9: if Statement
# ---------------------------------------------------------------------

print("\nSECTION 9: if Statement")

"""
if allows Python to run code only when a condition is True.
"""

disk_usage = 92

if disk_usage > 90:
    print("CRITICAL: Disk usage is above 90%")


# ---------------------------------------------------------------------
# SECTION 10: if-else Statement
# ---------------------------------------------------------------------

print("\nSECTION 10: if-else Statement")

"""
if-else gives Python two paths.

If condition is True:
    do this
Otherwise:
    do that
"""

backup_status = "SUCCESS"

if backup_status == "SUCCESS":
    print("Backup completed successfully.")
else:
    print("Backup failed. Please check logs.")


# ---------------------------------------------------------------------
# SECTION 11: if-elif-else Statement
# ---------------------------------------------------------------------

print("\nSECTION 11: if-elif-else Statement")

"""
if-elif-else is used when we have multiple possible decisions.

Example:
Disk usage:
0-69      NORMAL
70-84     WARNING
85-94     HIGH
95+       CRITICAL
"""

disk_usage = 88

if disk_usage >= 95:
    print("CRITICAL: Immediate action required.")
elif disk_usage >= 85:
    print("HIGH: Disk cleanup should be planned.")
elif disk_usage >= 70:
    print("WARNING: Monitor the disk usage.")
else:
    print("NORMAL: Disk usage is healthy.")


# ---------------------------------------------------------------------
# SECTION 12: Logical Operators
# ---------------------------------------------------------------------

print("\nSECTION 12: Logical Operators")

"""
Logical operators combine multiple conditions.

and -> both conditions must be True
or  -> at least one condition must be True
not -> reverses True/False
"""

cpu_usage = 82
memory_usage = 78

if cpu_usage > 80 and memory_usage > 75:
    print("Alert: CPU and Memory both are high.")

disk_usage = 91
inode_usage = 40

if disk_usage > 90 or inode_usage > 90:
    print("Alert: Disk or inode usage is high.")

is_server_up = False

if not is_server_up:
    print("Alert: Server is down.")


# ---------------------------------------------------------------------
# SECTION 13: Practical Program 1 - Server Health Decision
# ---------------------------------------------------------------------

print("\nSECTION 13: Practical Program 1 - Server Health Decision")

server_name = "linux-prod-01"
cpu_usage = 65
memory_usage = 72
disk_usage = 81

print(f"\nHealth Check Report for {server_name}")
print("-" * 40)
print(f"CPU Usage    : {cpu_usage}%")
print(f"Memory Usage : {memory_usage}%")
print(f"Disk Usage   : {disk_usage}%")

if cpu_usage > 90 or memory_usage > 90 or disk_usage > 90:
    print("Overall Status: CRITICAL")
elif cpu_usage > 75 or memory_usage > 75 or disk_usage > 75:
    print("Overall Status: WARNING")
else:
    print("Overall Status: HEALTHY")


# ---------------------------------------------------------------------
# SECTION 14: Practical Program 2 - Backup Status Checker
# ---------------------------------------------------------------------

print("\nSECTION 14: Practical Program 2 - Backup Status Checker")

backup_name = "daily_file_backup"
backup_status = "FAILED"
backup_duration_minutes = 125

print(f"\nBackup Name     : {backup_name}")
print(f"Backup Status   : {backup_status}")
print(f"Backup Duration : {backup_duration_minutes} minutes")

if backup_status == "SUCCESS" and backup_duration_minutes <= 120:
    print("Result: Backup is successful and completed within expected time.")
elif backup_status == "SUCCESS" and backup_duration_minutes > 120:
    print("Result: Backup completed, but took longer than expected.")
else:
    print("Result: Backup failed. Immediate validation required.")


# ---------------------------------------------------------------------
# SECTION 15: Guided Practice - Interactive Health Checker
# ---------------------------------------------------------------------

print("\nSECTION 15: Guided Practice - Interactive Health Checker")

"""
Uncomment this block and run it.

This is your first small interactive automation-style program.
It asks the user for values and prints a decision.

Important:
We use float() because CPU, memory, and disk usage can contain decimals.
"""

# server_name = input("Enter server name: ")
# cpu_usage = float(input("Enter CPU usage percentage: "))
# memory_usage = float(input("Enter memory usage percentage: "))
# disk_usage = float(input("Enter disk usage percentage: "))
#
# print("\nGenerated Health Report")
# print("-" * 40)
# print(f"Server Name  : {server_name}")
# print(f"CPU Usage    : {cpu_usage:.2f}%")
# print(f"Memory Usage : {memory_usage:.2f}%")
# print(f"Disk Usage   : {disk_usage:.2f}%")
#
# if cpu_usage >= 90 or memory_usage >= 90 or disk_usage >= 90:
#     print("Final Status : CRITICAL")
# elif cpu_usage >= 75 or memory_usage >= 75 or disk_usage >= 75:
#     print("Final Status : WARNING")
# else:
#     print("Final Status : HEALTHY")


# ---------------------------------------------------------------------
# SECTION 16: Common Beginner Mistakes
# ---------------------------------------------------------------------

print("\nSECTION 16: Common Beginner Mistakes")

"""
Mistake 1:
Using = instead of == while comparing.

Wrong:
if status = "SUCCESS":

Correct:
if status == "SUCCESS":


Mistake 2:
Forgetting type conversion.

Wrong:
disk_usage = input("Enter disk usage: ")
if disk_usage > 90:

Correct:
disk_usage = float(input("Enter disk usage: "))
if disk_usage > 90:


Mistake 3:
Indentation error.

Correct:
if disk_usage > 90:
    print("High usage")

The print line must be indented.
"""

print("Read the comments above carefully. These mistakes are very common.")


# ---------------------------------------------------------------------
# SECTION 17: Mini Challenge
# ---------------------------------------------------------------------

print("\nSECTION 17: Mini Challenge")

"""
Mini Challenge:
Create an interactive script that asks:

1. Your name
2. System name
3. CPU usage
4. Memory usage
5. Disk usage

Then print a clean report using f-strings.

Final decision:
- If any usage is >= 90, print CRITICAL
- Else if any usage is >= 75, print WARNING
- Else print HEALTHY

Bonus:
Also print which component caused the warning or critical status.
"""

print("Mini Challenge is described in comments above.")


# ---------------------------------------------------------------------
# SECTION 18: Day 3 Summary
# ---------------------------------------------------------------------

print("\nSECTION 18: Day 3 Summary")

"""
Today you learned:
- input()
- int() and float()
- f-strings
- comparison operators
- Boolean values
- if
- if-else
- if-elif-else
- and / or / not
- basic automation-style decisions

You are no longer just printing values.
You are now making Python think and decide.
"""

print("\nDay 3 completed. Keep practicing. Automation begins with decisions!")
