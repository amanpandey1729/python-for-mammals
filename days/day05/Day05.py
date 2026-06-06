"""
Python for Mammals - Day 5
Topic: String Practice for Operational Text

Audience:
- Complete beginners
- DBAs, Sysadmins, Support Engineers, Cloud Engineers, Monitoring Teams
- Anyone who wants Python for practical automation

Goal of Day 5:
By the end of today, you should be able to:
1. Clean messy log messages
2. Search alert text for important keywords
3. Extract useful parts from email-like text
4. Manipulate file names safely
5. Detect ORA errors from text
6. Build a mini ORA Error Extractor

Why this matters:
Most real automation starts with messy text.

Examples:
- A monitoring alert arrives as text
- A backup email has a subject and body
- A log line contains SUCCESS, FAILED, WARNING, ORA-, or timeout
- A file name contains environment, date, and extension
- A ticket update contains useful words hidden inside a long message

Day 4 taught string basics.
Day 5 is where we start using strings like operations professionals.
"""

print("=" * 70)
print("DAY 5 - STRING PRACTICE FOR OPERATIONAL TEXT")
print("=" * 70)


# ---------------------------------------------------------------------
# SECTION 1: Quick Revision from Day 4
# ---------------------------------------------------------------------

print("\nSECTION 1: Quick Revision")

raw_status = "  success  "
clean_status = raw_status.strip().upper()

print("Raw status  :", repr(raw_status))
print("Clean status:", clean_status)

if clean_status == "SUCCESS":
    print("Result      : Backup completed successfully")
else:
    print("Result      : Backup needs investigation")


# ---------------------------------------------------------------------
# SECTION 2: Why More String Practice?
# ---------------------------------------------------------------------

print("\nSECTION 2: Why More String Practice?")

"""
In real work, text is rarely clean.

You may receive:
- " ora-00600 internal error "
- "Backup FAILED on db-server-01"
- "Subject: Disk usage warning on linux-prod-01"
- "daily report final.csv"
- "ALERT: connection timeout from app node"

Before automation can make decisions, we need to clean and inspect text.
"""

alert_text = "  Backup FAILED on db-server-01  "
clean_alert = alert_text.strip()
normalized_alert = clean_alert.upper()

print("Original alert:", repr(alert_text))
print("Clean alert   :", clean_alert)
print("Normalized    :", normalized_alert)


# ---------------------------------------------------------------------
# SECTION 3: Log Messages - Searching for Severity
# ---------------------------------------------------------------------

print("\nSECTION 3: Log Messages - Searching for Severity")

"""
A log line is usually one long string.
Our first job is to search for important words.

Common useful keywords:
- ERROR
- FAILED
- WARNING
- SUCCESS
- TIMEOUT
- ORA-
"""

log_line = "2026-06-05 10:15:21 ERROR connection timeout for app-server-01"
normalized_log = log_line.upper()

print("Log line:", log_line)

if "ERROR" in normalized_log or "FAILED" in normalized_log or "TIMEOUT" in normalized_log:
    print("Severity: CRITICAL")
elif "WARNING" in normalized_log:
    print("Severity: WARNING")
elif "SUCCESS" in normalized_log:
    print("Severity: OK")
else:
    print("Severity: UNKNOWN")


# ---------------------------------------------------------------------
# SECTION 4: Alert Text - Cleaning and Classification
# ---------------------------------------------------------------------

print("\nSECTION 4: Alert Text - Cleaning and Classification")

raw_alert = "   warning: disk usage reached 82 percent on linux-prod-01   "
clean_alert = raw_alert.strip()
normalized_alert = clean_alert.upper()

print("Clean alert:", clean_alert)

if "ERROR" in normalized_alert or "FAILED" in normalized_alert:
    alert_status = "CRITICAL"
elif "WARNING" in normalized_alert:
    alert_status = "WARNING"
elif "SUCCESS" in normalized_alert:
    alert_status = "OK"
else:
    alert_status = "UNKNOWN"

print("Alert status:", alert_status)


# ---------------------------------------------------------------------
# SECTION 5: Checking Multiple Keywords Without Loops Yet
# ---------------------------------------------------------------------

print("\nSECTION 5: Checking Multiple Keywords Without Loops Yet")

"""
We have not formally learned loops yet.
So for now, we can check multiple keywords using or.

This is not the final professional way, but it is beginner-friendly
and enough for today's mini project.
"""

message = "Application job failed due to timeout"
message_upper = message.upper()

has_problem = "ERROR" in message_upper or "FAILED" in message_upper or "TIMEOUT" in message_upper

print("Message:", message)
print("Problem keyword found:", has_problem)

if has_problem:
    print("Action: Check application or server logs")
else:
    print("Action: No immediate problem keyword found")


# ---------------------------------------------------------------------
# SECTION 6: Email Subject Parsing
# ---------------------------------------------------------------------

print("\nSECTION 6: Email Subject Parsing")

"""
Many operational alerts arrive through email.
Even without reading a mailbox yet, we can practice parsing email-like text.
"""

subject = "Subject: CRITICAL - Backup failed on db-server-01"
subject_clean = subject.replace("Subject:", "").strip()
subject_upper = subject_clean.upper()

print("Original subject:", subject)
print("Clean subject   :", subject_clean)

if subject_upper.startswith("CRITICAL"):
    print("Email priority  : High")
elif subject_upper.startswith("WARNING"):
    print("Email priority  : Medium")
else:
    print("Email priority  : Normal")


# ---------------------------------------------------------------------
# SECTION 7: Extracting Basic Details from Email Text
# ---------------------------------------------------------------------

print("\nSECTION 7: Extracting Basic Details from Email Text")

email_line = "From: monitoring@company.com | Subject: ORA-01555 on prod-db-01"
parts = email_line.split("|")

from_part = parts[0].replace("From:", "").strip()
subject_part = parts[1].replace("Subject:", "").strip()

print("Email line:", email_line)
print("Sender    :", from_part)
print("Subject   :", subject_part)


# ---------------------------------------------------------------------
# SECTION 8: File Name Manipulation
# ---------------------------------------------------------------------

print("\nSECTION 8: File Name Manipulation")

"""
File names often contain useful information.
Example:
backup_prod_db01_20260605.log

We can check prefix, extension, and extract parts.
"""

file_name = "backup_prod_db01_20260605.log"
file_lower = file_name.lower()

print("File name:", file_name)
print("Starts with backup_:", file_lower.startswith("backup_"))
print("Ends with .log     :", file_lower.endswith(".log"))

file_without_extension = file_name.replace(".log", "")
file_parts = file_without_extension.split("_")

print("File parts:", file_parts)
print("Environment:", file_parts[1])
print("Server     :", file_parts[2])
print("Date       :", file_parts[3])


# ---------------------------------------------------------------------
# SECTION 9: Creating Safe File Names
# ---------------------------------------------------------------------

print("\nSECTION 9: Creating Safe File Names")

"""
Report titles may contain spaces and mixed case.
For automation, file names are easier when they are lowercase and use underscores.
"""

report_title = " Daily ORA Error Summary "
clean_title = report_title.strip().lower().replace(" ", "_")
report_file = clean_title + ".txt"

print("Report title:", repr(report_title))
print("Safe file   :", report_file)


# ---------------------------------------------------------------------
# SECTION 10: ORA Error Basics
# ---------------------------------------------------------------------

print("\nSECTION 10: ORA Error Basics")

"""
Oracle errors commonly start with ORA-.
Examples:
- ORA-00060 deadlock detected
- ORA-01555 snapshot too old
- ORA-00600 internal error code

Today we will detect simple ORA errors using string methods.
Regular expressions will come later.
"""

oracle_log = "2026-06-05 12:10:33 ORA-01555 snapshot too old during report run"
log_upper = oracle_log.upper()

print("Oracle log:", oracle_log)
print("Contains ORA error:", "ORA-" in log_upper)

if "ORA-" in log_upper:
    ora_position = log_upper.find("ORA-")
    ora_text = oracle_log[ora_position:]
    print("ORA detail:", ora_text)


# ---------------------------------------------------------------------
# SECTION 11: find() - Locating Text Position
# ---------------------------------------------------------------------

print("\nSECTION 11: find() - Locating Text Position")

"""
find() returns the position where text is found.
If text is not found, it returns -1.

This helps when we want to extract text after a known keyword.
"""

line = "Alert raised: ORA-00060 deadlock detected while updating order table"
position = line.find("ORA-")

print("Line:", line)
print("ORA starts at position:", position)

if position != -1:
    print("Extracted error:", line[position:])
else:
    print("No ORA error found")


# ---------------------------------------------------------------------
# SECTION 12: Extracting ORA Code Using Slicing
# ---------------------------------------------------------------------

print("\nSECTION 12: Extracting ORA Code Using Slicing")

"""
An ORA code is usually 9 characters long:
ORA-01555
ORA-00060
ORA-00600

If we know where ORA- starts, we can slice 9 characters.
"""

line = "Job failed with ORA-00060 deadlock detected"
position = line.find("ORA-")

if position != -1:
    ora_code = line[position:position + 9]
    print("Line    :", line)
    print("ORA code:", ora_code)
else:
    print("No ORA code found")


# ---------------------------------------------------------------------
# SECTION 13: Extracting Message After ORA Code
# ---------------------------------------------------------------------

print("\nSECTION 13: Extracting Message After ORA Code")

line = "Job failed with ORA-01555 snapshot too old during reporting"
position = line.find("ORA-")

if position != -1:
    ora_code = line[position:position + 9]
    ora_message = line[position + 10:]
    print("ORA code   :", ora_code)
    print("ORA message:", ora_message)
else:
    print("No ORA error found")


# ---------------------------------------------------------------------
# SECTION 14: Practical Program 1 - Alert Keyword Scanner
# ---------------------------------------------------------------------

print("\nSECTION 14: Practical Program 1 - Alert Keyword Scanner")

alert = "Connection timeout detected from app node"
alert_upper = alert.upper()

print("Alert:", alert)

if "TIMEOUT" in alert_upper:
    print("Finding : Timeout issue found")
    print("Action  : Check network, listener, or service availability")
elif "FAILED" in alert_upper or "ERROR" in alert_upper:
    print("Finding : Failure keyword found")
    print("Action  : Investigate immediately")
else:
    print("Finding : No critical keyword found")


# ---------------------------------------------------------------------
# SECTION 15: Practical Program 2 - Email Alert Cleaner
# ---------------------------------------------------------------------

print("\nSECTION 15: Practical Program 2 - Email Alert Cleaner")

email_subject = "  Subject: WARNING - Disk usage high on linux-prod-01  "
clean_subject = email_subject.strip().replace("Subject:", "").strip()
subject_upper = clean_subject.upper()

print("Clean subject:", clean_subject)

if "CRITICAL" in subject_upper or "FAILED" in subject_upper or "ERROR" in subject_upper:
    print("Priority     : High")
elif "WARNING" in subject_upper:
    print("Priority     : Medium")
else:
    print("Priority     : Normal")


# ---------------------------------------------------------------------
# SECTION 16: Practical Program 3 - Report File Name Builder
# ---------------------------------------------------------------------

print("\nSECTION 16: Practical Program 3 - Report File Name Builder")

environment = "PROD"
report_name = "Daily Alert Summary"
report_date = "20260605"

safe_report_name = report_name.strip().lower().replace(" ", "_")
file_name = environment.lower() + "_" + safe_report_name + "_" + report_date + ".txt"

print("Environment:", environment)
print("Report name:", report_name)
print("File name  :", file_name)


# ---------------------------------------------------------------------
# SECTION 17: Mini Project - ORA Error Extractor
# ---------------------------------------------------------------------

print("\nSECTION 17: Mini Project - ORA Error Extractor")

"""
This is a small but useful automation idea.

Input:
A log line or alert text.

Output:
- Whether an ORA error exists
- ORA code
- Error message after the code
- Suggested severity

For now, we handle one line at a time.
When we learn loops and file handling, we will scan full log files.
"""

log_line = "2026-06-05 15:30:44 Job failed with ORA-00060 deadlock detected while updating records"
clean_log = log_line.strip()
upper_log = clean_log.upper()
ora_position = upper_log.find("ORA-")

print("Input log:", clean_log)

if ora_position != -1:
    ora_code = clean_log[ora_position:ora_position + 9]
    ora_message = clean_log[ora_position + 10:]

    print("ORA Found  : Yes")
    print("ORA Code   :", ora_code)
    print("Message    :", ora_message)

    if ora_code == "ORA-00060":
        print("Severity   : CRITICAL")
        print("Hint       : Possible deadlock. Check trace file and involved sessions.")
    elif ora_code == "ORA-01555":
        print("Severity   : WARNING")
        print("Hint       : Snapshot too old. Check undo, query duration, and retention.")
    elif ora_code == "ORA-00600":
        print("Severity   : CRITICAL")
        print("Hint       : Internal error. Collect details and validate with support process.")
    else:
        print("Severity   : UNKNOWN")
        print("Hint       : ORA error found. Check documentation/runbook for next action.")
else:
    print("ORA Found  : No")
    print("Severity   : UNKNOWN")
    print("Hint       : No ORA pattern found in this line.")


# ---------------------------------------------------------------------
# SECTION 18: Guided Practice - Interactive ORA Extractor
# ---------------------------------------------------------------------

print("\nSECTION 18: Guided Practice - Interactive ORA Extractor")

"""
Uncomment this block and run it.

Try these inputs:
1. ORA-00060 deadlock detected
2. backup completed successfully
3. Job failed with ORA-01555 snapshot too old
4. internal error ORA-00600 detected in trace
"""

# raw_line = input("Enter one log line or alert message: ")
# clean_line = raw_line.strip()
# upper_line = clean_line.upper()
# ora_position = upper_line.find("ORA-")
#
# print("\nORA Error Extractor Report")
# print("-" * 40)
# print("Input Line:", clean_line)
#
# if ora_position != -1:
#     ora_code = clean_line[ora_position:ora_position + 9]
#     ora_message = clean_line[ora_position + 10:]
#
#     print("ORA Found : Yes")
#     print("ORA Code  :", ora_code)
#     print("Message   :", ora_message)
#
#     if ora_code == "ORA-00060":
#         print("Severity  : CRITICAL")
#         print("Hint      : Possible deadlock")
#     elif ora_code == "ORA-01555":
#         print("Severity  : WARNING")
#         print("Hint      : Possible undo/snapshot issue")
#     elif ora_code == "ORA-00600":
#         print("Severity  : CRITICAL")
#         print("Hint      : Internal error needs careful investigation")
#     else:
#         print("Severity  : UNKNOWN")
#         print("Hint      : ORA error found. Check runbook/documentation")
# else:
#     print("ORA Found : No")
#     print("Severity  : UNKNOWN")


# ---------------------------------------------------------------------
# SECTION 19: Common Beginner Mistakes
# ---------------------------------------------------------------------

print("\nSECTION 19: Common Beginner Mistakes")

"""
Mistake 1:
Searching without normalizing case.

Example:
"ora-01555" will not match "ORA-" unless you use upper().

Mistake 2:
Using replace() but forgetting to store the result.

Wrong:
text.replace("Subject:", "")
print(text)

Correct:
text = text.replace("Subject:", "")
print(text)

Mistake 3:
Assuming find() always succeeds.

If find() returns -1, the text was not found.
Always check before slicing.

Mistake 4:
Extracting ORA code from the original line after finding position in a changed line.
For basic uppercase conversion, position remains safe.
But be careful when the normalized line has different length.
"""

print("Read the comments above carefully before building your own extractor.")


# ---------------------------------------------------------------------
# SECTION 20: Homework
# ---------------------------------------------------------------------

print("\nSECTION 20: Homework")

"""
Homework:
1. Complete Day05_Exercise.py
2. Build the ORA Error Extractor from scratch
3. Test it with at least 5 different log lines
4. Try one line with no ORA error
5. Share one interesting test case with the community

Community Discussion Question:
What kind of messy text do you handle in your daily work?
Examples:
- alert emails
- log files
- incident descriptions
- report file names
- monitoring output
"""

print("Day 5 completed. You can now start extracting meaning from operational text.")
print("Next step: loops, so we can process many lines instead of one line at a time.")
