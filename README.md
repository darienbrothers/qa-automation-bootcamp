# 🧪 QA Automation Bootcamp 2025 — Python + Appium + API + BDD (with Java Add-On)

**Author:** Darien Brothers  
**Goal:** Become a job-ready SDET in 6 weeks using Python, Appium, API testing, GitHub, and BDD — plus Java toolchain familiarity to align with enterprise standards.

---

## 📅 6-Week Core Curriculum (Python Track)

### ✅ Week 1: Python Foundations
- Variables, loops, functions, exceptions
- File handling and CLI tools
- Markdown notes + GitHub commits daily

### ✅ Week 2: Appium Mobile Automation (Python)
- Install Appium + Inspector
- Connect to emulator or real device (iOS/Android)
- Automate app actions using `accessibility_id`, `xpath`, etc.

### ✅ Week 3: Page Object Model (POM) + Framework
- Reusable page classes
- Test execution, teardown, logging, and screenshots
- Structure code for scalability

### ✅ Week 4: API Testing (requests + Pytest)
- Automate REST APIs: GET, POST, PUT, DELETE
- Auth handling (Bearer, Basic)
- JSON schema + status validation
- Pytest reports

### ✅ Week 5: BDD with Gherkin (Behave)
- Write `.feature` files
- Create step definitions
- Integrate with Appium + API layers
- Human-readable test automation

### ✅ Week 6: Final Project + CI/CD + Reporting
- Build full-stack mobile/API/BDD test suite
- Generate HTML test reports
- Document GitHub repo + prep resume/demo projects

---

## 🧭 Dual-Track Add-On: Java-Based Enterprise Tools

> Parallel learning path for real-world tool coverage (used in most QA job descriptions)

### 🌐 Java Add-On Track (Optional But Recommended)
| Focus Area      | Toolset                     |
|-----------------|-----------------------------|
| API Testing     | **Rest Assured (Java)**      |
| BDD Framework   | **Cucumber + Gherkin (Java)**|
| Unit Test Runner| **JUnit**                   |
| Build Tool      | **Maven**                   |
| Editor          | **IntelliJ IDEA**           |

These will live inside:  
`/bootcamp-java-addons/java-api-restassured/`  
`/bootcamp-java-addons/java-bdd-cucumber/`

---

## 🧰 Tooling & Skills Summary

### 💻 Languages:
- ✅ **Primary:** Python 3.11+
- 🔄 **Secondary:** Java (Rest Assured + Cucumber)

### 🔧 Tools & Frameworks:
- **Appium (Mobile UI Automation)**
- **requests + Pytest (API testing)**
- **Behave (Python BDD with Gherkin)**
- **Rest Assured (Java API testing)**
- **Cucumber (Java BDD)**
- **GitHub Actions (CI)**
- **Allure or HTML reporting (Optional)**

### 📋 Dev Practices:
- Git branching, commit hygiene, CI pipelines
- Markdown documentation
- Modular framework design
- Resume/project-ready automation code

---

## 📂 Repository Structure

qa-automation-bootcamp/
├── venv/ # Virtual environment
├── LABS/ # All hands-on labs by week/day
│ └── weekX_dayY/
├── NOTES/ # Markdown notes per day
│ └── weekX_dayY_notes.md
├── week1/ # Python Foundations
├── week2/ # Appium Mobile Testing
├── week3/ # POM + Automation Framework
├── week4/ # API Testing (Python)
├── week5/ # BDD with Behave
├── week6/ # Final Project + CI/CD
├── bootcamp-java-addons/ # Java enterprise tooling
│ ├── java-api-restassured/
│ └── java-bdd-cucumber/
└── README.md


---

## ✅ Git Workflow

```bash
# Create a new branch for each day
git checkout -b week1_day1

# Stage and commit your changes
git add .
git commit -m "add: week1_day1 hello world setup"

# Push to GitHub
git push origin week1_day1