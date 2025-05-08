# Function: A reusable block of code that performs a specific task.

def greet_user(name):
    print(f"Hello, {name}! Welcome to QA Automation.")

# Call the function
greet_user("Darien")

# Function with return value
def sum_numbers(a, b):
    result = a + b
    return result

total = sum_numbers(10, 20)
print(f"Sum result: {total}")

# Function that runs test steps
def run_test_case(test_name, steps):
    print(f"Running Test: {test_name}")
    for step in steps:
        print(f"Step: {step}")
    print(f"Test '{test_name}' completed.\n")

# Test data
steps = ["Open browser", "Navigate to login", "Enter username", "Click submit"]

# Execute the function
run_test_case("Login Test", steps)

# Optional: Function with default parameters
def log_result(test_name, status="Passed"):
    print(f" {test_name}: {status}")

log_result("Login Test")  # Uses default status
log_result("Checkout Test", status="Failed")  # Custom status

