# 📂 Week 1 – Day 4: File Handling (TXT + JSON)

## ✅ What I Learned
- How to **write to a `.txt` file** for logging or documenting steps.
- How to **read a `.txt` file line by line** using `with open()`.
- How to store and load **structured test data in `.json` format**.
- How `json.dump()` and `json.load()` work for saving/loading test cases.

## 🧠 Code Examples
```python
# Write a file
with open("file.txt", "w") as f:
    f.write("Step 1\nStep 2")

# Read a file
with open("file.txt", "r") as f:
    for line in f:
        print(line)

# Write JSON
import json
with open("data.json", "w") as f:
    json.dump({"key": "value"}, f)

# Read JSON
with open("data.json", "r") as f:
    data = json.load(f)

Takeaways
- with open() is best practice — it auto-closes files to prevent memory leaks.
- Text files are great for step logs, test case checklists, or simple output.
- JSON is ideal for storing test data, expected results, and API payloads.
- File handling will help us automate test suites that pull data from external sources — just like Selenium/Appium frameworks use external config files or test data!