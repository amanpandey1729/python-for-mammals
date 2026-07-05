"""
Python for Mammals - Day 21 Exercise File
Topic: Exception Handling

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
By the end of these exercises, you should be able to use try, except,
else, and finally to handle common errors gracefully in automation scripts.
These skills help you build scripts that can survive bad input, missing files,
invalid calculations, and incomplete data.
"""

print("=" * 70)
print("DAY 21 EXERCISES - EXCEPTION HANDLING")
print("try, except, else, finally, common errors")
print("=" * 70)

# ---------------------------------------------------------------------
# EXERCISE 1: Handle Invalid Number Input
# ---------------------------------------------------------------------

"""
TODO:
- Ask the user to enter disk usage percentage
- Convert the input into a float inside a try block
- If conversion fails, handle ValueError
- Print a clear message instead of letting the script crash

Concept focus:
try, except, ValueError
"""

# Write your code below this line




# ---------------------------------------------------------------------
# EXERCISE 2: Safe Integer Conversion
# ---------------------------------------------------------------------

"""
TODO:
- Create a variable named raw_count with any text value
- Try to convert raw_count into an integer
- Handle ValueError if the value is not numeric
- Print either the converted count or a friendly error message

Concept focus:
protecting type conversion
"""

# Write your code below this line




# ---------------------------------------------------------------------
# EXERCISE 3: Handle Division by Zero
# ---------------------------------------------------------------------

"""
TODO:
- Create variables total_checks and failed_checks
- Try to calculate failure percentage:
  failed_checks / total_checks * 100
- Handle ZeroDivisionError
- Print a useful message if total_checks is 0

Concept focus:
ZeroDivisionError
"""

# Write your code below this line




# ---------------------------------------------------------------------
# EXERCISE 4: Safe Disk Usage Calculation
# ---------------------------------------------------------------------

"""
TODO:
- Ask the user for disk_total_gb and disk_used_gb
- Convert both values into float
- Calculate usage percentage
- Handle ValueError for invalid numbers
- Handle ZeroDivisionError for total value 0

Concept focus:
multiple except blocks
"""

# Write your code below this line




# ---------------------------------------------------------------------
# EXERCISE 5: Use else After Successful Conversion
# ---------------------------------------------------------------------

"""
TODO:
- Ask the user to enter memory usage percentage
- Convert it into float inside try
- Handle ValueError
- Use else to print:
  Memory value accepted: <value>

Concept focus:
else block
"""

# Write your code below this line




# ---------------------------------------------------------------------
# EXERCISE 6: Use finally for Completion Message
# ---------------------------------------------------------------------

"""
TODO:
- Ask the user for backup size in GB
- Convert it into float inside try
- Handle ValueError
- Use else to print the accepted backup size
- Use finally to print:
  Backup size validation completed

Concept focus:
finally block
"""

# Write your code below this line




# ---------------------------------------------------------------------
# EXERCISE 7: Handle Missing File
# ---------------------------------------------------------------------

"""
TODO:
- Ask the user for a file name
- Try to open and read the file
- Handle FileNotFoundError
- If file exists, print the content

Concept focus:
FileNotFoundError
"""

# Write your code below this line




# ---------------------------------------------------------------------
# EXERCISE 8: Create File Then Read Safely
# ---------------------------------------------------------------------

"""
TODO:
- Create a file named exercise21_status.txt
- Write at least 3 status lines into it
- Ask the user for a file name to read
- Try to read the file
- Handle FileNotFoundError if the entered name is wrong

Concept focus:
safe file reading workflow
"""

# Write your code below this line




# ---------------------------------------------------------------------
# EXERCISE 9: Handle Missing Dictionary Key
# ---------------------------------------------------------------------

"""
TODO:
- Create a dictionary for a server with keys:
  name, environment, status
- Try to access a key named owner
- Handle KeyError and print a clear message

Concept focus:
KeyError
"""

# Write your code below this line




# ---------------------------------------------------------------------
# EXERCISE 10: Safe Dictionary Report
# ---------------------------------------------------------------------

"""
TODO:
- Create a dictionary for an application with keys:
  app_name, environment, health
- Ask the user which key they want to read
- Try to print that key's value
- Handle KeyError if the key does not exist

Concept focus:
user-driven dictionary access
"""

# Write your code below this line




# ---------------------------------------------------------------------
# EXERCISE 11: Handle List Index Error
# ---------------------------------------------------------------------

"""
TODO:
- Create a list of at least 3 server names
- Ask the user for an index number
- Convert the input into int
- Try to print the server at that index
- Handle ValueError for invalid index input
- Handle IndexError for index outside the list range

Concept focus:
ValueError and IndexError
"""

# Write your code below this line




# ---------------------------------------------------------------------
# EXERCISE 12: Safe Report File Creation
# ---------------------------------------------------------------------

"""
TODO:
- Ask the user for a report file name
- Ask the user for a report title
- Try to create the report file in write mode
- Write the title and a separator line
- Use else to print a success message
- Use finally to print that the report creation attempt is complete

Concept focus:
try, else, finally with file writing
"""

# Write your code below this line




# ---------------------------------------------------------------------
# EXERCISE 13: Convert and Validate Multiple Counts
# ---------------------------------------------------------------------

"""
TODO:
- Ask the user for info_count, warning_count, and error_count
- Convert all three values into integers inside try
- Handle ValueError
- Use else to decide final status:
  CRITICAL if error_count > 0
  WARNING if warning_count > 0 and error_count == 0
  HEALTHY if both warning_count and error_count are 0
- Print the final status

Concept focus:
exception handling + conditions
"""

# Write your code below this line




# ---------------------------------------------------------------------
# EXERCISE 14: Common Errors Review
# ---------------------------------------------------------------------

"""
TODO:
Create 4 small independent try-except examples:
1. ValueError example
2. ZeroDivisionError example
3. FileNotFoundError example
4. KeyError example

For each example:
- Keep the risky code inside try
- Catch the specific error
- Print a clear friendly message

Concept focus:
recognizing common errors
"""

# Write your code below this line




# ---------------------------------------------------------------------
# EXERCISE 15: Mini Project - Safe Disk Usage Reporter
# ---------------------------------------------------------------------

"""
Build a small Safe Disk Usage Reporter.

Collect all required user inputs once at the beginning:
1. Server name
2. Environment name
3. Disk name or mount point
4. Disk total GB
5. Disk used GB
6. Report file name

Then reuse those variables throughout the mini project.

TODO:
- Collect all required inputs once
- Use try to convert disk total and disk used into numbers
- Calculate disk free GB
- Calculate disk usage percentage
- Handle ValueError if disk total or disk used is not numeric
- Handle ZeroDivisionError if disk total is 0
- Use else to generate the report only if calculation succeeds
- Decide health status:
    CRITICAL if usage is greater than or equal to 90
    WARNING if usage is greater than or equal to 80 and less than 90
    HEALTHY if usage is less than 80
- Write a clean report into the provided report file name
- Read the report back and print it on screen
- Use finally to print:
    Safe disk usage workflow completed

Important:
- Collect each input only once.
- Reuse those variables throughout the project.
- Do not ask for the same input repeatedly.
- The mini project should feel like one complete safe automation workflow.

Concept focus:
real-world exception handling with input, calculation, conditions, and file writing
"""

# Write your code below this line




print("\nEnd of Day 21 exercises. Complete the TODO sections one by one.")
