"""
Python for Mammals - Day 13
Topic: Tuples & Sets

Audience:
- Complete beginners
- DBAs, Sysadmins, Support Engineers, Cloud Engineers, Monitoring Teams
- Anyone who wants Python for practical automation

Goal of Day 13:
By the end of today, you should be able to:
1. Create tuples for fixed data
2. Understand why tuples are useful when values should not change
3. Access tuple values using indexes
4. Unpack tuple values into variables
5. Create sets for unique values
6. Remove duplicates using set()
7. Use set operations like union, intersection, difference, and symmetric difference
8. Use tuples and sets in practical automation workflows

Why this matters:
Day 11 and Day 12 taught us lists.
Lists are great when data may change.

Day 13 teaches two more useful collection types:
- Tuples: for fixed records that should not accidentally change
- Sets  : for unique values and comparison between groups

Real automation scripts often need to:
- store fixed server details
- store environment connection details
- remove duplicate server names from inventory
- compare expected servers with discovered servers
- find missing checks
- find common alerts between two monitoring sources
- find users present in one system but missing in another

Tuples and sets are small concepts, but they are very useful in clean automation.
"""

print("=" * 70)
print("DAY 13 - TUPLES & SETS")
print("TUPLES, SETS, DUPLICATES, SET OPERATIONS")
print("=" * 70)

# ---------------------------------------------------------------------
# SECTION 1: Why Tuples and Sets Matter
# ---------------------------------------------------------------------

print("\nSECTION 1: Why Tuples and Sets Matter")

"""
Lists are flexible.
You can add, remove, and change values.

But sometimes automation needs different behavior:

1. Fixed data
   Example: a server record that should not be accidentally modified.
   For this, tuples are useful.

2. Unique data
   Example: a server inventory where duplicate names should be removed.
   For this, sets are useful.
"""

print("Tuples protect fixed records. Sets help with unique values and comparisons.")

# ---------------------------------------------------------------------
# SECTION 2: Creating a Tuple
# ---------------------------------------------------------------------

print("\nSECTION 2: Creating a Tuple")

server_record = ("app01", "production", "linux")

print("Server record:", server_record)
print("Type         :", type(server_record))

"""
A tuple looks like a list, but it uses round brackets ().

Tuple example:
("app01", "production", "linux")

This can represent one fixed record:
- server name
- environment
- operating system
"""

# ---------------------------------------------------------------------
# SECTION 3: Accessing Tuple Values
# ---------------------------------------------------------------------

print("\nSECTION 3: Accessing Tuple Values")

server_record = ("app01", "production", "linux")

print("Server name :", server_record[0])
print("Environment :", server_record[1])
print("OS type     :", server_record[2])

"""
Tuple values can be accessed using indexes, just like lists.

Index positions start from 0:
0 -> first value
1 -> second value
2 -> third value
"""

# ---------------------------------------------------------------------
# SECTION 4: Tuple Immutability
# ---------------------------------------------------------------------

print("\nSECTION 4: Tuple Immutability")

server_record = ("db01", "production", "oracle")

print("Original tuple:", server_record)

"""
Tuples are immutable.
That means you cannot directly change a value inside a tuple.

The following line would fail if uncommented:

server_record[1] = "test"

This is useful when a record should remain stable during script execution.
"""

print("Tuple values are fixed after creation.")

# ---------------------------------------------------------------------
# SECTION 5: Tuple Unpacking
# ---------------------------------------------------------------------

print("\nSECTION 5: Tuple Unpacking")

server_record = ("web01", "uat", "windows")

server_name, environment, os_type = server_record

print("Server name :", server_name)
print("Environment :", environment)
print("OS type     :", os_type)

"""
Tuple unpacking means assigning tuple values into separate variables.

This improves readability when each position has a clear meaning.
"""

# ---------------------------------------------------------------------
# SECTION 6: Tuple Use Case - Fixed Connection Details
# ---------------------------------------------------------------------

print("\nSECTION 6: Tuple Use Case - Fixed Connection Details")

connection_info = ("dbprod01", 1521, "PRODDB")

host, port, service_name = connection_info

print("Host        :", host)
print("Port        :", port)
print("Service Name:", service_name)

"""
A tuple is useful for fixed connection-style details.

In real scripts, you may later store:
- host
- port
- service name
- environment
- region

For beginners, remember this simple rule:
Use tuple when the collection represents one fixed record.
"""

# ---------------------------------------------------------------------
# SECTION 7: Creating a Set
# ---------------------------------------------------------------------

print("\nSECTION 7: Creating a Set")

servers = {"app01", "db01", "web01"}

print("Server set:", servers)
print("Type      :", type(servers))

"""
A set uses curly braces {}.

Important point:
A set stores unique values only.
It does not keep duplicate values.
"""

# ---------------------------------------------------------------------
# SECTION 8: Removing Duplicates Using set()
# ---------------------------------------------------------------------

print("\nSECTION 8: Removing Duplicates Using set()")

server_list = ["app01", "db01", "app01", "web01", "db01"]

print("Original list :", server_list)

unique_servers = set(server_list)

print("Unique servers:", unique_servers)

"""
set(list_name) converts a list into a set.
Duplicate values are removed automatically.

This is very useful when inventory, logs, reports, or monitoring exports
contain repeated values.
"""

# ---------------------------------------------------------------------
# SECTION 9: Converting Set Back to List
# ---------------------------------------------------------------------

print("\nSECTION 9: Converting Set Back to List")

server_list = ["app01", "db01", "app01", "web01", "db01"]
unique_servers = set(server_list)
clean_server_list = list(unique_servers)

print("Clean server list:", clean_server_list)

"""
After removing duplicates, you can convert a set back into a list.

Note:
Sets do not guarantee the same order as the original list.
When order matters, you will later learn safer cleanup patterns.
For now, focus on the idea of uniqueness.
"""

# ---------------------------------------------------------------------
# SECTION 10: Set Union
# ---------------------------------------------------------------------

print("\nSECTION 10: Set Union")

linux_servers = {"app01", "batch01", "web01"}
database_servers = {"db01", "batch01", "report01"}

all_servers = linux_servers.union(database_servers)

print("Linux servers   :", linux_servers)
print("Database servers:", database_servers)
print("All servers     :", all_servers)

"""
union() combines values from both sets.
Duplicates are still shown only once.

Use case:
Combine inventories from two sources into one unique list.
"""

# ---------------------------------------------------------------------
# SECTION 11: Set Intersection
# ---------------------------------------------------------------------

print("\nSECTION 11: Set Intersection")

monitoring_a = {"app01", "db01", "web01"}
monitoring_b = {"db01", "web01", "batch01"}

common_servers = monitoring_a.intersection(monitoring_b)

print("Monitoring A :", monitoring_a)
print("Monitoring B :", monitoring_b)
print("Common       :", common_servers)

"""
intersection() returns values present in both sets.

Use case:
Find servers reported by both monitoring tools.
"""

# ---------------------------------------------------------------------
# SECTION 12: Set Difference
# ---------------------------------------------------------------------

print("\nSECTION 12: Set Difference")

expected_servers = {"app01", "db01", "web01", "batch01"}
discovered_servers = {"app01", "db01", "web01"}

missing_servers = expected_servers.difference(discovered_servers)

print("Expected  :", expected_servers)
print("Discovered:", discovered_servers)
print("Missing   :", missing_servers)

"""
difference() tells what exists in the first set but not in the second set.

Use case:
Find expected servers that were not discovered by a scan.
"""

# ---------------------------------------------------------------------
# SECTION 13: Symmetric Difference
# ---------------------------------------------------------------------

print("\nSECTION 13: Symmetric Difference")

cmdb_servers = {"app01", "db01", "web01"}
scan_servers = {"app01", "db01", "batch01"}

mismatch_servers = cmdb_servers.symmetric_difference(scan_servers)

print("CMDB servers:", cmdb_servers)
print("Scan servers:", scan_servers)
print("Mismatch    :", mismatch_servers)

"""
symmetric_difference() returns values that are different between two sets.

Use case:
Find inventory mismatch between CMDB and scan output.
"""

# ---------------------------------------------------------------------
# SECTION 14: Practical Example - Unique Alert Codes
# ---------------------------------------------------------------------

print("\nSECTION 14: Practical Example - Unique Alert Codes")

alert_codes = ["ORA-01555", "ORA-00060", "ORA-01555", "ORA-1652", "ORA-00060"]

unique_alerts = set(alert_codes)

print("Raw alert codes   :", alert_codes)
print("Unique alert codes:", unique_alerts)
print("Unique count      :", len(unique_alerts))

# ---------------------------------------------------------------------
# SECTION 15: Practical Example - Missing Daily Checks
# ---------------------------------------------------------------------

print("\nSECTION 15: Practical Example - Missing Daily Checks")

required_checks = {"CPU", "Memory", "Disk", "Backup"}
completed_checks = {"CPU", "Disk"}

pending_checks = required_checks.difference(completed_checks)

print("Required checks :", required_checks)
print("Completed checks:", completed_checks)
print("Pending checks  :", pending_checks)

# ---------------------------------------------------------------------
# SECTION 16: Guided Practice - Tuple
# ---------------------------------------------------------------------

print("\nSECTION 16: Guided Practice - Tuple")

"""
Uncomment this block and run it.
Create your own fixed server record.
"""

# server_record = ("app02", "test", "linux")
# server_name, environment, os_type = server_record
# print("Server:", server_name)
# print("Environment:", environment)
# print("OS:", os_type)

print("Guided practice: uncomment the tuple block.")

# ---------------------------------------------------------------------
# SECTION 17: Guided Practice - Remove Duplicates
# ---------------------------------------------------------------------

print("\nSECTION 17: Guided Practice - Remove Duplicates")

"""
Uncomment this block and run it.
Remove duplicate ticket IDs from a list.
"""

# tickets = ["INC001", "INC002", "INC001", "INC003", "INC002"]
# unique_tickets = set(tickets)
# print("Unique tickets:", unique_tickets)

print("Guided practice: uncomment the duplicate removal block.")

# ---------------------------------------------------------------------
# SECTION 18: Practical Program 1 - Fixed Server Record
# ---------------------------------------------------------------------

print("\nSECTION 18: Practical Program 1 - Fixed Server Record")

server_record = ("app01", "production", "linux")
server_name, environment, os_type = server_record

print("Server Record Report")
print("-" * 35)
print("Server Name :", server_name)
print("Environment :", environment)
print("OS Type     :", os_type)

# ---------------------------------------------------------------------
# SECTION 19: Practical Program 2 - Inventory Comparison
# ---------------------------------------------------------------------

print("\nSECTION 19: Practical Program 2 - Inventory Comparison")

cmdb_inventory = {"app01", "db01", "web01", "batch01"}
scan_inventory = {"app01", "db01", "web01", "report01"}

missing_from_scan = cmdb_inventory.difference(scan_inventory)
new_in_scan = scan_inventory.difference(cmdb_inventory)
common_inventory = cmdb_inventory.intersection(scan_inventory)

print("Inventory Comparison Report")
print("-" * 40)
print("Common servers   :", common_inventory)
print("Missing from scan:", missing_from_scan)
print("New in scan      :", new_in_scan)

# ---------------------------------------------------------------------
# SECTION 20: Mini Project - Inventory Cleanup and Comparison
# ---------------------------------------------------------------------

print("\nSECTION 20: Mini Project - Inventory Cleanup and Comparison")

"""
This mini project uses fixed values so the file can run without stopping
for user input.

In Day13_Exercise.py, you will build your own version using input().
"""

server_record = ("app01", "production", "linux")
raw_inventory = ["app01", "db01", "app01", "web01", "db01"]
expected_servers = {"app01", "db01", "web01", "batch01"}
discovered_servers = set(raw_inventory)

server_name, environment, os_type = server_record
missing_servers = expected_servers.difference(discovered_servers)
extra_servers = discovered_servers.difference(expected_servers)
common_servers = expected_servers.intersection(discovered_servers)

print("Inventory Cleanup and Comparison")
print("-" * 45)
print("Reference Server :", server_name)
print("Environment      :", environment)
print("OS Type          :", os_type)
print("Raw Inventory    :", raw_inventory)
print("Unique Inventory :", discovered_servers)
print("Expected Servers :", expected_servers)
print("Common Servers   :", common_servers)
print("Missing Servers  :", missing_servers)
print("Extra Servers    :", extra_servers)
print("Unique Count     :", len(discovered_servers))
print("-" * 45)

# ---------------------------------------------------------------------
# SECTION 21: Mini Challenge
# ---------------------------------------------------------------------

print("\nSECTION 21: Mini Challenge")

"""
Create an Inventory Cleanup and Comparison script.

It should:
1. Create one tuple named reference_server with server name, environment, and OS type
2. Unpack the tuple into three variables
3. Create a list containing five discovered server names, including duplicates
4. Convert the list to a set to remove duplicates
5. Create a set of expected servers
6. Find common servers using intersection()
7. Find missing servers using difference()
8. Find extra servers using difference()
9. Print unique server count using len()
10. Print a clean final report

Use:
- tuple
- tuple unpacking
- set()
- union() optionally
- intersection()
- difference()
- len()
- print()
"""

print("Mini challenge: Build an Inventory Cleanup and Comparison script.")

# ---------------------------------------------------------------------
# CLOSING MESSAGE
# ---------------------------------------------------------------------

print("\nDay 13 complete. You can now use tuples for fixed records and sets for unique values.")
print("This is a strong step toward cleaner inventory, monitoring, and reporting automation.")
