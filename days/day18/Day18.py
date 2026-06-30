"""
Python for Mammals - Day 18
Topic: Mini Project #2 - Server Inventory Tracker

Audience:
- Complete beginners
- DBAs, Sysadmins, Support Engineers, Cloud Engineers, Monitoring Teams
- Anyone who wants Python for practical automation

Goal of Day 18:
By the end of today, you should be able to:
1. Build a small project using lists, dictionaries, and functions together
2. Represent server inventory records using dictionaries
3. Store multiple server records inside a list
4. Create reusable functions for adding, displaying, filtering, and summarizing inventory
5. Think like an automation engineer: collect data once, process it cleanly, report it clearly

Why this matters:
Almost every operations team maintains some form of inventory.

You may track:
- server names
- environments
- operating systems
- application ownership
- CPU and memory allocation
- disk capacity
- patch status
- backup coverage
- monitoring status

In real work, inventory may come from Excel, CSV, CMDB, monitoring tools,
cloud APIs, or manual input.

Today we will keep it simple and build the logic in plain Python.
This mini project joins three important building blocks:
- lists for storing many records
- dictionaries for storing one structured record
- functions for reusable project logic
"""

print("=" * 70)
print("DAY 18 - MINI PROJECT #2")
print("SERVER INVENTORY TRACKER")
print("LISTS, DICTIONARIES, FUNCTIONS")
print("=" * 70)

# ---------------------------------------------------------------------
# SECTION 1: Project Introduction
# ---------------------------------------------------------------------

print("\nSECTION 1: Project Introduction")

"""
A Server Inventory Tracker stores details about servers.

For example:
- app01 belongs to production
- db01 runs Linux
- web01 belongs to UAT
- backup01 is owned by infra team

The goal is not to build a big enterprise CMDB today.
The goal is to understand how Python can structure and process inventory data.
"""

print("Today we will build the base logic for a Server Inventory Tracker.")

# ---------------------------------------------------------------------
# SECTION 2: One Server as a Dictionary
# ---------------------------------------------------------------------

print("\nSECTION 2: One Server as a Dictionary")

server = {
    "name": "app01",
    "environment": "production",
    "os": "Linux",
    "owner": "app-team",
    "status": "active"
}

print("Server Name :", server["name"])
print("Environment :", server["environment"])
print("OS          :", server["os"])
print("Owner       :", server["owner"])
print("Status      :", server["status"])

"""
A dictionary is perfect for one structured record.
Each key explains what the value means.

This is more readable than storing the same data in many loose variables.
"""

# ---------------------------------------------------------------------
# SECTION 3: Multiple Servers as a List of Dictionaries
# ---------------------------------------------------------------------

print("\nSECTION 3: Multiple Servers as a List of Dictionaries")

inventory = [
    {"name": "app01", "environment": "production", "os": "Linux", "owner": "app-team", "status": "active"},
    {"name": "db01", "environment": "production", "os": "Linux", "owner": "db-team", "status": "active"},
    {"name": "web01", "environment": "uat", "os": "Windows", "owner": "web-team", "status": "maintenance"}
]

print("Total servers in inventory:", len(inventory))

for item in inventory:
    print(item["name"], "|", item["environment"], "|", item["os"], "|", item["status"])

"""
A list stores many server dictionaries.
This pattern is common in automation:

[
    {server 1 details},
    {server 2 details},
    {server 3 details}
]
"""

# ---------------------------------------------------------------------
# SECTION 4: Function to Print One Server
# ---------------------------------------------------------------------

print("\nSECTION 4: Function to Print One Server")


def print_server(server_record):
    print("Server      :", server_record["name"])
    print("Environment :", server_record["environment"])
    print("OS          :", server_record["os"])
    print("Owner       :", server_record["owner"])
    print("Status      :", server_record["status"])
    print("-" * 40)


print_server(inventory[0])

"""
The function receives one dictionary.
It prints that server in a clean format.

This avoids repeating the same print lines again and again.
"""

# ---------------------------------------------------------------------
# SECTION 5: Function to Print Full Inventory
# ---------------------------------------------------------------------

print("\nSECTION 5: Function to Print Full Inventory")


def print_inventory(server_list):
    print("SERVER INVENTORY")
    print("-" * 40)
    for server_record in server_list:
        print(server_record["name"], "|", server_record["environment"], "|", server_record["os"], "|", server_record["status"])


print_inventory(inventory)

"""
The function receives the full list.
It loops through the list and prints every server.

This is a real automation pattern:
- function accepts data
- function loops through records
- function generates output
"""

# ---------------------------------------------------------------------
# SECTION 6: Function to Create a Server Record
# ---------------------------------------------------------------------

print("\nSECTION 6: Function to Create a Server Record")


def create_server_record(name, environment, os_name, owner, status):
    server_record = {
        "name": name,
        "environment": environment,
        "os": os_name,
        "owner": owner,
        "status": status
    }
    return server_record


new_server = create_server_record("batch01", "production", "Linux", "batch-team", "active")
print_server(new_server)

"""
This function returns a dictionary.
The main script can store the returned dictionary or append it to inventory.
"""

# ---------------------------------------------------------------------
# SECTION 7: Add a Server to Inventory
# ---------------------------------------------------------------------

print("\nSECTION 7: Add a Server to Inventory")

inventory.append(new_server)

print("Server added:", new_server["name"])
print("Updated inventory count:", len(inventory))

"""
append() adds a new dictionary to the inventory list.
In real scripts, new records may come from input(), CSV, Excel, API, or database queries.
"""

# ---------------------------------------------------------------------
# SECTION 8: Count Servers by Environment
# ---------------------------------------------------------------------

print("\nSECTION 8: Count Servers by Environment")


def count_servers_by_environment(server_list, target_environment):
    count = 0

    for server_record in server_list:
        if server_record["environment"] == target_environment:
            count = count + 1

    return count


production_count = count_servers_by_environment(inventory, "production")
uat_count = count_servers_by_environment(inventory, "uat")

print("Production servers:", production_count)
print("UAT servers:", uat_count)

"""
This function returns a count.
Returned counts can be reused in dashboards, reports, or alert summaries.
"""

# ---------------------------------------------------------------------
# SECTION 9: Filter Servers by Status
# ---------------------------------------------------------------------

print("\nSECTION 9: Filter Servers by Status")


def get_servers_by_status(server_list, target_status):
    matched_servers = []

    for server_record in server_list:
        if server_record["status"] == target_status:
            matched_servers.append(server_record)

    return matched_servers


maintenance_servers = get_servers_by_status(inventory, "maintenance")

print("Servers in maintenance:")
for server_record in maintenance_servers:
    print(server_record["name"], "|", server_record["environment"])

"""
Filtering means selecting only records that match a condition.
This is useful for:
- inactive servers
- production servers
- unpatched servers
- servers without backups
- servers not monitored
"""

# ---------------------------------------------------------------------
# SECTION 10: Search Server by Name
# ---------------------------------------------------------------------

print("\nSECTION 10: Search Server by Name")


def find_server_by_name(server_list, search_name):
    for server_record in server_list:
        if server_record["name"] == search_name:
            return server_record

    return None


found_server = find_server_by_name(inventory, "db01")

if found_server is not None:
    print("Server found:")
    print_server(found_server)
else:
    print("Server not found")

"""
Returning None is a common way to say:
No matching record was found.

Later, you can use this same idea while searching files, logs, or API results.
"""

# ---------------------------------------------------------------------
# SECTION 11: Inventory Summary Function
# ---------------------------------------------------------------------

print("\nSECTION 11: Inventory Summary Function")


def build_inventory_summary(server_list):
    total_servers = len(server_list)
    production_servers = count_servers_by_environment(server_list, "production")
    uat_servers = count_servers_by_environment(server_list, "uat")
    maintenance_servers = len(get_servers_by_status(server_list, "maintenance"))

    summary = {
        "total": total_servers,
        "production": production_servers,
        "uat": uat_servers,
        "maintenance": maintenance_servers
    }

    return summary


summary = build_inventory_summary(inventory)

print("Total servers       :", summary["total"])
print("Production servers  :", summary["production"])
print("UAT servers         :", summary["uat"])
print("Maintenance servers :", summary["maintenance"])

"""
This function returns a summary dictionary.
This is a powerful pattern because summary values can be reused later.
"""

# ---------------------------------------------------------------------
# SECTION 12: Add Capacity Data
# ---------------------------------------------------------------------

print("\nSECTION 12: Add Capacity Data")

capacity_inventory = [
    {"name": "app01", "environment": "production", "cpu": 4, "memory_gb": 16, "disk_gb": 200},
    {"name": "db01", "environment": "production", "cpu": 8, "memory_gb": 64, "disk_gb": 1000},
    {"name": "web01", "environment": "uat", "cpu": 2, "memory_gb": 8, "disk_gb": 100}
]


def calculate_total_disk(server_list):
    total_disk = 0

    for server_record in server_list:
        total_disk = total_disk + server_record["disk_gb"]

    return total_disk


def calculate_total_memory(server_list):
    total_memory = 0

    for server_record in server_list:
        total_memory = total_memory + server_record["memory_gb"]

    return total_memory


print("Total disk capacity  :", calculate_total_disk(capacity_inventory), "GB")
print("Total memory capacity:", calculate_total_memory(capacity_inventory), "GB")

"""
Inventory is not only for listing servers.
It can also help with capacity tracking and reporting.
"""

# ---------------------------------------------------------------------
# SECTION 13: Guided Practice - Build a Simple Inventory
# ---------------------------------------------------------------------

print("\nSECTION 13: Guided Practice - Build a Simple Inventory")

"""
Uncomment this block and run it.
Create a small inventory and print each server.
"""

# practice_inventory = [
#     {"name": "mon01", "environment": "production", "status": "active"},
#     {"name": "test01", "environment": "test", "status": "inactive"}
# ]
#
# for server_record in practice_inventory:
#     print(server_record["name"], "-", server_record["environment"], "-", server_record["status"])

print("Guided practice: uncomment the simple inventory block.")

# ---------------------------------------------------------------------
# SECTION 14: Guided Practice - Inventory Function
# ---------------------------------------------------------------------

print("\nSECTION 14: Guided Practice - Inventory Function")

"""
Uncomment this block and run it.
Create a function that returns a server dictionary.
"""

# def make_server(name, environment, status):
#     return {"name": name, "environment": environment, "status": status}
#
# server_one = make_server("api01", "production", "active")
# print(server_one)

print("Guided practice: uncomment the make_server function block.")

# ---------------------------------------------------------------------
# SECTION 15: Guided Practice - Filter Inventory
# ---------------------------------------------------------------------

print("\nSECTION 15: Guided Practice - Filter Inventory")

"""
Uncomment this block and run it.
Filter active servers from an inventory list.
"""

# sample_inventory = [
#     {"name": "app01", "status": "active"},
#     {"name": "old01", "status": "inactive"},
#     {"name": "web01", "status": "active"}
# ]
#
# for server_record in sample_inventory:
#     if server_record["status"] == "active":
#         print("Active server:", server_record["name"])

print("Guided practice: uncomment the filter inventory block.")

# ---------------------------------------------------------------------
# SECTION 16: Mini Challenge Preview
# ---------------------------------------------------------------------

print("\nSECTION 16: Mini Challenge Preview")

"""
Mini Challenge:
Build a Server Inventory Tracker.

Your script should:
1. Collect details for multiple servers
2. Store each server as a dictionary
3. Store all dictionaries inside one list
4. Use functions to create, print, search, filter, and summarize inventory
5. Print one final inventory report

This mirrors real automation:
- collect structured data
- store it consistently
- process it with reusable functions
- produce a useful operational report
"""

print("Mini challenge: build a Server Inventory Tracker using lists, dictionaries, and functions.")

# ---------------------------------------------------------------------
# SECTION 17: Closing Message
# ---------------------------------------------------------------------

print("\nSECTION 17: Closing Message")

print("Lists hold many records. Dictionaries describe one record. Functions process the records.")
print("Together, these three ideas can build many real automation scripts.")
print("Day 18 complete. You have built the foundation of an inventory automation workflow.")
