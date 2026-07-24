"""
Python for Mammals - Day 30
Topic: subprocess - Running Commands and Capturing Output

Audience:
- Complete beginners
- DBAs, Sysadmins, Support Engineers, Cloud Engineers, Monitoring Teams
- Anyone who wants Python for practical automation

Goal of Day 30:
By the end of today, you should be able to:
1. Understand why subprocess is useful in automation
2. Run a safe external command with subprocess.run()
3. Pass command arguments as a list
4. Capture standard output
5. Capture standard error
6. inspect a command's return code
7. Use text=True for readable string output
8. Use check=True when failure should raise an exception
9. Handle CalledProcessError and FileNotFoundError
10. Build a small command-check workflow

Why this matters:
Operations professionals already use command-line tools for health checks,
inventory collection, service inspection, version checks, diagnostics, and
daily administration. Python's subprocess module lets a script run those tools,
capture their results, evaluate success or failure, and include the result in
a larger automation workflow.

Safety note:
Commands can change systems. Today's examples use Python itself as the external
program so they remain cross-platform and harmless. In real automation, avoid
building command strings from untrusted input, prefer argument lists, validate
every command, and test read-only checks before using administrative actions.
"""

import subprocess
import sys

print("=" * 70)
print("DAY 30 - SUBPROCESS")
print("Running commands and capturing output")
print("=" * 70)

# ---------------------------------------------------------------------
# SECTION 1: Why Use subprocess?
# ---------------------------------------------------------------------

print("\nSECTION 1: Why Use subprocess?")

"""
subprocess connects Python automation with external programs.

A workflow can:
1. run a command
2. capture its output
3. inspect its return code
4. decide what should happen next

Examples:
- collect a tool version
- run a read-only health check
- capture command output for a report
- detect whether a utility is missing
- mark a check as SUCCESS or ATTENTION
"""

print("subprocess lets Python run external commands and evaluate the result.")

# ---------------------------------------------------------------------
# SECTION 2: Run a Safe Command
# ---------------------------------------------------------------------

print("\nSECTION 2: Run a Safe Command")

result = subprocess.run(
    [sys.executable, "-c", "print('Command completed')"],
    capture_output=True,
    text=True,
)

print("Return code:", result.returncode)
print("Output     :", result.stdout.strip())

"""
subprocess.run() waits for the command to finish.
Using a list keeps the program and each argument separate.

sys.executable points to the Python interpreter currently running this script.
That makes these examples more portable than assuming python or python3.
"""

# ---------------------------------------------------------------------
# SECTION 3: Capture Standard Output
# ---------------------------------------------------------------------

print("\nSECTION 3: Capture Standard Output")

output_result = subprocess.run(
    [
        sys.executable,
        "-c",
        "print('Server: app01'); print('Status: READY')",
    ],
    capture_output=True,
    text=True,
)

captured_output = output_result.stdout.strip()

print("Captured output:")
print(captured_output)

"""
capture_output=True captures stdout and stderr.
text=True returns readable strings instead of bytes.
strip() removes the final newline from captured text.
"""

# ---------------------------------------------------------------------
# SECTION 4: Capture Multiple Output Lines
# ---------------------------------------------------------------------

print("\nSECTION 4: Capture Multiple Output Lines")

multi_result = subprocess.run(
    [
        sys.executable,
        "-c",
        "print('CPU: 42%'); print('Memory: 68%'); print('Disk: 55%')",
    ],
    capture_output=True,
    text=True,
)

output_lines = multi_result.stdout.strip().splitlines()

print("Line count:", len(output_lines))

for line_number, line in enumerate(output_lines, start=1):
    print(f"{line_number}. {line}")

"""
Captured output is normal text.
splitlines() converts a multiline result into a list that can be filtered,
counted, validated, or added to a report.
"""

# ---------------------------------------------------------------------
# SECTION 5: Understand Return Codes
# ---------------------------------------------------------------------

print("\nSECTION 5: Understand Return Codes")

success_result = subprocess.run(
    [sys.executable, "-c", "raise SystemExit(0)"],
    capture_output=True,
    text=True,
)

failure_result = subprocess.run(
    [sys.executable, "-c", "raise SystemExit(3)"],
    capture_output=True,
    text=True,
)

print("Success return code:", success_result.returncode)
print("Failure return code:", failure_result.returncode)

"""
A return code of 0 normally means success.
A non-zero return code normally means the command reported a problem.

The exact meaning of a non-zero value depends on the external program.
Always check that tool's documentation before interpreting specific codes.
"""

# ---------------------------------------------------------------------
# SECTION 6: Capture Standard Error
# ---------------------------------------------------------------------

print("\nSECTION 6: Capture Standard Error")

error_result = subprocess.run(
    [
        sys.executable,
        "-c",
        "import sys; print('Configuration missing', file=sys.stderr); raise SystemExit(2)",
    ],
    capture_output=True,
    text=True,
)

print("Return code:", error_result.returncode)
print("Standard error:", error_result.stderr.strip())

"""
stderr is separate from stdout.
Operational tools often write warnings and failures to stderr.
A useful automation report should inspect both streams.
"""

# ---------------------------------------------------------------------
# SECTION 7: Decide Status from a Return Code
# ---------------------------------------------------------------------

print("\nSECTION 7: Decide Command Status")

status_result = subprocess.run(
    [sys.executable, "-c", "print('Health check complete'); raise SystemExit(0)"],
    capture_output=True,
    text=True,
)

if status_result.returncode == 0:
    command_status = "SUCCESS"
else:
    command_status = "ATTENTION"

print("Command output:", status_result.stdout.strip())
print("Command status:", command_status)

# ---------------------------------------------------------------------
# SECTION 8: Use check=True
# ---------------------------------------------------------------------

print("\nSECTION 8: Use check=True")

"""
check=True asks subprocess.run() to raise CalledProcessError when the command
returns a non-zero code. This is useful when failure should immediately move
execution into exception-handling logic.
"""

try:
    checked_result = subprocess.run(
        [sys.executable, "-c", "print('Validation passed')"],
        capture_output=True,
        text=True,
        check=True,
    )
    print("Checked output:", checked_result.stdout.strip())
except subprocess.CalledProcessError as error:
    print("Command failed with return code:", error.returncode)

# ---------------------------------------------------------------------
# SECTION 9: Handle a Failed Command
# ---------------------------------------------------------------------

print("\nSECTION 9: Handle a Failed Command")

try:
    subprocess.run(
        [
            sys.executable,
            "-c",
            "import sys; print('Validation failed', file=sys.stderr); raise SystemExit(4)",
        ],
        capture_output=True,
        text=True,
        check=True,
    )
except subprocess.CalledProcessError as error:
    print("Failure captured")
    print("Return code:", error.returncode)
    print("Error text :", error.stderr.strip())

# ---------------------------------------------------------------------
# SECTION 10: Handle a Missing Program
# ---------------------------------------------------------------------

print("\nSECTION 10: Handle a Missing Program")

try:
    subprocess.run(
        ["python_for_mammals_missing_program_30"],
        capture_output=True,
        text=True,
        check=True,
    )
except (FileNotFoundError, PermissionError):
    print("Program not found or not executable. Verify the executable name or path.")

"""
FileNotFoundError usually means the requested executable could not be found.
This is different from a program that starts and then returns a non-zero code.
"""

# ---------------------------------------------------------------------
# SECTION 11: Add a Timeout
# ---------------------------------------------------------------------

print("\nSECTION 11: Add a Timeout")

try:
    timeout_result = subprocess.run(
        [sys.executable, "-c", "print('Quick check finished')"],
        capture_output=True,
        text=True,
        timeout=5,
        check=True,
    )
    print("Timeout-safe output:", timeout_result.stdout.strip())
except subprocess.TimeoutExpired:
    print("Command exceeded the allowed time.")
except subprocess.CalledProcessError as error:
    print("Command failed with return code:", error.returncode)

"""
timeout prevents a command from waiting forever.
The value is measured in seconds.
Choose a timeout that fits the real command's expected behaviour.
"""

# ---------------------------------------------------------------------
# SECTION 12: Build a Reusable Command Runner
# ---------------------------------------------------------------------

print("\nSECTION 12: Build a Reusable Command Runner")


def run_command(command):
    """Run one command and return a compact result dictionary."""
    try:
        completed = subprocess.run(
            command,
            capture_output=True,
            text=True,
            timeout=10,
        )
        return {
            "status": "SUCCESS" if completed.returncode == 0 else "ATTENTION",
            "return_code": completed.returncode,
            "stdout": completed.stdout.strip(),
            "stderr": completed.stderr.strip(),
        }
    except FileNotFoundError:
        return {
            "status": "PROGRAM NOT FOUND",
            "return_code": None,
            "stdout": "",
            "stderr": "Executable could not be found",
        }
    except subprocess.TimeoutExpired:
        return {
            "status": "TIMEOUT",
            "return_code": None,
            "stdout": "",
            "stderr": "Command exceeded 10 seconds",
        }


command_result = run_command(
    [sys.executable, "-c", "print('Inventory collected')"]
)

print("Status      :", command_result["status"])
print("Return code :", command_result["return_code"])
print("Output      :", command_result["stdout"])

# ---------------------------------------------------------------------
# SECTION 13: Build a Command Summary
# ---------------------------------------------------------------------

print("\nSECTION 13: Build a Command Summary")

summary_result = subprocess.run(
    [
        sys.executable,
        "-c",
        "print('Check: storage'); print('Result: OK'); raise SystemExit(0)",
    ],
    capture_output=True,
    text=True,
)

summary_status = "SUCCESS" if summary_result.returncode == 0 else "ATTENTION"

summary_lines = [
    "=" * 60,
    "COMMAND EXECUTION SUMMARY",
    "=" * 60,
    f"Executable  : {sys.executable}",
    f"Return code : {summary_result.returncode}",
    f"Status      : {summary_status}",
    "Standard output:",
    summary_result.stdout.strip() or "<empty>",
    "Standard error:",
    summary_result.stderr.strip() or "<empty>",
    "=" * 60,
]

print("\n".join(summary_lines))

# ---------------------------------------------------------------------
# SECTION 14: Guided Practice
# ---------------------------------------------------------------------

print("\nSECTION 14: Guided Practice")

"""
Guided practice:
1. Change the printed message inside a safe Python -c command.
2. Capture two or three output lines and split them with splitlines().
3. Run a command that exits with 0 and one that exits with 2.
4. Print stdout, stderr, and returncode separately.
5. Add check=True and catch CalledProcessError.
6. Try a harmless missing executable and catch FileNotFoundError.
7. Add a short timeout to a quick command.
8. Reuse run_command() with both a successful and failed command.
9. Build a compact report from the returned dictionary.
"""

print("Guided practice: run, capture, inspect, handle, and report.")

# ---------------------------------------------------------------------
# SECTION 15: Mini Challenge
# ---------------------------------------------------------------------

print("\nSECTION 15: Mini Challenge")

"""
Build a Command Health Check Runner.

Collect these inputs once:
1. Check name
2. Command message
3. Simulated return code
4. Timeout in seconds

For safe cross-platform practice, build this command:
[
    sys.executable,
    "-c",
    <small Python code using the supplied message and return code>
]

Then:
- validate that the return code is a non-negative integer
- validate that timeout is positive
- run the command once
- capture stdout and stderr
- inspect the return code
- decide SUCCESS or ATTENTION
- record start time, end time, and elapsed duration
- handle CalledProcessError, TimeoutExpired, FileNotFoundError, and ValueError
- generate a clean final report
- avoid asking for the same input more than once

The final workflow should clearly show:
check name, command list, timeout, return code, stdout, stderr, duration,
final status, and any exception message.
"""

print("Mini challenge: build an input-driven Command Health Check Runner.")

# ---------------------------------------------------------------------
# SECTION 16: Day 30 Summary
# ---------------------------------------------------------------------

print("\nSECTION 16: Day 30 Summary")
print("Today you ran commands, captured output, and inspected return codes.")
print("You also handled failures, missing programs, and timeouts safely.")
print("Day 30 complete. Reliable automation checks both output and outcome.")
