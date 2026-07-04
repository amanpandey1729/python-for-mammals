"""
Python for Mammals - Day 20 Exercise File
Topic: Writing Files

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
By the end of these exercises, you should be able to create text files,
write lines using write(), append new entries using append mode, and generate
simple reports that can be reused in operational automation.
"""

print("=" * 70)
print("DAY 20 EXERCISES - WRITING FILES")
print("write(), append mode, creating reports")
print("=" * 70)

# ---------------------------------------------------------------------
# EXERCISE 1: Create a Simple Notes File
# ---------------------------------------------------------------------

"""
TODO:
- Create a file named exercise20_notes.txt in write mode
- Write 3 lines into the file:
  Python can create files
  Reports can be saved
  Automation output should be reusable
- Close the file
- Print a confirmation message

Concept focus:
write mode and write()
"""

# Write your code below this line




# ---------------------------------------------------------------------
# EXERCISE 2: Read Back the File You Created
# ---------------------------------------------------------------------

"""
TODO:
- Open exercise20_notes.txt in read mode
- Read the complete content using read()
- Print the content

Concept focus:
confirming written file content
"""

# Write your code below this line




# ---------------------------------------------------------------------
# EXERCISE 3: Write Using with open()
# ---------------------------------------------------------------------

"""
TODO:
- Create a file named exercise20_status.txt using with open()
- Write the following lines:
  app01 production running
  db01 production running
  web01 uat maintenance
- Print a confirmation message

Concept focus:
safe file writing with with open()
"""

# Write your code below this line




# ---------------------------------------------------------------------
# EXERCISE 4: Write Variables into a File
# ---------------------------------------------------------------------

"""
TODO:
- Create three variables:
  server_name
  environment
  status
- Assign any meaningful values
- Write these variables into a file named exercise20_server_report.txt
- Use labels like:
  Server Name:
  Environment:
  Status:

Concept focus:
writing variable values into a report
"""

# Write your code below this line




# ---------------------------------------------------------------------
# EXERCISE 5: Create a Disk Calculation Report
# ---------------------------------------------------------------------

"""
TODO:
- Create variables:
  disk_total_gb
  disk_used_gb
- Calculate disk usage percentage
- Write a report into exercise20_disk_report.txt containing:
  Total GB
  Used GB
  Usage Percentage
- Print a confirmation message

Concept focus:
writing calculated values
"""

# Write your code below this line




# ---------------------------------------------------------------------
# EXERCISE 6: Append One Line to a File
# ---------------------------------------------------------------------

"""
TODO:
- Open exercise20_activity.log in write mode
- Write one line: INFO script started
- Open the same file in append mode
- Append one line: INFO script completed
- Read and print the final file content

Concept focus:
append mode
"""

# Write your code below this line




# ---------------------------------------------------------------------
# EXERCISE 7: Append Multiple Activity Entries
# ---------------------------------------------------------------------

"""
TODO:
- Open exercise20_activity.log in append mode
- Append at least 3 more operational messages
- Example messages may include:
  INFO backup checked
  WARNING disk usage high
  INFO report generated
- Read and print the final file content

Concept focus:
using append mode for activity history
"""

# Write your code below this line




# ---------------------------------------------------------------------
# EXERCISE 8: Write List Items into a File
# ---------------------------------------------------------------------

"""
TODO:
- Create a list of at least 4 server names
- Create a file named exercise20_servers.txt
- Loop through the list
- Write each server name on a new line
- Print a confirmation message

Concept focus:
looping through a list and writing records
"""

# Write your code below this line




# ---------------------------------------------------------------------
# EXERCISE 9: Create a Service Checklist File
# ---------------------------------------------------------------------

"""
TODO:
- Create a list of services such as:
  listener
  database
  monitoring
  backup
- Write a checklist file named exercise20_service_checklist.txt
- Each line should look like:
  listener - PENDING
  database - PENDING

Concept focus:
generating checklist-style output
"""

# Write your code below this line




# ---------------------------------------------------------------------
# EXERCISE 10: Write a Health Check Summary
# ---------------------------------------------------------------------

"""
TODO:
- Create variables for:
  cpu_status
  memory_status
  disk_status
- Write a file named exercise20_health_summary.txt
- Include a title and all three statuses
- Use clean labels and new lines

Concept focus:
creating a readable summary report
"""

# Write your code below this line




# ---------------------------------------------------------------------
# EXERCISE 11: Decide Status and Write Report
# ---------------------------------------------------------------------

"""
TODO:
- Create variables:
  warning_count
  error_count
- Decide final_status:
  CRITICAL if error_count is greater than 0
  WARNING if warning_count is greater than 0 and error_count is 0
  HEALTHY if both counts are 0
- Write the counts and final_status into exercise20_final_status.txt

Concept focus:
conditions + file writing
"""

# Write your code below this line




# ---------------------------------------------------------------------
# EXERCISE 12: Create a Report with Header and Separator
# ---------------------------------------------------------------------

"""
TODO:
- Create a report title variable
- Create a separator using "=" multiplied by the length of the title
- Write both into exercise20_header_report.txt
- Add at least 3 summary lines below the header

Concept focus:
report formatting
"""

# Write your code below this line




# ---------------------------------------------------------------------
# EXERCISE 13: Collect Input and Write a Small Report
# ---------------------------------------------------------------------

"""
TODO:
- Ask the user for:
  application_name
  environment
  owner_team
- Write these values into exercise20_application_report.txt
- Read the file back and print it

Concept focus:
input + report generation
"""

# Write your code below this line




# ---------------------------------------------------------------------
# EXERCISE 14: Append User-Entered Activity
# ---------------------------------------------------------------------

"""
TODO:
- Ask the user for one activity message
- Append that message into exercise20_manual_activity.log
- Print a confirmation message

Concept focus:
using append mode with user input
"""

# Write your code below this line




# ---------------------------------------------------------------------
# EXERCISE 15: Mini Project - Disk Usage Report Generator
# ---------------------------------------------------------------------

"""
Build a small Disk Usage Report Generator.

Collect all required user inputs once at the beginning:
1. Server name
2. Environment name
3. Disk name or mount point
4. Disk total GB
5. Disk used GB
6. Report file name
7. Activity log file name

Then reuse those variables throughout the mini project.

TODO:
- Collect all required inputs once
- Convert disk total and disk used into numbers
- Calculate disk usage percentage
- Decide health status:
    CRITICAL if usage is greater than or equal to 90
    WARNING if usage is greater than or equal to 80 and less than 90
    HEALTHY if usage is less than 80
- Create a clean text report containing:
    Report title
    Server name
    Environment
    Disk name or mount point
    Disk total GB
    Disk used GB
    Disk free GB
    Disk usage percentage
    Health status
- Write the report into the report file name provided by the user
- Append one activity entry into the activity log file name provided by the user
  Example activity entry:
    Report generated for db01 production with status WARNING
- Read the final report file back
- Print the final report content on screen

Important:
- Collect each input only once.
- Reuse those variables throughout the project.
- Do not ask for the same input repeatedly.
- The mini project should feel like one complete report-generation workflow.

Concept focus:
real-world report generation using write mode, append mode, calculations, and conditions
"""

# Write your code below this line




print("\nEnd of Day 20 exercises. Complete the TODO sections one by one.")
