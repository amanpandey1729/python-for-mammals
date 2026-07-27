"""
Python for Mammals - Day 32 Exercise File
Topic: Configuration Files - Storing Settings and Reading Configuration

Instructions:
1. Do not look for solutions immediately.
2. Read each task carefully.
3. Write your code below each exercise.
4. Run the file after completing each exercise.
5. Keep practice credentials and secrets out of configuration files.

Important:
This file contains exercises only.
No complete solutions are provided here.

Goal:
By the end of these exercises, you should be able to create, read, convert,
validate, and use INI configuration settings in practical automation workflows.
"""

print("=" * 70)
print("DAY 32 EXERCISES - CONFIGURATION FILES")
print("Storing settings and reading configuration")
print("=" * 70)

# ---------------------------------------------------------------------
# EXERCISE 1: Import Required Tools
# ---------------------------------------------------------------------

"""
TODO:
- Import ConfigParser from configparser
- Import Path from pathlib
- Print a short confirmation message

Concept focus:
configuration modules
"""

# Write your code below this line




# ---------------------------------------------------------------------
# EXERCISE 2: Create a Simple INI File
# ---------------------------------------------------------------------

"""
TODO:
- Independently create a Path named settings.ini
- Store this content in it:

  [application]
  name = Daily Reporter
  environment = test

- Use write_text() with UTF-8
- Print the filename and whether it exists

Concept focus:
storing settings
"""

# Write your code below this line




# ---------------------------------------------------------------------
# EXERCISE 3: Read a Required Configuration File
# ---------------------------------------------------------------------

"""
TODO:
- Independently create a ConfigParser object
- Read settings.ini with UTF-8
- Store the list returned by read()
- Print how many files were successfully read
- Print CONFIGURATION MISSING when the list is empty

Concept focus:
reading configuration
"""

# Write your code below this line




# ---------------------------------------------------------------------
# EXERCISE 4: List Configuration Sections
# ---------------------------------------------------------------------

"""
TODO:
- Independently read settings.ini
- Print all normal section names
- Print the number of sections
- Handle the case where no file is loaded

Concept focus:
section discovery
"""

# Write your code below this line




# ---------------------------------------------------------------------
# EXERCISE 5: Read Application Settings
# ---------------------------------------------------------------------

"""
TODO:
- Independently read settings.ini
- Read:
    application name
    environment
- Print both values with clear labels
- Handle a missing file, section, or key safely

Concept focus:
section and key access
"""

# Write your code below this line




# ---------------------------------------------------------------------
# EXERCISE 6: Use an Optional Fallback
# ---------------------------------------------------------------------

"""
TODO:
- Independently read settings.ini
- Read [application] owner
- Use "Operations Team" as the fallback
- Print the final owner value

Concept focus:
fallback values
"""

# Write your code below this line




# ---------------------------------------------------------------------
# EXERCISE 7: Read an Integer Threshold
# ---------------------------------------------------------------------

"""
TODO:
- Independently create or read a configuration containing:

  [monitoring]
  disk_threshold = 80

- Use getint() to read disk_threshold
- Print its value and Python type
- Handle ValueError and missing configuration data

Concept focus:
typed integer settings
"""

# Write your code below this line




# ---------------------------------------------------------------------
# EXERCISE 8: Read a Boolean Feature Switch
# ---------------------------------------------------------------------

"""
TODO:
- Independently create or read a configuration containing:

  [monitoring]
  alerts_enabled = yes

- Use getboolean()
- Print whether alerts are enabled
- Change yes to no and test again
- Handle an invalid boolean value safely

Concept focus:
boolean settings
"""

# Write your code below this line




# ---------------------------------------------------------------------
# EXERCISE 9: Check Required Sections
# ---------------------------------------------------------------------

"""
TODO:
- Independently read a configuration file
- Required sections:
    application
    monitoring
    report
- Use has_section()
- Print FOUND or MISSING for each section

Concept focus:
section validation
"""

# Write your code below this line




# ---------------------------------------------------------------------
# EXERCISE 10: Check Required Options
# ---------------------------------------------------------------------

"""
TODO:
- Independently read a configuration file
- Required [report] options:
    folder
    filename
- Use has_option()
- Print FOUND or MISSING for each option

Concept focus:
option validation
"""

# Write your code below this line




# ---------------------------------------------------------------------
# EXERCISE 11: Validate Threshold Range
# ---------------------------------------------------------------------

"""
TODO:
- Independently read disk_threshold from [monitoring]
- Convert it with getint()
- Accept values from 0 through 100
- Print VALID or INVALID RANGE
- Handle missing and non-numeric values

Concept focus:
value validation
"""

# Write your code below this line




# ---------------------------------------------------------------------
# EXERCISE 12: Validate an Allowed Environment
# ---------------------------------------------------------------------

"""
TODO:
- Independently read [application] environment
- Normalize it with strip() and lower()
- Allow only:
    development
    test
    staging
    production
- Print VALID or INVALID
- Display the normalized value

Concept focus:
allowed-value validation
"""

# Write your code below this line




# ---------------------------------------------------------------------
# EXERCISE 13: Convert a Section to a Dictionary
# ---------------------------------------------------------------------

"""
TODO:
- Independently read a [monitoring] section
- Convert that section into a dictionary
- Print one key and value per line
- Print the number of settings
- Remember that dictionary values remain strings

Concept focus:
mapping-style configuration
"""

# Write your code below this line




# ---------------------------------------------------------------------
# EXERCISE 14: Use Shared DEFAULT Settings
# ---------------------------------------------------------------------

"""
TODO:
- Independently create configuration with:

  [DEFAULT]
  timeout_seconds = 10
  team = Operations

  [disk_check]
  threshold = 80

  [memory_check]
  threshold = 85

- Read timeout_seconds through both normal sections
- Read team through both normal sections
- Print the inherited values

Concept focus:
DEFAULT inheritance
"""

# Write your code below this line




# ---------------------------------------------------------------------
# EXERCISE 15: Build a Reusable Configuration Loader
# ---------------------------------------------------------------------

"""
TODO:
- Write a function that accepts a configuration path
- Create and read a ConfigParser object inside the function
- Raise or report a clear error when no file is loaded
- Catch malformed INI syntax
- Return the parser only when loading succeeds
- Test it with:
    an existing valid file
    a missing file
    an invalid file

Concept focus:
reusable loading and error handling
"""

# Write your code below this line




# ---------------------------------------------------------------------
# EXERCISE 16: Mini Project - Configuration-Driven Operations Report
# ---------------------------------------------------------------------

"""
Build a complete Configuration-Driven Operations Report.

Collect all required user inputs once at the beginning:
1. Configuration filename
2. Observed server name
3. Observed environment
4. Observed disk usage percentage
5. Observed memory usage percentage

The configuration file should contain:

[application]
name = Daily Operations Reporter
environment = production
owner = Operations Team

[monitoring]
disk_threshold = 80
memory_threshold = 85
alerts_enabled = yes

[report]
folder = reports
filename = operations_summary.txt
include_timestamp = yes

TODO:
- Store every collected input in a variable once
- Convert observed percentages to numeric values
- Build the configuration path with pathlib.Path
- Read the configuration only once
- Verify that the file was successfully loaded
- Validate required sections:
    application
    monitoring
    report
- Validate every required key listed above
- Reject blank required values
- Read thresholds with getint()
- Read feature switches with getboolean()
- Reject thresholds outside 0 to 100
- Normalize and validate configured environment
- Normalize the observed environment
- Decide whether the observation belongs to the configured environment
- Compare disk usage with the configured disk threshold
- Compare memory usage with the configured memory threshold
- Respect alerts_enabled:
    when enabled, list threshold breaches
    when disabled, suppress alert details but still calculate health
- Create the configured report folder when all settings are valid
- Build one final report containing:
    application name
    owner
    configured environment
    observed server
    observed environment
    disk threshold and observed disk usage
    memory threshold and observed memory usage
    alert switch
    environment match status
    disk status
    memory status
    alert count
    report destination
    final status
    all validation or exception messages
- Decide final status:
    HEALTHY when the environment matches and no threshold is breached
    ATTENTION when the environment matches and a threshold is breached
    SKIPPED when the observation belongs to another environment
    INVALID CONFIG when required configuration is missing or invalid
    INVALID INPUT when user input is invalid
- Handle:
    ValueError
    OSError
    malformed configuration syntax
    missing sections
    missing options
- Do not ask for the same input more than once
- Do not put passwords, tokens, or private keys in the INI file
- The result should feel like one complete operational workflow

Concept focus:
configuration-driven automation
"""

# Write your code below this line




print("\nEnd of Day 32 exercises. Complete the TODO sections one by one.")
