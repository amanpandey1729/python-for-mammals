"""
Python for Mammals - Day 16
Topic: Functions

Audience:
- Complete beginners
- DBAs, Sysadmins, Support Engineers, Cloud Engineers, Monitoring Teams
- Anyone who wants Python for practical automation

Goal of Day 16:
By the end of today, you should be able to:
1. Understand why functions are useful in automation scripts
2. Define your own functions using def
3. Call functions whenever you need them
4. Pass values into functions using parameters
5. Reduce repeated code in reports, checks, and calculations
6. Create small reusable building blocks for daily operational tasks

Why this matters:
In real work, we repeat the same logic many times.

You may repeatedly:
- print report headers
- calculate disk usage
- generate status messages
- format ticket summaries
- check CPU, memory, or disk thresholds
- print separators in reports

Without functions, the same code gets copied again and again.
With functions, we write the logic once and reuse it whenever needed.

Functions are the beginning of clean automation design.
"""

print("=" * 70)
print("DAY 16 - FUNCTIONS")
print("DEFINE FUNCTIONS, CALL FUNCTIONS, USE PARAMETERS")
print("=" * 70)

# ---------------------------------------------------------------------
# SECTION 1: Why Functions Matter
# ---------------------------------------------------------------------

print("\nSECTION 1: Why Functions Matter")

"""
A function is a reusable block of code.

Instead of writing the same lines again and again,
we place them inside a function and call the function when needed.

This helps automation scripts become:
- cleaner
- easier to read
- easier to update
- less error-prone
"""

print("Functions help us reuse logic instead of copying code repeatedly.")

# ---------------------------------------------------------------------
# SECTION 2: Repeated Code Without Functions
# ---------------------------------------------------------------------

print("\nSECTION 2: Repeated Code Without Functions")

print("Daily Server Report")
print("-" * 40)

print("Backup Job Report")
print("-" * 40)

print("Disk Usage Report")
print("-" * 40)

"""
The separator logic is repeated three times.
This is not a big problem here, but in a real script it becomes messy.

Functions help us place repeated logic in one place.
"""

# ---------------------------------------------------------------------
# SECTION 3: Define Your First Function
# ---------------------------------------------------------------------

print("\nSECTION 3: Define Your First Function")


def print_separator():
    print("-" * 40)


print("Daily Server Report")
print_separator()

print("Backup Job Report")
print_separator()

print("Disk Usage Report")
print_separator()

"""
def print_separator():
    creates a function named print_separator.

The indented line belongs to the function.
The function does not run automatically.
It runs only when we call it.
"""

# ---------------------------------------------------------------------
# SECTION 4: Calling a Function Multiple Times
# ---------------------------------------------------------------------

print("\nSECTION 4: Calling a Function Multiple Times")


def show_welcome_message():
    print("Welcome to the daily automation script")
    print("Please review the generated output carefully")


show_welcome_message()
show_welcome_message()

"""
Calling means using the function name followed by parentheses.

show_welcome_message()

Every time we call it, the code inside the function runs.
"""

# ---------------------------------------------------------------------
# SECTION 5: Function with One Parameter
# ---------------------------------------------------------------------

print("\nSECTION 5: Function with One Parameter")


def print_report_title(report_name):
    print(report_name)
    print("-" * 40)


print_report_title("Daily Health Check Report")
print_report_title("Backup Validation Report")
print_report_title("Ticket Summary Report")

"""
report_name is a parameter.
A parameter is a variable that receives a value when the function is called.

This makes the function flexible.
The same function can print different report titles.
"""

# ---------------------------------------------------------------------
# SECTION 6: Function with Multiple Parameters
# ---------------------------------------------------------------------

print("\nSECTION 6: Function with Multiple Parameters")


def print_server_summary(server_name, environment, status):
    print("Server     :", server_name)
    print("Environment:", environment)
    print("Status     :", status)
    print("-" * 40)


print_server_summary("app01", "production", "active")
print_server_summary("db01", "production", "maintenance")

"""
A function can accept multiple parameters.

Here the function receives:
- server_name
- environment
- status

This is useful when many records need the same output format.
"""

# ---------------------------------------------------------------------
# SECTION 7: Parameter Order Matters
# ---------------------------------------------------------------------

print("\nSECTION 7: Parameter Order Matters")


def show_ticket(ticket_id, priority, owner):
    print("Ticket:", ticket_id, "| Priority:", priority, "| Owner:", owner)


show_ticket("INC1001", "HIGH", "infra-team")
show_ticket("INC1002", "LOW", "app-team")

"""
Values are assigned to parameters by position.

show_ticket("INC1001", "HIGH", "infra-team")

means:
ticket_id = "INC1001"
priority  = "HIGH"
owner     = "infra-team"
"""

# ---------------------------------------------------------------------
# SECTION 8: Function for Disk Usage Calculation
# ---------------------------------------------------------------------

print("\nSECTION 8: Function for Disk Usage Calculation")


def calculate_disk_usage(total_gb, used_gb):
    usage_percent = (used_gb / total_gb) * 100
    print("Disk usage:", round(usage_percent, 2), "%")


calculate_disk_usage(100, 72)
calculate_disk_usage(500, 455)
calculate_disk_usage(200, 88)

"""
This function calculates disk usage.
We can reuse the same calculation for many servers.

For now, the function prints the result directly.
Later we will learn how functions can return values.
"""

# ---------------------------------------------------------------------
# SECTION 9: Function for Health Status
# ---------------------------------------------------------------------

print("\nSECTION 9: Function for Health Status")


def print_health_status(server_name, usage_percent):
    if usage_percent >= 90:
        status = "CRITICAL"
    elif usage_percent >= 80:
        status = "WARNING"
    else:
        status = "OK"

    print(server_name, "=>", usage_percent, "%", "=>", status)


print_health_status("app01", 72)
print_health_status("db01", 91)
print_health_status("web01", 84)

"""
A function can contain conditions.
This is useful for checks and alerts.

The same status logic can now be reused for CPU, memory, disk, or backup checks.
"""

# ---------------------------------------------------------------------
# SECTION 10: Function Used Inside a Loop
# ---------------------------------------------------------------------

print("\nSECTION 10: Function Used Inside a Loop")


def print_backup_status(database_name, backup_status):
    print(database_name, "backup status:", backup_status)


backup_jobs = [
    {"database": "PRODDB", "status": "SUCCESS"},
    {"database": "APPDB", "status": "SUCCESS"},
    {"database": "TESTDB", "status": "FAILED"}
]

for job in backup_jobs:
    print_backup_status(job["database"], job["status"])

"""
This is a powerful automation pattern:

1. Store data in a list of dictionaries
2. Loop through each record
3. Pass values into a function
4. Let the function handle the repeated formatting or logic
"""

# ---------------------------------------------------------------------
# SECTION 11: Function to Print a Simple Report Line
# ---------------------------------------------------------------------

print("\nSECTION 11: Function to Print a Simple Report Line")


def print_report_line(label, value):
    print(label + ":", value)


print_report_line("Server", "app01")
print_report_line("CPU", "76%")
print_report_line("Memory", "82%")
print_report_line("Disk", "69%")

"""
Small functions are not useless.
They make formatting consistent.

If you later want to change the report style, you change one function instead of many lines.
"""

# ---------------------------------------------------------------------
# SECTION 12: Function Naming
# ---------------------------------------------------------------------

print("\nSECTION 12: Function Naming")

"""
Good function names explain the action.

Good names:
- print_report_title
- calculate_disk_usage
- show_ticket_summary
- check_cpu_status
- generate_backup_message

Poor names:
- abc
- temp
- do_it
- function1

Use action words because functions usually do something.
"""

print("Use clear function names so your future self can understand the script.")

# ---------------------------------------------------------------------
# SECTION 13: Guided Practice - Report Header Function
# ---------------------------------------------------------------------

print("\nSECTION 13: Guided Practice - Report Header Function")

"""
Uncomment this block and run it.
Create a reusable function for report headers.
"""

# def show_header(title):
#     print("=" * 50)
#     print(title)
#     print("=" * 50)
#
# show_header("Morning Operations Report")
# show_header("Evening Operations Report")

print("Guided practice: uncomment the report header function block.")

# ---------------------------------------------------------------------
# SECTION 14: Guided Practice - Alert Message Function
# ---------------------------------------------------------------------

print("\nSECTION 14: Guided Practice - Alert Message Function")

"""
Uncomment this block and run it.
Create a reusable function for alert messages.
"""

# def show_alert(server_name, severity, message):
#     print("ALERT:", severity)
#     print("Server:", server_name)
#     print("Message:", message)
#     print("-" * 40)
#
# show_alert("app01", "HIGH", "CPU usage is above threshold")
# show_alert("db01", "CRITICAL", "Disk usage is above threshold")

print("Guided practice: uncomment the alert message function block.")

# ---------------------------------------------------------------------
# SECTION 15: Guided Practice - Function Inside Loop
# ---------------------------------------------------------------------

print("\nSECTION 15: Guided Practice - Function Inside Loop")

"""
Uncomment this block and run it.
Use a function inside a loop to print multiple server checks.
"""

# def show_check(server_name, check_name, status):
#     print(server_name, "|", check_name, "|", status)
#
# checks = [
#     {"server": "app01", "check": "CPU", "status": "OK"},
#     {"server": "db01", "check": "Disk", "status": "WARNING"},
#     {"server": "web01", "check": "Memory", "status": "OK"}
# ]
#
# for check in checks:
#     show_check(check["server"], check["check"], check["status"])

print("Guided practice: uncomment the function inside loop block.")

# ---------------------------------------------------------------------
# SECTION 16: Mini Challenge Preview
# ---------------------------------------------------------------------

print("\nSECTION 16: Mini Challenge Preview")

"""
Mini Challenge:
Build a simple function-based Daily Health Reporter.

Your script should:
1. Collect server name, environment, CPU usage, memory usage, and disk usage
2. Create a function to print a report title
3. Create a function to print one metric line
4. Create a function to print status based on usage percentage
5. Reuse these functions to generate a clean final report

This mirrors real automation:
- collect input once
- reuse function blocks
- produce a consistent report
"""

print("Mini challenge: build a function-based Daily Health Reporter.")

# ---------------------------------------------------------------------
# SECTION 17: Closing Message
# ---------------------------------------------------------------------

print("\nSECTION 17: Closing Message")

print("Functions are reusable automation blocks.")
print("Write once. Call many times. Keep scripts clean.")
print("Day 16 complete. Practice functions until calling them feels natural.")
