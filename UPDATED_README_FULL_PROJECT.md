
# 🧪 QA Python Exercise Bank

A comprehensive repository covering both **core Python programming** exercises and **Pytest-based test automation** examples.

---

## 📁 Folder Structure

```
qa_python_exercise_bank/
│
├── qa_python_foundations/         ← Core Python programs for logic, strings, OOP, etc.
└── qa_pytest_foundations/         ← Pytest automation examples with real-world scenarios
```

---

## ✅ Setup Instructions

### 🛠️ Python Version
- Python 3.10 or higher recommended

### 📦 Required Packages

```bash
pip install pytest
pip install openpyxl      # For Excel parameterization
pip install pytest-html   # For HTML reporting
```

---

## 🧠 Summary of Concepts Used

| Category              | Concepts Covered                                                                 |
|-----------------------|----------------------------------------------------------------------------------|
| Python Basics         | Loops, conditions, functions, file I/O, OOP (class, inheritance, encapsulation) |
| String Handling       | Anagram, palindrome, reversal, frequency count                                  |
| Lists & Dictionaries  | Sorting, merging, finding duplicates, comparison                                 |
| Pytest Basics         | Assertions, `-v`, `-k`, `-m`, `--maxfail`, test discovery                        |
| Pytest Advanced       | Fixtures, parameterization, `pytest.ini`, plugins, conftest                     |
| API Testing           | GET, POST, PUT, DELETE using `requests`                                         |
| Reporting             | HTML reports with `pytest-html`                                                 |
| Test Configuration    | pytest.ini settings, markers, test structure                                     |

---

## 🧪 QA Pytest Foundations

### 📂 `basic_tests/test_calculator.py`
**Scenario**: Validate a simple calculator’s add function  
**Concepts**: Basic assertion, test method structure  
**Run**:
```bash
pytest qa_pytest_foundations/basic_tests/test_calculator.py -v
```

---

### 📂 `exception_tests/test_common_exceptions.py`
**Scenario**: Check correct handling of divide-by-zero and invalid index  
**Concepts**: Exception testing with `pytest.raises`  
**Run**:
```bash
pytest qa_pytest_foundations/exception_tests/test_common_exceptions.py -v
```

---

### 📂 `parameterized_tests/test_login_csv.py`
**Scenario**: Login validation using data from Excel  
**Concepts**: `@pytest.mark.parametrize`, Excel file reading via `openpyxl`, helper functions  
**Run**:
```bash
pytest qa_pytest_foundations/parameterized_tests/test_login_csv.py -v
```

---

### 📂 `api_tests/test_api_http_methods.py`
**Scenario**: Test all major HTTP methods (GET, POST, PUT, DELETE) on placeholder API  
**Concepts**: API automation using `requests`, response validation  
**Run**:
```bash
pytest qa_pytest_foundations/api_tests/test_api_http_methods.py -v
```

---

### 📂 `file_handling/test_temp_file.py`
**Scenario**: Write and read from temporary files  
**Concepts**: `tmp_path` fixture, file operations  
**Run**:
```bash
pytest qa_pytest_foundations/file_handling/test_temp_file.py -v
```

---

### 📂 `fixture_tests/test_wallet.py`, `wallet.py`, `conftest.py`
**Scenario**: Wallet class with balance checks and reusable fixture  
**Concepts**: Fixtures in `conftest.py`, modular test setup, `raise`, `assert`  
**Run**:
```bash
pytest qa_pytest_foundations/fixture_tests/test_wallet.py -v
```

---

### 📂 `property_tests/test_person.py`
**Scenario**: Test setter/getter via `@property` and `@<property>.setter`  
**Concepts**: Encapsulation, data validation  
**Run**:
```bash
pytest qa_pytest_foundations/property_tests/test_person.py -v
```

---

### 📂 `plugins_reports/test_with_plugins.py`
**Scenario**: Generate HTML test report  
**Concepts**: Plugin usage (`pytest-html`), command-line reporting  
**Run**:
```bash
pytest qa_pytest_foundations/plugins_reports/test_with_plugins.py --html=report.html
```

---

### 📂 `marker_tests/test_marked_smoke.py`
**Scenario**: Tagging test cases with custom markers (e.g., `@pytest.mark.smoke`)  
**Concepts**: Filtering with `-m`, declaring markers in `pytest.ini`  
**Run**:
```bash
pytest qa_pytest_foundations/marker_tests/test_marked_smoke.py -m "smoke" -v
```

---

## ⚙️ `pytest.ini`

```ini
[pytest]
addopts = -v
markers =
    smoke: run the smoke tests
    api: tag for API tests
    regression: tag for regression scenarios
```

📌 Used to define global options, avoid repetitive `-v` flag, and suppress marker warnings.

---

## 🧩 QA Python Foundations

### ✅ Basics
- `add_two_numbers.py`, `find_even_numbers.py`, `prime_number_check.py`, etc.
- Concepts: Input handling, math operations, loops, functions

### ✅ String Handling
- `anagram.py`, `palindrome.py`, `string_reverse.py`
- Concepts: String slicing, sorting, frequency checks

### ✅ List & Dictionary
- `list_comparison.py`, `sort-merge_list&Dictionary.py`
- Concepts: Set operations, loops, sorting

### ✅ OOPs Concepts
- `encapsulation.py`, `inheritance&overriding.py`
- Concepts: Classes, `super()`, method overriding

### ✅ File Handling
- `filehandling_operations.py`
- Concepts: File open/write/read/close, `with` context manager

### ✅ API Testing
- `api_testing.py`
- Concepts: GET requests with `requests`, status code checks

---

## 📚 How to Use This Repo

1. Clone the repo:
```bash
git clone https://github.com/<your-username>/qa-python-exercise-bank.git
```

2. Navigate and run:
```bash
cd qa-python-exercise-bank/qa_pytest_foundations
pytest <folder>/<test_file>.py -v
```

3. Review code to understand each scenario and concept applied.

---

## 🧠 Ideal For:
- QA Engineers learning automation
- Interview preparation
- Building a Python-based test automation portfolio

_Last updated: 2025-06-26_  
