"""
Python for Mammals - Day 6
Topic: Operators & Calculations

Audience:
- Complete beginners
- DBAs, Sysadmins, Support Engineers, Cloud Engineers, Monitoring Teams
- Anyone who wants Python for practical automation

Goal of Day 6:
By the end of today, you should be able to:
1. Perform arithmetic calculations in Python
2. Update values using assignment operators
3. Revise comparison operators from decision making
4. Understand operator precedence
5. Build practical calculations for reports, capacity, alerts, and daily checks

Why this matters:
Automation is not only about reading text.
Automation also needs calculations.

Examples:
- Calculate disk usage percentage
- Calculate free space
- Calculate backup duration
- Calculate ticket SLA breach risk
- Calculate total report count
- Compare current value with threshold
- Prepare capacity summary for daily reports

Day 5 helped us extract meaning from text.
Day 6 helps us calculate useful values from numbers.
"""

print("=" * 70)
print("DAY 6 - OPERATORS & CALCULATIONS")
print("=" * 70)


# ---------------------------------------------------------------------
# SECTION 1: Why Operators Matter in Automation
# ---------------------------------------------------------------------

print("\nSECTION 1: Why Operators Matter in Automation")

"""
Operators help Python perform work on values.

In daily operations, you may need to answer questions like:
- How much disk space is used?
- How much memory is free?
- Did backup duration cross the allowed limit?
- Is incident count increasing?
- What percentage of checks passed?

These questions require calculations and comparisons.
"""

total_checks = 10
passed_checks = 8
failed_checks = total_checks - passed_checks

print("Total checks :", total_checks)
print("Passed checks:", passed_checks)
print("Failed checks:", failed_checks)


# ---------------------------------------------------------------------
# SECTION 2: Arithmetic Operators
# ---------------------------------------------------------------------

print("\nSECTION 2: Arithmetic Operators")

"""
Common arithmetic operators:

+   Addition
-   Subtraction
*   Multiplication
/   Division
//  Floor division
%   Modulus, remainder
**  Power
"""

used_gb = 75
free_gb = 25
total_gb = used_gb + free_gb

print("Used space  :", used_gb, "GB")
print("Free space  :", free_gb, "GB")
print("Total space :", total_gb, "GB")


# ---------------------------------------------------------------------
# SECTION 3: Subtraction for Remaining Capacity
# ---------------------------------------------------------------------

print("\nSECTION 3: Subtraction for Remaining Capacity")

total_storage = 500
used_storage = 365
remaining_storage = total_storage - used_storage

print("Total storage    :", total_storage, "GB")
print("Used storage     :", used_storage, "GB")
print("Remaining storage:", remaining_storage, "GB")


# ---------------------------------------------------------------------
# SECTION 4: Multiplication for Repeated Values
# ---------------------------------------------------------------------

print("\nSECTION 4: Multiplication for Repeated Values")

servers = 12
checks_per_server = 5
total_daily_checks = servers * checks_per_server

print("Servers          :", servers)
print("Checks per server:", checks_per_server)
print("Total checks     :", total_daily_checks)


# ---------------------------------------------------------------------
# SECTION 5: Division for Percentages
# ---------------------------------------------------------------------

print("\nSECTION 5: Division for Percentages")

used_space = 82
total_space = 100
usage_percent = (used_space / total_space) * 100

print("Used space    :", used_space, "GB")
print("Total space   :", total_space, "GB")
print("Usage percent :", usage_percent, "%")


# ---------------------------------------------------------------------
# SECTION 6: round() for Cleaner Reports
# ---------------------------------------------------------------------

print("\nSECTION 6: round() for Cleaner Reports")

used_space = 236
total_space = 300
usage_percent = (used_space / total_space) * 100
rounded_percent = round(usage_percent, 2)

print("Raw percent    :", usage_percent)
print("Rounded percent:", rounded_percent)


# ---------------------------------------------------------------------
# SECTION 7: Floor Division
# ---------------------------------------------------------------------

print("\nSECTION 7: Floor Division")

"""
Floor division // gives the whole-number result.

Example:
If 17 checks are distributed across 5 engineers,
Python can calculate how many complete checks each engineer gets.
"""

total_tasks = 17
engineers = 5
tasks_per_engineer = total_tasks // engineers

print("Total tasks       :", total_tasks)
print("Engineers         :", engineers)
print("Tasks per engineer:", tasks_per_engineer)


# ---------------------------------------------------------------------
# SECTION 8: Modulus for Remainders
# ---------------------------------------------------------------------

print("\nSECTION 8: Modulus for Remainders")

remaining_tasks = total_tasks % engineers

print("Total tasks    :", total_tasks)
print("Engineers      :", engineers)
print("Remaining tasks:", remaining_tasks)


# ---------------------------------------------------------------------
# SECTION 9: Assignment Operators
# ---------------------------------------------------------------------

print("\nSECTION 9: Assignment Operators")

"""
Assignment operators update existing values.

count = count + 1
can be written as:
count += 1

Common forms:
+=
-=
*=
/=
"""

incident_count = 0
print("Initial incident count:", incident_count)

incident_count += 1
print("After first incident  :", incident_count)

incident_count += 2
print("After two more        :", incident_count)

incident_count -= 1
print("After one resolved    :", incident_count)


# ---------------------------------------------------------------------
# SECTION 10: Practical Counter Example
# ---------------------------------------------------------------------

print("\nSECTION 10: Practical Counter Example")

successful_backups = 0
failed_backups = 0

backup_1_status = "SUCCESS"
backup_2_status = "FAILED"
backup_3_status = "SUCCESS"

if backup_1_status == "SUCCESS":
    successful_backups += 1
else:
    failed_backups += 1

if backup_2_status == "SUCCESS":
    successful_backups += 1
else:
    failed_backups += 1

if backup_3_status == "SUCCESS":
    successful_backups += 1
else:
    failed_backups += 1

print("Successful backups:", successful_backups)
print("Failed backups    :", failed_backups)


# ---------------------------------------------------------------------
# SECTION 11: Comparison Operators Revision
# ---------------------------------------------------------------------

print("\nSECTION 11: Comparison Operators Revision")

"""
Comparison operators return True or False.

==  equal to
!=  not equal to
>   greater than
<   less than
>=  greater than or equal to
<=  less than or equal to
"""

disk_usage = 87
threshold = 85

print("Disk usage:", disk_usage)
print("Threshold :", threshold)
print("Usage above threshold:", disk_usage > threshold)

if disk_usage > threshold:
    print("Action: Raise warning")
else:
    print("Action: Disk usage is acceptable")


# ---------------------------------------------------------------------
# SECTION 12: SLA Duration Check
# ---------------------------------------------------------------------

print("\nSECTION 12: SLA Duration Check")

allowed_minutes = 60
actual_minutes = 75

print("Allowed duration:", allowed_minutes, "minutes")
print("Actual duration :", actual_minutes, "minutes")

if actual_minutes > allowed_minutes:
    delay = actual_minutes - allowed_minutes
    print("Status          : SLA BREACHED")
    print("Delay           :", delay, "minutes")
else:
    print("Status          : Within SLA")


# ---------------------------------------------------------------------
# SECTION 13: Operator Precedence
# ---------------------------------------------------------------------

print("\nSECTION 13: Operator Precedence")

"""
Operator precedence means Python follows an order while calculating.

Example:
2 + 3 * 4 gives 14, not 20.
Multiplication happens before addition.

Use brackets when you want to make your intention clear.
"""

result_without_brackets = 2 + 3 * 4
result_with_brackets = (2 + 3) * 4

print("Without brackets:", result_without_brackets)
print("With brackets   :", result_with_brackets)


# ---------------------------------------------------------------------
# SECTION 14: Precedence in Real Calculation
# ---------------------------------------------------------------------

print("\nSECTION 14: Precedence in Real Calculation")

passed = 17
failed = 3
total = passed + failed

wrong_percent = passed + failed / total * 100
correct_percent = (passed / total) * 100

print("Passed checks         :", passed)
print("Failed checks         :", failed)
print("Total checks          :", total)
print("Wrong calculation     :", wrong_percent)
print("Correct pass percent  :", correct_percent)


# ---------------------------------------------------------------------
# SECTION 15: Practical Program 1 - Disk Usage Calculator
# ---------------------------------------------------------------------

print("\nSECTION 15: Practical Program 1 - Disk Usage Calculator")

total_disk = 250
used_disk = 211
free_disk = total_disk - used_disk
usage_percent = round((used_disk / total_disk) * 100, 2)

print("Total disk    :", total_disk, "GB")
print("Used disk     :", used_disk, "GB")
print("Free disk     :", free_disk, "GB")
print("Usage percent :", usage_percent, "%")

if usage_percent >= 90:
    print("Status        : CRITICAL")
elif usage_percent >= 80:
    print("Status        : WARNING")
else:
    print("Status        : OK")


# ---------------------------------------------------------------------
# SECTION 16: Practical Program 2 - Backup Duration Calculator
# ---------------------------------------------------------------------

print("\nSECTION 16: Practical Program 2 - Backup Duration Calculator")

start_hour = 1
end_hour = 4
backup_duration = end_hour - start_hour
allowed_duration = 2

print("Start hour      :", start_hour)
print("End hour        :", end_hour)
print("Backup duration :", backup_duration, "hours")

if backup_duration > allowed_duration:
    print("Status          : Needs review")
else:
    print("Status          : Normal")


# ---------------------------------------------------------------------
# SECTION 17: Practical Program 3 - Daily Check Pass Percentage
# ---------------------------------------------------------------------

print("\nSECTION 17: Practical Program 3 - Daily Check Pass Percentage")

passed_checks = 46
failed_checks = 4
total_checks = passed_checks + failed_checks
pass_percent = round((passed_checks / total_checks) * 100, 2)
fail_percent = round((failed_checks / total_checks) * 100, 2)

print("Passed checks:", passed_checks)
print("Failed checks:", failed_checks)
print("Total checks :", total_checks)
print("Pass percent :", pass_percent, "%")
print("Fail percent :", fail_percent, "%")


# ---------------------------------------------------------------------
# SECTION 18: Mini Project - Capacity Status Calculator
# ---------------------------------------------------------------------

print("\nSECTION 18: Mini Project - Capacity Status Calculator")

"""
This mini project calculates capacity status from used and total values.

Input:
- Resource name
- Used value
- Total value

Output:
- Free value
- Usage percentage
- Status

Today we use fixed values.
You can later convert this into an input-based tool.
"""

resource_name = "Disk /u01"
used_value = 428
total_value = 500
free_value = total_value - used_value
usage_percent = round((used_value / total_value) * 100, 2)

print("Capacity Status Report")
print("-" * 40)
print("Resource      :", resource_name)
print("Used          :", used_value, "GB")
print("Total         :", total_value, "GB")
print("Free          :", free_value, "GB")
print("Usage Percent :", usage_percent, "%")

if usage_percent >= 90:
    print("Status        : CRITICAL")
    print("Hint          : Immediate cleanup or capacity increase needed")
elif usage_percent >= 80:
    print("Status        : WARNING")
    print("Hint          : Monitor closely and plan cleanup")
else:
    print("Status        : OK")
    print("Hint          : Capacity is currently acceptable")


# ---------------------------------------------------------------------
# SECTION 19: Guided Practice - Interactive Capacity Calculator
# ---------------------------------------------------------------------

print("\nSECTION 19: Guided Practice - Interactive Capacity Calculator")

"""
Uncomment this block and run it.

Try these inputs:
1. Resource: Disk /data, Used: 780, Total: 1000
2. Resource: Memory, Used: 14, Total: 16
3. Resource: Backup Mount, Used: 450, Total: 500
"""

# resource_name = input("Enter resource name: ")
# used_value = float(input("Enter used value: "))
# total_value = float(input("Enter total value: "))
#
# free_value = total_value - used_value
# usage_percent = round((used_value / total_value) * 100, 2)
#
# print("\nCapacity Status Report")
# print("-" * 40)
# print("Resource      :", resource_name)
# print("Used          :", used_value)
# print("Total         :", total_value)
# print("Free          :", free_value)
# print("Usage Percent :", usage_percent, "%")
#
# if usage_percent >= 90:
#     print("Status        : CRITICAL")
# elif usage_percent >= 80:
#     print("Status        : WARNING")
# else:
#     print("Status        : OK")


# ---------------------------------------------------------------------
# SECTION 20: Common Beginner Mistakes
# ---------------------------------------------------------------------

print("\nSECTION 20: Common Beginner Mistakes")

"""
Mistake 1:
Forgetting that input() gives text.
If you use input for numbers, convert using int() or float().

Mistake 2:
Using / when you need a whole number.
Use // for floor division.

Mistake 3:
Forgetting brackets in percentage calculations.
Prefer:
(used / total) * 100

Mistake 4:
Dividing by zero.
If total value is zero, percentage calculation will fail.
We will handle such cases better when we learn exception handling.

Mistake 5:
Comparing text and numbers.
"90" and 90 are not the same type.
"""

print("Read the comments above carefully before building your own calculator.")


# ---------------------------------------------------------------------
# SECTION 21: Homework
# ---------------------------------------------------------------------

print("\nSECTION 21: Homework")

"""
Homework:
1. Complete Day06_Exercise.py
2. Build the Capacity Status Calculator from scratch
3. Test it with at least 5 resources
4. Try values that produce OK, WARNING, and CRITICAL
5. Share one practical calculation from your daily work with the community

Community Discussion Question:
What calculation do you perform repeatedly in your daily work?
Examples:
- disk usage percentage
- backup duration
- incident count
- SLA delay
- capacity growth
- report totals
"""

print("Day 6 completed. You can now calculate useful operational values.")
print("Next step: deeper conditions, so our calculations can drive smarter decisions.")
