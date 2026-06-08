"""
Python for Mammals - Day 7
Topic: Conditions Deep Dive

Audience:
- Complete beginners
- DBAs, Sysadmins, Support Engineers, Cloud Engineers, Monitoring Teams
- Anyone who wants Python for practical automation

Goal of Day 7:
By the end of today, you should be able to:
1. Write nested if conditions
2. Combine multiple conditions using and
3. Use or when more than one situation can trigger the same action
4. Use not to reverse a condition clearly
5. Build real-world validation logic for operational scripts

Why this matters:
Real automation rarely makes decisions from only one value.

Examples:
- Disk is high AND environment is production
- Backup failed OR backup duration crossed the limit
- Server is reachable AND disk is OK AND backup is successful
- Do not continue if required input is missing
- Raise different statuses based on multiple checks

Day 6 helped us calculate useful values.
Day 7 helps us make smarter decisions from those values.
"""

print("=" * 70)
print("DAY 7 - CONDITIONS DEEP DIVE")
print("=" * 70)


# ---------------------------------------------------------------------
# SECTION 1: Why Deeper Conditions Matter in Automation
# ---------------------------------------------------------------------

print("\nSECTION 1: Why Deeper Conditions Matter in Automation")

"""
A simple if condition checks one thing.

But operational scripts usually need to check multiple things together.

Example:
- Is the server reachable?
- Is the disk usage safe?
- Did backup finish successfully?
- Is the environment production?

Your script should make decisions based on combinations of these checks.
"""

server_name = "app-server-01"
server_reachable = True
backup_status = "SUCCESS"

print("Server name     :", server_name)
print("Server reachable:", server_reachable)
print("Backup status   :", backup_status)

if server_reachable:
    print("Action          : Continue health check")
else:
    print("Action          : Stop and report server unreachable")


# ---------------------------------------------------------------------
# SECTION 2: Revision - Simple if / elif / else
# ---------------------------------------------------------------------

print("\nSECTION 2: Revision - Simple if / elif / else")

usage_percent = 86

print("Usage percent:", usage_percent, "%")

if usage_percent >= 90:
    print("Status       : CRITICAL")
elif usage_percent >= 80:
    print("Status       : WARNING")
else:
    print("Status       : OK")


# ---------------------------------------------------------------------
# SECTION 3: Multiple Conditions with and
# ---------------------------------------------------------------------

print("\nSECTION 3: Multiple Conditions with and")

"""
and means all conditions must be True.

Example:
Raise high priority only when:
- Disk usage is high
- Environment is production
"""

environment = "PROD"
disk_usage = 91

print("Environment:", environment)
print("Disk usage :", disk_usage, "%")

if environment == "PROD" and disk_usage >= 90:
    print("Action     : Raise high-priority ticket")
else:
    print("Action     : Normal monitoring")


# ---------------------------------------------------------------------
# SECTION 4: Multiple Conditions with or
# ---------------------------------------------------------------------

print("\nSECTION 4: Multiple Conditions with or")

"""
or means at least one condition must be True.

Example:
Review a backup if it failed OR if it took too long.
"""

backup_status = "SUCCESS"
backup_duration_minutes = 145

print("Backup status  :", backup_status)
print("Backup duration:", backup_duration_minutes, "minutes")

if backup_status == "FAILED" or backup_duration_minutes > 120:
    print("Action         : Review backup job")
else:
    print("Action         : Backup looks normal")


# ---------------------------------------------------------------------
# SECTION 5: Reversing Conditions with not
# ---------------------------------------------------------------------

print("\nSECTION 5: Reversing Conditions with not")

"""
not reverses a True/False condition.

This is useful when you want to stop a script if something is missing,
not reachable, not approved, or not ready.
"""

server_reachable = False

print("Server reachable:", server_reachable)

if not server_reachable:
    print("Action          : Stop script and notify support")
else:
    print("Action          : Continue checks")


# ---------------------------------------------------------------------
# SECTION 6: Nested if Conditions
# ---------------------------------------------------------------------

print("\nSECTION 6: Nested if Conditions")

"""
Nested if means an if inside another if.

Use it when the second decision should happen only after the first
condition is already true.

Example:
First check whether server is reachable.
Only then check disk usage.
"""

server_reachable = True
disk_usage = 93

print("Server reachable:", server_reachable)
print("Disk usage      :", disk_usage, "%")

if server_reachable:
    print("Server check    : PASSED")

    if disk_usage >= 90:
        print("Disk status     : CRITICAL")
    elif disk_usage >= 80:
        print("Disk status     : WARNING")
    else:
        print("Disk status     : OK")
else:
    print("Server check    : FAILED")
    print("Disk status     : NOT CHECKED")


# ---------------------------------------------------------------------
# SECTION 7: Nested Conditions with Environment Awareness
# ---------------------------------------------------------------------

print("\nSECTION 7: Nested Conditions with Environment Awareness")

environment = "PROD"
incident_count = 6

print("Environment   :", environment)
print("Incident count:", incident_count)

if environment == "PROD":
    if incident_count >= 5:
        print("Priority      : P1 review required")
    else:
        print("Priority      : Monitor closely")
else:
    if incident_count >= 5:
        print("Priority      : Non-prod cleanup required")
    else:
        print("Priority      : Low priority")


# ---------------------------------------------------------------------
# SECTION 8: Combining Conditions Carefully
# ---------------------------------------------------------------------

print("\nSECTION 8: Combining Conditions Carefully")

"""
You can combine and/or in one condition.

Use brackets to make your intention clear.
"""

environment = "PROD"
cpu_usage = 88
memory_usage = 92

print("Environment :", environment)
print("CPU usage   :", cpu_usage, "%")
print("Memory usage:", memory_usage, "%")

if environment == "PROD" and (cpu_usage >= 90 or memory_usage >= 90):
    print("Action      : Raise production performance alert")
else:
    print("Action      : Continue monitoring")


# ---------------------------------------------------------------------
# SECTION 9: Real-world Validation - Missing Input
# ---------------------------------------------------------------------

print("\nSECTION 9: Real-world Validation - Missing Input")

server_name = "   "
clean_server_name = server_name.strip()

print("Original server name:", repr(server_name))
print("Clean server name   :", repr(clean_server_name))

if clean_server_name == "":
    print("Validation result   : Server name is required")
else:
    print("Validation result   : Server name accepted")


# ---------------------------------------------------------------------
# SECTION 10: Real-world Validation - Allowed Values
# ---------------------------------------------------------------------

print("\nSECTION 10: Real-world Validation - Allowed Values")

environment = "PRODUCTION"

print("Environment entered:", environment)

if environment == "PROD" or environment == "DEV" or environment == "TEST":
    print("Validation result  : Environment accepted")
else:
    print("Validation result  : Invalid environment")
    print("Allowed values     : PROD, DEV, TEST")


# ---------------------------------------------------------------------
# SECTION 11: Real-world Validation - Numeric Range
# ---------------------------------------------------------------------

print("\nSECTION 11: Real-world Validation - Numeric Range")

disk_usage = 104

print("Disk usage entered:", disk_usage)

if disk_usage < 0 or disk_usage > 100:
    print("Validation result : Invalid percentage")
else:
    print("Validation result : Percentage accepted")


# ---------------------------------------------------------------------
# SECTION 12: and vs Nested if
# ---------------------------------------------------------------------

print("\nSECTION 12: and vs Nested if")

"""
Both styles can be correct.

Use and when the condition is short and easy to read.
Use nested if when each step deserves its own message or action.
"""

server_reachable = True
login_successful = True

print("Server reachable:", server_reachable)
print("Login successful:", login_successful)

if server_reachable and login_successful:
    print("Combined check  : Ready to collect report")
else:
    print("Combined check  : Not ready")

if server_reachable:
    print("Nested check    : Server reachable")
    if login_successful:
        print("Nested check    : Login successful")
        print("Nested result   : Ready to collect report")
    else:
        print("Nested result   : Login failed")
else:
    print("Nested result   : Server unreachable")


# ---------------------------------------------------------------------
# SECTION 13: Practical Program 1 - Backup Validation
# ---------------------------------------------------------------------

print("\nSECTION 13: Practical Program 1 - Backup Validation")

backup_status = "SUCCESS"
backup_duration_minutes = 95
backup_size_gb = 0

print("Backup status  :", backup_status)
print("Backup duration:", backup_duration_minutes, "minutes")
print("Backup size    :", backup_size_gb, "GB")

if backup_status == "SUCCESS" and backup_duration_minutes <= 120 and backup_size_gb > 0:
    print("Backup result  : VALID")
else:
    print("Backup result  : NEEDS REVIEW")

    if backup_status != "SUCCESS":
        print("Reason         : Backup status is not SUCCESS")

    if backup_duration_minutes > 120:
        print("Reason         : Backup took longer than expected")

    if backup_size_gb <= 0:
        print("Reason         : Backup size is not valid")


# ---------------------------------------------------------------------
# SECTION 14: Practical Program 2 - Server Health Decision
# ---------------------------------------------------------------------

print("\nSECTION 14: Practical Program 2 - Server Health Decision")

server_reachable = True
cpu_usage = 76
memory_usage = 89
disk_usage = 92

print("Server reachable:", server_reachable)
print("CPU usage       :", cpu_usage, "%")
print("Memory usage    :", memory_usage, "%")
print("Disk usage      :", disk_usage, "%")

if not server_reachable:
    print("Health status   : CRITICAL")
    print("Reason          : Server is not reachable")
elif cpu_usage >= 90 or memory_usage >= 90 or disk_usage >= 90:
    print("Health status   : WARNING")
    print("Reason          : One or more resources are above threshold")
else:
    print("Health status   : OK")
    print("Reason          : Core checks are within threshold")


# ---------------------------------------------------------------------
# SECTION 15: Practical Program 3 - Change Window Validator
# ---------------------------------------------------------------------

print("\nSECTION 15: Practical Program 3 - Change Window Validator")

environment = "PROD"
approval_available = True
current_hour = 23

print("Environment       :", environment)
print("Approval available:", approval_available)
print("Current hour      :", current_hour)

if environment == "PROD":
    if approval_available and (current_hour >= 22 or current_hour <= 5):
        print("Change decision   : Allowed")
    else:
        print("Change decision   : Not allowed")
else:
    print("Change decision   : Follow non-prod process")


# ---------------------------------------------------------------------
# SECTION 16: Mini Project - Operational Health Validator
# ---------------------------------------------------------------------

print("\nSECTION 16: Mini Project - Operational Health Validator")

"""
This mini project evaluates a small operational health workflow.

Input values used today:
- Server name
- Environment
- Server reachability
- Disk usage
- Backup status
- Backup age

Output:
- Validation messages
- Final status
- Suggested action

Today we use fixed values.
You can later convert this into an input-based tool.
"""

server_name = "app-server-01"
environment = "PROD"
server_reachable = True
disk_usage = 91
backup_status = "SUCCESS"
backup_age_hours = 18

print("Operational Health Report")
print("-" * 40)
print("Server name     :", server_name)
print("Environment     :", environment)
print("Server reachable:", server_reachable)
print("Disk usage      :", disk_usage, "%")
print("Backup status   :", backup_status)
print("Backup age      :", backup_age_hours, "hours")

if not server_reachable:
    print("Final status    : CRITICAL")
    print("Action          : Check network, host, or access immediately")
elif environment == "PROD" and disk_usage >= 90:
    print("Final status    : CRITICAL")
    print("Action          : Cleanup or extend capacity urgently")
elif backup_status != "SUCCESS" or backup_age_hours > 24:
    print("Final status    : WARNING")
    print("Action          : Review backup job")
else:
    print("Final status    : OK")
    print("Action          : No immediate action required")


# ---------------------------------------------------------------------
# SECTION 17: Guided Practice - Input-based Health Validator
# ---------------------------------------------------------------------

print("\nSECTION 17: Guided Practice - Input-based Health Validator")

"""
Uncomment this block and run it.

Try these inputs:
1. Server: app01, Env: PROD, Reachable: YES, Disk: 91, Backup: SUCCESS, Age: 18
2. Server: dev01, Env: DEV, Reachable: YES, Disk: 75, Backup: SUCCESS, Age: 10
3. Server: db01, Env: PROD, Reachable: NO, Disk: 40, Backup: SUCCESS, Age: 12
"""

# server_name = input("Enter server name: ").strip()
# environment = input("Enter environment PROD/DEV/TEST: ").strip().upper()
# reachable_input = input("Is server reachable? YES/NO: ").strip().upper()
# disk_usage = float(input("Enter disk usage percentage: "))
# backup_status = input("Enter backup status SUCCESS/FAILED: ").strip().upper()
# backup_age_hours = float(input("Enter backup age in hours: "))
#
# server_reachable = reachable_input == "YES"
#
# print("\nOperational Health Report")
# print("-" * 40)
# print("Server name     :", server_name)
# print("Environment     :", environment)
# print("Server reachable:", server_reachable)
# print("Disk usage      :", disk_usage, "%")
# print("Backup status   :", backup_status)
# print("Backup age      :", backup_age_hours, "hours")
#
# if server_name == "":
#     print("Final status    : INVALID")
#     print("Action          : Server name is required")
# elif environment != "PROD" and environment != "DEV" and environment != "TEST":
#     print("Final status    : INVALID")
#     print("Action          : Environment must be PROD, DEV, or TEST")
# elif disk_usage < 0 or disk_usage > 100:
#     print("Final status    : INVALID")
#     print("Action          : Disk usage must be between 0 and 100")
# elif not server_reachable:
#     print("Final status    : CRITICAL")
#     print("Action          : Check network, host, or access immediately")
# elif environment == "PROD" and disk_usage >= 90:
#     print("Final status    : CRITICAL")
#     print("Action          : Cleanup or extend capacity urgently")
# elif backup_status != "SUCCESS" or backup_age_hours > 24:
#     print("Final status    : WARNING")
#     print("Action          : Review backup job")
# else:
#     print("Final status    : OK")
#     print("Action          : No immediate action required")


# ---------------------------------------------------------------------
# SECTION 18: Mini Challenge
# ---------------------------------------------------------------------

print("\nSECTION 18: Mini Challenge")

"""
Create a Production Readiness Validator.

It should check:
1. Application name is not empty
2. Environment is PROD, DEV, or TEST
3. Approval is available for PROD
4. CPU, memory, and disk usage are between 0 and 100
5. Any usage above 90 should generate a warning or critical status
6. Final report should clearly say whether the system is READY or NOT READY

Use:
- input()
- strip()
- upper()
- float()
- if / elif / else
- nested if
- and / or / not
- print()
"""

print("Mini challenge: Build a Production Readiness Validator using conditions.")


# ---------------------------------------------------------------------
# SECTION 19: Homework
# ---------------------------------------------------------------------

print("\nSECTION 19: Homework")

"""
Homework:
1. Complete Day07_Exercise.py
2. Practice and, or, not with your own operational examples
3. Modify the guided health validator with one extra check:
   - backup_age_hours must not be negative
4. Share one real validation rule from your work in the community

Community discussion question:
What is one operational task where your script should stop immediately
instead of continuing with bad or missing input?
"""

print("Homework: Complete Day07_Exercise.py and share one validation rule.")


print("\nDay 7 completed. You can now handle more complex decisions in Python.")
