"""
Python for Mammals - Day 9 Exercise File
Topic: While Loops

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
By the end of these exercises, you should be comfortable using while loops,
infinite loop safety, break, continue, and validation loops to control
repetitive execution in practical automation scripts.
"""

print("=" * 70)
print("DAY 9 EXERCISES - WHILE LOOPS")
print("=" * 70)

# ---------------------------------------------------------------------
# EXERCISE 1: Basic Counter Loop
# ---------------------------------------------------------------------

"""
TODO:
- Create counter = 1
- Use a while loop to print counter from 1 to 5
- Increase counter inside the loop

Expected style:
Counter: 1
Counter: 2
...
Counter: 5

Concept focus:
basic while loop with counter update
"""

# Write your code below this line




# ---------------------------------------------------------------------
# EXERCISE 2: Health Check Attempts
# ---------------------------------------------------------------------

"""
TODO:
- Create attempt = 1
- Create max_attempts = 3
- Use a while loop to print each attempt

Expected style:
Running health check attempt: 1
Running health check attempt: 2
Running health check attempt: 3

Concept focus:
controlled repetition with while
"""

# Write your code below this line




# ---------------------------------------------------------------------
# EXERCISE 3: Pending Alert Countdown
# ---------------------------------------------------------------------

"""
Given:
pending_alerts = 5

TODO:
- Use a while loop
- Print pending alert count
- Reduce pending_alerts by 1 each time
- Print No pending alerts left at the end

Concept focus:
loop until value reaches zero
"""

pending_alerts = 5

# Write your code below this line




# ---------------------------------------------------------------------
# EXERCISE 4: Avoid Infinite Loop
# ---------------------------------------------------------------------

"""
TODO:
- Create count = 1
- Write a while loop that runs while count <= 4
- Print count
- Update count inside the loop

Important:
Do not forget to update count.
Without update, the loop may run forever.

Concept focus:
infinite loop prevention
"""

# Write your code below this line




# ---------------------------------------------------------------------
# EXERCISE 5: Stop with break
# ---------------------------------------------------------------------

"""
TODO:
- Create attempt = 1
- Create max_attempts = 5
- Use a while loop
- Print attempt number
- If attempt == 3, print Success and stop the loop using break
- Otherwise increase attempt

Concept focus:
break statement
"""

# Write your code below this line




# ---------------------------------------------------------------------
# EXERCISE 6: Skip with continue
# ---------------------------------------------------------------------

"""
TODO:
- Create window = 0
- Use a while loop to process windows 1 to 5
- Skip window 3 using continue
- Print processed windows only

Expected style:
Processing window: 1
Processing window: 2
Processing window: 4
Processing window: 5

Concept focus:
continue statement
"""

# Write your code below this line




# ---------------------------------------------------------------------
# EXERCISE 7: Validate Environment
# ---------------------------------------------------------------------

"""
TODO:
- Ask the user to enter environment
- Clean input using strip()
- Convert input to uppercase
- Keep asking while environment is not DEV, TEST, or PROD
- Print accepted environment

Concept focus:
validation loop
"""

# Write your code below this line




# ---------------------------------------------------------------------
# EXERCISE 8: Validate Non-Blank Server Name
# ---------------------------------------------------------------------

"""
TODO:
- Ask the user to enter server name
- Keep asking while the cleaned value is blank
- Print accepted server name in lowercase

Concept focus:
blank input validation
"""

# Write your code below this line




# ---------------------------------------------------------------------
# EXERCISE 9: Validate Disk Usage Range
# ---------------------------------------------------------------------

"""
TODO:
- Ask the user for disk usage percentage
- Convert it to float
- Keep asking while value is less than 0 or greater than 100
- Print accepted disk usage

Assume the user enters numeric input for now.

Concept focus:
numeric validation with while
"""

# Write your code below this line




# ---------------------------------------------------------------------
# EXERCISE 10: Retry Confirmation
# ---------------------------------------------------------------------

"""
TODO:
- Ask user to type YES to confirm
- Allow maximum 3 attempts
- If user types YES, print Confirmation accepted and stop
- If attempts finish without YES, print Maximum attempts reached

Concept focus:
while loop with retry limit and break
"""

# Write your code below this line




# ---------------------------------------------------------------------
# EXERCISE 11: Simple Menu Loop
# ---------------------------------------------------------------------

"""
TODO:
- Display a small menu:
    1. Show health summary
    2. Show backup summary
    3. Exit
- Ask user for choice
- Keep running while choice is not 3
- Print a different message for option 1 and option 2
- Print Invalid choice for other values
- Ask for choice again inside the loop
- Print Menu closed at the end

Concept focus:
menu-driven while loop
"""

# Write your code below this line




# ---------------------------------------------------------------------
# EXERCISE 12: Process Until Queue Empty
# ---------------------------------------------------------------------

"""
Given:
queue_count = 4

TODO:
- Use a while loop
- Print Processing queue item: <queue_count>
- Reduce queue_count each time
- Print Queue processing completed at the end

Concept focus:
operational countdown workflow
"""

queue_count = 4

# Write your code below this line




# ---------------------------------------------------------------------
# EXERCISE 13: Mini Project - Validated Disk Usage Reporter
# ---------------------------------------------------------------------

"""
Build a mini Validated Disk Usage Reporter.

Collect all required inputs once at the beginning using validation loops:
1. Server name
2. Environment
3. Disk total size in GB
4. Disk used size in GB

TODO:
- Keep asking for server name until it is not blank
- Keep asking for environment until it is DEV, TEST, or PROD
- Keep asking for disk total until it is greater than 0
- Keep asking for disk used until it is between 0 and disk total
- Calculate disk usage percentage
- Decide status:
    CRITICAL if usage >= 90
    WARNING if usage >= 80
    OK otherwise
- Generate a final report

Expected output style:
========================================
Validated Disk Usage Reporter
========================================
Server      : app01
Environment : PROD
Total GB    : 100.0
Used GB     : 86.0
Usage %     : 86.0
Status      : WARNING
========================================

Important:
Ask each input only once in its own validation section.
Reuse those variables throughout the project.
This should feel like one complete automation workflow.
"""

# Write your mini project code below this line




print("\nExercise file loaded successfully. Complete the tasks one by one.")
