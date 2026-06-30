"""
Python for Mammals - Day 18 Exercise File
Topic: Mini Project #2 - Server Inventory Tracker

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
By the end of these exercises, you should be able to combine lists,
dictionaries, and functions to build a small Server Inventory Tracker.
This is one of the most useful automation patterns for operations work.
"""

print("=" * 70)
print("DAY 18 EXERCISES - MINI PROJECT #2")
print("SERVER INVENTORY TRACKER")
print("LISTS, DICTIONARIES, FUNCTIONS")
print("=" * 70)

# ---------------------------------------------------------------------
# EXERCISE 1: Create One Server Dictionary
# ---------------------------------------------------------------------

"""
TODO:
- Create a dictionary named server
- Store these keys:
  name
  environment
  os
  owner
  status
- Print each value clearly

Concept focus:
one structured server record
"""

# Write your code below this line




# ---------------------------------------------------------------------
# EXERCISE 2: Create a List of Server Dictionaries
# ---------------------------------------------------------------------

"""
TODO:
- Create a list named inventory
- Add at least 3 server dictionaries inside it
- Each dictionary should contain:
  name, environment, os, owner, status
- Print the total number of servers using len()

Concept focus:
list of dictionaries
"""

# Write your code below this line




# ---------------------------------------------------------------------
# EXERCISE 3: Loop Through Inventory
# ---------------------------------------------------------------------

"""
TODO:
- Create an inventory list with at least 3 server dictionaries
- Loop through the inventory
- Print server name and environment for each server

Concept focus:
looping through list of dictionaries
"""

# Write your code below this line




# ---------------------------------------------------------------------
# EXERCISE 4: Function to Print One Server
# ---------------------------------------------------------------------

"""
TODO:
- Create a function named print_server
- The function should accept one parameter named server_record
- It should print name, environment, os, owner, and status
- Create one server dictionary
- Call the function using that dictionary

Concept focus:
passing a dictionary to a function
"""

# Write your code below this line




# ---------------------------------------------------------------------
# EXERCISE 5: Function to Create a Server Record
# ---------------------------------------------------------------------

"""
TODO:
- Create a function named create_server_record
- It should accept:
  name, environment, os_name, owner, status
- It should return a dictionary containing those values
- Call the function once
- Store the returned dictionary in a variable
- Print the returned dictionary

Concept focus:
function returning a dictionary
"""

# Write your code below this line




# ---------------------------------------------------------------------
# EXERCISE 6: Add Server to Inventory
# ---------------------------------------------------------------------

"""
TODO:
- Create an empty list named inventory
- Create a function named create_server_record
- Use the function to create 2 server dictionaries
- Append both dictionaries to inventory
- Print the inventory count

Concept focus:
creating records and adding them to a list
"""

# Write your code below this line




# ---------------------------------------------------------------------
# EXERCISE 7: Print Full Inventory Using a Function
# ---------------------------------------------------------------------

"""
TODO:
- Create an inventory list with at least 3 servers
- Create a function named print_inventory
- The function should accept server_list
- It should loop through server_list and print one clean line per server
- Call the function

Concept focus:
function processing a full list
"""

# Write your code below this line




# ---------------------------------------------------------------------
# EXERCISE 8: Count Servers by Environment
# ---------------------------------------------------------------------

"""
TODO:
- Create an inventory list with production, uat, and test servers
- Create a function named count_servers_by_environment
- The function should accept server_list and target_environment
- It should return the count of matching servers
- Call the function for production and uat
- Print the returned counts

Concept focus:
filtering and returning count
"""

# Write your code below this line




# ---------------------------------------------------------------------
# EXERCISE 9: Filter Servers by Status
# ---------------------------------------------------------------------

"""
TODO:
- Create an inventory list with active, inactive, and maintenance servers
- Create a function named get_servers_by_status
- The function should accept server_list and target_status
- It should return a list of matching server dictionaries
- Call the function for maintenance servers
- Print the names of matching servers

Concept focus:
returning a filtered list
"""

# Write your code below this line




# ---------------------------------------------------------------------
# EXERCISE 10: Search Server by Name
# ---------------------------------------------------------------------

"""
TODO:
- Create an inventory list with at least 3 servers
- Create a function named find_server_by_name
- The function should accept server_list and search_name
- If a matching server is found, return that dictionary
- If no server is found, return None
- Search for one existing server
- Print whether the server was found

Concept focus:
searching structured data
"""

# Write your code below this line




# ---------------------------------------------------------------------
# EXERCISE 11: Capacity Inventory
# ---------------------------------------------------------------------

"""
TODO:
- Create a list named capacity_inventory
- Add at least 3 server dictionaries
- Each dictionary should contain:
  name, cpu, memory_gb, disk_gb
- Create a function named calculate_total_disk
- It should return total disk capacity across all servers
- Print the returned value

Concept focus:
summing numeric values from inventory records
"""

# Write your code below this line




# ---------------------------------------------------------------------
# EXERCISE 12: Build Inventory Summary Dictionary
# ---------------------------------------------------------------------

"""
TODO:
- Create an inventory list with different environments and statuses
- Create a function named build_inventory_summary
- It should return a dictionary containing:
  total_servers
  production_servers
  active_servers
  maintenance_servers
- Print the returned summary dictionary clearly

Concept focus:
returning a summary dictionary
"""

# Write your code below this line




# ---------------------------------------------------------------------
# EXERCISE 13: User Input Server Record
# ---------------------------------------------------------------------

"""
TODO:
- Collect these inputs once:
  server name
  environment
  os
  owner
  status
- Create a function named create_server_record
- The function should return a dictionary
- Pass the input values into the function
- Store the returned dictionary
- Print a clean server summary

Concept focus:
input once, create structured record
"""

# Write your code below this line




# ---------------------------------------------------------------------
# EXERCISE 14: Mini Project - Server Inventory Tracker
# ---------------------------------------------------------------------

"""
Build a small Server Inventory Tracker script.

Collect all required inputs once at the beginning:
1. How many servers do you want to add?

For each server, collect:
1. Server Name
2. Environment
3. Operating System
4. Owner Team
5. Status
6. CPU Count
7. Memory GB
8. Disk GB

TODO:
- Create an empty list named inventory

- Create a function named create_server_record
  - It should accept:
    name, environment, os_name, owner, status, cpu, memory_gb, disk_gb
  - It should return one server dictionary

- Create a function named print_server_line
  - It should accept one server dictionary
  - It should print one clean inventory line

- Create a function named count_by_environment
  - It should accept inventory and target_environment
  - It should return count of matching servers

- Create a function named count_by_status
  - It should accept inventory and target_status
  - It should return count of matching servers

- Create a function named calculate_total_disk
  - It should accept inventory
  - It should return total disk capacity

- Create a function named calculate_total_memory
  - It should accept inventory
  - It should return total memory capacity

- Ask for the server count once
- Use a loop to collect details for each server
- Convert CPU, memory, and disk values into numbers
- Create a server dictionary using create_server_record
- Append each server dictionary to inventory

- Generate one final report containing:
  - All server lines
  - Total server count
  - Production server count
  - UAT server count
  - Active server count
  - Maintenance server count
  - Total CPU count
  - Total memory GB
  - Total disk GB

Important:
- Collect each input only once.
- Reuse variables throughout the project.
- Do not ask for the same input repeatedly.
- Store each server as one dictionary.
- Store all server dictionaries in one list.
- Use functions for repeated logic.
- The mini project should feel like one complete inventory workflow.

Concept focus:
real-world mini automation using lists, dictionaries, and functions
"""

# Write your code below this line




print("\nEnd of Day 18 exercises. Complete the TODO sections one by one.")
