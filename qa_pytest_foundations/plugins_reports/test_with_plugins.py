# ----------------------------------------------------------------------------------------------------------------------------
# Run a simple test that will generate HTML and code coverage reports using pytest plugins.
# This is useful for sharing test results with teams and tracking how much of your code is tested.
# ----------------------------------------------------------------------------------------------------------------------------

# This test file is used to demonstrate pytest plugin usage (pytest-html & pytest-cov)

def add(a, b):
    return a + b

def multiply(a, b):
    return a * b

# Basic test case to validate addition
def test_add():
    assert add(3, 2) == 5

# Basic test case to validate multiplication
def test_multiply():
    assert multiply(3, 2) == 6
