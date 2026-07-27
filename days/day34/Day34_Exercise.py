"""
Python for Mammals - Day 34 Exercise File
Topic: Logging - Recording What an Automation Did

Instructions:
1. Do not look for solutions immediately.
2. Read each task carefully.
3. Write your code below each exercise.
4. Run the file after completing each exercise.
5. Never place passwords, tokens, or private keys in logs.

Important:
This file contains exercises only.
No complete solutions are provided here.

Goal:
By the end of these exercises, you should be able to configure loggers, choose
appropriate levels, write useful log files, record handled exceptions, and add
a trustworthy execution trail to an operational workflow.
"""

print("=" * 70)
print("DAY 34 EXERCISES - LOGGING")
print("Recording what an automation did")
print("=" * 70)

# ---------------------------------------------------------------------
# EXERCISE 1: Import Logging
# ---------------------------------------------------------------------

"""
TODO:
- Import Python's logging module
- Print a short confirmation message
- Print the numeric value of logging.WARNING

Concept focus:
logging module
"""

# Write your code below this line




# ---------------------------------------------------------------------
# EXERCISE 2: Create a Named Logger
# ---------------------------------------------------------------------

"""
TODO:
- Independently create a logger named operations.inventory
- Set the logger level to DEBUG
- Disable propagation for this practice logger
- Print the logger name and effective level

Concept focus:
named loggers
"""

# Write your code below this line




# ---------------------------------------------------------------------
# EXERCISE 3: Add a Console Handler
# ---------------------------------------------------------------------

"""
TODO:
- Independently create a named logger
- Clear any handlers left by an earlier run
- Add one StreamHandler
- Set the handler level to INFO
- Use this format:
    LEVEL - message
- Write one INFO record saying that a daily check started

Concept focus:
console logging
"""

# Write your code below this line




# ---------------------------------------------------------------------
# EXERCISE 4: Practise All Five Levels
# ---------------------------------------------------------------------

"""
TODO:
- Independently configure a console logger that accepts DEBUG and above
- Write one meaningful operational message at each level:
    DEBUG
    INFO
    WARNING
    ERROR
    CRITICAL
- Do not use generic text such as "debug message"

Concept focus:
log levels
"""

# Write your code below this line




# ---------------------------------------------------------------------
# EXERCISE 5: Filter Console Messages
# ---------------------------------------------------------------------

"""
TODO:
- Independently create a logger that accepts DEBUG and above
- Add a console handler that accepts WARNING and above
- Write DEBUG, INFO, WARNING, and ERROR records
- Confirm by observation that only WARNING and ERROR appear
- Print one normal summary line explaining the filter

Concept focus:
logger level versus handler level
"""

# Write your code below this line




# ---------------------------------------------------------------------
# EXERCISE 6: Add Timestamp and Logger Name
# ---------------------------------------------------------------------

"""
TODO:
- Independently configure this format:
    date time | level | logger name | message
- Use date format YYYY-MM-DD HH:MM:SS
- Write an INFO record for a report-generation start

Concept focus:
formatters
"""

# Write your code below this line




# ---------------------------------------------------------------------
# EXERCISE 7: Write a UTF-8 Log File
# ---------------------------------------------------------------------

"""
TODO:
- Independently create a Path named daily_operations.log
- Create a FileHandler using UTF-8
- Write these records:
    INFO: collection started
    INFO: 12 records processed
    WARNING: 2 records were incomplete
- Flush the handler
- Print whether the file exists and its number of lines

Concept focus:
log files
"""

# Write your code below this line




# ---------------------------------------------------------------------
# EXERCISE 8: Append Instead of Replace
# ---------------------------------------------------------------------

"""
TODO:
- Independently configure a FileHandler in append mode
- Write one run-start record
- Run your exercise twice
- Read the file and prove that records from both runs remain
- Avoid counting unrelated records from other exercises

Concept focus:
log history
"""

# Write your code below this line




# ---------------------------------------------------------------------
# EXERCISE 9: Console WARNING, File DEBUG
# ---------------------------------------------------------------------

"""
TODO:
- Independently create one logger accepting DEBUG and above
- Add:
    a console handler accepting WARNING and above
    a file handler accepting DEBUG and above
- Write DEBUG, INFO, WARNING, and ERROR records
- Confirm that the file contains all four records
- Confirm that the console shows only two records

Concept focus:
multiple handlers
"""

# Write your code below this line




# ---------------------------------------------------------------------
# EXERCISE 10: Log Values with Placeholders
# ---------------------------------------------------------------------

"""
TODO:
- Independently collect or define:
    server name
    usage percentage
    threshold percentage
- Use logging placeholder arguments rather than building the complete message
  with string concatenation
- Log INFO for the server being checked
- Log WARNING only when usage meets or exceeds the threshold
- Otherwise log INFO that usage is healthy

Concept focus:
parameterised log messages
"""

# Write your code below this line




# ---------------------------------------------------------------------
# EXERCISE 11: Choose the Correct Level
# ---------------------------------------------------------------------

"""
TODO:
Log each event using an appropriate level:
- configuration loaded successfully
- optional report column is missing but processing can continue
- required input file cannot be opened
- raw parsed value useful only during troubleshooting
- no configured target could be checked

Also add a short comment explaining each choice.

Concept focus:
severity and operational impact
"""

# Write your code below this line




# ---------------------------------------------------------------------
# EXERCISE 12: Record a Handled Exception
# ---------------------------------------------------------------------

"""
TODO:
- Independently attempt to convert "not_available" to float
- Catch ValueError
- Use logger.exception() inside the except block
- Write the record to exception_practice.log
- Flush and read the file
- Print whether both "Traceback" and "ValueError" are present

Concept focus:
exception logging
"""

# Write your code below this line




# ---------------------------------------------------------------------
# EXERCISE 13: Log File-Processing Progress
# ---------------------------------------------------------------------

"""
TODO:
- Independently create a small list of filenames containing:
    two .log files
    one .txt file
    one .csv file
- Log INFO when processing begins and ends
- Log DEBUG for every filename inspected
- Log INFO for every .log file selected
- Log WARNING when a file is skipped because its suffix is unsupported
- Log the final selected and skipped counts

Concept focus:
progress and decision logging
"""

# Write your code below this line




# ---------------------------------------------------------------------
# EXERCISE 14: Prevent Duplicate Handlers
# ---------------------------------------------------------------------

"""
TODO:
- Write a function that returns a configured named logger
- The function may be called multiple times
- Add a FileHandler only when the logger has no handlers
- Call the function twice for the same logger name
- Prove that the logger contains exactly one handler
- Write one record and prove it appears only once in the file

Concept focus:
reusable logger setup
"""

# Write your code below this line




# ---------------------------------------------------------------------
# EXERCISE 15: Add Logging to a Report Workflow
# ---------------------------------------------------------------------

"""
TODO:
- Independently create a list of operational records containing:
    item name
    status
- Count healthy and failed records
- Log workflow start and finish at INFO
- Log each item at DEBUG
- Log failed items at ERROR
- Write a text summary file
- Log successful report creation at INFO
- Handle OSError and record it with logger.exception()

Concept focus:
logging around useful work
"""

# Write your code below this line




# ---------------------------------------------------------------------
# EXERCISE 16: Mini Project - Logged Daily Operations Checker
# ---------------------------------------------------------------------

"""
Build a complete Logged Daily Operations Checker.

Collect all required user inputs once at the beginning:
1. Server name
2. Environment
3. Disk usage percentage
4. Memory usage percentage
5. Disk warning threshold
6. Memory warning threshold
7. Log filename
8. Report filename

TODO:
- Store every collected input in a variable once
- Reject blank server, environment, log filename, and report filename values
- Convert usage and threshold inputs safely
- Reject percentages outside 0 to 100
- Build log and report paths with pathlib.Path
- Create parent folders where required
- Configure one named logger
- Set the logger to accept DEBUG and above
- Add:
    a console handler for WARNING and above
    a UTF-8 file handler for DEBUG and above
- Use a timestamp, level, logger name, and message in file records
- Prevent duplicate handlers if logger setup is called repeatedly
- Record:
    workflow start at INFO
    safe input context at INFO
    converted values at DEBUG
    each health decision at DEBUG
    each threshold breach at WARNING
    invalid input at ERROR
    report creation success at INFO
    handled exceptions with logger.exception()
    workflow finish and final status at INFO
- Calculate:
    disk status
    memory status
    alert count
    final status
- Use final status:
    HEALTHY when both metrics are below their thresholds
    ATTENTION when one or both thresholds are breached
    INVALID INPUT when input is blank, non-numeric, or outside 0 to 100
    FAILED when the log or report cannot be created
- Generate one operator-facing report containing:
    server
    environment
    disk usage and threshold
    memory usage and threshold
    disk status
    memory status
    alert count
    final status
    log destination
    report destination
- Print a concise summary to the console
- Write the detailed execution trail to the log file
- Do not ask for the same input more than once
- Do not log passwords, tokens, private keys, or other secrets

Test these scenarios:
- both metrics healthy
- only disk breached
- both metrics breached
- invalid numeric input
- percentage outside 0 to 100
- destination folder cannot be written

The result should feel like one complete operational workflow rather than a
collection of unrelated logging statements.

Concept focus:
production-style execution logging
"""

# Write your code below this line




print("\nEnd of Day 34 exercises. Complete the TODO sections one by one.")
