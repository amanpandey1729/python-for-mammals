"""
Python for Mammals - Day 25 Exercise File
Topic: Modules & Imports

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
By the end of these exercises, you should be able to use import,
from ... import, aliases, built-in modules, custom modules, and the
__main__ guard to organize reusable automation code.
"""

print("=" * 70)
print("DAY 25 EXERCISES - MODULES & IMPORTS")
print("import, from import, aliases, creating modules")
print("=" * 70)

# ---------------------------------------------------------------------
# EXERCISE 1: Import a Complete Module
# ---------------------------------------------------------------------

"""
TODO:
- Import the math module
- Print a message that says:
  math module imported successfully

Concept focus:
import module_name
"""

# Write your code below this line




# ---------------------------------------------------------------------
# EXERCISE 2: Use Dot Notation
# ---------------------------------------------------------------------

"""
TODO:
- Import the math module
- Create a variable containing 72.4
- Print the result of math.ceil()
- Print the result of math.floor()

Concept focus:
module.function()
"""

# Write your code below this line




# ---------------------------------------------------------------------
# EXERCISE 3: Import One Specific Name
# ---------------------------------------------------------------------

"""
TODO:
- Import sqrt from the math module using from ... import
- Calculate the square root of 144
- Print the result

Concept focus:
from module import name
"""

# Write your code below this line




# ---------------------------------------------------------------------
# EXERCISE 4: Import Multiple Names
# ---------------------------------------------------------------------

"""
TODO:
- Import ceil and floor from math
- Ask the user for one decimal capacity value
- Print the rounded-up and rounded-down values

Concept focus:
importing multiple selected names
"""

# Write your code below this line




# ---------------------------------------------------------------------
# EXERCISE 5: Use an Import Alias
# ---------------------------------------------------------------------

"""
TODO:
- Import statistics using the alias stats
- Create a list of at least 5 response-time values
- Calculate and print the mean using stats.mean()

Concept focus:
import module as alias
"""

# Write your code below this line




# ---------------------------------------------------------------------
# EXERCISE 6: Use the platform Module
# ---------------------------------------------------------------------

"""
TODO:
- Import platform
- Print:
  operating-system name
  machine type
  Python version

Concept focus:
built-in system-information module
"""

# Write your code below this line




# ---------------------------------------------------------------------
# EXERCISE 7: Use pathlib with from import
# ---------------------------------------------------------------------

"""
TODO:
- Import Path from pathlib
- Create a path for reports/daily/health_report.txt
- Print the complete path
- Print only the file name
- Print only the file suffix

Concept focus:
selected import + path operations
"""

# Write your code below this line




# ---------------------------------------------------------------------
# EXERCISE 8: Create Your First Custom Module
# ---------------------------------------------------------------------

"""
TODO:
- Create a separate file named greeting_utils.py
- Inside it, create a function named build_greeting(name, role)
- The function should return a professional welcome message
- In this exercise file, import greeting_utils
- Call the function and print the returned message

Important:
Keep greeting_utils.py in the same folder as this exercise file.

Concept focus:
creating and importing a custom module
"""

# Write your code below this line




# ---------------------------------------------------------------------
# EXERCISE 9: Import a Function from a Custom Module
# ---------------------------------------------------------------------

"""
TODO:
- Create a separate file named validation_utils.py
- Add a function named is_valid_percent(value)
- It should return True when value is between 0 and 100 inclusive
- Import only is_valid_percent into this exercise
- Ask the user for a percentage
- Print whether it is valid

Concept focus:
from custom_module import function
"""

# Write your code below this line




# ---------------------------------------------------------------------
# EXERCISE 10: Build a Capacity Utility Module
# ---------------------------------------------------------------------

"""
TODO:
- Create capacity_utils.py
- Add a function named calculate_usage(used, total)
- Add a function named calculate_free(used, total)
- Import the complete capacity_utils module
- Use it to calculate usage percentage and free capacity
- Print both values

Concept focus:
reusable calculation module
"""

# Write your code below this line




# ---------------------------------------------------------------------
# EXERCISE 11: Add Status Logic to a Module
# ---------------------------------------------------------------------

"""
TODO:
- In a separate module named health_utils.py, create get_status(usage)
- Return:
  CRITICAL when usage >= 90
  WARNING when usage >= 80 and below 90
  HEALTHY otherwise
- Import get_status into this exercise
- Ask the user for usage percentage
- Print the returned status

Concept focus:
reusable decision logic
"""

# Write your code below this line




# ---------------------------------------------------------------------
# EXERCISE 12: Protect Module Test Code
# ---------------------------------------------------------------------

"""
TODO:
- Create report_utils.py
- Add a function named build_summary(system_name, status)
- Add a small test call under:
  if __name__ == "__main__":
- Run report_utils.py directly and confirm the test runs
- Import report_utils here and confirm the test does not run automatically
- Call build_summary() yourself and print the result

Concept focus:
__name__ and the __main__ guard
"""

# Write your code below this line




# ---------------------------------------------------------------------
# EXERCISE 13: Custom Module for Log Classification
# ---------------------------------------------------------------------

"""
TODO:
- Create log_utils.py
- Add classify_log(message)
- Return:
  ERROR when the message contains ERROR
  WARNING when the message contains WARNING
  INFO otherwise
- Import the function
- Ask the user for one log message
- Print its classification

Concept focus:
module for text-processing logic
"""

# Write your code below this line




# ---------------------------------------------------------------------
# EXERCISE 14: Handle a Missing Module
# ---------------------------------------------------------------------

"""
TODO:
- Use try and except
- Try to import a deliberately nonexistent module name
- Handle ModuleNotFoundError
- Print a friendly message explaining that the module is unavailable

Concept focus:
import error handling
"""

# Write your code below this line




# ---------------------------------------------------------------------
# EXERCISE 15: Modular Inventory Formatter
# ---------------------------------------------------------------------

"""
TODO:
- Create inventory_utils.py
- Add a function that accepts:
  system name, environment, owner, status
- Return one formatted inventory line
- In this exercise, ask for those four values
- Import and call the formatter
- Write the formatted line into exercise25_inventory.txt
- Read the file back and print it

Concept focus:
custom module + input + file report
"""

# Write your code below this line




# ---------------------------------------------------------------------
# EXERCISE 16: Mini Project - Modular Capacity Report
# ---------------------------------------------------------------------

"""
Build a small Modular Capacity Report using two Python files.

File 1: capacity_utils.py
File 2: your main report code below this TODO section

Collect all required user inputs once at the beginning of the main workflow:
1. System name
2. Environment
3. Capacity type, such as disk, memory, or storage pool
4. Total capacity
5. Used capacity
6. Output report file name

TODO for capacity_utils.py:
- Create calculate_free(total, used)
- Create calculate_usage(total, used)
- Create get_status(usage_percent)
- Create build_summary(system_name, capacity_type, usage_percent, status)
- Place optional module tests under if __name__ == "__main__":

TODO for the main workflow:
- Import the required functions from capacity_utils.py
- Collect all required inputs once
- Convert total and used capacity into numbers
- Validate that total capacity is greater than zero
- Validate that used capacity is not negative
- Calculate free capacity
- Calculate usage percentage
- Decide status:
    CRITICAL if usage >= 90
    WARNING if usage >= 80 and below 90
    HEALTHY otherwise
- Build a summary using the imported function
- Write a clean report containing:
    system name
    environment
    capacity type
    total capacity
    used capacity
    free capacity
    usage percentage
    health status
    summary
- Read the same report file back
- Print the complete report on screen

Important:
- Collect each input only once.
- Reuse those variables throughout the workflow.
- Keep calculation and status logic inside capacity_utils.py.
- Keep input, file writing, and workflow control in the main script.
- Do not ask for the same input repeatedly.
- Handle invalid numeric input using ValueError.

Concept focus:
real-world separation of reusable logic and main automation workflow
"""

# Write your code below this line




print("\nEnd of Day 25 exercises. Complete the TODO sections one by one.")
