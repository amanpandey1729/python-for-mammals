"""
Python for Mammals - Day 13 Exercise File
Topic: Tuples & Sets

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
By the end of these exercises, you should be able to create tuples,
unpack tuples, create sets, remove duplicates, and compare groups of
values using set operations for practical automation workflows.
"""

print("=" * 70)
print("DAY 13 EXERCISES - TUPLES & SETS")
print("TUPLES, SETS, DUPLICATES, UNION, INTERSECTION, DIFFERENCE")
print("=" * 70)

# ---------------------------------------------------------------------
# EXERCISE 1: Create a Fixed Server Record
# ---------------------------------------------------------------------

"""
TODO:
- Create a tuple named server_record with three values:
  server name, environment, operating system
- Print the tuple
- Print the type of the tuple

Concept focus:
tuple creation
"""

# Write your code below this line




# ---------------------------------------------------------------------
# EXERCISE 2: Access Tuple Values by Index
# ---------------------------------------------------------------------

"""
Given:
server_record = ("app01", "production", "linux")

TODO:
- Print the server name using index 0
- Print the environment using index 1
- Print the OS type using index 2

Concept focus:
tuple indexing
"""

server_record = ("app01", "production", "linux")

# Write your code below this line




# ---------------------------------------------------------------------
# EXERCISE 3: Tuple Unpacking
# ---------------------------------------------------------------------

"""
Given:
connection_info = ("dbprod01", 1521, "PRODDB")

TODO:
- Unpack the tuple into host, port, and service_name
- Print all three variables in a readable format

Concept focus:
tuple unpacking
"""

connection_info = ("dbprod01", 1521, "PRODDB")

# Write your code below this line




# ---------------------------------------------------------------------
# EXERCISE 4: Fixed Backup Window
# ---------------------------------------------------------------------

"""
TODO:
- Create a tuple named backup_window with start time, end time, and timezone
- Unpack the tuple into three variables
- Print a readable backup window summary

Example style:
Backup Window: 22:00 to 23:30 IST

Concept focus:
using tuples for fixed operational information
"""

# Write your code below this line




# ---------------------------------------------------------------------
# EXERCISE 5: Create a Set of Servers
# ---------------------------------------------------------------------

"""
TODO:
- Create a set named servers with app01, db01, and web01
- Print the set
- Print the type of the set

Concept focus:
set creation
"""

# Write your code below this line




# ---------------------------------------------------------------------
# EXERCISE 6: Remove Duplicate Server Names
# ---------------------------------------------------------------------

"""
Given:
server_list = ["app01", "db01", "app01", "web01", "db01"]

TODO:
- Convert server_list into a set named unique_servers
- Print the original list
- Print the unique server set
- Print the number of unique servers

Concept focus:
removing duplicates using set()
"""

server_list = ["app01", "db01", "app01", "web01", "db01"]

# Write your code below this line




# ---------------------------------------------------------------------
# EXERCISE 7: Remove Duplicate Alert Codes
# ---------------------------------------------------------------------

"""
Given:
alert_codes = ["ORA-01555", "ORA-00060", "ORA-01555", "ORA-1652", "ORA-00060"]

TODO:
- Convert alert_codes into a set named unique_alert_codes
- Print the unique alert codes
- Print the unique alert count

Concept focus:
deduplication for log or alert analysis
"""

alert_codes = ["ORA-01555", "ORA-00060", "ORA-01555", "ORA-1652", "ORA-00060"]

# Write your code below this line




# ---------------------------------------------------------------------
# EXERCISE 8: Convert a Set Back to a List
# ---------------------------------------------------------------------

"""
Given:
raw_users = ["aman", "riya", "aman", "dev", "riya"]

TODO:
- Convert raw_users into a set to remove duplicates
- Convert the set back into a list named clean_users
- Print clean_users

Concept focus:
set() and list() conversion
"""

raw_users = ["aman", "riya", "aman", "dev", "riya"]

# Write your code below this line




# ---------------------------------------------------------------------
# EXERCISE 9: Combine Two Inventories Using Union
# ---------------------------------------------------------------------

"""
Given:
linux_inventory = {"app01", "batch01", "web01"}
database_inventory = {"db01", "batch01", "report01"}

TODO:
- Use union() to combine both inventories into all_servers
- Print all_servers

Concept focus:
set union
"""

linux_inventory = {"app01", "batch01", "web01"}
database_inventory = {"db01", "batch01", "report01"}

# Write your code below this line




# ---------------------------------------------------------------------
# EXERCISE 10: Find Common Servers
# ---------------------------------------------------------------------

"""
Given:
monitoring_tool_a = {"app01", "db01", "web01"}
monitoring_tool_b = {"db01", "web01", "batch01"}

TODO:
- Use intersection() to find servers present in both tools
- Store the result in common_servers
- Print common_servers

Concept focus:
set intersection
"""

monitoring_tool_a = {"app01", "db01", "web01"}
monitoring_tool_b = {"db01", "web01", "batch01"}

# Write your code below this line




# ---------------------------------------------------------------------
# EXERCISE 11: Find Missing Servers
# ---------------------------------------------------------------------

"""
Given:
expected_servers = {"app01", "db01", "web01", "batch01"}
discovered_servers = {"app01", "db01", "web01"}

TODO:
- Use difference() to find servers that are expected but not discovered
- Store the result in missing_servers
- Print missing_servers

Concept focus:
set difference
"""

expected_servers = {"app01", "db01", "web01", "batch01"}
discovered_servers = {"app01", "db01", "web01"}

# Write your code below this line




# ---------------------------------------------------------------------
# EXERCISE 12: Find New Servers in Scan Output
# ---------------------------------------------------------------------

"""
Given:
cmdb_servers = {"app01", "db01", "web01"}
scan_servers = {"app01", "db01", "web01", "report01"}

TODO:
- Find servers that are present in scan_servers but not in cmdb_servers
- Store the result in new_servers
- Print new_servers

Concept focus:
difference in the opposite direction
"""

cmdb_servers = {"app01", "db01", "web01"}
scan_servers = {"app01", "db01", "web01", "report01"}

# Write your code below this line




# ---------------------------------------------------------------------
# EXERCISE 13: Find Inventory Mismatch
# ---------------------------------------------------------------------

"""
Given:
cmdb_servers = {"app01", "db01", "web01"}
scan_servers = {"app01", "db01", "batch01"}

TODO:
- Use symmetric_difference() to find values that do not match between both sets
- Store the result in mismatch_servers
- Print mismatch_servers

Concept focus:
symmetric difference
"""

cmdb_servers = {"app01", "db01", "web01"}
scan_servers = {"app01", "db01", "batch01"}

# Write your code below this line




# ---------------------------------------------------------------------
# EXERCISE 14: Mini Project - Inventory Cleanup and Comparison
# ---------------------------------------------------------------------

"""
Build a small Inventory Cleanup and Comparison script.

Collect all required inputs once at the beginning:
1. Reference server name
2. Reference environment
3. Reference OS type
4. Discovered server 1
5. Discovered server 2
6. Discovered server 3
7. Discovered server 4
8. Discovered server 5
9. Expected server 1
10. Expected server 2
11. Expected server 3
12. Expected server 4

TODO:
- Store the reference server details in a tuple named reference_server
- Unpack the tuple into server_name, environment, and os_type
- Store the five discovered server inputs in a list named raw_discovered_servers
- Convert raw_discovered_servers into a set named discovered_servers
- Store the four expected server inputs in a set named expected_servers
- Find common servers using intersection()
- Find missing servers using difference()
- Find extra servers using difference()
- Find mismatch servers using symmetric_difference()
- Print total raw discovered entries using len()
- Print total unique discovered servers using len()
- Print a clean final inventory comparison report

Expected output style:
========================================
Inventory Cleanup and Comparison
========================================
Reference Server : app01
Environment      : production
OS Type          : linux
Raw Entries      : 5
Unique Servers   : 3
Expected Servers : {'app01', 'db01', 'web01', 'batch01'}
Discovered       : {'app01', 'db01', 'web01'}
Common Servers   : {'app01', 'db01', 'web01'}
Missing Servers  : {'batch01'}
Extra Servers    : set()
Mismatch Servers : {'batch01'}
========================================

Important:
Collect each required input once at the beginning.
Reuse those variables throughout the mini project.
Do not ask for the same input multiple times.
This should feel like one complete automation workflow.
"""

# Write your mini project code below this line




print("\nExercise file loaded successfully. Complete the tasks one by one.")
