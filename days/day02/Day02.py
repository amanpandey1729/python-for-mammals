"""
Day 2 Python Practice
Topic: Comments, print(), arithmetic, variables, assignment, data types, and type()

How to run:
    python Day2.py

Goal:
    Read the comments, run the file, change some values, and observe the output.
"""

# ============================================================
# 1. COMMENTS
# ============================================================

# This is a single-line comment.
# Python ignores comments. They are written for humans.

"""
This is a multi-line string.
It is often used as a file-level note or documentation.
For Day 2, use comments to explain WHY something is done,
not to explain every obvious line.
"""


# ============================================================
# 2. PRINTING OUTPUT
# ============================================================

print("=" * 60)
print("DAY 2: PYTHON BASICS PRACTICE")
print("=" * 60)

print("Hello, Mammals!")
print("Python can print text, numbers, and calculated results.")
print()  # prints a blank line


# ============================================================
# 3. BASIC ARITHMETIC
# ============================================================

print("1) Basic Arithmetic")
print("Addition:", 10 + 5)
print("Subtraction:", 10 - 5)
print("Multiplication:", 10 * 5)
print("Division:", 10 / 5)          # always returns a float
print("Floor Division:", 11 // 5)  # returns quotient without decimal part
print("Remainder:", 11 % 5)        # modulo operator
print("Power:", 2 ** 5)            # 2 raised to the power 5
print()

# Operator precedence matters.
print("Without parentheses:", 10 + 5 * 2)
print("With parentheses:", (10 + 5) * 2)
print()


# ============================================================
# 4. VARIABLES AND ASSIGNMENT
# ============================================================

print("2) Variables and Assignment")

# A variable is a name that stores a value.
movie_name = "Interstellar"
rating = 8.7
year_released = 2014
is_rewatch_worthy = True

print("Movie:", movie_name)
print("Rating:", rating)
print("Year:", year_released)
print("Rewatch worthy:", is_rewatch_worthy)
print()

# Assignment means giving a value to a variable.
score = 50
print("Initial score:", score)

score = score + 10
print("After bonus:", score)

# Shorter version of score = score + 5
score += 5
print("After small reward:", score)
print()


# ============================================================
# 5. MEANINGFUL MINI EXAMPLE: TRIP BUDGET ESTIMATOR
# ============================================================

print("3) Mini Example: Trip Budget Estimator")

city = "Jaipur"
days = 3
hotel_per_day = 1800
food_per_day = 700
travel_cost = 2500
misc_cost = 1000

hotel_total = days * hotel_per_day
food_total = days * food_per_day
total_budget = hotel_total + food_total + travel_cost + misc_cost
per_day_average = total_budget / days

print("Destination:", city)
print("Days:", days)
print("Hotel total:", hotel_total)
print("Food total:", food_total)
print("Travel cost:", travel_cost)
print("Misc cost:", misc_cost)
print("Total budget:", total_budget)
print("Average cost per day:", per_day_average)
print()


# ============================================================
# 6. DATA TYPES
# ============================================================

print("4) Common Data Types")

name = "Aarav"          # str: text
age = 24                # int: whole number
height = 5.9            # float: decimal number
is_student = False      # bool: True or False
nothing_here = None     # NoneType: absence of value

print(name, "is", type(name))
print(age, "is", type(age))
print(height, "is", type(height))
print(is_student, "is", type(is_student))
print(nothing_here, "is", type(nothing_here))
print()


# ============================================================
# 7. STRING + NUMBER: IMPORTANT BEGINNER LESSON
# ============================================================

print("5) Strings and Numbers")

apples = 5
oranges = 3

print("Total fruits:", apples + oranges)

# The following would cause an error because Python cannot directly add str + int:
# print("I have " + apples + " apples")

# Correct options:
print("I have", apples, "apples")
print("I have " + str(apples) + " apples")
print(f"I have {apples} apples and {oranges} oranges")
print()


# ============================================================
# 8. TYPE CONVERSION
# ============================================================

print("6) Type Conversion")

price_text = "499"
quantity = 2

# price_text is currently a string, so convert it to int before arithmetic.
price_number = int(price_text)
bill_amount = price_number * quantity

print("price_text:", price_text, "| type:", type(price_text))
print("price_number:", price_number, "| type:", type(price_number))
print("Bill amount:", bill_amount)
print()

# Other useful conversions
print("float('99.5') gives", float("99.5"))
print("str(2026) gives", str(2026))
print("bool(0) gives", bool(0))
print("bool(1) gives", bool(1))
print()


# ============================================================
# 9. QUICK SELF-CHECK SECTION
# ============================================================

print("7) Quick Self-Check")

item_name = "Notebook"
item_price = 45
item_quantity = 4
discount = 20

amount_before_discount = item_price * item_quantity
amount_after_discount = amount_before_discount - discount

print("Item:", item_name)
print("Amount before discount:", amount_before_discount)
print("Discount:", discount)
print("Amount after discount:", amount_after_discount)
print("Type of amount_after_discount:", type(amount_after_discount))
print()

print("Practice idea: Change the values above and run the file again.")
print("Done with Day 2 practice. Keep experimenting!")
