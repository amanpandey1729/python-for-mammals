"""
Python for Mammals - Day 17
Topic: Return Values & Scope

Audience:
- Complete beginners
- DBAs, Sysadmins, Support Engineers, Cloud Engineers, Monitoring Teams
- Anyone who wants Python for practical automation

Goal of Day 17:
By the end of today, you should be able to:
1. Understand why return values are useful in automation scripts
2. Return calculated values from functions using return
3. Store returned values in variables
4. Use returned values in conditions, reports, and other functions
5. Understand local variables and global variables
6. Build reusable functions that calculate first and print later

Why this matters:
In Day 16, many functions printed their result directly.
That is useful, but it has a limitation.

Real automation scripts often need to:
- calculate disk usage and reuse it later
- calculate ticket age and decide priority
- generate a status value and include it in a report
- validate backup status and send it to another function
- keep function logic reusable across many scripts

return allows a function to give a value back to the main program.
Scope helps us understand where variables are available.
Together, they make functions cleaner, safer, and more reusable.
"""

print("=" * 70)
print("DAY 17 - RETURN VALUES & SCOPE")
print("RETURN VALUES, LOCAL VARIABLES, GLOBAL VARIABLES, REUSABLE FUNCTIONS")
print("=" * 70)

# ---------------------------------------------------------------------
# SECTION 1: Why Return Values Matter
# ---------------------------------------------------------------------

print("\nSECTION 1: Why Return Values Matter")

"""
A function can either:
1. Do something directly, like print a message
2. Calculate something and return the result

When a function returns a value, the main script can reuse that value.
This is very important for automation.
"""

print("A return value lets a function send a result back to the main script.")

# ---------------------------------------------------------------------
# SECTION 2: Printing Inside a Function
# ---------------------------------------------------------------------

print("\nSECTION 2: Printing Inside a Function")


def print_disk_usage(total_gb, used_gb):
    usage_percent = (used_gb / total_gb) * 100
    print("Disk usage:", round(usage_percent, 2), "%")


print_disk_usage(500, 375)

"""
This function prints the disk usage.
But the calculated usage_percent is trapped inside the function.
The main program cannot reuse it later.
"""

# ---------------------------------------------------------------------
# SECTION 3: Returning a Value from a Function
# ---------------------------------------------------------------------

print("\nSECTION 3: Returning a Value from a Function")


def calculate_disk_usage(total_gb, used_gb):
    usage_percent = (used_gb / total_gb) * 100
    return usage_percent


disk_usage = calculate_disk_usage(500, 375)
print("Returned disk usage:", round(disk_usage, 2), "%")

"""
return sends the value back to the place where the function was called.

Here:
disk_usage = calculate_disk_usage(500, 375)

The returned value is stored in disk_usage.
Now we can print it, compare it, or include it in a report.
"""

# ---------------------------------------------------------------------
# SECTION 4: Use Returned Value in a Condition
# ---------------------------------------------------------------------

print("\nSECTION 4: Use Returned Value in a Condition")


def get_usage_status(usage_percent):
    if usage_percent >= 90:
        return "CRITICAL"
    elif usage_percent >= 80:
        return "WARNING"
    else:
        return "OK"


memory_usage = 84
memory_status = get_usage_status(memory_usage)
print("Memory usage:", memory_usage, "%")
print("Memory status:", memory_status)

"""
This function returns a status text.
It does not print anything.

This makes it reusable because the returned status can be used in:
- reports
- alerts
- dashboards
- emails
- files
"""

# ---------------------------------------------------------------------
# SECTION 5: Return Values Can Be Used Directly
# ---------------------------------------------------------------------

print("\nSECTION 5: Return Values Can Be Used Directly")


def calculate_free_space(total_gb, used_gb):
    free_gb = total_gb - used_gb
    return free_gb


print("Free space:", calculate_free_space(200, 145), "GB")

"""
You can store a returned value in a variable.
You can also use the returned value directly inside print().

For beginners, storing it in a variable is usually easier to read.
"""

# ---------------------------------------------------------------------
# SECTION 6: Return Multiple Values
# ---------------------------------------------------------------------

print("\nSECTION 6: Return Multiple Values")


def calculate_storage_summary(total_gb, used_gb):
    free_gb = total_gb - used_gb
    usage_percent = (used_gb / total_gb) * 100
    return free_gb, usage_percent


free_space, usage = calculate_storage_summary(1000, 790)
print("Free space:", free_space, "GB")
print("Usage:", round(usage, 2), "%")

"""
A function can return more than one value.
Python returns them as a tuple-like result.
We can capture them in separate variables.
"""

# ---------------------------------------------------------------------
# SECTION 7: Local Variables
# ---------------------------------------------------------------------

print("\nSECTION 7: Local Variables")


def calculate_cpu_average(cpu1, cpu2, cpu3):
    average_cpu = (cpu1 + cpu2 + cpu3) / 3
    return average_cpu


avg_cpu = calculate_cpu_average(70, 80, 90)
print("Average CPU:", round(avg_cpu, 2), "%")

"""
average_cpu is a local variable.
It is created inside the function.
It is available only inside that function.

This is good because temporary calculation variables do not pollute
the rest of the script.
"""

# ---------------------------------------------------------------------
# SECTION 8: Global Variables
# ---------------------------------------------------------------------

print("\nSECTION 8: Global Variables")

company_name = "Python for Mammals"


def print_company_report_title(report_name):
    print(company_name, "-", report_name)


print_company_report_title("Daily Operations Report")

"""
company_name is a global variable because it is created outside functions.
A function can read a global variable.

But for clean automation scripts, avoid depending too much on globals.
Passing values as parameters is usually safer and clearer.
"""

# ---------------------------------------------------------------------
# SECTION 9: Prefer Parameters Over Global Dependence
# ---------------------------------------------------------------------

print("\nSECTION 9: Prefer Parameters Over Global Dependence")


def print_report_title(team_name, report_name):
    print(team_name, "-", report_name)


print_report_title("Infra Team", "Server Health Report")
print_report_title("DB Team", "Backup Validation Report")

"""
This version is more reusable.
The function does not depend on a global company_name variable.
It receives the required values as parameters.
"""

# ---------------------------------------------------------------------
# SECTION 10: Local Variable with Same Name as Global Variable
# ---------------------------------------------------------------------

print("\nSECTION 10: Local Variable with Same Name as Global Variable")

status = "GLOBAL STATUS"


def create_local_status():
    status = "LOCAL STATUS"
    return status


returned_status = create_local_status()
print("Returned status:", returned_status)
print("Global status:", status)

"""
The local status inside the function is different from the global status.
They share the same name, but they live in different scopes.

This is why clear variable names matter.
"""

# ---------------------------------------------------------------------
# SECTION 11: Function Calling Another Function
# ---------------------------------------------------------------------

print("\nSECTION 11: Function Calling Another Function")


def calculate_usage(total_gb, used_gb):
    return (used_gb / total_gb) * 100


def build_disk_summary(server_name, total_gb, used_gb):
    usage_percent = calculate_usage(total_gb, used_gb)
    status_text = get_usage_status(usage_percent)
    return server_name + " disk usage is " + str(round(usage_percent, 2)) + "% - " + status_text


summary = build_disk_summary("app01", 500, 455)
print(summary)

"""
Reusable functions can call other reusable functions.

This is a very common automation design:
- one function calculates
- one function decides status
- one function builds report text
"""

# ---------------------------------------------------------------------
# SECTION 12: Return vs Print
# ---------------------------------------------------------------------

print("\nSECTION 12: Return vs Print")

"""
Use print when:
- you only want to show something on screen
- the result is not needed later

Use return when:
- the result must be reused
- the result will be checked in a condition
- the result will be passed to another function
- the result will be written into a report later
"""

print("print shows output. return gives a reusable value back to the script.")

# ---------------------------------------------------------------------
# SECTION 13: Guided Practice - Return Backup Status
# ---------------------------------------------------------------------

print("\nSECTION 13: Guided Practice - Return Backup Status")

"""
Uncomment this block and run it.
Create a function that returns backup health.
"""

# def get_backup_health(backup_status):
#     if backup_status == "SUCCESS":
#         return "OK"
#     else:
#         return "ACTION REQUIRED"
#
# health = get_backup_health("FAILED")
# print("Backup health:", health)

print("Guided practice: uncomment the backup health return block.")

# ---------------------------------------------------------------------
# SECTION 14: Guided Practice - Local Variable
# ---------------------------------------------------------------------

print("\nSECTION 14: Guided Practice - Local Variable")

"""
Uncomment this block and run it.
Observe that ticket_age is local to the function.
"""

# def calculate_ticket_age(open_day, current_day):
#     ticket_age = current_day - open_day
#     return ticket_age
#
# age = calculate_ticket_age(10, 17)
# print("Ticket age:", age, "days")

print("Guided practice: uncomment the ticket age local variable block.")

# ---------------------------------------------------------------------
# SECTION 15: Guided Practice - Reusable Functions
# ---------------------------------------------------------------------

print("\nSECTION 15: Guided Practice - Reusable Functions")

"""
Uncomment this block and run it.
One function calculates. Another function decides status.
"""

# def calculate_usage_percent(total, used):
#     return (used / total) * 100
#
# def decide_status(usage_percent):
#     if usage_percent >= 90:
#         return "CRITICAL"
#     elif usage_percent >= 80:
#         return "WARNING"
#     else:
#         return "OK"
#
# usage = calculate_usage_percent(300, 270)
# status_text = decide_status(usage)
# print("Usage:", round(usage, 2), "%")
# print("Status:", status_text)

print("Guided practice: uncomment the reusable function block.")

# ---------------------------------------------------------------------
# SECTION 16: Mini Challenge Preview
# ---------------------------------------------------------------------

print("\nSECTION 16: Mini Challenge Preview")

"""
Mini Challenge:
Build a Return-Based Server Health Reporter.

Your script should:
1. Collect server name, environment, CPU, memory, disk, backup status, and ticket count
2. Create functions that return calculated values and status values
3. Store returned values in variables
4. Reuse those returned values to print one final report
5. Avoid depending on global variables inside functions

This mirrors real automation:
- collect input once
- calculate reusable values
- make decisions from returned values
- generate a clean report
"""

print("Mini challenge: build a return-based Server Health Reporter.")

# ---------------------------------------------------------------------
# SECTION 17: Closing Message
# ---------------------------------------------------------------------

print("\nSECTION 17: Closing Message")

print("Return values make functions reusable beyond printing.")
print("Scope keeps variables controlled and predictable.")
print("Day 17 complete. Build functions that calculate, return, and support automation workflows.")
