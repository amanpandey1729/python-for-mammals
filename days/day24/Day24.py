"""
Python for Mammals - Day 24
Topic: Datetime

Audience:
- Complete beginners
- DBAs, Sysadmins, Support Engineers, Cloud Engineers, Monitoring Teams
- Anyone who wants Python for practical automation

Goal of Day 24:
By the end of today, you should be able to:
1. Import and use Python's built-in datetime module
2. Get the current date and current time
3. Extract date and time components such as year, month, hour, and minute
4. Format dates and times using strftime()
5. Convert date text into datetime objects using strptime()
6. Add and subtract time using timedelta
7. Calculate age, duration, remaining days, and elapsed time
8. Build timestamped operational reports and maintenance reminders

Why this matters:
Automation often needs to know when something happened, how long it took,
and when the next action is due.

You will use dates and times in:
- timestamped health checks
- backup duration reports
- maintenance schedules
- certificate expiry checks
- log retention cleanup
- incident timelines
- daily report file names
- SLA and response-time tracking

Today you learn how Python can work with dates and times safely and clearly.
"""

from datetime import date, datetime, time, timedelta

print("=" * 70)
print("DAY 24 - DATETIME")
print("current date, current time, formatting, date calculations")
print("=" * 70)

# ---------------------------------------------------------------------
# SECTION 1: Project Introduction
# ---------------------------------------------------------------------

print("\nSECTION 1: Project Introduction")

"""
Dates and times appear in almost every real automation workflow.

Examples:
- When did a backup start?
- How long did a job run?
- How many days remain before a certificate expires?
- What timestamp should be added to a report name?
- Which log files are older than the retention period?

Python's datetime module gives us tools for these tasks.
"""

print("Today we will use datetime to build time-aware automation logic.")

# ---------------------------------------------------------------------
# SECTION 2: Why Datetime Matters in Automation
# ---------------------------------------------------------------------

print("\nSECTION 2: Why Datetime Matters in Automation")

"""
Operational scripts frequently need timestamps and date calculations.

Common examples:
- add the current date to a report
- calculate backup runtime
- identify expired items
- schedule the next review date
- compare an event time with the current time
- calculate file age before cleanup
"""

print("Datetime helps automation track events, durations, schedules, and deadlines.")

# ---------------------------------------------------------------------
# SECTION 3: Importing from datetime
# ---------------------------------------------------------------------

print("\nSECTION 3: Importing from datetime")

"""
We imported these tools at the top of the file:

from datetime import date, datetime, time, timedelta

- date stores a calendar date
- time stores a time of day
- datetime stores both date and time
- timedelta stores a duration or difference
"""

print("datetime tools imported successfully.")

# ---------------------------------------------------------------------
# SECTION 4: Current Date
# ---------------------------------------------------------------------

print("\nSECTION 4: Current Date")

today = date.today()

print("Current date:", today)
print("Year        :", today.year)
print("Month       :", today.month)
print("Day         :", today.day)

"""
date.today() returns the current local calendar date.
The year, month, and day can be accessed separately.
"""

# ---------------------------------------------------------------------
# SECTION 5: Current Date and Time
# ---------------------------------------------------------------------

print("\nSECTION 5: Current Date and Time")

current_datetime = datetime.now()

print("Current date and time:", current_datetime)
print("Current hour         :", current_datetime.hour)
print("Current minute       :", current_datetime.minute)
print("Current second       :", current_datetime.second)

"""
datetime.now() returns the current local date and time.
The exact displayed value changes every time the script runs.
"""

# ---------------------------------------------------------------------
# SECTION 6: Creating Specific Date and Time Values
# ---------------------------------------------------------------------

print("\nSECTION 6: Creating Specific Date and Time Values")

maintenance_date = date(2026, 8, 15)
maintenance_time = time(22, 30)
maintenance_window = datetime(2026, 8, 15, 22, 30)

print("Maintenance date  :", maintenance_date)
print("Maintenance time  :", maintenance_time)
print("Maintenance window:", maintenance_window)

"""
Use date(year, month, day) for a calendar date.
Use time(hour, minute) for a time of day.
Use datetime(year, month, day, hour, minute) for both.
"""

# ---------------------------------------------------------------------
# SECTION 7: Formatting with strftime()
# ---------------------------------------------------------------------

print("\nSECTION 7: Formatting with strftime()")

sample_datetime = datetime(2026, 7, 11, 18, 45, 30)

print("ISO style       :", sample_datetime.strftime("%Y-%m-%d %H:%M:%S"))
print("Readable style  :", sample_datetime.strftime("%d %B %Y, %I:%M %p"))
print("Report file date:", sample_datetime.strftime("%Y%m%d_%H%M%S"))
print("Weekday         :", sample_datetime.strftime("%A"))

"""
strftime() means string format time.
It converts a date or datetime object into formatted text.

Useful format codes:
%Y = four-digit year
%m = month number
%d = day number
%H = hour in 24-hour format
%I = hour in 12-hour format
%M = minute
%S = second
%p = AM or PM
%A = full weekday name
%B = full month name
"""

# ---------------------------------------------------------------------
# SECTION 8: Parsing Text with strptime()
# ---------------------------------------------------------------------

print("\nSECTION 8: Parsing Text with strptime()")

maintenance_text = "20-07-2026 23:15"
parsed_maintenance = datetime.strptime(maintenance_text, "%d-%m-%Y %H:%M")

print("Original text   :", maintenance_text)
print("Parsed datetime :", parsed_maintenance)
print("Parsed year     :", parsed_maintenance.year)
print("Parsed hour     :", parsed_maintenance.hour)

"""
strptime() means string parse time.
It converts correctly formatted text into a datetime object.
The format pattern must match the text exactly.
"""

# ---------------------------------------------------------------------
# SECTION 9: Adding Time with timedelta
# ---------------------------------------------------------------------

print("\nSECTION 9: Adding Time with timedelta")

start_date = date(2026, 7, 11)
review_date = start_date + timedelta(days=30)
next_check = datetime(2026, 7, 11, 9, 0) + timedelta(hours=6)

print("Start date :", start_date)
print("Review date:", review_date)
print("Next check :", next_check)

"""
timedelta represents a duration.
It can store days, hours, minutes, seconds, and weeks.
"""

# ---------------------------------------------------------------------
# SECTION 10: Subtracting Dates
# ---------------------------------------------------------------------

print("\nSECTION 10: Subtracting Dates")

backup_start = datetime(2026, 7, 11, 1, 15)
backup_end = datetime(2026, 7, 11, 3, 5)
backup_duration = backup_end - backup_start

print("Backup start   :", backup_start)
print("Backup end     :", backup_end)
print("Backup duration:", backup_duration)
print("Duration hours :", backup_duration.total_seconds() / 3600)

"""
Subtracting two datetime objects returns a timedelta.
total_seconds() is useful for converting the duration into seconds,
minutes, or hours.
"""

# ---------------------------------------------------------------------
# SECTION 11: Days Remaining Until a Deadline
# ---------------------------------------------------------------------

print("\nSECTION 11: Days Remaining Until a Deadline")

reference_date = date(2026, 7, 11)
certificate_expiry = date(2026, 8, 25)
days_remaining = (certificate_expiry - reference_date).days

print("Reference date    :", reference_date)
print("Certificate expiry:", certificate_expiry)
print("Days remaining    :", days_remaining)

if days_remaining < 0:
    print("Status            : EXPIRED")
elif days_remaining <= 30:
    print("Status            : EXPIRING SOON")
else:
    print("Status            : VALID")

"""
This pattern is useful for certificates, passwords, contracts,
licenses, maintenance windows, and review deadlines.
"""

# ---------------------------------------------------------------------
# SECTION 12: Timestamped File Names
# ---------------------------------------------------------------------

print("\nSECTION 12: Timestamped File Names")

report_time = datetime(2026, 7, 11, 21, 40, 5)
report_timestamp = report_time.strftime("%Y%m%d_%H%M%S")
report_file_name = "health_report_" + report_timestamp + ".txt"

print("Report timestamp:", report_timestamp)
print("Report file name:", report_file_name)

"""
Timestamped names prevent reports from overwriting each other.
They also make files easier to sort chronologically.
"""

# ---------------------------------------------------------------------
# SECTION 13: Comparing Date and Time Values
# ---------------------------------------------------------------------

print("\nSECTION 13: Comparing Date and Time Values")

current_check_time = datetime(2026, 7, 11, 20, 0)
maintenance_start = datetime(2026, 7, 11, 22, 0)

if current_check_time < maintenance_start:
    print("Maintenance status: NOT STARTED")
elif current_check_time == maintenance_start:
    print("Maintenance status: STARTING NOW")
else:
    print("Maintenance status: STARTED")

"""
Date and datetime objects can be compared using normal comparison operators.
This is useful for schedules, deadlines, and age checks.
"""

# ---------------------------------------------------------------------
# SECTION 14: Date Calculations with Exception Handling
# ---------------------------------------------------------------------

print("\nSECTION 14: Date Calculations with Exception Handling")

expiry_text = "31-08-2026"

try:
    expiry_date = datetime.strptime(expiry_text, "%d-%m-%Y").date()
    remaining_days = (expiry_date - date(2026, 7, 11)).days
    print("Expiry date   :", expiry_date)
    print("Remaining days:", remaining_days)
except ValueError:
    print("Date format is invalid. Use DD-MM-YYYY.")

"""
strptime() raises ValueError when the text does not match the format
or contains an impossible date.
"""

# ---------------------------------------------------------------------
# SECTION 15: Important Difference - date, time, datetime, timedelta
# ---------------------------------------------------------------------

print("\nSECTION 15: Important Datetime Objects")

"""
date
- stores only year, month, and day

time
- stores only hour, minute, second, and microsecond

datetime
- stores both calendar date and time of day

timedelta
- stores a duration or difference between two dates or datetimes
"""

print("Use date for calendar days, datetime for timestamps, and timedelta for durations.")

# ---------------------------------------------------------------------
# SECTION 16: Guided Practice - Build a Maintenance Reminder
# ---------------------------------------------------------------------

print("\nSECTION 16: Guided Practice - Build a Maintenance Reminder")

"""
Uncomment this block and run it.
It reads a maintenance date, calculates the remaining days,
and prints a simple reminder.
"""

# maintenance_text = input("Enter maintenance date (DD-MM-YYYY): ")
# maintenance_date = datetime.strptime(maintenance_text, "%d-%m-%Y").date()
# today = date.today()
# days_left = (maintenance_date - today).days
#
# print("Maintenance date:", maintenance_date.strftime("%d %B %Y"))
# print("Days remaining  :", days_left)
#
# if days_left < 0:
#     print("Status          : MISSED")
# elif days_left == 0:
#     print("Status          : TODAY")
# elif days_left <= 7:
#     print("Status          : DUE SOON")
# else:
#     print("Status          : SCHEDULED")

print("Guided practice: uncomment the maintenance reminder block.")

# ---------------------------------------------------------------------
# SECTION 17: Mini Challenge Preview
# ---------------------------------------------------------------------

print("\nSECTION 17: Mini Challenge Preview")

"""
Mini Challenge:
Build an Operational Task Deadline Tracker.

Your script should:
1. Collect task name, owner, start date, due date, completion percentage,
   and report file name once
2. Parse both dates using strptime()
3. Calculate total planned days and days remaining
4. Decide whether the task is COMPLETED, OVERDUE, DUE TODAY,
   DUE SOON, or ON TRACK
5. Create a timestamp for the report
6. Write a clean text report
7. Read the report back and display it

This mirrors real automation:
- collect schedule information
- convert text into date objects
- calculate durations and deadlines
- determine operational status
- generate a timestamped audit report
"""

print("Mini challenge: build an Operational Task Deadline Tracker.")

# ---------------------------------------------------------------------
# SECTION 18: Closing Message
# ---------------------------------------------------------------------

print("\nSECTION 18: Closing Message")

print("You have completed Day 24.")
print("You can now format dates, calculate durations, and build time-aware automation.")
print("Datetime will help your scripts track events, schedules, retention, and deadlines.")
