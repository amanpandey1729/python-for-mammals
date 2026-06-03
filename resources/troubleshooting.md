# Troubleshooting Guide

Welcome to the Python for Mammals troubleshooting guide.

If something is not working, don't panic.

Most beginner issues have simple fixes.

Use this guide before asking for help in the community.

---

# Python Installation Issues

## Problem

```text
python is not recognized as an internal or external command
```

### Cause

Python was either:

* Not installed
* Not added to PATH

### Solution

1. Reinstall Python
2. Check:

```text
Add Python to PATH
```

during installation.

3. Restart your terminal.

4. Verify:

```bash
python --version
```

---

# Python Version Not Displayed

## Problem

```bash
python --version
```

returns an error.

### Solution

Try:

```bash
py --version
```

If this works, Python is installed correctly.

---

# VS Code Issues

## Problem

VS Code cannot find Python.

### Solution

Press:

```text
Ctrl + Shift + P
```

Search:

```text
Python: Select Interpreter
```

Choose the Python version you installed.

---

## Problem

Run button is missing.

### Solution

Install:

```text
Python Extension (Microsoft)
```

from the Extensions Marketplace.

Restart VS Code.

---

# Terminal Issues

## Problem

Terminal opens but commands do not work.

### Solution

Close all VS Code windows.

Reopen VS Code.

Create a new terminal:

```text
Terminal → New Terminal
```

---

# File Issues

## Problem

Program runs but nothing happens.

### Cause

File was not saved.

### Solution

Save the file:

```text
Ctrl + S
```

Then run again.

---

## Problem

Python file opens in Notepad.

### Solution

Right-click file.

Select:

```text
Open With
```

Choose:

```text
Visual Studio Code
```

---

# Syntax Errors

## Problem

You see:

```python
SyntaxError
```

### Cause

Python could not understand the code.

### Common Reasons

Missing quote:

```python
print("Hello)
```

Missing bracket:

```python
print("Hello"
```

Incorrect indentation:

```python
if True:
print("Hello")
```

### Solution

Read the error carefully.

Python usually tells you the line causing the issue.

---

# Indentation Errors

## Problem

```python
IndentationError
```

### Cause

Spacing is incorrect.

Python uses indentation to understand code blocks.

### Wrong

```python
if True:
print("Hello")
```

### Correct

```python
if True:
    print("Hello")
```

---

# Module Not Found

## Problem

```python
ModuleNotFoundError
```

### Cause

Python cannot find the requested package.

### Example

```python
import pandas
```

but pandas is not installed.

### Solution

Install the package:

```bash
pip install pandas
```

---

# GitHub Issues

## Problem

Push rejected.

### Solution

Pull latest changes first:

```bash
git pull
```

Then:

```bash
git push
```

---

# GitHub Pages Not Updating

## Problem

Website changes are not visible.

### Solution

Wait 2–5 minutes.

Then refresh:

```text
Ctrl + F5
```

GitHub Pages may take time to redeploy.

---

# The Most Important Rule

When asking for help:

Always share:

1. The full error message
2. A screenshot
3. The code you executed
4. What you expected to happen

Never write:

```text
It is not working.
```

Always explain what you tried and what happened.

---

# Remember

Every programmer sees errors.

Errors are not signs of failure.

Errors are clues.

Learning how to read and solve errors is one of the most valuable skills you will develop during this challenge.

Happy debugging. 🐍
