"""
Python for Mammals - Day 26 Exercise File
Topic: Mini Project #3 - Log File Analyzer

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
By the end of these exercises, you should be able to combine files,
strings, loops, conditions, lists, and dictionaries to analyze logs and
generate a useful operational report.
"""

print("=" * 70)
print("DAY 26 EXERCISES - MINI PROJECT #3: LOG FILE ANALYZER")
print("Files, strings, loops, dictionaries")
print("=" * 70)

# ---------------------------------------------------------------------
# EXERCISE 1: Read a Small Log File
# ---------------------------------------------------------------------

"""
TODO:
- Create a text file named exercise26_basic.log
- Add at least five operational log messages
- Open the file using with
- Read and print the complete content

Concept focus:
basic file reading
"""

# Write your code below this line




# ---------------------------------------------------------------------
# EXERCISE 2: Process One Line at a Time
# ---------------------------------------------------------------------

"""
TODO:
- Create or reuse a small log file
- Read it one line at a time using a for loop
- Remove the newline from each line with strip()
- Print each cleaned line

Concept focus:
file loop + string cleaning
"""

# Write your code below this line




# ---------------------------------------------------------------------
# EXERCISE 3: Ignore Blank Lines
# ---------------------------------------------------------------------

"""
TODO:
- Create a log file containing normal lines and blank lines
- Read the file line by line
- Skip blank lines
- Count and print only the non-empty lines

Concept focus:
continue + cleaned strings
"""

# Write your code below this line




# ---------------------------------------------------------------------
# EXERCISE 4: Count a Word in Log Messages
# ---------------------------------------------------------------------

"""
TODO:
- Ask the user for one search word
- Read a log file
- Count how many lines contain that word
- Make the search case-insensitive
- Print the final count

Concept focus:
string search + loop counter
"""

# Write your code below this line




# ---------------------------------------------------------------------
# EXERCISE 5: Split a Structured Log Line
# ---------------------------------------------------------------------

"""
TODO:
- Use this sample line:
  2026-07-14 10:15:00 | ERROR | backup | Backup failed
- Split it using |
- Strip spaces from every part
- Store the four values as:
  timestamp, level, component, message
- Print each value separately

Concept focus:
split(), strip(), unpacking
"""

# Write your code below this line




# ---------------------------------------------------------------------
# EXERCISE 6: Validate Log Structure
# ---------------------------------------------------------------------

"""
TODO:
- Create a list containing valid and malformed log lines
- A valid line must contain exactly four fields separated by |
- Loop through the list
- Print VALID or MALFORMED for each line
- Count malformed lines

Concept focus:
validation with len()
"""

# Write your code below this line




# ---------------------------------------------------------------------
# EXERCISE 7: Count INFO and ERROR Entries
# ---------------------------------------------------------------------

"""
TODO:
- Read a structured log file
- Count INFO entries
- Count ERROR entries
- Print both totals

Important:
Do not count a word merely because it appears in the message.
Use the level field after splitting the line.

Concept focus:
field-based counting
"""

# Write your code below this line




# ---------------------------------------------------------------------
# EXERCISE 8: Build a Level Dictionary
# ---------------------------------------------------------------------

"""
TODO:
- Create a dictionary with these keys:
  INFO, WARNING, ERROR, CRITICAL, UNKNOWN
- Initialize every count to zero
- Read structured log lines
- Increase the matching dictionary value
- Put unrecognized levels under UNKNOWN
- Print the completed dictionary

Concept focus:
dictionary counters
"""

# Write your code below this line




# ---------------------------------------------------------------------
# EXERCISE 9: Count Entries per Component
# ---------------------------------------------------------------------

"""
TODO:
- Read structured log lines
- Extract the component field
- Use a dictionary to count entries per component
- Do not predefine component names
- Print the completed component-count dictionary

Hint:
A dictionary get() call can provide a default count of zero.

Concept focus:
dynamic dictionary counting
"""

# Write your code below this line




# ---------------------------------------------------------------------
# EXERCISE 10: Collect Serious Events
# ---------------------------------------------------------------------

"""
TODO:
- Read structured log lines
- Add ERROR and CRITICAL lines to a list
- Print the number of serious events
- Print each serious event with a sequence number

Concept focus:
filtering + list collection
"""

# Write your code below this line




# ---------------------------------------------------------------------
# EXERCISE 11: Decide Overall Status
# ---------------------------------------------------------------------

"""
TODO:
- Ask for CRITICAL, ERROR, and WARNING counts
- Decide:
  CRITICAL when critical count is greater than zero
  ATTENTION when error or warning count is greater than zero
  HEALTHY otherwise
- Print the final status

Concept focus:
conditions using summary counts
"""

# Write your code below this line




# ---------------------------------------------------------------------
# EXERCISE 12: Find the Busiest Component
# ---------------------------------------------------------------------

"""
TODO:
- Create a dictionary of component counts
- Identify the component with the highest count
- Print the component name and count
- Handle an empty dictionary safely

Concept focus:
dictionary analysis
"""

# Write your code below this line




# ---------------------------------------------------------------------
# EXERCISE 13: Build a Text Summary
# ---------------------------------------------------------------------

"""
TODO:
- Create independent sample values for:
  source file, total entries, INFO, WARNING, ERROR, CRITICAL, status
- Build a clear multi-line report using those values
- Print the report

Concept focus:
report formatting
"""

# Write your code below this line




# ---------------------------------------------------------------------
# EXERCISE 14: Save and Verify a Report
# ---------------------------------------------------------------------

"""
TODO:
- Ask for an output report file name
- Create a small analysis summary
- Write it into the requested file
- Read the same file back
- Print the saved content

Concept focus:
write + read-back verification
"""

# Write your code below this line




# ---------------------------------------------------------------------
# EXERCISE 15: Analyze a Monitoring Alert File
# ---------------------------------------------------------------------

"""
TODO:
- Create a file containing one alert per line
- Each line should use:
  timestamp | severity | system | message
- Count alerts by severity
- Count alerts by system
- Collect CRITICAL alerts
- Print a compact alert summary

Concept focus:
practical structured-text analysis
"""

# Write your code below this line




# ---------------------------------------------------------------------
# EXERCISE 16: Mini Project - Log File Analyzer
# ---------------------------------------------------------------------

"""
Build a complete Log File Analyzer.

Collect all required user inputs once at the beginning:
1. Source log file name
2. Output report file name
3. Search keyword

Expected source-log format:
timestamp | level | component | message

TODO:
- Store the three inputs in variables and reuse them
- Verify that the source file exists before reading
- Open the source file safely
- Read one line at a time
- Strip surrounding whitespace
- Skip blank lines
- Count total non-empty lines
- Split each line using |
- Treat lines without exactly four fields as malformed
- Extract timestamp, level, component, and message
- Normalize level using upper()
- Count:
    INFO
    WARNING
    ERROR
    CRITICAL
    UNKNOWN
- Build a dictionary that counts entries per component
- Collect complete ERROR and CRITICAL lines in a list
- Count lines containing the search keyword
- Make keyword matching case-insensitive
- Decide overall status:
    CRITICAL when at least one CRITICAL entry exists
    ATTENTION when ERROR or WARNING exists
    HEALTHY otherwise
- Identify the busiest component
- Generate a clean report containing:
    source file
    total entries
    malformed entries
    every level count
    serious-event count
    search keyword
    keyword-match count
    busiest component and its count
    overall status
    complete serious-event section
- Write the report to the requested output file
- Read the report back
- Print the complete saved report
- Handle at least:
    FileNotFoundError
    PermissionError

Important:
- Collect each input only once.
- Reuse the same variables throughout the workflow.
- Do not ask for the same value again.
- The final result should feel like one complete automation workflow.
- Do not hardcode the user's file names or search keyword.
"""

# Write your code below this line




print("\nEnd of Day 26 exercises. Complete the TODO sections one by one.")
