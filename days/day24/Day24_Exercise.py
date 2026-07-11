"""
Python for Mammals - Day 24 Exercise File
Topic: Datetime

Instructions:
1. Do not look for solutions immediately.
2. Read each task carefully.
3. Write your code below each exercise.
4. Run the file after completing each exercise.
5. Fix errors patiently. Errors are part of learning.

Important:
This file contains exercises only.
No complete solutions are provided here.

Goal:
By the end of these exercises, you should be able to get the current date
and time, format datetime values, parse date text, perform date calculations,
measure durations, and build small time-aware automation reports.
"""

print("=" * 70)
print("DAY 24 EXERCISES - DATETIME")
print("current date, current time, formatting, date calculations")
print("=" * 70)

# ---------------------------------------------------------------------
# EXERCISE 1: Import Datetime Tools
# ---------------------------------------------------------------------

"""
TODO:
- Import date, datetime, and timedelta from the datetime module
- Print a message that says:
  Datetime tools imported successfully

Concept focus:
importing built-in datetime tools
"""

# Write your code below this line




# ---------------------------------------------------------------------
# EXERCISE 2: Display the Current Date
# ---------------------------------------------------------------------

"""
TODO:
- Get the current local date using date.today()
- Print the complete date
- Print the year, month, and day separately

Concept focus:
date.today and date attributes
"""

# Write your code below this line




# ---------------------------------------------------------------------
# EXERCISE 3: Display the Current Date and Time
# ---------------------------------------------------------------------

"""
TODO:
- Get the current local date and time using datetime.now()
- Print the complete value
- Print the current hour, minute, and second separately

Concept focus:
datetime.now and time attributes
"""

# Write your code below this line




# ---------------------------------------------------------------------
# EXERCISE 4: Create a Maintenance Datetime
# ---------------------------------------------------------------------

"""
TODO:
- Create a datetime object for a future maintenance window
- Include year, month, day, hour, and minute
- Print the datetime

Concept focus:
creating a specific datetime object
"""

# Write your code below this line




# ---------------------------------------------------------------------
# EXERCISE 5: Format a Report Timestamp
# ---------------------------------------------------------------------

"""
TODO:
- Create any datetime object
- Use strftime() to print it in these formats:
  1. YYYY-MM-DD HH:MM:SS
  2. DD Month YYYY
  3. YYYYMMDD_HHMMSS
  4. Full weekday name

Concept focus:
strftime formatting
"""

# Write your code below this line




# ---------------------------------------------------------------------
# EXERCISE 6: Build a Timestamped File Name
# ---------------------------------------------------------------------

"""
TODO:
- Get the current datetime
- Format it as YYYYMMDD_HHMMSS
- Create a file name like:
  system_report_20260711_184530.txt
- Print the generated file name

Concept focus:
timestamped report naming
"""

# Write your code below this line




# ---------------------------------------------------------------------
# EXERCISE 7: Parse a Date from User Input
# ---------------------------------------------------------------------

"""
TODO:
- Ask the user for a date in DD-MM-YYYY format
- Convert the text into a datetime object using strptime()
- Print the parsed date in YYYY-MM-DD format

Concept focus:
strptime parsing
"""

# Write your code below this line




# ---------------------------------------------------------------------
# EXERCISE 8: Calculate a Review Date
# ---------------------------------------------------------------------

"""
TODO:
- Ask the user for a start date in DD-MM-YYYY format
- Ask for the review interval in days
- Parse the start date
- Add the interval using timedelta
- Print the calculated review date

Concept focus:
adding days with timedelta
"""

# Write your code below this line




# ---------------------------------------------------------------------
# EXERCISE 9: Calculate Backup Duration
# ---------------------------------------------------------------------

"""
TODO:
- Create a backup start datetime
- Create a backup end datetime
- Subtract start from end
- Print the duration
- Print the duration in total minutes

Concept focus:
datetime subtraction and total_seconds
"""

# Write your code below this line




# ---------------------------------------------------------------------
# EXERCISE 10: Calculate Days Until Expiry
# ---------------------------------------------------------------------

"""
TODO:
- Ask the user for an expiry date in DD-MM-YYYY format
- Parse the expiry date
- Compare it with today's date
- Print the number of days remaining
- Print EXPIRED if the value is negative
- Print EXPIRING SOON if 30 days or fewer remain
- Print VALID otherwise

Concept focus:
date subtraction and status decisions
"""

# Write your code below this line




# ---------------------------------------------------------------------
# EXERCISE 11: Calculate File Age
# ---------------------------------------------------------------------

"""
TODO:
- Create a fixed file-created date
- Use today's date as the current date
- Calculate the file age in days
- Print whether the file is eligible for cleanup when it is older than 30 days

Concept focus:
retention and cleanup calculations
"""

# Write your code below this line




# ---------------------------------------------------------------------
# EXERCISE 12: Maintenance Window Status
# ---------------------------------------------------------------------

"""
TODO:
- Create a current datetime value
- Create a maintenance start datetime
- Create a maintenance end datetime
- Print one status:
  NOT STARTED
  IN PROGRESS
  COMPLETED

Concept focus:
datetime comparison
"""

# Write your code below this line




# ---------------------------------------------------------------------
# EXERCISE 13: Process a List of Deadlines
# ---------------------------------------------------------------------

"""
TODO:
- Create a list of dictionaries for at least 4 operational tasks
- Each dictionary should contain:
  task, due_date
- Store due_date as DD-MM-YYYY text
- Parse each due date
- Print the task name and days remaining
- Clearly mark overdue tasks

Concept focus:
loops, dictionaries, parsing, date calculations
"""

# Write your code below this line




# ---------------------------------------------------------------------
# EXERCISE 14: Datetime with Exception Handling
# ---------------------------------------------------------------------

"""
TODO:
- Ask the user for a date in DD-MM-YYYY format
- Try to parse it using strptime()
- Print the parsed date when valid
- Handle ValueError with a friendly message

Concept focus:
invalid date handling
"""

# Write your code below this line




# ---------------------------------------------------------------------
# EXERCISE 15: Generate a Timestamped Text Report
# ---------------------------------------------------------------------

"""
TODO:
- Ask the user for:
  1. System name
  2. Check status
  3. Report file name prefix
- Get the current datetime once
- Format a readable timestamp for the report content
- Format a compact timestamp for the file name
- Create a text file containing the system, status, and timestamp
- Print the generated file name

Concept focus:
datetime + file writing
"""

# Write your code below this line




# ---------------------------------------------------------------------
# EXERCISE 16: Mini Project - Operational Task Deadline Tracker
# ---------------------------------------------------------------------

"""
Build a small Operational Task Deadline Tracker.

Collect all required user inputs once at the beginning:
1. Task name
2. Task owner
3. Start date in DD-MM-YYYY format
4. Due date in DD-MM-YYYY format
5. Completion percentage
6. Output report file name

Then reuse those variables throughout the mini project.

TODO:
- Import date, datetime, and timedelta if not already imported
- Collect all required inputs once
- Convert completion percentage into a number
- Parse the start date and due date using strptime()
- Use today's date as the report date
- Calculate:
    total planned days
    elapsed days since the start date
    days remaining until the due date
- Decide task status:
    COMPLETED if completion percentage is 100 or more
    OVERDUE if the due date has passed and task is not complete
    DUE TODAY if zero days remain
    DUE SOON if 1 to 7 days remain
    ON TRACK otherwise
- Create a generated timestamp using datetime.now()
- Write a clean text report containing:
    task name
    owner
    start date
    due date
    total planned days
    elapsed days
    days remaining
    completion percentage
    task status
    report generated timestamp
- Read the same report file back
- Print the complete report on screen

Important:
- Collect each input only once.
- Reuse those variables throughout the project.
- Do not ask for the same input repeatedly.
- Handle an invalid date format using ValueError.
- The mini project should feel like one complete deadline-tracking workflow.

Concept focus:
real-world date parsing, calculations, status logic, and report generation
"""

# Write your code below this line




print("\nEnd of Day 24 exercises. Complete the TODO sections one by one.")
