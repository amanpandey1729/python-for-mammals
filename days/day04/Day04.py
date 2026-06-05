"""
Python for Mammals - Day 4
Topic: Strings

Audience:
- Complete beginners
- DBAs, Sysadmins, Support Engineers, Cloud Engineers, Monitoring Teams
- Anyone who wants Python for practical automation

Goal of Day 4:
By the end of today, you should be able to:
1. Create and print strings
2. Join strings using concatenation and f-strings
3. Find string length using len()
4. Access characters using indexing
5. Extract parts of text using slicing
6. Clean text using strip(), lower(), upper(), title(), and replace()
7. Search inside text using in, startswith(), and endswith()
8. Split useful information from log-like text

Why this matters:
Most automation work is text work.

Examples:
- Server names are text
- Log lines are text
- Backup statuses are text
- File names are text
- Email subjects are text
- Alert messages are text
- CSV rows are text before we process them

If you can control text, you can start controlling real operational data.
"""

print("=" * 70)
print("DAY 4 - STRINGS")
print("=" * 70)


# ---------------------------------------------------------------------
# SECTION 1: Quick Revision from Day 3
# ---------------------------------------------------------------------

print("\nSECTION 1: Quick Revision")

server_name = "app-server-01"
disk_usage = 82

if disk_usage >= 90:
    status = "CRITICAL"
elif disk_usage >= 75:
    status = "WARNING"
else:
    status = "HEALTHY"

print(f"Server {server_name} disk usage is {disk_usage}%. Status: {status}")


# ---------------------------------------------------------------------
# SECTION 2: What is a String?
# ---------------------------------------------------------------------

print("\nSECTION 2: What is a String?")

"""
A string is text inside quotes.

You can use:
- Double quotes: "text"
- Single quotes: 'text'

In automation, strings are everywhere:
- "SUCCESS"
- "FAILED"
- "server-01"
- "backup_2026_06_04.log"
- "ERROR: connection timeout"
"""

message = "Backup completed successfully"
server = 'linux-prod-01'

print(message)
print(server)
print("Type of message:", type(message))


# ---------------------------------------------------------------------
# SECTION 3: Single Quotes, Double Quotes, and Apostrophes
# ---------------------------------------------------------------------

print("\nSECTION 3: Single Quotes and Double Quotes")

"""
Both single and double quotes create strings.

Use double quotes when the text contains an apostrophe.
Use single quotes when the text contains double quotes.
"""

line_1 = "Server's backup completed"
line_2 = 'Status says "SUCCESS"'

print(line_1)
print(line_2)


# ---------------------------------------------------------------------
# SECTION 4: Multi-line Strings
# ---------------------------------------------------------------------

print("\nSECTION 4: Multi-line Strings")

"""
Triple quotes can store text across multiple lines.
This is useful for templates, notes, long messages, and reports.
"""

report = """
Daily Summary
-------------
Server : app-server-01
Status : Healthy
Action : No action required
"""

print(report)


# ---------------------------------------------------------------------
# SECTION 5: Joining Strings
# ---------------------------------------------------------------------

print("\nSECTION 5: Joining Strings")

"""
Joining strings is called concatenation.
Use + to join text.

Important:
You can join string + string.
You cannot directly join string + number.
"""

first_name = "Python"
last_name = "Mammal"
full_name = first_name + " " + last_name

print(full_name)

server_name = "db-server-01"
status = "UP"
message = "Server " + server_name + " is " + status
print(message)


# ---------------------------------------------------------------------
# SECTION 6: Converting Numbers to Strings
# ---------------------------------------------------------------------

print("\nSECTION 6: Converting Numbers to Strings")

"""
If you want to join text and number using +,
convert the number using str().

But in most report-style output, f-strings are cleaner.
"""

disk_usage = 86

print("Disk usage is " + str(disk_usage) + "%")
print(f"Disk usage is {disk_usage}%")


# ---------------------------------------------------------------------
# SECTION 7: len() - Finding Text Length
# ---------------------------------------------------------------------

print("\nSECTION 7: len()")

"""
len() returns the number of characters in a string.

Automation use cases:
- Check if a username is empty
- Check if a ticket ID has expected length
- Validate if a server naming standard looks correct
"""

username = "oracle_admin"
ticket_id = "INC1234567"

print("Username:", username)
print("Username length:", len(username))
print("Ticket ID length:", len(ticket_id))


# ---------------------------------------------------------------------
# SECTION 8: Indexing - Reading One Character
# ---------------------------------------------------------------------

print("\nSECTION 8: String Indexing")

"""
Every character in a string has a position.
Python positions start from 0, not 1.

Example:
Text:  P y t h o n
Index: 0 1 2 3 4 5
"""

word = "Python"

print("Word:", word)
print("First character:", word[0])
print("Second character:", word[1])
print("Last character:", word[-1])


# ---------------------------------------------------------------------
# SECTION 9: Slicing - Extracting Part of Text
# ---------------------------------------------------------------------

print("\nSECTION 9: String Slicing")

"""
Slicing extracts part of a string.

Syntax:
text[start:end]

Important:
The start position is included.
The end position is not included.
"""

server_name = "prod-db-server-01"

environment = server_name[0:4]
server_type = server_name[5:7]

print("Server name:", server_name)
print("Environment:", environment)
print("Server type:", server_type)
print("First 4 characters:", server_name[:4])
print("Last 2 characters:", server_name[-2:])


# ---------------------------------------------------------------------
# SECTION 10: Changing Case
# ---------------------------------------------------------------------

print("\nSECTION 10: Changing Case")

"""
String case methods help normalize input.

Common methods:
lower() -> converts to lowercase
upper() -> converts to uppercase
title() -> first letter of each word uppercase

Why useful?
User may type success, SUCCESS, Success, or SuCcEsS.
We can normalize it before comparison.
"""

backup_status = "success"
server_owner = "platform operations team"

print("Original status:", backup_status)
print("Uppercase status:", backup_status.upper())
print("Owner title case:", server_owner.title())

if backup_status.upper() == "SUCCESS":
    print("Backup status matched successfully.")


# ---------------------------------------------------------------------
# SECTION 11: strip() - Removing Extra Spaces
# ---------------------------------------------------------------------

print("\nSECTION 11: strip()")

"""
strip() removes extra spaces from the beginning and end of text.

This is very important when reading:
- User input
- CSV values
- Log fields
- Copy-pasted values
"""

raw_server_name = "   app-server-01   "
clean_server_name = raw_server_name.strip()

print("Before strip:", repr(raw_server_name))
print("After strip :", repr(clean_server_name))


# ---------------------------------------------------------------------
# SECTION 12: replace() - Replacing Text
# ---------------------------------------------------------------------

print("\nSECTION 12: replace()")

"""
replace() replaces one piece of text with another.

Automation use cases:
- Normalize alert names
- Clean file names
- Replace spaces with underscores
- Remove unwanted characters
"""

alert_name = "Disk Usage High"
file_name = alert_name.replace(" ", "_").lower()

print("Alert name:", alert_name)
print("File-friendly name:", file_name)

message = "ERROR: database connection failed"
clean_message = message.replace("ERROR:", "")

print("Original message:", message)
print("Clean message:", clean_message.strip())


# ---------------------------------------------------------------------
# SECTION 13: Checking if Text Exists
# ---------------------------------------------------------------------

print("\nSECTION 13: Checking if Text Exists")

"""
Use 'in' to check whether some text exists inside another string.

This is one of the most useful ideas for log analysis.
"""

log_line = "2026-06-04 10:15:22 ERROR backup failed for server app-01"

print("Log line:", log_line)
print("Does log contain ERROR?", "ERROR" in log_line)
print("Does log contain SUCCESS?", "SUCCESS" in log_line)

if "ERROR" in log_line:
    print("Action: Investigate the log line.")


# ---------------------------------------------------------------------
# SECTION 14: startswith() and endswith()
# ---------------------------------------------------------------------

print("\nSECTION 14: startswith() and endswith()")

"""
startswith() checks the beginning of text.
endswith() checks the end of text.

Automation use cases:
- Check if file starts with backup_
- Check if file ends with .log, .csv, or .txt
- Identify naming standards
"""

file_name = "backup_prod_20260604.log"

print("File name:", file_name)
print("Starts with backup_:", file_name.startswith("backup_"))
print("Ends with .log:", file_name.endswith(".log"))

if file_name.startswith("backup_") and file_name.endswith(".log"):
    print("This looks like a backup log file.")


# ---------------------------------------------------------------------
# SECTION 15: split() - Breaking Text into Pieces
# ---------------------------------------------------------------------

print("\nSECTION 15: split()")

"""
split() breaks a string into multiple parts.

By default, it splits on spaces.
You can also split by comma, pipe, colon, or any separator.

This is very useful for reports, logs, and CSV-like data.
"""

line = "app-server-01 CPU 86 WARNING"
parts = line.split()

print("Original line:", line)
print("Split parts:", parts)
print("Server:", parts[0])
print("Metric:", parts[1])
print("Value:", parts[2])
print("Status:", parts[3])

csv_line = "db-server-01,CPU,91,CRITICAL"
csv_parts = csv_line.split(",")

print("CSV line:", csv_line)
print("CSV parts:", csv_parts)


# ---------------------------------------------------------------------
# SECTION 16: Practical Program 1 - Clean User Input
# ---------------------------------------------------------------------

print("\nSECTION 16: Practical Program 1 - Clean User Input")

raw_status = "  success  "
clean_status = raw_status.strip().upper()

print("Raw status:", repr(raw_status))
print("Clean status:", clean_status)

if clean_status == "SUCCESS":
    print("Result: Backup completed successfully.")
else:
    print("Result: Backup needs investigation.")


# ---------------------------------------------------------------------
# SECTION 17: Practical Program 2 - Log Line Classifier
# ---------------------------------------------------------------------

print("\nSECTION 17: Practical Program 2 - Log Line Classifier")

log_line = "2026-06-04 11:20:15 WARNING disk usage reached 82 percent"

print("Log line:", log_line)

if "ERROR" in log_line:
    print("Severity: ERROR")
elif "WARNING" in log_line:
    print("Severity: WARNING")
elif "SUCCESS" in log_line:
    print("Severity: SUCCESS")
else:
    print("Severity: UNKNOWN")


# ---------------------------------------------------------------------
# SECTION 18: Practical Program 3 - File Name Validator
# ---------------------------------------------------------------------

print("\nSECTION 18: Practical Program 3 - File Name Validator")

file_name = "daily_report_20260604.csv"

print("File name:", file_name)

if file_name.startswith("daily_report_") and file_name.endswith(".csv"):
    print("Valid report file name.")
else:
    print("Invalid report file name.")


# ---------------------------------------------------------------------
# SECTION 19: Guided Practice - Interactive Text Cleaner
# ---------------------------------------------------------------------

print("\nSECTION 19: Guided Practice - Interactive Text Cleaner")

"""
Uncomment this block and run it.

This small program asks for a raw alert message,
cleans extra spaces, converts it to uppercase, and checks severity.
"""

# raw_alert = input("Enter alert message: ")
# clean_alert = raw_alert.strip()
# normalized_alert = clean_alert.upper()
#
# print("\nClean Alert Report")
# print("-" * 40)
# print(f"Original   : {raw_alert}")
# print(f"Cleaned    : {clean_alert}")
# print(f"Normalized : {normalized_alert}")
#
# if "ERROR" in normalized_alert or "FAILED" in normalized_alert:
#     print("Severity   : CRITICAL")
# elif "WARNING" in normalized_alert:
#     print("Severity   : WARNING")
# elif "SUCCESS" in normalized_alert:
#     print("Severity   : OK")
# else:
#     print("Severity   : UNKNOWN")


# ---------------------------------------------------------------------
# SECTION 20: Common Beginner Mistakes
# ---------------------------------------------------------------------

print("\nSECTION 20: Common Beginner Mistakes")

"""
Mistake 1:
Forgetting that indexing starts at 0.

text = "Python"
text[0] gives P, not y.

Mistake 2:
Using a string method without parentheses.

Wrong:
status.upper

Correct:
status.upper()

Mistake 3:
Expecting string methods to change the original string automatically.

Wrong:
name = "  Aman  "
name.strip()
print(name)      # still has spaces

Correct:
name = name.strip()
print(name)

Mistake 4:
Case-sensitive search.

"error" in "ERROR found" is False.
Normalize first using upper() or lower().
"""

print("Read the comments above carefully. These string mistakes are common.")


# ---------------------------------------------------------------------
# SECTION 21: Mini Challenge
# ---------------------------------------------------------------------

print("\nSECTION 21: Mini Challenge")

"""
Mini Challenge:
Create an interactive script that asks for:

1. Server name
2. Raw backup status
3. Raw log line
4. File name

Then:
- Clean server name using strip()
- Normalize backup status using strip().upper()
- Check if log line contains ERROR, WARNING, SUCCESS, or FAILED
- Check if file name ends with .log or .csv
- Print a clean summary using f-strings

Final decision:
- If backup status is FAILED or log contains ERROR/FAILED, print CRITICAL
- Else if log contains WARNING, print WARNING
- Else if backup status is SUCCESS, print OK
- Else print UNKNOWN
"""

print("Mini Challenge is described in comments above.")


# ---------------------------------------------------------------------
# SECTION 22: Day 4 Summary
# ---------------------------------------------------------------------

print("\nSECTION 22: Day 4 Summary")

"""
Today you learned:
- What strings are
- Single, double, and triple quoted strings
- String concatenation
- str() conversion
- len()
- Indexing
- Slicing
- lower(), upper(), title()
- strip()
- replace()
- in
- startswith() and endswith()
- split()
- Cleaning and classifying text

Why this matters:
Automation is mostly about reading, cleaning, checking, and reporting text.
Once you understand strings, logs and reports become less scary.
"""

print("Great work! Day 4 complete. Strings are the foundation of log analysis and report automation.")
