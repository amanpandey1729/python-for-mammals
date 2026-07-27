"""
Python for Mammals - Day 31 Exercise File
Topic: Linux Commands from Python - df, free, uptime, ps, and Output Processing

Instructions:
1. Do not look for solutions immediately.
2. Read each task carefully.
3. Write your code below each exercise.
4. Run the file after completing each exercise.
5. Use read-only Linux commands only.

Important:
This file contains exercises only.
No complete solutions are provided here.

Goal:
By the end of these exercises, you should be able to run common Linux
commands, capture their output, parse useful values, apply thresholds, and
build a compact Linux health workflow.
"""

print("=" * 70)
print("DAY 31 EXERCISES - LINUX COMMANDS FROM PYTHON")
print("df, free, uptime, ps, and output processing")
print("=" * 70)

# ---------------------------------------------------------------------
# EXERCISE 1: Import Required Modules
# ---------------------------------------------------------------------

"""
TODO:
- Import shutil
- Import subprocess
- Print a short confirmation message

Concept focus:
imports
"""

# Write your code below this line




# ---------------------------------------------------------------------
# EXERCISE 2: Check Linux Command Availability
# ---------------------------------------------------------------------

"""
TODO:
- Create an independent list:
  df, free, uptime, ps
- Use shutil.which() for each command
- Print AVAILABLE or MISSING

Concept focus:
command discovery
"""

# Write your code below this line




# ---------------------------------------------------------------------
# EXERCISE 3: Run df Safely
# ---------------------------------------------------------------------

"""
TODO:
- Check whether df exists
- Run:
  df -P
- Use capture_output=True
- Use text=True
- Use a timeout
- Print return code
- Print the first output line
- Print SKIPPED when df is unavailable

Concept focus:
running df
"""

# Write your code below this line




# ---------------------------------------------------------------------
# EXERCISE 4: Count df Output Rows
# ---------------------------------------------------------------------

"""
TODO:
- Independently run df -P
- Split stdout into lines
- Count filesystem rows without counting the header
- Print the count
- Handle missing command and timeout conditions

Concept focus:
multiline output processing
"""

# Write your code below this line




# ---------------------------------------------------------------------
# EXERCISE 5: Extract Disk Usage Percentages
# ---------------------------------------------------------------------

"""
TODO:
- Independently run df -P
- Ignore the header
- Split each row into columns
- Extract:
  filesystem
  use percentage
  mount point
- Convert the use percentage into an integer
- Print one compact line per valid filesystem row

Concept focus:
df parsing
"""

# Write your code below this line




# ---------------------------------------------------------------------
# EXERCISE 6: Apply a Disk Threshold
# ---------------------------------------------------------------------

"""
TODO:
- Ask independently for a disk warning threshold
- Run df -P
- Keep filesystems at or above the threshold
- Print matching mount points and percentages
- Print the final alert count
- Handle ValueError

Concept focus:
threshold-based disk analysis
"""

# Write your code below this line




# ---------------------------------------------------------------------
# EXERCISE 7: Run free Safely
# ---------------------------------------------------------------------

"""
TODO:
- Check whether free exists
- Run:
  free -m
- Capture stdout and stderr
- Print return code
- Print the complete captured stdout
- Print SKIPPED when unavailable

Concept focus:
running free
"""

# Write your code below this line




# ---------------------------------------------------------------------
# EXERCISE 8: Parse the Mem Row
# ---------------------------------------------------------------------

"""
TODO:
- Independently run free -m
- Locate the line beginning with Mem:
- Extract:
  total
  used
  available
- Convert them to integers
- Print the three values with MB labels

Concept focus:
free output parsing
"""

# Write your code below this line




# ---------------------------------------------------------------------
# EXERCISE 9: Calculate Memory Usage
# ---------------------------------------------------------------------

"""
TODO:
- Independently run free -m
- Parse total and used memory
- Calculate used percentage
- Round to two decimal places
- Print HEALTHY below the selected threshold
- Print ATTENTION at or above the selected threshold
- Allow this exercise to collect its own threshold

Concept focus:
memory calculation + decision
"""

# Write your code below this line




# ---------------------------------------------------------------------
# EXERCISE 10: Run uptime
# ---------------------------------------------------------------------

"""
TODO:
- Check whether uptime exists
- Run uptime
- Capture output
- Print the output without its final newline
- Print the return code
- Handle TimeoutExpired and OSError

Concept focus:
running uptime
"""

# Write your code below this line




# ---------------------------------------------------------------------
# EXERCISE 11: Parse Load Averages
# ---------------------------------------------------------------------

"""
TODO:
- Independently run uptime
- Support both labels:
  load average:
  load averages:
- Extract up to three load values
- Convert them to floats
- Print the final list

Concept focus:
uptime output processing
"""

# Write your code below this line




# ---------------------------------------------------------------------
# EXERCISE 12: Run ps and Capture Top Rows
# ---------------------------------------------------------------------

"""
TODO:
- Check whether ps exists
- Run:
  ps -eo pid,comm,%cpu,%mem --sort=-%cpu
- Capture output
- Print the header
- Print only the first five process rows
- Handle command failure safely

Concept focus:
running ps
"""

# Write your code below this line




# ---------------------------------------------------------------------
# EXERCISE 13: Convert ps Rows into Dictionaries
# ---------------------------------------------------------------------

"""
TODO:
- Independently run the ps command used above
- Parse the first five process rows
- Convert each row into a dictionary with:
  pid
  command
  cpu_percent
  memory_percent
- Store dictionaries in a list
- Print the list one dictionary per line

Concept focus:
structured process data
"""

# Write your code below this line




# ---------------------------------------------------------------------
# EXERCISE 14: Filter High-CPU Processes
# ---------------------------------------------------------------------

"""
TODO:
- Independently ask for a CPU threshold
- Run and parse ps output
- Keep processes whose CPU percentage is at or above the threshold
- Print process name, PID, and CPU percentage
- Print the final matching count

Concept focus:
process filtering
"""

# Write your code below this line




# ---------------------------------------------------------------------
# EXERCISE 15: Build a Compact Linux Check Summary
# ---------------------------------------------------------------------

"""
TODO:
- Independently check availability of df, free, uptime, and ps
- Run each available command once
- Record for every command:
  status
  return code
  first meaningful output line or error
- Print a compact four-command summary
- Do not parse detailed metrics in this exercise

Concept focus:
multi-command reporting
"""

# Write your code below this line




# ---------------------------------------------------------------------
# EXERCISE 16: Mini Project - Linux Health Snapshot
# ---------------------------------------------------------------------

"""
Build a complete Linux Health Snapshot.

Collect all required user inputs once at the beginning:
1. Server label
2. Disk warning threshold
3. Memory warning threshold
4. Process CPU threshold
5. Number of top processes to display

TODO:
- Normalize and validate the server label
- Convert thresholds to numeric values
- Convert top-process count to an integer
- Reject thresholds outside 0 to 100
- Reject a top-process count below 1
- Check availability of:
    df
    free
    uptime
    ps
- Build each command list once
- Run each available command only once
- Use:
    capture_output=True
    text=True
    timeout=<reasonable value>
- Capture for every command:
    status
    return code
    stdout
    stderr
- Parse df -P output
- Build a list of filesystem dictionaries
- Identify disk alerts at or above the disk threshold
- Parse free -m output
- Extract total, used, and available memory
- Calculate memory usage percentage
- Decide memory HEALTHY or ATTENTION
- Parse uptime output
- Extract up to three load averages
- Parse ps output
- Build process dictionaries
- Keep only the requested number of top processes
- Identify processes at or above the CPU threshold
- Count:
    commands available
    commands successful
    disk filesystems checked
    disk alerts
    process rows parsed
    high-CPU processes
- Decide final status:
    HEALTHY when all commands succeed and no threshold is breached
    ATTENTION when one or more thresholds are breached
    PARTIAL when some commands are unavailable or fail
    UNAVAILABLE when no required command can run
    INVALID INPUT when validation fails
- Handle:
    ValueError
    subprocess.TimeoutExpired
    OSError
- Generate a clean final report containing:
    server label
    thresholds
    command statuses
    disk summary
    memory summary
    load averages
    top process list
    high-CPU process list
    all counts
    exception messages
    final status
- Show <empty> or NOT AVAILABLE for unavailable values
- Do not ask for the same input more than once

Important:
- Do not use shell=True.
- Do not run destructive or administrative commands.
- The final result should feel like one complete operational workflow.
"""

# Write your code below this line




print("\nEnd of Day 31 exercises. Complete the TODO sections one by one.")
