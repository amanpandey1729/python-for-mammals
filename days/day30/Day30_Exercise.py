"""
Python for Mammals - Day 30 Exercise File
Topic: subprocess - Running Commands and Capturing Output

Instructions:
1. Do not look for solutions immediately.
2. Read each task carefully.
3. Write your code below each exercise.
4. Run the file after completing each exercise.
5. Use harmless, read-only practice commands.

Important:
This file contains exercises only.
No complete solutions are provided here.

Goal:
By the end of these exercises, you should be able to run external commands,
capture output, inspect return codes, handle failures, add timeouts, and build
a practical command-check workflow.
"""

print("=" * 70)
print("DAY 30 EXERCISES - SUBPROCESS")
print("Running commands and capturing output")
print("=" * 70)

# ---------------------------------------------------------------------
# EXERCISE 1: Import Required Modules
# ---------------------------------------------------------------------

"""
TODO:
- Import subprocess
- Import sys
- Print a short confirmation message

Concept focus:
imports
"""

# Write your code below this line




# ---------------------------------------------------------------------
# EXERCISE 2: Run One Safe Command
# ---------------------------------------------------------------------

"""
TODO:
- Use subprocess.run()
- Run sys.executable with:
  -c
  print('Automation ready')
- Pass the command as a list
- Do not use shell=True
- Print the returned object's type name

Concept focus:
subprocess.run()
"""

# Write your code below this line




# ---------------------------------------------------------------------
# EXERCISE 3: Capture Standard Output
# ---------------------------------------------------------------------

"""
TODO:
- Independently run a safe Python -c command
- Make the command print:
  Report generated
- Use capture_output=True
- Use text=True
- Print result.stdout after removing the final newline

Concept focus:
stdout capture
"""

# Write your code below this line




# ---------------------------------------------------------------------
# EXERCISE 4: Inspect a Return Code
# ---------------------------------------------------------------------

"""
TODO:
- Independently run a command that exits with code 0
- Capture its output
- Print the return code
- Print SUCCESS when the code is 0
- Otherwise print ATTENTION

Concept focus:
returncode
"""

# Write your code below this line




# ---------------------------------------------------------------------
# EXERCISE 5: Capture Multiple Lines
# ---------------------------------------------------------------------

"""
TODO:
- Run a safe command that prints three inventory lines
- Capture stdout
- Use splitlines()
- Print the line count
- Print each line with a number

Concept focus:
multiline output processing
"""

# Write your code below this line




# ---------------------------------------------------------------------
# EXERCISE 6: Capture Standard Error
# ---------------------------------------------------------------------

"""
TODO:
- Run a safe Python -c command that:
  imports sys
  prints Configuration missing to stderr
  exits with code 2
- Capture output
- Print the return code
- Print stderr without its final newline

Concept focus:
stderr capture
"""

# Write your code below this line




# ---------------------------------------------------------------------
# EXERCISE 7: Compare Success and Failure
# ---------------------------------------------------------------------

"""
TODO:
- Independently run two safe commands
- First command must exit with 0
- Second command must exit with a non-zero code
- Print both return codes
- Print a clear status for each

Concept focus:
command outcome comparison
"""

# Write your code below this line




# ---------------------------------------------------------------------
# EXERCISE 8: Use check=True
# ---------------------------------------------------------------------

"""
TODO:
- Run a successful safe command
- Use check=True
- Capture and print its output
- Catch subprocess.CalledProcessError
- Print the return code if an unexpected failure occurs

Concept focus:
check=True
"""

# Write your code below this line




# ---------------------------------------------------------------------
# EXERCISE 9: Handle a Failed Command
# ---------------------------------------------------------------------

"""
TODO:
- Run a safe Python -c command that:
  writes Validation failed to stderr
  exits with code 4
- Use check=True
- Catch subprocess.CalledProcessError
- Print:
  return code
  captured stderr

Concept focus:
CalledProcessError
"""

# Write your code below this line




# ---------------------------------------------------------------------
# EXERCISE 10: Handle a Missing Program
# ---------------------------------------------------------------------

"""
TODO:
- Try to run a clearly non-existent executable name
- Use capture_output=True and text=True
- Catch FileNotFoundError
- Print a beginner-friendly explanation

Concept focus:
missing executable handling
"""

# Write your code below this line




# ---------------------------------------------------------------------
# EXERCISE 11: Add a Timeout
# ---------------------------------------------------------------------

"""
TODO:
- Run a harmless Python -c command
- Add a timeout value
- Print the output when it finishes
- Catch subprocess.TimeoutExpired
- Print TIMEOUT when the limit is exceeded

Concept focus:
timeout
"""

# Write your code below this line




# ---------------------------------------------------------------------
# EXERCISE 12: Build a Reusable Runner Function
# ---------------------------------------------------------------------

"""
TODO:
- Create a function named run_command
- Accept one command list
- Use subprocess.run() with:
  capture_output=True
  text=True
  timeout=10
- Return a dictionary containing:
  status
  return_code
  stdout
  stderr
- Handle FileNotFoundError and TimeoutExpired
- Test the function with one harmless command

Concept focus:
reusable subprocess wrapper
"""

# Write your code below this line




# ---------------------------------------------------------------------
# EXERCISE 13: Filter Captured Output
# ---------------------------------------------------------------------

"""
TODO:
- Run a safe command that prints mixed lines such as:
  INFO: started
  WARNING: disk high
  INFO: completed
- Capture stdout
- Keep only lines containing WARNING
- Print matching lines and the warning count

Concept focus:
captured output filtering
"""

# Write your code below this line




# ---------------------------------------------------------------------
# EXERCISE 14: Build a Command Report
# ---------------------------------------------------------------------

"""
TODO:
- Independently run one harmless command
- Collect:
  executable name
  command arguments
  return code
  stdout
  stderr
  final status
- Print a clean command execution report
- Show <empty> when stdout or stderr is empty

Concept focus:
operational reporting
"""

# Write your code below this line




# ---------------------------------------------------------------------
# EXERCISE 15: Validate User-Supplied Simulation Values
# ---------------------------------------------------------------------

"""
TODO:
- Independently ask for:
  command message
  simulated return code
  timeout in seconds
- Convert return code and timeout to integers
- Validate:
  return code cannot be negative
  timeout must be greater than zero
- Print READY TO RUN when valid
- Handle ValueError
- Do not run the command in this exercise

Concept focus:
input validation before subprocess execution
"""

# Write your code below this line




# ---------------------------------------------------------------------
# EXERCISE 16: Mini Project - Command Health Check Runner
# ---------------------------------------------------------------------

"""
Build a complete Command Health Check Runner.

Collect all required user inputs once at the beginning:
1. Check name
2. Command message
3. Simulated return code
4. Timeout in seconds

For safe cross-platform practice, construct one command using:
- sys.executable
- the -c argument
- a short Python code string that:
    prints the command message to stdout
    exits using the supplied return code

TODO:
- Normalize and validate the check name
- Convert the simulated return code to an integer
- Convert timeout to an integer or float
- Reject a negative return code
- Reject a timeout that is zero or negative
- Build the command list once
- Reuse that command list throughout the workflow
- Record the start time
- Run the command only once
- Use:
    capture_output=True
    text=True
    check=True
    timeout=<validated timeout>
- Record the end time
- Calculate elapsed duration
- Capture stdout
- Capture stderr
- Capture the actual return code
- Decide:
    SUCCESS when the command completes with code 0
    ATTENTION for a non-zero result
    TIMEOUT when the time limit is exceeded
    PROGRAM NOT FOUND when the executable is missing
    INVALID INPUT for invalid values
- Handle:
    subprocess.CalledProcessError
    subprocess.TimeoutExpired
    FileNotFoundError
    ValueError
- Generate a clean final report containing:
    check name
    command list
    timeout
    start time
    end time
    elapsed duration
    return code
    stdout
    stderr
    exception message
    final status
- Show <empty> when a captured text field is empty
- Do not ask for the same input more than once

Important:
- Do not use shell=True.
- Do not execute administrative or destructive commands.
- The final result should feel like one complete automation workflow.
"""

# Write your code below this line




print("\nEnd of Day 30 exercises. Complete the TODO sections one by one.")
