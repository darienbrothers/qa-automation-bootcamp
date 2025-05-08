# 📘 Week 1 - Day 2: Lists, Dictionaries, Type Conversion & Loops

## ✅ What I Learned
- **Lists** hold multiple items in a single variable (like a list of test steps).
- **Dictionaries** store data as key-value pairs (like a test case or user profile).
- **Type conversion** is important to ensure data types match (like converting a string number to integer).
- **Loops** allow us to process collections (e.g., iterate through test results).

## 🧠 Concepts Covered
```python
test_steps = ["Open browser", "Click login"]
for step in test_steps:
    print(step)

test_case = {"id": 1, "status": "Passed"}
print(test_case["status"])

num = "100"
print(int(num) + 1)

Takeaways
- Lists are perfect for handling ordered data like test steps or user input sequences.
- Dictionaries are like mini-JSON objects — you’ll use them to model test data, responses, or configs.
- Always check the data type (type() or isinstance()) before doing conversions in automation scripts.
- Loops are essential for scalable test logic — loop through user data, test cases, elements on a page, etc.
- This is how real-world frameworks pass around test data (e.g., reading from Excel or JSON files).