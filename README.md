🧪 QA Python Exercise Bank
This repository helps you learn and revise Python and Pytest for QA Automation. It includes hands-on exercises and real-world scenarios to strengthen your programming and testing skills.

📦 Project Structure
bash
Copy
Edit
qa-python-exercise-bank/
├── qa_python_foundations/       # Core Python practice programs
├── qa_pytest_foundations/       # Pytest-based automation scenarios
└── README.md                    # This file
🔧 Installation & Setup
✅ Requirements:
Python 3.8+

Install dependencies:

bash
Copy
Edit
pip install pytest openpyxl requests pytest-html
📁 Folder 1: qa_python_foundations
✅ Objective:
Covers core Python concepts such as string handling, file operations, list/dict manipulations, and OOPs — tailored for QA interviews.

Category	Description	Concepts Used	Run Example
Basics	Add, even, prime, missing numbers	Arithmetic, loops, range(), logic	Run manually, not via pytest
String Handling	Reverse, anagram, email validation	Slicing, sorted(), re module	Run manually, not via pytest
List & Dict	Sort, merge, remove duplicates	set(), loops, comparisons	Run manually, not via pytest
File Handling	File create/read/update/delete	open(), with, os.path	Run manually, not via pytest
OOP Concepts	Class, inheritance, @property	Class, __init__, encapsulation	Run manually, not via pytest
API Testing	GET, POST, PUT, DELETE	requests, headers, status code, JSON parsing	python qa_python_foundations/api_testing.py

📁 Folder 2: qa_pytest_foundations
✅ Objective:
Test real-world-like scenarios using pytest. Covers fixtures, markers, parameterization, plugins, and more.

Folder	Scenario	Concepts Used	Run Command Example
basic_tests/	Calculator test	assert, basic validation	python -m pytest basic_tests/test_calculator.py -v
exception_tests/	Handle ZeroDivision, KeyError	pytest.raises, exception message validation	python -m pytest exception_tests/test_exceptions.py -v
parameterized_tests/	Validate login using Excel	@pytest.mark.parametrize, Excel reading with openpyxl	python -m pytest parameterized_tests/test_login_excel.py -v
api_tests/	GET, POST, PUT, DELETE requests to dummy API	requests, JSON parsing, status codes, API response checks	python -m pytest api_tests/test_api_http_methods.py -v
file_handling/	File creation with temp path	Built-in fixture tmp_path, file operations	python -m pytest file_handling/test_temp_file.py -v
fixture_tests/	Wallet object with shared fixture	Custom fixture in conftest.py, modular test setup	python -m pytest fixture_tests/test_wallet.py -v
property_tests/	Setter/getter validation on Circle class	@property, encapsulation, validation logic	python -m pytest property_tests/test_circle.py -v
plugins_reports/	HTML test report generation	pytest-html plugin	pytest plugins_reports/test_with_plugins.py --html=report.html
marker_tests/	Smoke test with markers	@pytest.mark.smoke, test filtering	pytest -m smoke

🗂️ Shared Fixture File: conftest.py
Contains fixtures shared across test modules (e.g., wallet()).

Automatically recognized by pytest.

Promotes reusability and DRY code.

🧪 pytest.ini
📄 Objective:
Configuration file to:

Define markers (e.g., smoke, api)

Control output format

📌 Example:
ini
Copy
Edit
[pytest]
markers =
    api: marks tests as API-related
    smoke: marks tests as smoke test
addopts = -v
🔁 Summary of Concepts Covered
Concept	Explanation
assert	Core assertion for validating expected vs actual result
pytest.raises	Validate exceptions and messages
@pytest.mark.parametrize	Run tests with multiple sets of data (DDT)
@pytest.mark.<tag>	Tag tests for filtered execution (-m tagname)
fixture	Reusable test setup/teardown function
conftest.py	Shared fixture definitions for reuse
tmp_path	Pytest fixture for creating temporary directories/files
pytest-html	Plugin to generate beautiful HTML test reports
pytest.ini	Configure global pytest options and define custom markers

🚀 How to Run All Tests at Once
bash
Copy
Edit
python -m pytest qa_pytest_foundations/ -v
✅ Perfect For:
QA Testers prepping for interviews

Learning Python & Pytest from scratch

Building strong testing foundations

Transitioning from manual to automation testing

