"""
Python for Mammals - Day 26
Topic: Mini Project #3 - Log File Analyzer

Audience:
- Complete beginners
- DBAs, Sysadmins, Support Engineers, Cloud Engineers, Monitoring Teams
- Anyone who wants Python for practical automation

Goal of Day 26:
By the end of today, you should be able to:
1. Read a text log file safely
2. Process the file one line at a time
3. Clean and inspect log messages using string methods
4. Count log levels with a dictionary
5. Collect important messages for investigation
6. Produce a useful summary report
7. Combine files, strings, loops, conditions, lists, and dictionaries
8. Build a complete Log File Analyzer workflow

Why this matters:
Operational teams often receive large log files containing hundreds or
thousands of messages. Reading every line manually is slow and unreliable.

A log analyzer can:
- count INFO, WARNING, ERROR, and CRITICAL entries
- identify the most serious events
- search for a word, service, host, or error code
- calculate a simple health status
- create a summary report for handover or incident review

Today is a mini-project day. Instead of learning a new isolated concept,
you will combine previously learned concepts into one useful automation.
"""

from pathlib import Path

print("=" * 70)
print("DAY 26 - MINI PROJECT #3: LOG FILE ANALYZER")
print("Files, strings, loops, dictionaries")
print("=" * 70)

# ---------------------------------------------------------------------
# SECTION 1: Project Introduction
# ---------------------------------------------------------------------

print("\nSECTION 1: Project Introduction")

"""
Our project will analyze a plain-text log file.

Each line follows this simple pattern:

timestamp | level | component | message

Example:
2026-07-14 09:00:01 | INFO | scheduler | Daily job started

The analyzer will:
1. open the file
2. process every non-empty line
3. split each line into fields
4. count each log level
5. collect serious messages
6. search for a keyword
7. decide an overall status
8. write a report
"""

print("Project goal: turn a raw log file into a quick operational summary.")

# ---------------------------------------------------------------------
# SECTION 2: Create a Safe Practice Log
# ---------------------------------------------------------------------

print("\nSECTION 2: Create a Safe Practice Log")

sample_log_lines = [
    "2026-07-14 09:00:01 | INFO | scheduler | Daily job started",
    "2026-07-14 09:02:14 | WARNING | storage | Disk usage reached 82 percent",
    "2026-07-14 09:03:48 | ERROR | backup | Backup file could not be created",
    "2026-07-14 09:05:10 | INFO | scheduler | Daily job completed",
    "2026-07-14 09:07:21 | CRITICAL | network | Primary service is unreachable",
    "2026-07-14 09:08:33 | ERROR | authentication | Three login attempts failed",
    "2026-07-14 09:10:00 | INFO | monitoring | Health check completed",
]

log_file = Path("day26_sample.log")

with log_file.open("w", encoding="utf-8") as file_object:
    for log_line in sample_log_lines:
        file_object.write(log_line + "\n")

print("Practice log created:", log_file)
print("Lines written       :", len(sample_log_lines))

# ---------------------------------------------------------------------
# SECTION 3: Prepare Counters and Collections
# ---------------------------------------------------------------------

print("\nSECTION 3: Prepare Counters and Collections")

level_counts = {
    "INFO": 0,
    "WARNING": 0,
    "ERROR": 0,
    "CRITICAL": 0,
    "UNKNOWN": 0,
}

serious_events = []
component_counts = {}
search_keyword = "backup"
matching_lines = []
total_lines = 0
malformed_lines = 0

print("Counters and collections are ready.")
print("Search keyword:", search_keyword)

# ---------------------------------------------------------------------
# SECTION 4: Read the File Line by Line
# ---------------------------------------------------------------------

print("\nSECTION 4: Read the File Line by Line")

"""
Line-by-line reading is useful for logs because it avoids loading the
entire file into memory at once.

with log_file.open(...) also closes the file automatically.
"""

with log_file.open("r", encoding="utf-8") as file_object:
    for raw_line in file_object:
        clean_line = raw_line.strip()

        if clean_line == "":
            continue

        total_lines += 1

print("Non-empty lines processed:", total_lines)

# ---------------------------------------------------------------------
# SECTION 5: Split and Validate Each Log Line
# ---------------------------------------------------------------------

print("\nSECTION 5: Split and Validate Each Log Line")

"""
split("|") separates the line into fields.
strip() removes surrounding spaces from every field.

A valid line should contain exactly four fields:
timestamp, level, component, and message.
"""

with log_file.open("r", encoding="utf-8") as file_object:
    first_line = file_object.readline().strip()

first_parts = [part.strip() for part in first_line.split("|")]

print("First timestamp:", first_parts[0])
print("First level    :", first_parts[1])
print("First component:", first_parts[2])
print("First message  :", first_parts[3])

# ---------------------------------------------------------------------
# SECTION 6: Complete Analysis Loop
# ---------------------------------------------------------------------

print("\nSECTION 6: Complete Analysis Loop")

# Reset values because the complete workflow will perform the analysis.
level_counts = {
    "INFO": 0,
    "WARNING": 0,
    "ERROR": 0,
    "CRITICAL": 0,
    "UNKNOWN": 0,
}
serious_events = []
component_counts = {}
matching_lines = []
total_lines = 0
malformed_lines = 0

with log_file.open("r", encoding="utf-8") as file_object:
    for raw_line in file_object:
        clean_line = raw_line.strip()

        if clean_line == "":
            continue

        total_lines += 1
        parts = [part.strip() for part in clean_line.split("|")]

        if len(parts) != 4:
            malformed_lines += 1
            continue

        timestamp, level, component, message = parts
        level = level.upper()

        if level in level_counts:
            level_counts[level] += 1
        else:
            level_counts["UNKNOWN"] += 1

        component_counts[component] = component_counts.get(component, 0) + 1

        if level in ("ERROR", "CRITICAL"):
            serious_events.append(
                f"{timestamp} | {level} | {component} | {message}"
            )

        if search_keyword.lower() in clean_line.lower():
            matching_lines.append(clean_line)

print("Analysis loop completed.")

# ---------------------------------------------------------------------
# SECTION 7: Understand Dictionary Counting
# ---------------------------------------------------------------------

print("\nSECTION 7: Dictionary Counting")

"""
A dictionary connects each category with its count.

component_counts.get(component, 0) means:
- return the current count when the key exists
- otherwise return 0

Then + 1 records the current log entry.
"""

print("Level counts    :", level_counts)
print("Component counts:", component_counts)

# ---------------------------------------------------------------------
# SECTION 8: Identify Serious Events
# ---------------------------------------------------------------------

print("\nSECTION 8: Identify Serious Events")

print("Serious event count:", len(serious_events))

for event_number, event in enumerate(serious_events, start=1):
    print(f"{event_number}. {event}")

# ---------------------------------------------------------------------
# SECTION 9: Search the Log
# ---------------------------------------------------------------------

print("\nSECTION 9: Search the Log")

print("Keyword:", search_keyword)
print("Matches:", len(matching_lines))

for matching_line in matching_lines:
    print(matching_line)

# ---------------------------------------------------------------------
# SECTION 10: Decide Overall Health
# ---------------------------------------------------------------------

print("\nSECTION 10: Decide Overall Health")

"""
This is a simple project rule, not a universal monitoring standard:

- CRITICAL when at least one CRITICAL entry exists
- ATTENTION when there are ERROR or WARNING entries
- HEALTHY when only informational entries exist
"""

if level_counts["CRITICAL"] > 0:
    overall_status = "CRITICAL"
elif level_counts["ERROR"] > 0 or level_counts["WARNING"] > 0:
    overall_status = "ATTENTION"
else:
    overall_status = "HEALTHY"

print("Overall log status:", overall_status)

# ---------------------------------------------------------------------
# SECTION 11: Find the Busiest Component
# ---------------------------------------------------------------------

print("\nSECTION 11: Find the Busiest Component")

if component_counts:
    busiest_component = max(component_counts, key=component_counts.get)
    busiest_count = component_counts[busiest_component]
else:
    busiest_component = "NONE"
    busiest_count = 0

print("Busiest component:", busiest_component)
print("Entries recorded :", busiest_count)

# ---------------------------------------------------------------------
# SECTION 12: Build the Summary Report
# ---------------------------------------------------------------------

print("\nSECTION 12: Build the Summary Report")

report_lines = [
    "=" * 60,
    "LOG FILE ANALYSIS REPORT",
    "=" * 60,
    f"Source file      : {log_file}",
    f"Total entries    : {total_lines}",
    f"Malformed entries: {malformed_lines}",
    f"INFO count       : {level_counts['INFO']}",
    f"WARNING count    : {level_counts['WARNING']}",
    f"ERROR count      : {level_counts['ERROR']}",
    f"CRITICAL count   : {level_counts['CRITICAL']}",
    f"UNKNOWN count    : {level_counts['UNKNOWN']}",
    f"Serious events   : {len(serious_events)}",
    f"Search keyword   : {search_keyword}",
    f"Keyword matches  : {len(matching_lines)}",
    f"Busiest component: {busiest_component}",
    f"Overall status   : {overall_status}",
    "=" * 60,
]

report_text = "\n".join(report_lines)
print(report_text)

# ---------------------------------------------------------------------
# SECTION 13: Add Serious Events to the Report
# ---------------------------------------------------------------------

print("\nSECTION 13: Add Serious Events to the Report")

report_text += "\n\nSERIOUS EVENTS\n"

if serious_events:
    for event_number, event in enumerate(serious_events, start=1):
        report_text += f"{event_number}. {event}\n"
else:
    report_text += "No ERROR or CRITICAL events found.\n"

print("Serious-event section added.")

# ---------------------------------------------------------------------
# SECTION 14: Write and Read Back the Report
# ---------------------------------------------------------------------

print("\nSECTION 14: Write and Read Back the Report")

report_file = Path("day26_log_analysis_report.txt")
report_file.write_text(report_text, encoding="utf-8")

saved_report = report_file.read_text(encoding="utf-8")

print("Report saved to:", report_file)
print("Saved report size:", len(saved_report), "characters")

# ---------------------------------------------------------------------
# SECTION 15: Real-World Improvement Ideas
# ---------------------------------------------------------------------

print("\nSECTION 15: Real-World Improvement Ideas")

"""
You can improve this project later by adding:
- user input for source and report file names
- date-range filtering
- multiple search keywords
- top error-message counting
- CSV or JSON report output
- exception handling for missing or unreadable files
- command-line arguments
- email or monitoring integration
- regular expressions for complex log formats
"""

print("The same workflow can be adapted to application, database, OS, and cloud logs.")

# ---------------------------------------------------------------------
# SECTION 16: Guided Practice
# ---------------------------------------------------------------------

print("\nSECTION 16: Guided Practice")

"""
Guided practice:
1. Change search_keyword from backup to failed.
2. Add one malformed line to sample_log_lines.
3. Add one new log level named DEBUG.
4. Decide whether DEBUG should have its own counter or become UNKNOWN.
5. Run the script and inspect how the report changes.
"""

print("Guided practice: change the sample data and observe every report counter.")

# ---------------------------------------------------------------------
# SECTION 17: Mini Challenge
# ---------------------------------------------------------------------

print("\nSECTION 17: Mini Challenge")

"""
Build your own Log File Analyzer.

Collect these inputs once:
1. source log file name
2. report file name
3. search keyword

Then:
- validate that the source file exists
- read every non-empty line
- split valid lines into four fields
- count INFO, WARNING, ERROR, CRITICAL, and UNKNOWN
- count entries per component
- collect ERROR and CRITICAL entries
- count keyword matches
- decide overall status
- identify the busiest component
- generate and save a complete report
- read the report back and print it

Do not ask for the same input repeatedly.
Reuse the collected values throughout the workflow.
"""

print("Mini challenge: build an input-driven Log File Analyzer.")

# ---------------------------------------------------------------------
# SECTION 18: Closing Message
# ---------------------------------------------------------------------

print("\nSECTION 18: Closing Message")

print("You have completed Day 26 and Mini Project #3.")
print("You combined files, strings, loops, lists, conditions, and dictionaries.")
print("You can now turn a raw text log into a useful operational report.")
