import json

# 📝 1. Write test steps to a plain text file
with open("LABS/week1_day4/test_steps.txt", "w") as file:
    file.write("Step 1: Open browser\n")
    file.write("Step 2: Go to login page\n")
    file.write("Step 3: Enter username and password\n")
    file.write("Step 4: Click login\n")

# 📖 2. Read and display contents of the text file
print("📂 Reading test_steps.txt:")
with open("LABS/week1_day4/test_steps.txt", "r") as file:
    for line in file:
        print(f"🔹 {line.strip()}")

# 🧠 3. Define a dictionary as test data
test_case = {
    "test_name": "Login Test",
    "steps": ["Open browser", "Enter credentials", "Submit"],
    "expected_result": "Dashboard should load"
}

# 💾 4. Save the dictionary to a JSON file
with open("LABS/week1_day4/test_data.json", "w") as json_file:
    json.dump(test_case, json_file, indent=4)

# 📥 5. Read and print data from JSON file
print("\n📘 Test Case from JSON:")
with open("LABS/week1_day4/test_data.json", "r") as json_file:
    loaded_data = json.load(json_file)
    print(f"🧪 Test Name: {loaded_data['test_name']}")
    for step in loaded_data["steps"]:
        print(f"✔️ Step: {step}")
    print(f"🎯 Expected Result: {loaded_data['expected_result']}")
