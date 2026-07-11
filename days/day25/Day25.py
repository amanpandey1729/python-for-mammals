"""
Python for Mammals - Day 25
Topic: Modules & Imports

Audience:
- Complete beginners
- DBAs, Sysadmins, Support Engineers, Cloud Engineers, Monitoring Teams
- Anyone who wants Python for practical automation

Goal of Day 25:
By the end of today, you should be able to:
1. Understand why modules are useful in automation
2. Import a complete module using import
3. Access module functions with dot notation
4. Import selected names using from ... import
5. Use aliases with as
6. Create your own reusable Python module
7. Protect test code with if __name__ == "__main__"
8. Build a small modular operational reporting workflow

Why this matters:
Large automation scripts become difficult to read and maintain.
Modules help split one large script into smaller reusable files.

You will use modules for:
- health-check functions
- report formatting
- file and path utilities
- date and time helpers
- inventory calculations
- validation functions
- database connection helpers
- shared configuration logic

Today you learn how to reuse Python's built-in tools and how to create
small modules for your own automation projects.
"""

import math
import platform
from datetime import datetime
from pathlib import Path

print("=" * 70)
print("DAY 25 - MODULES & IMPORTS")
print("import, from import, aliases, creating modules")
print("=" * 70)

# ---------------------------------------------------------------------
# SECTION 1: Project Introduction
# ---------------------------------------------------------------------

print("\nSECTION 1: Project Introduction")

"""
A module is a Python file that contains reusable code.

Python already includes many built-in modules:
- math for mathematical operations
- datetime for date and time work
- pathlib for file-system paths
- platform for operating-system information
- json and csv for structured data files

You can also create your own modules for repeated operational logic.
"""

print("Today we will reuse built-in modules and create our own automation module.")

# ---------------------------------------------------------------------
# SECTION 2: Why Modules Matter in Automation
# ---------------------------------------------------------------------

print("\nSECTION 2: Why Modules Matter in Automation")

"""
Without modules, one automation file can become very large.
The same calculation or validation may also be copied into many scripts.

Modules help you:
- reuse code
- organize related functions
- reduce duplication
- test smaller units
- maintain scripts more safely
- share common logic across a team
"""

print("Modules keep automation scripts reusable, organized, and easier to maintain.")

# ---------------------------------------------------------------------
# SECTION 3: Importing a Complete Module
# ---------------------------------------------------------------------

print("\nSECTION 3: Importing a Complete Module")

"""
Syntax:
import module_name

After importing the module, use dot notation:
module_name.function_name()
"""

rounded_up = math.ceil(72.4)
rounded_down = math.floor(72.4)

print("Rounded up  :", rounded_up)
print("Rounded down:", rounded_down)

# ---------------------------------------------------------------------
# SECTION 4: Dot Notation Makes the Source Clear
# ---------------------------------------------------------------------

print("\nSECTION 4: Dot Notation")

system_name = platform.system()
python_version = platform.python_version()

print("Operating system:", system_name)
print("Python version  :", python_version)

"""
platform.system() clearly shows that system() comes from platform.
This is helpful when several modules contain similarly named functions.
"""

# ---------------------------------------------------------------------
# SECTION 5: Importing Selected Names
# ---------------------------------------------------------------------

print("\nSECTION 5: Importing Selected Names")

"""
Syntax:
from module_name import name

We imported datetime directly:
from datetime import datetime

Now we use datetime.now() without writing datetime.datetime.now().
"""

report_time = datetime(2026, 7, 12, 9, 30)
print("Report time:", report_time)

# ---------------------------------------------------------------------
# SECTION 6: Using Aliases with as
# ---------------------------------------------------------------------

print("\nSECTION 6: Using Aliases with as")

"""
An alias gives a shorter or clearer local name.

Examples:
import datetime as dt
from pathlib import Path as FilePath

Aliases are common, but they should remain understandable.
"""

import statistics as stats

cpu_samples = [42, 55, 61, 48, 70]
average_cpu = stats.mean(cpu_samples)

print("CPU samples:", cpu_samples)
print("Average CPU:", average_cpu)

# ---------------------------------------------------------------------
# SECTION 7: Importing Multiple Names
# ---------------------------------------------------------------------

print("\nSECTION 7: Importing Multiple Names")

from math import ceil, floor

used_gb = 86.7
print("Ceiling value:", ceil(used_gb))
print("Floor value  :", floor(used_gb))

"""
Import only the names you need when it improves readability.
Avoid importing many unrelated names into the same namespace.
"""

# ---------------------------------------------------------------------
# SECTION 8: Avoid import *
# ---------------------------------------------------------------------

print("\nSECTION 8: Avoid import *")

"""
Avoid:
from math import *

It becomes difficult to know where names came from.
It can also overwrite another variable or imported function.

Prefer:
import math
or
from math import ceil
"""

print("Use explicit imports so the source of each function remains clear.")

# ---------------------------------------------------------------------
# SECTION 9: Creating Your Own Module
# ---------------------------------------------------------------------

print("\nSECTION 9: Creating Your Own Module")

"""
A custom module is simply another .py file.

Example file: health_utils.py

    def calculate_usage(used, total):
        return (used / total) * 100

    def get_status(usage):
        if usage >= 90:
            return "CRITICAL"
        elif usage >= 80:
            return "WARNING"
        return "HEALTHY"

A second file can import it:

    import health_utils
    usage = health_utils.calculate_usage(430, 500)
    status = health_utils.get_status(usage)
"""

print("A custom module stores reusable functions in a separate Python file.")

# ---------------------------------------------------------------------
# SECTION 10: Demonstrating Reusable Module Logic
# ---------------------------------------------------------------------

print("\nSECTION 10: Reusable Module Logic")

# These functions demonstrate what could be placed inside health_utils.py.
def calculate_usage(used, total):
    return (used / total) * 100


def get_health_status(usage):
    if usage >= 90:
        return "CRITICAL"
    if usage >= 80:
        return "WARNING"
    return "HEALTHY"


disk_usage = calculate_usage(430, 500)
disk_status = get_health_status(disk_usage)

print("Disk usage %:", round(disk_usage, 2))
print("Disk status :", disk_status)

# ---------------------------------------------------------------------
# SECTION 11: Module Search Location
# ---------------------------------------------------------------------

print("\nSECTION 11: Module Search Location")

"""
For a beginner project, keep your custom module in the same folder
as the script that imports it.

Example folder:
operations_project/
    main.py
    health_utils.py

Then main.py can use:
import health_utils
"""

project_folder = Path("operations_project")
print("Example project folder:", project_folder)
print("Example module file   :", project_folder / "health_utils.py")

# ---------------------------------------------------------------------
# SECTION 12: Understanding __name__
# ---------------------------------------------------------------------

print("\nSECTION 12: Understanding __name__")

"""
Every Python module has a special variable named __name__.

When a file runs directly:
__name__ is "__main__"

When a file is imported:
__name__ is the module name

This pattern prevents demonstration or test code from running during import:

if __name__ == "__main__":
    print("Run module tests here")
"""

print("Current module name:", __name__)

# ---------------------------------------------------------------------
# SECTION 13: Safe Test Code in a Module
# ---------------------------------------------------------------------

print("\nSECTION 13: Safe Test Code in a Module")

"""
Inside health_utils.py:

    def get_status(usage):
        ...

    if __name__ == "__main__":
        print(get_status(86))

The test runs only when health_utils.py is executed directly.
It does not run when another script imports health_utils.
"""

print("Use the __main__ guard for optional module tests and demonstrations.")

# ---------------------------------------------------------------------
# SECTION 14: Handling Import Errors
# ---------------------------------------------------------------------

print("\nSECTION 14: Handling Import Errors")

try:
    import json
    print("json module imported successfully.")
except ModuleNotFoundError:
    print("Required module could not be found.")

"""
Built-in modules normally exist with Python.
Third-party modules may need installation.
A misspelled custom-module name can also raise ModuleNotFoundError.
"""

# ---------------------------------------------------------------------
# SECTION 15: Choosing an Import Style
# ---------------------------------------------------------------------

print("\nSECTION 15: Choosing an Import Style")

"""
Use import module when:
- you want the module name visible
- you use several functions from the same module
- clarity is more important than shorter code

Use from module import name when:
- you need only one or two specific names
- the imported name is clear in the current file

Use aliases when:
- the original name is long
- a standard and understandable alias exists
"""

print("Choose explicit imports that make the script easy to understand.")

# ---------------------------------------------------------------------
# SECTION 16: Guided Practice - Create a Utility Module
# ---------------------------------------------------------------------

print("\nSECTION 16: Guided Practice - Create a Utility Module")

"""
Create two files in the same folder.

File 1: report_utils.py

    def build_summary(system_name, status):
        return f"{system_name} | {status}"

File 2: run_report.py

    from report_utils import build_summary

    summary = build_summary("app01", "HEALTHY")
    print(summary)

Run run_report.py and verify the imported function works.
"""

print("Guided practice: create report_utils.py and import it from run_report.py.")

# ---------------------------------------------------------------------
# SECTION 17: Mini Challenge Preview
# ---------------------------------------------------------------------

print("\nSECTION 17: Mini Challenge Preview")

"""
Mini Challenge:
Build a Modular Capacity Report.

Create capacity_utils.py with reusable functions to:
1. calculate free capacity
2. calculate usage percentage
3. decide HEALTHY, WARNING, or CRITICAL
4. build a one-line summary

Create Day25_Capacity_Report.py to:
1. collect system, environment, total capacity, used capacity, and report file once
2. import the functions from capacity_utils
3. calculate capacity values
4. generate a clean report
5. write and read back the report

This mirrors real automation:
- reusable logic lives in a module
- the main script handles input and workflow
- repeated calculations are not copied everywhere
"""

print("Mini challenge: build a Modular Capacity Report using two Python files.")

# ---------------------------------------------------------------------
# SECTION 18: Closing Message
# ---------------------------------------------------------------------

print("\nSECTION 18: Closing Message")

print("You have completed Day 25.")
print("You can now import built-in tools and organize reusable code into modules.")
print("Modules will help your automation projects stay clean, testable, and maintainable.")
