test_steps = ["Open browser", "Go to login page", "Enter credentials", "Click login"]
print("Test Steps:", test_steps)

# Lopping through steps
print(f"\nExecuting Test Steps:")
for step in test_steps:
    print("✔️", step)

# Now let's use a dictionary (key-value pairs)
test_case = {
    "id": 101,
    "name": "Login Test",
    "status": "Passed",
    "execution_time": 1.23
}

print(f"\nTest Case Details:", test_case)

# Access values
print("ID:", test_case["id"])
print("Name:", test_case["name"])

# Type conversion
num = "100"
print(f"\nConverting string to int:", int(num) + 1) # Outputs 101

# If-else with type check
if isinstance(num, str):
    print(f"\'num' is a string, converting it to int:", int(num))

# Loop through test cases list of dicts
test_suite = [
    {"id": 1, "status": "Passed"},
    {"id": 2, "status": "Failed"},
    {"id": 3, "status": "Skipped"}
]

print(f"\nTest Suite Results:")
for case in test_suite:
    print(f"Test Case {case['id']}: {case['status']}")

