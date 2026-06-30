"""
Python for Mammals - Day 19 Exercise File
Topic: Reading Files

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
By the end of these exercises, you should be able to read text files using
open(), read(), readline(), readlines(), and the with statement.
These skills are the base of log analysis, report reading, inventory parsing,
and many day-to-day automation scripts.
"""

print("=" * 70)
print("DAY 19 EXERCISES - READING FILES")
print("open(), read(), readline(), readlines(), with")
print("=" * 70)

# ---------------------------------------------------------------------
# EXERCISE 1: Create a Practice Text File
# ---------------------------------------------------------------------

"""
TODO:
- Create a file named exercise19_notes.txt in write mode
- Write 3 lines into the file:
  Python file reading practice
  Logs are text files
  Automation starts with input data
- Close the file
- Print a confirmation message

Concept focus:
creating a small file for reading practice
"""

# Write your code below this line




# ---------------------------------------------------------------------
# EXERCISE 2: Open and Read Complete File
# ---------------------------------------------------------------------

"""
TODO:
- Open exercise19_notes.txt in read mode using open()
- Read the full content using read()
- Close the file
- Print the content

Concept focus:
open(), read(), close()
"""

# Write your code below this line




# ---------------------------------------------------------------------
# EXERCISE 3: Read Complete File Using with
# ---------------------------------------------------------------------

"""
TODO:
- Open exercise19_notes.txt using with open()
- Read the full content using read()
- Print the content

Concept focus:
with statement for safe file handling
"""

# Write your code below this line




# ---------------------------------------------------------------------
# EXERCISE 4: Read First Line
# ---------------------------------------------------------------------

"""
TODO:
- Open exercise19_notes.txt using with open()
- Read only the first line using readline()
- Print the first line after applying strip()

Concept focus:
readline()
"""

# Write your code below this line




# ---------------------------------------------------------------------
# EXERCISE 5: Read First Two Lines
# ---------------------------------------------------------------------

"""
TODO:
- Open exercise19_notes.txt using with open()
- Use readline() twice
- Store both lines in two different variables
- Print both lines clearly after applying strip()

Concept focus:
multiple readline() calls
"""

# Write your code below this line




# ---------------------------------------------------------------------
# EXERCISE 6: Read All Lines as a List
# ---------------------------------------------------------------------

"""
TODO:
- Open exercise19_notes.txt using with open()
- Read all lines using readlines()
- Store the result in a variable named lines
- Print the type of lines
- Print the number of lines using len()

Concept focus:
readlines() returns a list
"""

# Write your code below this line




# ---------------------------------------------------------------------
# EXERCISE 7: Loop Through File Lines
# ---------------------------------------------------------------------

"""
TODO:
- Open exercise19_notes.txt using with open()
- Loop through the file object directly
- Print each line after applying strip()

Concept focus:
reading one line at a time using a loop
"""

# Write your code below this line




# ---------------------------------------------------------------------
# EXERCISE 8: Create and Read a Server Status File
# ---------------------------------------------------------------------

"""
TODO:
- Create a file named server_status.txt
- Write at least 4 server status lines like:
  app01 production running
  db01 production running
  web01 uat maintenance
  test01 test stopped
- Read the file using with open()
- Print each line cleanly

Concept focus:
reading simple inventory-style records
"""

# Write your code below this line




# ---------------------------------------------------------------------
# EXERCISE 9: Count Lines in a File
# ---------------------------------------------------------------------

"""
TODO:
- Open server_status.txt using with open()
- Count how many lines are present in the file
- Print the total line count

Concept focus:
counting file records
"""

# Write your code below this line




# ---------------------------------------------------------------------
# EXERCISE 10: Search for a Word in a File
# ---------------------------------------------------------------------

"""
TODO:
- Open server_status.txt using with open()
- Search for lines containing the word production
- Print only matching lines

Concept focus:
keyword search in file lines
"""

# Write your code below this line




# ---------------------------------------------------------------------
# EXERCISE 11: Create and Analyze a Log File
# ---------------------------------------------------------------------

"""
TODO:
- Create a file named app_log.txt
- Add at least 5 lines containing a mix of:
  INFO
  WARNING
  ERROR
- Read the file using with open()
- Print only lines containing ERROR

Concept focus:
basic log scanning
"""

# Write your code below this line




# ---------------------------------------------------------------------
# EXERCISE 12: Count WARNING and ERROR Lines
# ---------------------------------------------------------------------

"""
TODO:
- Open app_log.txt using with open()
- Count how many lines contain WARNING
- Count how many lines contain ERROR
- Print both counts clearly

Concept focus:
file scanning with counters
"""

# Write your code below this line




# ---------------------------------------------------------------------
# EXERCISE 13: Split File Lines into Columns
# ---------------------------------------------------------------------

"""
TODO:
- Open server_status.txt using with open()
- For each line:
  - apply strip()
  - apply split()
  - store server name, environment, and status in variables
  - print them in this format:
    Server: app01 | Environment: production | Status: running

Concept focus:
turning plain text lines into useful fields
"""

# Write your code below this line




# ---------------------------------------------------------------------
# EXERCISE 14: Store Matching Lines in a List
# ---------------------------------------------------------------------

"""
TODO:
- Create an empty list named error_lines
- Open app_log.txt using with open()
- Add every line containing ERROR into error_lines
- Print the total number of error lines
- Print the error_lines list

Concept focus:
storing useful file records for later processing
"""

# Write your code below this line




# ---------------------------------------------------------------------
# EXERCISE 15: Mini Project - Log Reader Summary
# ---------------------------------------------------------------------

"""
Build a small Log Reader Summary script.

Collect all required user inputs once at the beginning:
1. Log file name
2. Application name
3. Environment name

Then create or read the log file.
For beginner practice, you may create the file first with sample lines.

Suggested sample log lines:
INFO application started
WARNING disk usage above threshold
ERROR backup job failed
INFO health check completed
ERROR connection timeout

TODO:
- Collect log_file_name, application_name, and environment once
- Create the log file using the provided file name
- Write at least 5 sample log lines into the file
- Open the same file using with open()
- Read the file line by line
- Count:
  - total lines
  - INFO lines
  - WARNING lines
  - ERROR lines
- Store ERROR lines in a list named error_lines
- Print a final report containing:
  - Application name
  - Environment name
  - Log file name
  - Total lines scanned
  - INFO count
  - WARNING count
  - ERROR count
  - All ERROR lines cleanly
  - Final health status:
      CRITICAL if error count is greater than 0
      WARNING if warning count is greater than 0 and error count is 0
      HEALTHY if both error count and warning count are 0

Important:
- Collect each input only once.
- Reuse those variables throughout the project.
- Do not ask for the same input repeatedly.
- The mini project should feel like one complete log-reading workflow.

Concept focus:
real-world file reading, log scanning, counting, and summary reporting
"""

# Write your code below this line




print("\nEnd of Day 19 exercises. Complete the TODO sections one by one.")
