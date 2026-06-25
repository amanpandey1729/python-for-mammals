"""
Python for Mammals - Day 15
Topic: Nested Data Structure

Audience:
- Complete beginners
- DBAs, Sysadmins, Support Engineers, Cloud Engineers, Monitoring Teams
- Anyone who wants Python for practical automation

Goal of Day 15:
By the end of today, you should be able to:
1. Understand why nested data is needed in real automation scripts
2. Create a list of dictionaries
3. Loop through a list of dictionaries
4. Access values inside nested records
5. Create a dictionary of lists
6. Use nested data to represent inventories, reports, alerts, and checks
7. Generate simple summary reports from structured data

Why this matters:
In real operational work, we rarely deal with only one record.

You may have:
- many servers
- many tickets
- many backup jobs
- many disk checks
- many alert records

A single dictionary can represent one server.
A list of dictionaries can represent many servers.

This is the bridge between beginner Python and real automation reports.
Later, when you work with CSV, JSON, Excel, APIs, or database query output,
you will often see data in nested structures.
"""

print("=" * 70)
print("DAY 15 - NESTED DATA STRUCTURE")
print("LIST OF DICTIONARIES, DICTIONARY OF LISTS, REAL-WORLD DATA")
print("=" * 70)

# ---------------------------------------------------------------------
# SECTION 1: Why Nested Data Matters
# ---------------------------------------------------------------------

print("\nSECTION 1: Why Nested Data Matters")

"""
Day 14 taught us dictionaries.
A dictionary is excellent for one record.

Example:
One server = one dictionary

But automation usually works with multiple records.
For multiple records, we combine lists and dictionaries.
"""

print("Nested data helps us store multiple structured records together.")

# ---------------------------------------------------------------------
# SECTION 2: One Dictionary Represents One Record
# ---------------------------------------------------------------------

print("\nSECTION 2: One Dictionary Represents One Record")

server = {
    "name": "app01",
    "environment": "production",
    "status": "active"
}

print("One server record:")
print(server)

"""
This dictionary represents one server.
It has multiple fields:
- name
- environment
- status
"""

# ---------------------------------------------------------------------
# SECTION 3: List of Dictionaries
# ---------------------------------------------------------------------

print("\nSECTION 3: List of Dictionaries")

servers = [
    {"name": "app01", "environment": "production", "status": "active"},
    {"name": "web01", "environment": "uat", "status": "active"},
    {"name": "batch01", "environment": "test", "status": "maintenance"}
]

print("Server inventory:")
print(servers)

"""
This is a list of dictionaries.

The list stores multiple records.
Each dictionary inside the list stores one structured record.

This pattern is extremely common in automation.
"""

# ---------------------------------------------------------------------
# SECTION 4: Access One Record from a List of Dictionaries
# ---------------------------------------------------------------------

print("\nSECTION 4: Access One Record from a List of Dictionaries")

servers = [
    {"name": "app01", "environment": "production", "status": "active"},
    {"name": "web01", "environment": "uat", "status": "active"},
    {"name": "batch01", "environment": "test", "status": "maintenance"}
]

first_server = servers[0]

print("First record:", first_server)
print("First server name:", first_server["name"])
print("First server status:", first_server["status"])

"""
servers[0] gives the first dictionary.
first_server["name"] reads the name from that dictionary.

Step by step:
1. Pick one record from the list
2. Read a key from that dictionary
"""

# ---------------------------------------------------------------------
# SECTION 5: Direct Access Inside Nested Data
# ---------------------------------------------------------------------

print("\nSECTION 5: Direct Access Inside Nested Data")

servers = [
    {"name": "app01", "environment": "production", "status": "active"},
    {"name": "web01", "environment": "uat", "status": "active"},
    {"name": "batch01", "environment": "test", "status": "maintenance"}
]

print("Second server name:", servers[1]["name"])
print("Third server environment:", servers[2]["environment"])

"""
servers[1]["name"] means:
- Go to index 1 in the list
- From that dictionary, read the name key

This is useful, but too much direct indexing can become hard to read.
For reports, loops are usually better.
"""

# ---------------------------------------------------------------------
# SECTION 6: Loop Through List of Dictionaries
# ---------------------------------------------------------------------

print("\nSECTION 6: Loop Through List of Dictionaries")

servers = [
    {"name": "app01", "environment": "production", "status": "active"},
    {"name": "web01", "environment": "uat", "status": "active"},
    {"name": "batch01", "environment": "test", "status": "maintenance"}
]

for server in servers:
    print(server["name"], "-", server["environment"], "-", server["status"])

"""
This is the most important pattern for today.

for server in servers:
    server becomes one dictionary at a time.

Then we can read:
server["name"]
server["environment"]
server["status"]
"""

# ---------------------------------------------------------------------
# SECTION 7: Generate a Server Inventory Report
# ---------------------------------------------------------------------

print("\nSECTION 7: Generate a Server Inventory Report")

servers = [
    {"name": "app01", "environment": "production", "os": "linux"},
    {"name": "db01", "environment": "production", "os": "linux"},
    {"name": "win01", "environment": "uat", "os": "windows"}
]

print("Server Inventory Report")
print("-" * 40)

for server in servers:
    print("Server     :", server["name"])
    print("Environment:", server["environment"])
    print("OS         :", server["os"])
    print("-" * 40)

# ---------------------------------------------------------------------
# SECTION 8: Count Records Based on a Condition
# ---------------------------------------------------------------------

print("\nSECTION 8: Count Records Based on a Condition")

servers = [
    {"name": "app01", "environment": "production", "status": "active"},
    {"name": "web01", "environment": "uat", "status": "active"},
    {"name": "batch01", "environment": "production", "status": "maintenance"},
    {"name": "test01", "environment": "test", "status": "active"}
]

production_count = 0

for server in servers:
    if server["environment"] == "production":
        production_count += 1

print("Production servers:", production_count)

"""
This is how reports become useful.
We can loop through structured records and count what matters.
"""

# ---------------------------------------------------------------------
# SECTION 9: Filter Records Based on Status
# ---------------------------------------------------------------------

print("\nSECTION 9: Filter Records Based on Status")

servers = [
    {"name": "app01", "status": "active"},
    {"name": "batch01", "status": "maintenance"},
    {"name": "oldweb01", "status": "retired"},
    {"name": "db01", "status": "active"}
]

print("Servers not active:")

for server in servers:
    if server["status"] != "active":
        print(server["name"], "=>", server["status"])

# ---------------------------------------------------------------------
# SECTION 10: Add Calculated Values to Each Dictionary
# ---------------------------------------------------------------------

print("\nSECTION 10: Add Calculated Values to Each Dictionary")

disks = [
    {"server": "app01", "total_gb": 100, "used_gb": 72},
    {"server": "db01", "total_gb": 500, "used_gb": 455},
    {"server": "web01", "total_gb": 200, "used_gb": 88}
]

for disk in disks:
    usage_percent = (disk["used_gb"] / disk["total_gb"]) * 100
    disk["usage_percent"] = round(usage_percent, 2)

print("Disk records after calculation:")
for disk in disks:
    print(disk)

"""
Each dictionary can be updated inside a loop.
This is how automation scripts enrich raw data with calculated fields.
"""

# ---------------------------------------------------------------------
# SECTION 11: Add Status to Each Record
# ---------------------------------------------------------------------

print("\nSECTION 11: Add Status to Each Record")

disks = [
    {"server": "app01", "usage_percent": 72},
    {"server": "db01", "usage_percent": 91},
    {"server": "web01", "usage_percent": 84}
]

for disk in disks:
    if disk["usage_percent"] >= 90:
        disk["status"] = "CRITICAL"
    elif disk["usage_percent"] >= 80:
        disk["status"] = "WARNING"
    else:
        disk["status"] = "OK"

for disk in disks:
    print(disk["server"], "-", disk["usage_percent"], "-", disk["status"])

# ---------------------------------------------------------------------
# SECTION 12: Dictionary of Lists
# ---------------------------------------------------------------------

print("\nSECTION 12: Dictionary of Lists")

monitoring_data = {
    "servers": ["app01", "db01", "web01"],
    "cpu_percent": [65, 82, 91],
    "memory_percent": [70, 76, 88]
}

print("Servers       :", monitoring_data["servers"])
print("CPU values    :", monitoring_data["cpu_percent"])
print("Memory values :", monitoring_data["memory_percent"])

"""
A dictionary of lists stores columns of related data.
This is useful when you receive data column-wise.

But for beginner automation reports, list of dictionaries is usually easier to read.
"""

# ---------------------------------------------------------------------
# SECTION 13: Loop Through Dictionary of Lists Using Index
# ---------------------------------------------------------------------

print("\nSECTION 13: Loop Through Dictionary of Lists Using Index")

monitoring_data = {
    "servers": ["app01", "db01", "web01"],
    "cpu_percent": [65, 82, 91],
    "memory_percent": [70, 76, 88]
}

for index in range(len(monitoring_data["servers"])):
    print(
        monitoring_data["servers"][index],
        "CPU:", monitoring_data["cpu_percent"][index],
        "Memory:", monitoring_data["memory_percent"][index]
    )

# ---------------------------------------------------------------------
# SECTION 14: Practical Example - Alert Records
# ---------------------------------------------------------------------

print("\nSECTION 14: Practical Example - Alert Records")

alerts = [
    {"alert_id": "A1001", "server": "app01", "severity": "HIGH"},
    {"alert_id": "A1002", "server": "db01", "severity": "CRITICAL"},
    {"alert_id": "A1003", "server": "web01", "severity": "LOW"}
]

print("High priority alerts:")
for alert in alerts:
    if alert["severity"] in ["HIGH", "CRITICAL"]:
        print(alert["alert_id"], "on", alert["server"], "=>", alert["severity"])

# ---------------------------------------------------------------------
# SECTION 15: Practical Example - Backup Job Summary
# ---------------------------------------------------------------------

print("\nSECTION 15: Practical Example - Backup Job Summary")

backup_jobs = [
    {"database": "PRODDB", "type": "FULL", "status": "SUCCESS"},
    {"database": "APPDB", "type": "ARCHIVELOG", "status": "SUCCESS"},
    {"database": "TESTDB", "type": "FULL", "status": "FAILED"}
]

success_count = 0
failed_count = 0

for job in backup_jobs:
    if job["status"] == "SUCCESS":
        success_count += 1
    elif job["status"] == "FAILED":
        failed_count += 1

print("Successful backups:", success_count)
print("Failed backups    :", failed_count)

# ---------------------------------------------------------------------
# SECTION 16: Guided Practice - Create Your Own List of Dictionaries
# ---------------------------------------------------------------------

print("\nSECTION 16: Guided Practice - Create Your Own List of Dictionaries")

"""
Uncomment this block and run it.
Create your own small server inventory.
"""

# my_servers = [
#     {"name": "server01", "environment": "dev"},
#     {"name": "server02", "environment": "test"}
# ]
#
# for server in my_servers:
#     print(server["name"], "belongs to", server["environment"])

print("Guided practice: uncomment the list of dictionaries block.")

# ---------------------------------------------------------------------
# SECTION 17: Guided Practice - Update Each Record
# ---------------------------------------------------------------------

print("\nSECTION 17: Guided Practice - Update Each Record")

"""
Uncomment this block and run it.
Add a default checked value to every server record.
"""

# checks = [
#     {"server": "app01", "status": "OK"},
#     {"server": "db01", "status": "WARNING"}
# ]
#
# for check in checks:
#     check["checked"] = True
#
# print(checks)

print("Guided practice: uncomment the update each record block.")

# ---------------------------------------------------------------------
# SECTION 18: Practical Program 1 - Inventory Summary
# ---------------------------------------------------------------------

print("\nSECTION 18: Practical Program 1 - Inventory Summary")

inventory = [
    {"server": "app01", "environment": "production", "owner": "app-team"},
    {"server": "db01", "environment": "production", "owner": "database-team"},
    {"server": "web01", "environment": "uat", "owner": "web-team"}
]

print("Inventory Summary")
print("-" * 35)
for item in inventory:
    print("Server:", item["server"], "| Environment:", item["environment"], "| Owner:", item["owner"])

# ---------------------------------------------------------------------
# SECTION 19: Practical Program 2 - Disk Report from Nested Records
# ---------------------------------------------------------------------

print("\nSECTION 19: Practical Program 2 - Disk Report from Nested Records")

disk_checks = [
    {"server": "app01", "mount": "/app", "total_gb": 100, "used_gb": 72},
    {"server": "db01", "mount": "/data", "total_gb": 500, "used_gb": 455},
    {"server": "web01", "mount": "/logs", "total_gb": 200, "used_gb": 166}
]

for check in disk_checks:
    usage_percent = (check["used_gb"] / check["total_gb"]) * 100
    check["usage_percent"] = round(usage_percent, 2)

    if check["usage_percent"] >= 90:
        check["status"] = "CRITICAL"
    elif check["usage_percent"] >= 80:
        check["status"] = "WARNING"
    else:
        check["status"] = "OK"

print("Disk Report")
print("-" * 50)
for check in disk_checks:
    print(check["server"], check["mount"], check["usage_percent"], check["status"])

# ---------------------------------------------------------------------
# SECTION 20: Mini Project - Daily Operations Nested Report
# ---------------------------------------------------------------------

print("\nSECTION 20: Mini Project - Daily Operations Nested Report")

"""
This mini project uses fixed values so the file can run without stopping
for user input.

In Day15_Exercise.py, you will build your own version using input().
"""

daily_checks = [
    {"server": "app01", "environment": "production", "cpu": 76, "memory": 68, "disk": 81},
    {"server": "db01", "environment": "production", "cpu": 92, "memory": 85, "disk": 91},
    {"server": "web01", "environment": "uat", "cpu": 45, "memory": 58, "disk": 63}
]

critical_count = 0
warning_count = 0
ok_count = 0

for check in daily_checks:
    highest_usage = max(check["cpu"], check["memory"], check["disk"])
    check["highest_usage"] = highest_usage

    if highest_usage >= 90:
        check["status"] = "CRITICAL"
        check["action"] = "Immediate review required"
        critical_count += 1
    elif highest_usage >= 80:
        check["status"] = "WARNING"
        check["action"] = "Monitor closely"
        warning_count += 1
    else:
        check["status"] = "OK"
        check["action"] = "No action required"
        ok_count += 1

print("Daily Operations Nested Report")
print("=" * 50)
for check in daily_checks:
    print("Server        :", check["server"])
    print("Environment   :", check["environment"])
    print("Highest Usage :", check["highest_usage"])
    print("Status        :", check["status"])
    print("Action        :", check["action"])
    print("-" * 50)

print("Summary")
print("Critical:", critical_count)
print("Warning :", warning_count)
print("OK      :", ok_count)
print("=" * 50)

# ---------------------------------------------------------------------
# SECTION 21: Homework
# ---------------------------------------------------------------------

print("\nSECTION 21: Homework")

"""
Homework:
1. Create a list of 3 ticket dictionaries.
2. Each ticket should have ticket_id, priority, owner, and status.
3. Loop through the list and print only open tickets.
4. Create a list of 3 disk check dictionaries.
5. Calculate usage percentage for each disk record.
6. Add a status field to each disk record.
7. Print a clean summary report.

Community discussion question:
Where do you see nested data in your daily work?
Examples: Excel rows, CSV files, JSON reports, API output, monitoring alerts,
server inventory, backup reports, or ticket exports.
"""

print("Homework assigned. Practice nested data with real operational records.")

# ---------------------------------------------------------------------
# CLOSING MESSAGE
# ---------------------------------------------------------------------

print("\nDay 15 complete.")
print("You can now represent multiple structured records using nested data.")
print("This skill prepares you for CSV, JSON, Excel, APIs, and real automation reports.")
