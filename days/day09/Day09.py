"""
Python for Mammals - Day 9
Topic: While Loops

Audience:
- Complete beginners
- DBAs, Sysadmins, Support Engineers, Cloud Engineers, Monitoring Teams
- Anyone who wants Python for practical automation

Goal of Day 9:
By the end of today, you should be able to:
1. Understand what a while loop does
2. Repeat code while a condition remains True
3. Avoid accidental infinite loops
4. Use break to stop a loop early
5. Use continue to skip one loop cycle
6. Build validation loops for safer user input
7. Control repetitive execution in practical automation scripts

Why this matters:
A for loop is great when you already know how many items you have.
A while loop is useful when repetition depends on a condition.

Examples:
- Keep asking for valid input until the user enters it correctly
- Keep retrying a check until it passes or reaches a limit
- Keep reading commands until the user types exit
- Keep processing alert counts until no pending alerts remain
- Keep a menu running until the operator chooses to quit

Day 8 helped us repeat work across known items.
Day 9 helps us repeat work until a condition changes.
"""

print("=" * 70)
print("DAY 9 - WHILE LOOPS")
print("=" * 70)

# ---------------------------------------------------------------------
# SECTION 1: Why while Loops Matter in Automation
# ---------------------------------------------------------------------

print("\nSECTION 1: Why while Loops Matter in Automation")

"""
In operations work, we often do not know the exact number of repetitions.

Example:
- Ask for a valid environment until the user enters DEV, TEST, or PROD
- Retry a failed health check up to 3 times
- Keep showing a menu until the user selects exit

A while loop keeps running while a condition is True.
"""

print("A while loop is useful when repetition depends on a condition.")

# ---------------------------------------------------------------------
# SECTION 2: First while Loop
# ---------------------------------------------------------------------

print("\nSECTION 2: First while Loop")

counter = 1

while counter <= 3:
    print("Health check attempt:", counter)
    counter += 1

"""
Important:
The counter must change inside the loop.
Otherwise, the condition may remain True forever.
"""

# ---------------------------------------------------------------------
# SECTION 3: Understanding the Loop Condition
# ---------------------------------------------------------------------

print("\nSECTION 3: Understanding the Loop Condition")

pending_tasks = 3

while pending_tasks > 0:
    print("Pending tasks remaining:", pending_tasks)
    pending_tasks -= 1

print("All pending tasks reviewed.")

# ---------------------------------------------------------------------
# SECTION 4: while Loop vs for Loop
# ---------------------------------------------------------------------

print("\nSECTION 4: while Loop vs for Loop")

"""
Use for loop when:
- You have a list of items
- You know the number of repetitions

Use while loop when:
- You repeat until something changes
- You wait for valid input
- You run a menu until exit
- You retry until success or retry limit
"""

print("for loop  : repeat for known items")
print("while loop: repeat while a condition is True")

# ---------------------------------------------------------------------
# SECTION 5: Infinite Loops
# ---------------------------------------------------------------------

print("\nSECTION 5: Infinite Loops")

"""
An infinite loop happens when the condition never becomes False.

Do NOT run this example:

count = 1
while count <= 3:
    print(count)

The value of count never changes, so the loop never stops.
"""

print("Avoid infinite loops by making sure the loop condition can change.")

# ---------------------------------------------------------------------
# SECTION 6: Safe Retry Loop
# ---------------------------------------------------------------------

print("\nSECTION 6: Safe Retry Loop")

attempt = 1
max_attempts = 3

while attempt <= max_attempts:
    print("Running connection retry:", attempt)
    attempt += 1

print("Retry loop finished.")

# ---------------------------------------------------------------------
# SECTION 7: break - Stop a Loop Early
# ---------------------------------------------------------------------

print("\nSECTION 7: break - Stop a Loop Early")

attempt = 1
max_attempts = 5
service_available = False

while attempt <= max_attempts:
    print("Checking service. Attempt:", attempt)

    if attempt == 3:
        service_available = True
        print("Service is available.")
        break

    attempt += 1

print("Service check completed.")

# ---------------------------------------------------------------------
# SECTION 8: continue - Skip Current Cycle
# ---------------------------------------------------------------------

print("\nSECTION 8: continue - Skip Current Cycle")

number = 0

while number < 5:
    number += 1

    if number == 3:
        print("Skipping maintenance window:", number)
        continue

    print("Processing window:", number)

# ---------------------------------------------------------------------
# SECTION 9: Validation Loop Concept
# ---------------------------------------------------------------------

print("\nSECTION 9: Validation Loop Concept")

"""
Validation loops are extremely useful.

They help you keep asking until the user gives acceptable input.
This prevents scripts from running with bad values.
"""

print("Validation loops protect scripts from invalid input.")

# ---------------------------------------------------------------------
# SECTION 10: Validation Loop with Fixed Sample Value
# ---------------------------------------------------------------------

print("\nSECTION 10: Validation Loop with Fixed Sample Value")

sample_inputs = ["", "   ", "prod"]
index = 0
server_name = sample_inputs[index]

while server_name.strip() == "":
    print("Blank server name found. Asking again.")
    index += 1
    server_name = sample_inputs[index]

clean_server_name = server_name.strip().lower()
print("Accepted server name:", clean_server_name)

# ---------------------------------------------------------------------
# SECTION 11: Menu-style Loop
# ---------------------------------------------------------------------

print("\nSECTION 11: Menu-style Loop")

menu_choice = "1"

while menu_choice != "3":
    print("Menu choice selected:", menu_choice)

    if menu_choice == "1":
        print("Action: Show health summary")
        menu_choice = "2"
    elif menu_choice == "2":
        print("Action: Show backup summary")
        menu_choice = "3"
    else:
        print("Action: Invalid menu choice")
        menu_choice = "3"

print("Menu closed.")

# ---------------------------------------------------------------------
# SECTION 12: Practical Program 1 - Alert Countdown
# ---------------------------------------------------------------------

print("\nSECTION 12: Practical Program 1 - Alert Countdown")

pending_alerts = 4

while pending_alerts > 0:
    print("Reviewing alert. Pending before review:", pending_alerts)
    pending_alerts -= 1

print("No pending alerts left.")

# ---------------------------------------------------------------------
# SECTION 13: Practical Program 2 - Retry Until Success
# ---------------------------------------------------------------------

print("\nSECTION 13: Practical Program 2 - Retry Until Success")

attempt = 1
max_attempts = 4
success_attempt = 3

while attempt <= max_attempts:
    print("Backup validation attempt:", attempt)

    if attempt == success_attempt:
        print("Backup validation successful.")
        break

    attempt += 1

# ---------------------------------------------------------------------
# SECTION 14: Practical Program 3 - Skip Planned Maintenance
# ---------------------------------------------------------------------

print("\nSECTION 14: Practical Program 3 - Skip Planned Maintenance")

window = 0

while window < 5:
    window += 1

    if window == 4:
        print("Window", window, "is reserved. Skipping.")
        continue

    print("Window", window, "is available for checks.")

# ---------------------------------------------------------------------
# SECTION 15: Guided Practice - Input Validation Loop
# ---------------------------------------------------------------------

print("\nSECTION 15: Guided Practice - Input Validation Loop")

"""
Uncomment this block and run it.

This program keeps asking until the user enters a valid environment.
Try:
- blank input
- stage
- prod
- DEV
"""

# environment = input("Enter environment DEV, TEST, or PROD: ").strip().upper()
#
# while environment not in ["DEV", "TEST", "PROD"]:
#     print("Invalid environment. Please try again.")
#     environment = input("Enter environment DEV, TEST, or PROD: ").strip().upper()
#
# print("Accepted environment:", environment)

print("Guided practice: uncomment the validation loop and test user input.")

# ---------------------------------------------------------------------
# SECTION 16: Guided Practice - Retry Limit
# ---------------------------------------------------------------------

print("\nSECTION 16: Guided Practice - Retry Limit")

"""
Uncomment this block and run it.

This program asks for a YES response but stops after 3 attempts.
"""

# attempts = 1
# max_attempts = 3
# answer = input("Type YES to confirm: ").strip().upper()
#
# while answer != "YES":
#     if attempts == max_attempts:
#         print("Maximum attempts reached.")
#         break
#
#     print("Invalid confirmation. Try again.")
#     attempts += 1
#     answer = input("Type YES to confirm: ").strip().upper()
#
# if answer == "YES":
#     print("Confirmation accepted.")

print("Guided practice: uncomment the retry limit example.")

# ---------------------------------------------------------------------
# SECTION 17: Mini Project - Controlled Health Retry
# ---------------------------------------------------------------------

print("\nSECTION 17: Mini Project - Controlled Health Retry")

"""
This mini project simulates a health check retry workflow.

Input values used today:
- Server name
- Maximum retry count
- Attempt number where success happens

Output:
- Each retry attempt
- Final status

Today we use fixed values.
Later this logic can be used with command output, API checks, database checks,
or monitoring alerts.
"""

server_name = "app01"
max_retries = 5
success_on_attempt = 3
attempt = 1
final_status = "FAILED"

print("Controlled Health Retry")
print("-" * 40)
print("Server:", server_name)

while attempt <= max_retries:
    print("Attempt:", attempt)

    if attempt == success_on_attempt:
        final_status = "SUCCESS"
        print("Result : Health check passed")
        break

    print("Result : Health check failed")
    attempt += 1

print("Final status:", final_status)

# ---------------------------------------------------------------------
# SECTION 18: Mini Challenge
# ---------------------------------------------------------------------

print("\nSECTION 18: Mini Challenge")

"""
Create a validated Disk Usage Reporter.

It should:
1. Ask for server name until the value is not blank
2. Ask for environment until it is DEV, TEST, or PROD
3. Ask for disk usage until it is between 0 and 100
4. Decide status:
   - CRITICAL if usage >= 90
   - WARNING if usage >= 80
   - OK otherwise
5. Print a final report

Use:
- while loop
- validation conditions
- break where useful
- input()
- strip(), upper(), float()
- if / elif / else
"""

print("Mini challenge: Build a validated Disk Usage Reporter using while loops.")

# ---------------------------------------------------------------------
# SECTION 19: Homework
# ---------------------------------------------------------------------

print("\nSECTION 19: Homework")

"""
Homework:
1. Complete Day09_Exercise.py
2. Practice a simple while loop with a counter
3. Create one validation loop for environment input
4. Create one retry loop with a maximum attempt limit
5. Create one menu loop that runs until the user enters exit
6. Share one real task where Python should keep asking, retrying, or waiting

Community discussion question:
Where can a validation loop prevent mistakes in your daily operations work?
"""

print("Homework: Complete Day09_Exercise.py and share one validation use case.")

print("\nDay 9 completed. You can now control repetitive execution using while loops.")
