"""
Python for Mammals - Day 23
Topic: JSON Files

Audience:
- Complete beginners
- DBAs, Sysadmins, Support Engineers, Cloud Engineers, Monitoring Teams
- Anyone who wants Python for practical automation

Goal of Day 23:
By the end of today, you should be able to:
1. Understand what JSON is and why it is common in automation
2. Import and use Python's built-in json module
3. Store Python dictionaries and lists as JSON files using json.dump()
4. Read JSON files back into Python using json.load()
5. Understand the difference between JSON text and Python data
6. Use indentation to make JSON files human-readable
7. Update JSON data safely after reading it
8. Build small JSON-based configuration and report files

Why this matters:
JSON files are everywhere in modern IT operations.

You will see JSON in:
- application configuration files
- cloud resource exports
- API responses
- monitoring payloads
- server inventory data
- backup metadata
- deployment settings
- automation tool configuration

CSV is excellent for tables.
JSON is excellent for structured data.
Today you learn how Python can save and read structured operational data
using JSON files.
"""

import json

print("=" * 70)
print("DAY 23 - JSON FILES")
print("json module, load(), dump()")
print("=" * 70)

# ---------------------------------------------------------------------
# SECTION 1: Project Introduction
# ---------------------------------------------------------------------

print("\nSECTION 1: Project Introduction")

"""
JSON means JavaScript Object Notation.
Do not worry about the JavaScript part.
For us, JSON is simply a popular text format for storing structured data.

Example JSON:
{
    "server": "app01",
    "environment": "production",
    "status": "running"
}

It looks very similar to a Python dictionary.
That is why JSON feels natural after learning dictionaries.
"""

print("Today we will use JSON files to store configuration and operational data.")

# ---------------------------------------------------------------------
# SECTION 2: Why JSON Matters in Automation
# ---------------------------------------------------------------------

print("\nSECTION 2: Why JSON Matters in Automation")

"""
JSON is useful because it can store nested data.

CSV is good for flat rows and columns.
JSON is better when one item has many related details.

Common examples:
- Server configuration with CPU, memory, disk, and owner details
- API response from a cloud provider
- Monitoring alert with severity, metric, timestamp, and labels
- Backup metadata with database name, status, duration, and files
- Script configuration with paths, thresholds, and email recipients
"""

print("JSON helps Python exchange structured data with tools, APIs, and config files.")

# ---------------------------------------------------------------------
# SECTION 3: Importing the json Module
# ---------------------------------------------------------------------

print("\nSECTION 3: Importing the json Module")

"""
Python has a built-in json module.
You do not need to install anything.

We imported it at the top of this file:
import json
"""

print("json module imported successfully.")

# ---------------------------------------------------------------------
# SECTION 4: Python Dictionary to JSON File using dump()
# ---------------------------------------------------------------------

print("\nSECTION 4: Python Dictionary to JSON File using dump()")

server_status = {
    "server": "app01",
    "environment": "production",
    "status": "running"
}

with open("day23_server_status.json", "w") as file_object:
    json.dump(server_status, file_object, indent=4)

print("Created file: day23_server_status.json")

"""
Important details:
- open(..., "w") creates or overwrites the file
- json.dump() writes Python data into a JSON file
- indent=4 makes the JSON file easy for humans to read
"""

# ---------------------------------------------------------------------
# SECTION 5: Reading JSON File using load()
# ---------------------------------------------------------------------

print("\nSECTION 5: Reading JSON File using load()")

with open("day23_server_status.json", "r") as file_object:
    loaded_status = json.load(file_object)

print(loaded_status)

"""
json.load() reads a JSON file and converts it into Python data.
In this example, the JSON object becomes a Python dictionary.
"""

# ---------------------------------------------------------------------
# SECTION 6: Accessing Values from Loaded JSON
# ---------------------------------------------------------------------

print("\nSECTION 6: Accessing Values from Loaded JSON")

print("Server     :", loaded_status["server"])
print("Environment:", loaded_status["environment"])
print("Status     :", loaded_status["status"])

"""
After loading JSON, you can use normal dictionary access.
This is useful when your automation script reads a config file.
"""

# ---------------------------------------------------------------------
# SECTION 7: JSON with Nested Data
# ---------------------------------------------------------------------

print("\nSECTION 7: JSON with Nested Data")

server_inventory = {
    "server": "db01",
    "environment": "production",
    "owner_team": "database",
    "resources": {
        "cpu_count": 8,
        "memory_gb": 64,
        "disk_total_gb": 500,
        "disk_used_gb": 410
    },
    "services": ["listener", "database", "backup_agent"]
}

with open("day23_inventory.json", "w") as file_object:
    json.dump(server_inventory, file_object, indent=4)

print("Created file: day23_inventory.json")

"""
JSON can store:
- strings
- numbers
- lists
- dictionaries
- nested dictionaries
- boolean values
- null values

This makes JSON very useful for configuration and API-style data.
"""

# ---------------------------------------------------------------------
# SECTION 8: Reading Nested JSON
# ---------------------------------------------------------------------

print("\nSECTION 8: Reading Nested JSON")

with open("day23_inventory.json", "r") as file_object:
    inventory_data = json.load(file_object)

print("Server:", inventory_data["server"])
print("CPU Count:", inventory_data["resources"]["cpu_count"])
print("Memory GB:", inventory_data["resources"]["memory_gb"])
print("Services:", inventory_data["services"])

"""
Nested JSON becomes nested Python dictionaries and lists.
Use multiple keys to go deeper into the data.
"""

# ---------------------------------------------------------------------
# SECTION 9: JSON List of Dictionaries
# ---------------------------------------------------------------------

print("\nSECTION 9: JSON List of Dictionaries")

backup_report = [
    {"database": "salesdb", "backup_type": "full", "status": "success"},
    {"database": "hrdb", "backup_type": "archive", "status": "success"},
    {"database": "testdb", "backup_type": "full", "status": "failed"}
]

with open("day23_backup_report.json", "w") as file_object:
    json.dump(backup_report, file_object, indent=4)

print("Created file: day23_backup_report.json")

"""
A list of dictionaries is common in automation reports.
Each dictionary represents one item or one record.
"""

# ---------------------------------------------------------------------
# SECTION 10: Reading JSON and Counting Status Values
# ---------------------------------------------------------------------

print("\nSECTION 10: Reading JSON and Counting Status Values")

success_count = 0
failed_count = 0

with open("day23_backup_report.json", "r") as file_object:
    loaded_backup_report = json.load(file_object)

for backup in loaded_backup_report:
    if backup["status"] == "success":
        success_count += 1
    elif backup["status"] == "failed":
        failed_count += 1

print("Successful backups:", success_count)
print("Failed backups    :", failed_count)

"""
This pattern is very practical:
- read JSON
- loop through records
- check values
- count what matters
"""

# ---------------------------------------------------------------------
# SECTION 11: Updating JSON Data
# ---------------------------------------------------------------------

print("\nSECTION 11: Updating JSON Data")

with open("day23_inventory.json", "r") as file_object:
    inventory_data = json.load(file_object)

inventory_data["status"] = "reviewed"
inventory_data["resources"]["disk_used_gb"] = 430

with open("day23_inventory_updated.json", "w") as file_object:
    json.dump(inventory_data, file_object, indent=4)

print("Created file: day23_inventory_updated.json")

"""
Common JSON update workflow:
1. Read JSON using load()
2. Modify Python dictionary/list data
3. Write it back using dump()
"""

# ---------------------------------------------------------------------
# SECTION 12: Creating a JSON Config File
# ---------------------------------------------------------------------

print("\nSECTION 12: Creating a JSON Config File")

script_config = {
    "report_name": "daily_health_check",
    "warning_threshold": 80,
    "critical_threshold": 90,
    "output_file": "health_report.txt",
    "notify_team": True
}

with open("day23_config.json", "w") as file_object:
    json.dump(script_config, file_object, indent=4)

print("Created file: day23_config.json")

"""
Configuration files help avoid hardcoding values inside scripts.
Instead of editing Python code, you can edit JSON settings.
"""

# ---------------------------------------------------------------------
# SECTION 13: Using JSON Config Values in Logic
# ---------------------------------------------------------------------

print("\nSECTION 13: Using JSON Config Values in Logic")

with open("day23_config.json", "r") as file_object:
    config = json.load(file_object)

current_usage = 86

if current_usage >= config["critical_threshold"]:
    health_status = "CRITICAL"
elif current_usage >= config["warning_threshold"]:
    health_status = "WARNING"
else:
    health_status = "HEALTHY"

print("Current usage:", str(current_usage) + "%")
print("Health status:", health_status)

"""
This is a real automation pattern.
The script reads thresholds from a config file and then applies logic.
"""

# ---------------------------------------------------------------------
# SECTION 14: JSON + Exception Handling
# ---------------------------------------------------------------------

print("\nSECTION 14: JSON + Exception Handling")

try:
    with open("day23_config.json", "r") as file_object:
        config = json.load(file_object)
    print("Config loaded:", config["report_name"])
except FileNotFoundError:
    print("JSON config file not found.")
except json.JSONDecodeError:
    print("JSON file exists but contains invalid JSON.")

"""
JSON automation becomes safer when combined with exception handling.
FileNotFoundError handles missing files.
json.JSONDecodeError handles broken JSON syntax.
"""

# ---------------------------------------------------------------------
# SECTION 15: Important Difference - dump() vs load()
# ---------------------------------------------------------------------

print("\nSECTION 15: Important Difference - dump() vs load()")

"""
json.dump(data, file_object)
- Writes Python data into a JSON file
- Think: dump data out to a file

json.load(file_object)
- Reads JSON from a file into Python
- Think: load data into Python

Easy memory trick:
- dump = save
- load = read
"""

print("dump() saves Python data to JSON. load() reads JSON data into Python.")

# ---------------------------------------------------------------------
# SECTION 16: Guided Practice - Write Your Own JSON
# ---------------------------------------------------------------------

print("\nSECTION 16: Guided Practice - Write Your Own JSON")

"""
Uncomment this block and run it.
It collects one service record and writes it to a JSON file.
"""

# service_name = input("Enter service name: ")
# service_status = input("Enter service status: ")
# owner_team = input("Enter owner team: ")
#
# service_record = {
#     "service": service_name,
#     "status": service_status,
#     "owner_team": owner_team
# }
#
# with open("service_status.json", "w") as file_object:
#     json.dump(service_record, file_object, indent=4)
#
# print("Created service_status.json")

print("Guided practice: uncomment the service_status.json block.")

# ---------------------------------------------------------------------
# SECTION 17: Mini Challenge Preview
# ---------------------------------------------------------------------

print("\nSECTION 17: Mini Challenge Preview")

"""
Mini Challenge:
Build a Server Health JSON Reporter.

Your script should:
1. Collect server name, environment, CPU %, memory %, disk %, and JSON file name once
2. Decide CPU, memory, and disk status using thresholds
3. Create one structured dictionary
4. Write the dictionary into a JSON file
5. Read the JSON file back and print a clean report

This mirrors real automation:
- collect operational values
- convert them into structured data
- store them in a reusable JSON file
- read the file again for validation or reporting
"""

print("Mini challenge: build a Server Health JSON Reporter.")

# ---------------------------------------------------------------------
# SECTION 18: Closing Message
# ---------------------------------------------------------------------

print("\nSECTION 18: Closing Message")

print("You have completed Day 23.")
print("You can now read and write JSON files for configuration and structured reports.")
print("Next, you will keep improving how scripts exchange data with real-world systems.")
