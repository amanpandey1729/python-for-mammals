"""
Python for Mammals - Day 33 Exercise File
Mini Project #4: Linux Health Check Script

Checks:
- CPU
- Memory
- Disk

Instructions:
1. Complete the TODO sections in order.
2. Each normal exercise is independent.
3. Do not search for complete solutions immediately.
4. Use only read-only Linux commands.
5. Never use shell=True.
6. Use timeouts when running commands.

Important:
This file contains exercises only.
No complete solutions are provided.

Goal:
Build confidence in the individual parts of a Linux health check before
assembling them into one complete operational script.
"""

print("=" * 70)
print("DAY 33 EXERCISES - MINI PROJECT #4")
print("LINUX HEALTH CHECK SCRIPT")
print("CPU, memory, and disk")
print("=" * 70)

# ---------------------------------------------------------------------
# EXERCISE 1: Define Health Thresholds
# ---------------------------------------------------------------------

"""
TODO:
- Independently ask for:
    CPU warning threshold
    Memory warning threshold
    Disk warning threshold
- Convert all values to floats
- Validate that every threshold is between 0 and 100
- Print VALID or INVALID INPUT
- Handle ValueError

Concept focus:
input validation
"""

# Write your code below this line




# ---------------------------------------------------------------------
# EXERCISE 2: Calculate CPU Pressure
# ---------------------------------------------------------------------

"""
TODO:
- Independently ask for:
    one-minute load average
    logical CPU count
- Calculate:
    load average / CPU count * 100
- Round to two decimal places
- Reject a CPU count below 1
- Print the estimated CPU pressure percentage

Concept focus:
CPU calculation
"""

# Write your code below this line




# ---------------------------------------------------------------------
# EXERCISE 3: Parse Sample uptime Output
# ---------------------------------------------------------------------

"""
TODO:
- Use an independent sample uptime string containing:
    load average: 1.25, 0.95, 0.70
- Extract all three load values
- Convert them to floats
- Print the final list
- Also support the text:
    load averages:

Concept focus:
uptime parsing
"""

# Write your code below this line




# ---------------------------------------------------------------------
# EXERCISE 4: Parse Sample Memory Output
# ---------------------------------------------------------------------

"""
TODO:
- Use an independent multiline string representing free -m output
- Locate the Mem: row
- Extract:
    total memory
    used memory
    available memory
- Convert the values to integers
- Calculate used percentage
- Print all four values
- Handle missing or incomplete Mem: rows

Concept focus:
memory parsing
"""

# Write your code below this line




# ---------------------------------------------------------------------
# EXERCISE 5: Parse Sample Disk Output
# ---------------------------------------------------------------------

"""
TODO:
- Use an independent multiline string representing df -P output
- Ignore the header
- Extract for each valid row:
    filesystem
    usage percentage
    mount point
- Convert usage percentage to an integer
- Store every filesystem as a dictionary
- Print one dictionary per line

Concept focus:
disk parsing
"""

# Write your code below this line




# ---------------------------------------------------------------------
# EXERCISE 6: Apply One Health Rule
# ---------------------------------------------------------------------

"""
TODO:
- Independently ask for:
    observed usage percentage
    warning threshold
- Print:
    HEALTHY when observed usage is below the threshold
    ATTENTION when observed usage is at or above the threshold
- Validate both numbers are between 0 and 100

Concept focus:
threshold decision
"""

# Write your code below this line




# ---------------------------------------------------------------------
# EXERCISE 7: Find Disk Alerts
# ---------------------------------------------------------------------

"""
TODO:
- Independently create a list of filesystem dictionaries
- Ask for a disk threshold
- Keep filesystems at or above that threshold
- Print each matching mount point and percentage
- Print the number of alerts
- Print HEALTHY when there are no matching filesystems

Concept focus:
list filtering
"""

# Write your code below this line




# ---------------------------------------------------------------------
# EXERCISE 8: Decide Overall Status
# ---------------------------------------------------------------------

"""
TODO:
- Independently create statuses for:
    CPU
    Memory
    Disk
- Allowed values:
    HEALTHY
    ATTENTION
- Decide:
    HEALTHY when all three are HEALTHY
    ATTENTION when at least one is ATTENTION
- Print the names of components requiring attention

Concept focus:
combined status
"""

# Write your code below this line




# ---------------------------------------------------------------------
# EXERCISE 9: Check Command Availability
# ---------------------------------------------------------------------

"""
TODO:
- Independently check availability of:
    uptime
    free
    df
- Use shutil.which()
- Print AVAILABLE or UNAVAILABLE for each command
- Do not run the commands yet

Concept focus:
safe command discovery
"""

# Write your code below this line




# ---------------------------------------------------------------------
# EXERCISE 10: Build a Safe Command Runner
# ---------------------------------------------------------------------

"""
TODO:
- Independently write a function accepting:
    command list
    timeout
- Check whether the executable exists
- Run the command with:
    capture_output=True
    text=True
    timeout=<value>
    check=False
- Return a dictionary containing:
    status
    return_code
    stdout
    stderr
- Handle:
    unavailable command
    TimeoutExpired
    OSError
    non-zero return code
- Test with one read-only command

Concept focus:
reusable subprocess execution
"""

# Write your code below this line




# ---------------------------------------------------------------------
# EXERCISE 11: Build a Compact Component Report
# ---------------------------------------------------------------------

"""
TODO:
- Independently create values for:
    server label
    CPU pressure and status
    memory usage and status
    disk alert count and status
    overall status
- Build a list of formatted report lines
- Join the lines with newline characters
- Print one compact report

Concept focus:
report construction
"""

# Write your code below this line




# ---------------------------------------------------------------------
# EXERCISE 12: Save a Health Report
# ---------------------------------------------------------------------

"""
TODO:
- Independently ask for:
    output folder
    report filename
- Create the folder with pathlib.Path
- Build a short sample health report
- Save it with UTF-8 encoding
- Print the final report path
- Handle OSError

Concept focus:
report file output
"""

# Write your code below this line




# ---------------------------------------------------------------------
# EXERCISE 13: Mini Project - Linux Health Check Script
# ---------------------------------------------------------------------

"""
Build one complete Linux Health Check Script.

Collect all required user inputs once at the beginning:
1. Server label
2. CPU warning threshold
3. Memory warning threshold
4. Disk warning threshold
5. Command timeout in seconds
6. Output folder
7. Report filename

Reuse these variables throughout the project.

Configuration and validation:
- Normalize the server label
- Convert thresholds to floats
- Convert timeout to an integer
- Reject blank server labels
- Reject thresholds outside 0 to 100
- Reject timeout values below 1
- Build the output path with pathlib.Path
- Do not request the same input more than once

Command safety:
- Check availability of:
    uptime
    free
    df
- Run each available command only once
- Use command lists, not command strings
- Use:
    capture_output=True
    text=True
    timeout=<configured value>
    check=False
- Never use shell=True
- Handle:
    subprocess.TimeoutExpired
    OSError
    non-zero return codes
    unavailable commands

CPU check:
- Discover logical CPU count with os.cpu_count()
- Parse one-minute, five-minute, and fifteen-minute load averages
- Calculate estimated CPU pressure:
    one-minute load / logical CPU count * 100
- Round to two decimal places
- Compare with the configured CPU threshold
- Store CPU result in a dictionary

Memory check:
- Parse the Mem: row from free -m
- Extract total, used, and available memory
- Calculate memory usage percentage
- Compare with the configured memory threshold
- Store memory result in a dictionary

Disk check:
- Parse every valid filesystem row from df -P
- Create one dictionary per filesystem
- Identify filesystems at or above the disk threshold
- Store:
    filesystems checked
    alert count
    alert details
    disk status

Final decision:
- HEALTHY:
    all commands succeed and no threshold is breached
- ATTENTION:
    all commands succeed and one or more thresholds are breached
- PARTIAL:
    at least one command is unavailable, times out, or fails while another
    command succeeds
- UNAVAILABLE:
    no required command succeeds
- INVALID INPUT:
    collected input is invalid

Final report:
- Include:
    timestamp
    server label
    configured thresholds
    logical CPU count
    load averages
    estimated CPU pressure
    CPU status
    total, used, and available memory
    memory usage percentage
    memory status
    every filesystem and usage percentage
    disk alert details
    command statuses and return codes
    successful command count
    failed or unavailable command count
    alert count
    final status
    validation and exception messages
- Show NOT AVAILABLE for unavailable metrics
- Create the configured output folder
- Save the report with UTF-8 encoding
- Print the final report and saved path
- The script must not crash because one command is missing
- The result should feel like one complete operational workflow

Optional extension:
- Read thresholds, timeout, output folder, and filename from an INI file
  instead of asking for them interactively.

Safety:
- Run only read-only commands
- Do not place passwords, tokens, or private keys in the report or code
"""

# Write your code below this line




print("\nEnd of Day 33 exercises. Complete the TODO sections one by one.")
