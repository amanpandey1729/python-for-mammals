"""
Python for Mammals - Day 14
Topic: Dictionaries

Audience:
- Complete beginners
- DBAs, Sysadmins, Support Engineers, Cloud Engineers, Monitoring Teams
- Anyone who wants Python for practical automation

Goal of Day 14:
By the end of today, you should be able to:
1. Create dictionaries using key-value pairs
2. Understand why dictionaries are useful for structured operational data
3. Access values using keys
4. Update existing values
5. Add new key-value pairs
6. Loop through dictionary keys, values, and items
7. Use dictionaries in practical automation-style reports

Why this matters:
In real operational work, one value is rarely enough.
A server has a name, environment, CPU usage, memory usage, owner, and status.
A ticket has an ID, priority, assignee, and current state.
A backup has a database name, start time, end time, status, and size.

A dictionary allows us to store this kind of related information cleanly.
Instead of remembering index positions like list[0] or tuple[2], we can use meaningful keys:
server["name"]
server["environment"]
server["status"]

This makes automation scripts easier to read, easier to modify, and easier to convert into reports later.
"""

print("=" * 70)
print("DAY 14 - DICTIONARIES")
print("KEY-VALUE PAIRS, ACCESS, UPDATE, LOOPING")
print("=" * 70)

# ---------------------------------------------------------------------
# SECTION 1: Why Dictionaries Matter
# ---------------------------------------------------------------------

print("\nSECTION 1: Why Dictionaries Matter")

"""
Lists store values by position.
Tuples store fixed values by position.
Sets store unique values.

Dictionaries store values by name.

That is why dictionaries are excellent for automation reports.
They allow us to store data like this:
- server name
- environment
- CPU usage
- memory usage
- health status

Each value gets a meaningful label called a key.
"""

print("Dictionaries help us store structured data using meaningful names.")

# ---------------------------------------------------------------------
# SECTION 2: Creating a Dictionary
# ---------------------------------------------------------------------

print("\nSECTION 2: Creating a Dictionary")

server = {
    "name": "app01",
    "environment": "production",
    "os": "linux"
}

print("Server dictionary:", server)
print("Type             :", type(server))

"""
A dictionary uses curly braces {}.
Inside the dictionary, data is stored as key-value pairs.

Example:
"name" is the key
"app01" is the value

Together, this is one key-value pair:
"name": "app01"
"""

# ---------------------------------------------------------------------
# SECTION 3: Accessing Values Using Keys
# ---------------------------------------------------------------------

print("\nSECTION 3: Accessing Values Using Keys")

server = {
    "name": "app01",
    "environment": "production",
    "os": "linux"
}

print("Server name :", server["name"])
print("Environment :", server["environment"])
print("OS type     :", server["os"])

"""
In a list, we access values using index numbers.
In a dictionary, we access values using keys.

server["name"] is easier to understand than server[0].
This makes dictionaries very useful for readable automation scripts.
"""

# ---------------------------------------------------------------------
# SECTION 4: Dictionary Keys Should Be Meaningful
# ---------------------------------------------------------------------

print("\nSECTION 4: Dictionary Keys Should Be Meaningful")

backup_job = {
    "database": "PRODDB",
    "backup_type": "FULL",
    "status": "SUCCESS"
}

print("Database   :", backup_job["database"])
print("Backup Type:", backup_job["backup_type"])
print("Status     :", backup_job["status"])

"""
Good keys make your script self-explanatory.

Prefer:
"database"
"backup_type"
"status"

Avoid confusing keys like:
"x"
"value1"
"abc"

Readable keys are a gift to your future self.
"""

# ---------------------------------------------------------------------
# SECTION 5: Updating Dictionary Values
# ---------------------------------------------------------------------

print("\nSECTION 5: Updating Dictionary Values")

server_health = {
    "server": "web01",
    "cpu_percent": 65,
    "status": "OK"
}

print("Before update:", server_health)

server_health["cpu_percent"] = 92
server_health["status"] = "CRITICAL"

print("After update :", server_health)

"""
Dictionary values can be updated using the key.

Example:
server_health["status"] = "CRITICAL"

This is common in automation.
A script may start with default status as OK and later update it based on checks.
"""

# ---------------------------------------------------------------------
# SECTION 6: Adding a New Key-Value Pair
# ---------------------------------------------------------------------

print("\nSECTION 6: Adding a New Key-Value Pair")

server = {
    "name": "db01",
    "environment": "production"
}

print("Before adding:", server)

server["owner"] = "platform-team"
server["status"] = "active"

print("After adding :", server)

"""
If a key does not exist, assigning a value creates a new key-value pair.

This is useful when a script calculates something later.
Example:
- usage_percent
- health_status
- remarks
- action_required
"""

# ---------------------------------------------------------------------
# SECTION 7: Accessing Values Safely with get()
# ---------------------------------------------------------------------

print("\nSECTION 7: Accessing Values Safely with get()")

server = {
    "name": "app01",
    "environment": "uat"
}

print("Server name:", server.get("name"))
print("Owner      :", server.get("owner", "not assigned"))

"""
server["owner"] would fail if the key does not exist.

server.get("owner", "not assigned") is safer.
If owner exists, it returns the owner.
If owner does not exist, it returns "not assigned".

This prevents simple reporting scripts from crashing due to missing optional data.
"""

# ---------------------------------------------------------------------
# SECTION 8: Checking If a Key Exists
# ---------------------------------------------------------------------

print("\nSECTION 8: Checking If a Key Exists")

server = {
    "name": "app01",
    "environment": "production",
    "status": "active"
}

if "status" in server:
    print("Status key exists.")

if "owner" not in server:
    print("Owner key is missing.")

"""
The in operator can check whether a key exists in a dictionary.

This is useful before reading optional data from reports, files, APIs, or future JSON data.
"""

# ---------------------------------------------------------------------
# SECTION 9: Looping Through Dictionary Keys
# ---------------------------------------------------------------------

print("\nSECTION 9: Looping Through Dictionary Keys")

server = {
    "name": "app01",
    "environment": "production",
    "os": "linux"
}

for key in server:
    print("Key:", key)

"""
When you loop directly through a dictionary, Python gives you the keys.

This is useful when you want to inspect what fields exist in a record.
"""

# ---------------------------------------------------------------------
# SECTION 10: Looping Through Dictionary Values
# ---------------------------------------------------------------------

print("\nSECTION 10: Looping Through Dictionary Values")

server = {
    "name": "app01",
    "environment": "production",
    "os": "linux"
}

for value in server.values():
    print("Value:", value)

"""
values() gives only the values from the dictionary.

This is useful when you only care about the stored values and not the field names.
"""

# ---------------------------------------------------------------------
# SECTION 11: Looping Through Keys and Values Together
# ---------------------------------------------------------------------

print("\nSECTION 11: Looping Through Keys and Values Together")

server = {
    "name": "app01",
    "environment": "production",
    "os": "linux"
}

for key, value in server.items():
    print(key, "=>", value)

"""
items() gives both key and value together.

This is one of the most common dictionary loops.
It is excellent for printing readable reports.
"""

# ---------------------------------------------------------------------
# SECTION 12: Practical Example - Server Health Dictionary
# ---------------------------------------------------------------------

print("\nSECTION 12: Practical Example - Server Health Dictionary")

server_health = {
    "server": "app01",
    "cpu_percent": 72,
    "memory_percent": 68,
    "disk_percent": 81
}

print("Server Health Report")
print("-" * 35)
for key, value in server_health.items():
    print(key, ":", value)

# ---------------------------------------------------------------------
# SECTION 13: Practical Example - Update Health Status
# ---------------------------------------------------------------------

print("\nSECTION 13: Practical Example - Update Health Status")

server_health = {
    "server": "app01",
    "cpu_percent": 92,
    "memory_percent": 78,
    "disk_percent": 84,
    "status": "OK"
}

if server_health["cpu_percent"] >= 90:
    server_health["status"] = "CRITICAL"
elif server_health["disk_percent"] >= 80:
    server_health["status"] = "WARNING"
else:
    server_health["status"] = "OK"

print("Server:", server_health["server"])
print("CPU   :", server_health["cpu_percent"])
print("Disk  :", server_health["disk_percent"])
print("Status:", server_health["status"])

# ---------------------------------------------------------------------
# SECTION 14: Practical Example - Ticket Dictionary
# ---------------------------------------------------------------------

print("\nSECTION 14: Practical Example - Ticket Dictionary")

ticket = {
    "ticket_id": "INC1001",
    "priority": "P2",
    "owner": "support-team",
    "status": "open"
}

print("Ticket Summary")
print("-" * 30)
for key, value in ticket.items():
    print(key, ":", value)

# ---------------------------------------------------------------------
# SECTION 15: Practical Example - Backup Report Dictionary
# ---------------------------------------------------------------------

print("\nSECTION 15: Practical Example - Backup Report Dictionary")

backup_report = {
    "database": "PRODDB",
    "backup_type": "FULL",
    "size_gb": 480,
    "duration_minutes": 95,
    "status": "SUCCESS"
}

print("Backup Report")
print("-" * 30)
print("Database        :", backup_report["database"])
print("Backup Type     :", backup_report["backup_type"])
print("Size GB         :", backup_report["size_gb"])
print("Duration Minutes:", backup_report["duration_minutes"])
print("Status          :", backup_report["status"])

# ---------------------------------------------------------------------
# SECTION 16: Guided Practice - Create Your Own Dictionary
# ---------------------------------------------------------------------

print("\nSECTION 16: Guided Practice - Create Your Own Dictionary")

"""
Uncomment this block and run it.
Create your own server dictionary.
"""

# my_server = {
#     "name": "batch01",
#     "environment": "test",
#     "os": "linux"
# }
# print(my_server)
# print("Server Name:", my_server["name"])

print("Guided practice: uncomment the dictionary creation block.")

# ---------------------------------------------------------------------
# SECTION 17: Guided Practice - Update a Dictionary
# ---------------------------------------------------------------------

print("\nSECTION 17: Guided Practice - Update a Dictionary")

"""
Uncomment this block and run it.
Update the status value in a task dictionary.
"""

# task = {
#     "task_name": "daily backup check",
#     "status": "pending"
# }
# task["status"] = "completed"
# print(task)

print("Guided practice: uncomment the dictionary update block.")

# ---------------------------------------------------------------------
# SECTION 18: Practical Program 1 - Server Record Report
# ---------------------------------------------------------------------

print("\nSECTION 18: Practical Program 1 - Server Record Report")

server = {
    "name": "app01",
    "environment": "production",
    "owner": "app-team",
    "status": "active"
}

print("Server Record Report")
print("-" * 35)
for key, value in server.items():
    print(key, ":", value)

# ---------------------------------------------------------------------
# SECTION 19: Practical Program 2 - Disk Health Summary
# ---------------------------------------------------------------------

print("\nSECTION 19: Practical Program 2 - Disk Health Summary")

disk_check = {
    "server": "db01",
    "mount_point": "/u01",
    "total_gb": 500,
    "used_gb": 425
}

usage_percent = (disk_check["used_gb"] / disk_check["total_gb"]) * 100
disk_check["usage_percent"] = round(usage_percent, 2)

if disk_check["usage_percent"] >= 90:
    disk_check["status"] = "CRITICAL"
elif disk_check["usage_percent"] >= 80:
    disk_check["status"] = "WARNING"
else:
    disk_check["status"] = "OK"

print("Disk Health Summary")
print("-" * 35)
for key, value in disk_check.items():
    print(key, ":", value)

# ---------------------------------------------------------------------
# SECTION 20: Mini Project - Server Health Dictionary Report
# ---------------------------------------------------------------------

print("\nSECTION 20: Mini Project - Server Health Dictionary Report")

"""
This mini project uses fixed values so the file can run without stopping
for user input.

In Day14_Exercise.py, you will build your own version using input().
"""

server_health = {
    "server": "app01",
    "environment": "production",
    "cpu_percent": 88,
    "memory_percent": 76,
    "disk_percent": 91
}

highest_usage = max(
    server_health["cpu_percent"],
    server_health["memory_percent"],
    server_health["disk_percent"]
)

if highest_usage >= 90:
    server_health["status"] = "CRITICAL"
    server_health["action"] = "Immediate review required"
elif highest_usage >= 80:
    server_health["status"] = "WARNING"
    server_health["action"] = "Monitor closely"
else:
    server_health["status"] = "OK"
    server_health["action"] = "No action required"

print("Server Health Dictionary Report")
print("-" * 45)
for key, value in server_health.items():
    print(key, ":", value)
print("-" * 45)

# ---------------------------------------------------------------------
# CLOSING MESSAGE
# ---------------------------------------------------------------------

print("\nDay 14 completed.")
print("You can now store structured operational data using dictionaries.")
print("Next step: use dictionaries with nested data and real automation workflows.")
