"""
Python for Mammals - Day 23 Exercise File
Topic: JSON Files

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
By the end of these exercises, you should be able to use Python's json module
to create JSON files, read JSON files, update structured data, use load(),
use dump(), and create small configuration/report files for automation.
"""

print("=" * 70)
print("DAY 23 EXERCISES - JSON FILES")
print("json module, load(), dump()")
print("=" * 70)

# ---------------------------------------------------------------------
# EXERCISE 1: Import the json Module
# ---------------------------------------------------------------------

"""
TODO:
- Import the json module
- Print a message that says:
  JSON module imported successfully

Concept focus:
importing built-in modules
"""

# Write your code below this line




# ---------------------------------------------------------------------
# EXERCISE 2: Create a Simple Server Dictionary
# ---------------------------------------------------------------------

"""
TODO:
- Create a dictionary named server_status
- Include these keys:
  server, environment, status
- Use any practical values
- Print the dictionary

Concept focus:
Python dictionary as JSON-ready data
"""

# Write your code below this line




# ---------------------------------------------------------------------
# EXERCISE 3: Write a Simple JSON File using dump()
# ---------------------------------------------------------------------

"""
TODO:
- Create a file named exercise23_server_status.json
- Write the server_status dictionary into the file using json.dump()
- Use indent=4
- Print a success message after creating the file

Concept focus:
json.dump, writing JSON files
"""

# Write your code below this line




# ---------------------------------------------------------------------
# EXERCISE 4: Read a JSON File using load()
# ---------------------------------------------------------------------

"""
TODO:
- Open exercise23_server_status.json in read mode
- Read it using json.load()
- Store the result in a variable
- Print the loaded data

Concept focus:
json.load, reading JSON files
"""

# Write your code below this line




# ---------------------------------------------------------------------
# EXERCISE 5: Print Values from Loaded JSON
# ---------------------------------------------------------------------

"""
TODO:
- Read exercise23_server_status.json again
- Print clean output like:
  Server app01 is running in production

Concept focus:
accessing dictionary values after json.load()
"""

# Write your code below this line




# ---------------------------------------------------------------------
# EXERCISE 6: Create Nested JSON Data
# ---------------------------------------------------------------------

"""
TODO:
- Create a dictionary named server_inventory
- Include:
  server
  environment
  owner_team
  resources
- resources should be another dictionary with:
  cpu_count, memory_gb, disk_total_gb, disk_used_gb
- Write this data into exercise23_inventory.json using json.dump()
- Use indent=4

Concept focus:
nested dictionaries and JSON structure
"""

# Write your code below this line




# ---------------------------------------------------------------------
# EXERCISE 7: Read Nested JSON Values
# ---------------------------------------------------------------------

"""
TODO:
- Read exercise23_inventory.json
- Print:
  server name
  environment
  CPU count
  memory GB
  disk used GB

Concept focus:
accessing nested JSON values
"""

# Write your code below this line




# ---------------------------------------------------------------------
# EXERCISE 8: Create JSON List of Backup Records
# ---------------------------------------------------------------------

"""
TODO:
- Create a list of dictionaries named backup_report
- Add at least 4 backup records
- Each record should have:
  database, backup_type, status
- Write it into exercise23_backup_report.json
- Use indent=4

Concept focus:
list of dictionaries in JSON
"""

# Write your code below this line




# ---------------------------------------------------------------------
# EXERCISE 9: Count Success and Failed Backups from JSON
# ---------------------------------------------------------------------

"""
TODO:
- Read exercise23_backup_report.json
- Count how many records have status success
- Count how many records have status failed
- Print both counts

Concept focus:
JSON reading + loop + conditions + counters
"""

# Write your code below this line




# ---------------------------------------------------------------------
# EXERCISE 10: Filter Failed Backup Records
# ---------------------------------------------------------------------

"""
TODO:
- Read exercise23_backup_report.json
- Print only records where status is failed
- Output should show database and backup_type
- If no backup failed, print a clear message

Concept focus:
filtering JSON records
"""

# Write your code below this line




# ---------------------------------------------------------------------
# EXERCISE 11: Create a JSON Config File
# ---------------------------------------------------------------------

"""
TODO:
- Create a dictionary named config
- Include these keys:
  report_name
  warning_threshold
  critical_threshold
  output_file
  notify_team
- Write it into exercise23_config.json using json.dump()
- Use indent=4

Concept focus:
JSON as script configuration
"""

# Write your code below this line




# ---------------------------------------------------------------------
# EXERCISE 12: Use JSON Config Values in Logic
# ---------------------------------------------------------------------

"""
TODO:
- Read exercise23_config.json
- Create a variable named current_usage with any number
- Use warning_threshold and critical_threshold from the JSON file
- Decide status:
  CRITICAL if current_usage >= critical_threshold
  WARNING if current_usage >= warning_threshold and below critical_threshold
  HEALTHY otherwise
- Print current usage and status

Concept focus:
using JSON config values in decisions
"""

# Write your code below this line




# ---------------------------------------------------------------------
# EXERCISE 13: Update Existing JSON Data
# ---------------------------------------------------------------------

"""
TODO:
- Read exercise23_inventory.json
- Add a new key named status with value reviewed
- Update disk_used_gb inside resources to a new value
- Write the updated data into exercise23_inventory_updated.json
- Use indent=4

Concept focus:
read JSON, modify Python data, write JSON again
"""

# Write your code below this line




# ---------------------------------------------------------------------
# EXERCISE 14: JSON with User Input
# ---------------------------------------------------------------------

"""
TODO:
- Ask the user for:
  1. Service name
  2. Environment
  3. Service status
  4. Owner team
- Store these values in a dictionary
- Write the dictionary into exercise23_service_status.json
- Use indent=4
- Print a success message

Concept focus:
input + JSON writing
"""

# Write your code below this line




# ---------------------------------------------------------------------
# EXERCISE 15: JSON with Basic Exception Handling
# ---------------------------------------------------------------------

"""
TODO:
- Ask the user for a JSON file name
- Try to open and read the file using json.load()
- Print the loaded data if the file exists and is valid JSON
- Handle FileNotFoundError with a friendly message
- Handle json.JSONDecodeError with a friendly message

Concept focus:
JSON reading + exception handling
"""

# Write your code below this line




# ---------------------------------------------------------------------
# EXERCISE 16: Mini Project - Server Health JSON Reporter
# ---------------------------------------------------------------------

"""
Build a small Server Health JSON Reporter.

Collect all required user inputs once at the beginning:
1. Server name
2. Environment name
3. CPU usage percent
4. Memory usage percent
5. Disk usage percent
6. JSON report file name

Then reuse those variables throughout the mini project.

TODO:
- Import json if not already imported
- Collect all required inputs once
- Convert CPU, memory, and disk usage into numbers
- Decide individual status for CPU, memory, and disk:
    CRITICAL if usage is greater than or equal to 90
    WARNING if usage is greater than or equal to 80 and less than 90
    HEALTHY if usage is less than 80
- Decide overall server status:
    CRITICAL if any one component is CRITICAL
    WARNING if no component is CRITICAL but at least one component is WARNING
    HEALTHY if all components are HEALTHY
- Create one dictionary with this structure idea:
    server
    environment
    overall_status
    metrics
        cpu
        memory
        disk
- Each metric should store usage_percent and status
- Write the dictionary into the JSON report file using json.dump()
- Use indent=4
- Read the same JSON file back using json.load()
- Print a clean final report on screen

Important:
- Collect each input only once.
- Reuse those variables throughout the project.
- Do not ask for the same input repeatedly.
- The mini project should feel like one complete JSON reporting workflow.

Concept focus:
real-world JSON report generation workflow
"""

# Write your code below this line




print("\nEnd of Day 23 exercises. Complete the TODO sections one by one.")
