# Python Installation Guide

Welcome to Day 1 of **Python for Mammals**.

Before writing Python programs, we need to install Python correctly and confirm that our system can run it.

---

## 1. Download Python

Go to the official Python website:

https://www.python.org/downloads/

Download the latest stable version for your operating system.

Recommended:

* Windows: 64-bit installer
* macOS: macOS installer
* Linux: Usually Python is pre-installed, but version should be checked

---

## 2. Install Python on Windows

Run the downloaded installer.

Very important:

✅ Check this option before clicking Install:

```text
Add Python to PATH
```

Then click:

```text
Install Now
```

---

## 3. Verify Python Installation

Open Command Prompt, PowerShell, or Terminal.

Run:

```bash
python --version
```

or:

```bash
py --version
```

Expected output:

```text
Python 3.x.x
```

If you see a Python version, installation is successful.

---

## 4. Common Issue: Python Not Recognized

If you see:

```text
python is not recognized as an internal or external command
```

It usually means Python was installed without adding it to PATH.

### Fix

Option 1:

Reinstall Python and make sure this box is checked:

```text
Add Python to PATH
```

Option 2:

Manually add Python to Environment Variables.

For beginners, reinstalling is easier and safer.

---

## 5. Test Your First Python Command

Run:

```bash
python
```

You should enter Python interactive mode.

Then type:

```python
print("Hello Mammals")
```

Expected output:

```text
Hello Mammals
```

To exit Python interactive mode:

```python
exit()
```

---

## 6. What Did We Achieve?

By the end of this setup, you should be able to:

* Install Python
* Open terminal
* Check Python version
* Run a basic Python command
* Confirm your machine is ready for the challenge

---

## Quick Checklist

* [ ] Python downloaded
* [ ] Python installed
* [ ] Add Python to PATH selected
* [ ] `python --version` works
* [ ] `print("Hello Mammals")` runs successfully

---

Happy learning.

Welcome to **Python for Mammals** 🐍
