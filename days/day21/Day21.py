"""
Python for Mammals - Day 21
Topic: Exception Handling

Audience:
- Complete beginners
- DBAs, Sysadmins, Support Engineers, Cloud Engineers, Monitoring Teams
- Anyone who wants Python for practical automation

Goal of Day 21:
By the end of today, you should be able to:
1. Use try to protect risky code
2. Use except to handle common errors gracefully
3. Use else when code succeeds without an exception
4. Use finally for cleanup-style actions
5. Recognize common errors such as ValueError, ZeroDivisionError, FileNotFoundError, and KeyError
6. Build automation scripts that fail safely instead of crashing suddenly

Why this matters:
Real automation rarely runs in perfect conditions.

Your script may face:
- missing files
- wrong user input
- blank values
- invalid numbers
- unavailable reports
- unexpected dictionary keys
- division by zero in calculations
- failed file operations

Exception handling helps your script respond clearly instead of stopping with a scary error message.
Today you learn how to make automation safer and more professional.
"""

print("=" * 70)
print("DAY 21 - EXCEPTION HANDLING")
print("try, except, else, finally, common errors")
print("=" * 70)

# ---------------------------------------------------------------------
# SECTION 1: Project Introduction
# ---------------------------------------------------------------------

print("\nSECTION 1: Project Introduction")

"""
So far, most examples assumed that everything works correctly.
But real operational scripts face imperfect input and imperfect environments.

Exception handling allows your script to continue gracefully or show a useful
message when something goes wrong.
"""

print("Today we will learn how to handle errors safely in automation scripts.")

# ---------------------------------------------------------------------
# SECTION 2: What Happens Without Exception Handling
# ---------------------------------------------------------------------

print("\nSECTION 2: What Happens Without Exception Handling")

"""
The code below would fail if uncommented because the value is not a number.

bad_number = int("abc")

Python would raise ValueError and stop the script.
In automation, one bad value should not always break the entire workflow.
"""

print("Without exception handling, one bad input can stop the script.")

# ---------------------------------------------------------------------
# SECTION 3: Basic try and except
# ---------------------------------------------------------------------

print("\nSECTION 3: Basic try and except")

try:
    disk_used_gb = int("390")
    print("Disk used GB:", disk_used_gb)
except ValueError:
    print("Invalid number received for disk usage.")

"""
try contains code that may fail.
except contains the response if that specific error happens.

Here, int("390") succeeds, so the except block does not run.
"""

# ---------------------------------------------------------------------
# SECTION 4: Handling ValueError
# ---------------------------------------------------------------------

print("\nSECTION 4: Handling ValueError")

raw_input_value = "eighty"

try:
    cpu_usage = int(raw_input_value)
    print("CPU Usage:", cpu_usage)
except ValueError:
    print("CPU usage must be a number. Received:", raw_input_value)

"""
ValueError commonly appears when converting text to numbers.

Examples:
int("abc")
float("high")

This is very common when scripts collect user input or read text files.
"""

# ---------------------------------------------------------------------
# SECTION 5: Handling ZeroDivisionError
# ---------------------------------------------------------------------

print("\nSECTION 5: Handling ZeroDivisionError")

disk_total_gb = 0
disk_used_gb = 50

try:
    usage_percent = (disk_used_gb / disk_total_gb) * 100
    print("Usage %:", usage_percent)
except ZeroDivisionError:
    print("Disk total cannot be zero. Usage percentage not calculated.")

"""
ZeroDivisionError happens when a number is divided by zero.

In reporting scripts, this may happen when total size, total rows, or total
checks are accidentally provided as 0.
"""

# ---------------------------------------------------------------------
# SECTION 6: Handling FileNotFoundError
# ---------------------------------------------------------------------

print("\nSECTION 6: Handling FileNotFoundError")

try:
    with open("missing_day21_report.txt", "r") as file_object:
        content = file_object.read()
    print(content)
except FileNotFoundError:
    print("Report file not found. Please verify the file name or path.")

"""
FileNotFoundError is common in file automation.

It can happen when:
- the file name is wrong
- the file is not yet generated
- the script is running from a different folder
- a report was deleted or moved
"""

# ---------------------------------------------------------------------
# SECTION 7: Handling KeyError
# ---------------------------------------------------------------------

print("\nSECTION 7: Handling KeyError")

server = {
    "name": "db01",
    "environment": "production",
    "status": "running"
}

try:
    owner = server["owner"]
    print("Owner:", owner)
except KeyError:
    print("Owner key is missing from the server dictionary.")

"""
KeyError happens when a dictionary key does not exist.

This is useful to understand because inventories and configuration data are
often stored as dictionaries.
"""

# ---------------------------------------------------------------------
# SECTION 8: Multiple except Blocks
# ---------------------------------------------------------------------

print("\nSECTION 8: Multiple except Blocks")

raw_total = "500"
raw_used = "390"

try:
    total_gb = int(raw_total)
    used_gb = int(raw_used)
    usage_percent = (used_gb / total_gb) * 100
    print("Disk Usage %:", round(usage_percent, 2))
except ValueError:
    print("Total GB and Used GB must be valid numbers.")
except ZeroDivisionError:
    print("Total GB cannot be zero.")

"""
One try block can have multiple except blocks.
This helps your script respond differently for different problems.
"""

# ---------------------------------------------------------------------
# SECTION 9: else Block
# ---------------------------------------------------------------------

print("\nSECTION 9: else Block")

raw_memory_percent = "72"

try:
    memory_percent = int(raw_memory_percent)
except ValueError:
    print("Memory percentage must be numeric.")
else:
    print("Memory percentage accepted:", memory_percent)

"""
else runs only when no exception happens inside try.

Use else for success actions that should happen only after risky code succeeds.
"""

# ---------------------------------------------------------------------
# SECTION 10: finally Block
# ---------------------------------------------------------------------

print("\nSECTION 10: finally Block")

try:
    check_name = "backup validation"
    print("Running check:", check_name)
except Exception:
    print("Something went wrong during the check.")
finally:
    print("Check attempt completed.")

"""
finally runs whether the try block succeeds or fails.

It is commonly used for cleanup actions, final messages, or closing resources.
When using with open(), Python already handles file closing safely.
"""

# ---------------------------------------------------------------------
# SECTION 11: Avoid Catching Everything Too Early
# ---------------------------------------------------------------------

print("\nSECTION 11: Avoid Catching Everything Too Early")

"""
You may see this pattern:

try:
    risky_code
except Exception:
    print("Something failed")

This can be useful sometimes, but beginners should first learn specific errors.
Specific errors make troubleshooting easier.
"""

print("Prefer specific errors like ValueError or FileNotFoundError when possible.")

# ---------------------------------------------------------------------
# SECTION 12: Exception Handling in a Small Report Workflow
# ---------------------------------------------------------------------

print("\nSECTION 12: Exception Handling in a Small Report Workflow")

raw_total_checks = "5"
raw_failed_checks = "1"

try:
    total_checks = int(raw_total_checks)
    failed_checks = int(raw_failed_checks)
    success_percent = ((total_checks - failed_checks) / total_checks) * 100
except ValueError:
    print("Check counts must be numeric.")
except ZeroDivisionError:
    print("Total checks cannot be zero.")
else:
    print("Total checks  :", total_checks)
    print("Failed checks :", failed_checks)
    print("Success %     :", round(success_percent, 2))
finally:
    print("Report workflow finished.")

"""
This combines try, except, else, and finally in one practical workflow.
"""

# ---------------------------------------------------------------------
# SECTION 13: Guided Practice - Safe Number Conversion
# ---------------------------------------------------------------------

print("\nSECTION 13: Guided Practice - Safe Number Conversion")

"""
Uncomment this block and run it.
Try values like 90, abc, and blank input.
"""

# raw_value = input("Enter disk usage percentage: ")
#
# try:
#     disk_usage = float(raw_value)
# except ValueError:
#     print("Please enter a valid number.")
# else:
#     print("Disk usage accepted:", disk_usage)

print("Guided practice: uncomment the safe number conversion block.")

# ---------------------------------------------------------------------
# SECTION 14: Guided Practice - Safe File Reading
# ---------------------------------------------------------------------

print("\nSECTION 14: Guided Practice - Safe File Reading")

"""
Uncomment this block and run it.
Try an existing and a non-existing file name.
"""

# file_name = input("Enter file name to read: ")
#
# try:
#     with open(file_name, "r") as file_object:
#         content = file_object.read()
# except FileNotFoundError:
#     print("File not found:", file_name)
# else:
#     print(content)

print("Guided practice: uncomment the safe file reading block.")

# ---------------------------------------------------------------------
# SECTION 15: Guided Practice - Safe Dictionary Access
# ---------------------------------------------------------------------

print("\nSECTION 15: Guided Practice - Safe Dictionary Access")

"""
Uncomment this block and run it.
It catches a missing key in a dictionary.
"""

# service = {"name": "listener", "status": "running"}
#
# try:
#     print("Port:", service["port"])
# except KeyError:
#     print("Port information is missing from service data.")

print("Guided practice: uncomment the safe dictionary access block.")

# ---------------------------------------------------------------------
# SECTION 16: Mini Challenge Preview
# ---------------------------------------------------------------------

print("\nSECTION 16: Mini Challenge Preview")

"""
Mini Challenge:
Build a Safe Disk Usage Reporter.

Your script should:
1. Collect server name, environment, disk total, and disk used once
2. Convert disk total and disk used safely using try and except
3. Handle invalid numbers using ValueError
4. Handle zero total size using ZeroDivisionError
5. Use else to generate the report only after calculation succeeds
6. Use finally to print a final workflow completion message

This mirrors real automation:
- collect input
- protect risky conversions
- protect risky calculations
- report clear errors
- continue professionally
"""

print("Mini challenge: build a Safe Disk Usage Reporter using exception handling.")

# ---------------------------------------------------------------------
# SECTION 17: Closing Message
# ---------------------------------------------------------------------

print("\nSECTION 17: Closing Message")

print("You have completed Day 21.")
print("You can now handle common errors without letting scripts crash suddenly.")
print("Next, you will keep making automation scripts safer, cleaner, and more professional.")
