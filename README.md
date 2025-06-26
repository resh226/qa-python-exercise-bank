
# 📚 QA Python Exercise Bank

This repository contains two subprojects designed to help QA engineers practice core Python skills and Pytest automation scenarios.

---

## 📦 Project Structure

```
qa-python-exercise-bank/
├── qa_python_foundations/       # Core Python practice programs
├── qa_pytest_foundations/       # Pytest-based automation scenarios
└── README.md                    # This file
```

---

## 🔧 Installation & Setup

**Requirements:**
- Python 3.8+
- Install dependencies: pytest( python's test framework), openpyxl(for reading excel) pytest-html(for html report)
- I used PyCharm 2025.1.2 as IDE for running and writing test cases. You can install PyCharm or run direclty using command line.

```bash
pip install pytest openpyxl requests pytest-html
```

---

## 📁 Folder 1: `qa_python_foundations`

**Objective:** Hands-on practice practice and revision on Python basics, useful for QA automation and interviews.

**Topics Covered:**
- ✅ Basics: Arithmetic, conditionals, loops
- ✅ String Handling: Slicing, manipulation, regex
- ✅ List & Dictionary Operations: Sorting, merging, lookups
- ✅ File Handling: Create/read/write/delete files
- ✅ OOP: Classes, `@property`, encapsulation
- ✅ API Testing: Using `requests` for GET, POST, PUT, DELETE

---

## 📁 Folder 2: `qa_pytest_foundations`

**Objective:** Hands-on practice with real-world scenarios using pytest.

| Folder               | Scenario                        | Concepts Used                            | Run Command   (in cmd or using pycharm terminal)                                                   |
|----------------------|----------------------------------|-------------------------------------------|------------------------------------------------------------------|
| `basic_tests/`       | Calculator test                  | `assert`, basic validation                | `pytest basic_tests/test_calculator.py -v`                       |
| `exception_tests/`   | Handle common exceptions         | `pytest.raises`, exception validation     | `pytest exception_tests/test_exceptions.py -v`                   |
| `parameterized_tests/| Login using Excel                | `@pytest.mark.parametrize`, `openpyxl`    | `pytest parameterized_tests/test_login_excel.py -v`              |
| `api_tests/`         | HTTP methods to dummy API        | `requests`, status codes, CRUD validation | `pytest api_tests/test_api_http_methods.py -v`                   |
| `file_handling/`     | Temp file operations             | `tmp_path`, file handling                 | `pytest file_handling/test_temp_file.py -v`                      |
| `fixture_tests/`     | Wallet with shared fixture       | `@pytest.fixture`, `conftest.py`          | `pytest fixture_tests/test_wallet.py -v`                         |
| `property_tests/`    | Covers setter/getter validation  | `@property`, OOP                          | `pytest property_tests/test_circle.py -v`                        |
| `plugins_reports/`   | Generate HTML test report        | `pytest-html` plugin                      | `pytest plugins_reports/test_with_plugins.py --html=report.html` |
| `marker_tests/`      | Smoke marker example             | `@pytest.mark.smoke`, filtering           | `pytest -m smoke`                                                |

---

## 🗂️ Shared Fixture: `conftest.py`

Used for reusable setup logic across multiple test files, e.g., shared Wallet fixture.

---

## 🧪 pytest.ini

Used to configure test behavior and markers globally.

```ini
[pytest]
markers =
    api: API-related tests
    smoke: Smoke tests
addopts = -v
```

---

## 🔁 Concepts Summary

- `assert`: Validates expected results
- `pytest.raises`: Asserts exceptions
- `@pytest.mark.parametrize`: Data-driven tests
- `@pytest.mark`: Tag-based test filtering
- `@property`: Getter/setter methods for encapsulation
- `tmp_path`: Built-in fixture for temp directories
- `openpyxl`: Read Excel for test data
- `conftest.py`: Global fixtures for DRY code
- `pytest.ini`: Configures pytest options # addopts = - v (create verbose results) markers specified in ini so that it wont raise unknown warnings for markers while executing the tests having markers.
- `pytest-html`: HTML reporting plugin

---

## 🎯 Purpose

This repository is built to help:
- 📘 QA professionals preparing for interviews
- 🧪 Beginners learning pytest with real cases
- 🛠️ Practitioners transitioning to automation
- 🔁 Regular practice of Python testing skills

Happy Testing! 🧪🚀

---

## 📅 Author

Reshma Sajeev| ISTQB Certified Tester| Manual & Automation | 🔗 https://www.linkedin.com/in/reshma-sajeev-889b7215b/
* ⭐ This repository is part of my QA learning and practice journey. I'm actively improving it as I grow!

---

> Star this repo if it helped you learn something new! ⭐

