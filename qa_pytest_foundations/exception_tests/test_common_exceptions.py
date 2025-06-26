# ----------------------------------------------------------------------------------------------------------------------------
#To intentionally trigger and validate common built-in Python exceptions using pytest.raises() along with message verification.
# ----------------------------------------------------------------------------------------------------------------------------

import pytest  # Importing the pytest framework

# Test: Division by zero should raise ZeroDivisionError
def test_zero_division():
    # Expecting a ZeroDivisionError when dividing by zero
    with pytest.raises(ZeroDivisionError) as e:
        result = 1 / 0
    # Validating the error message
    assert "division by zero" in str(e.value)

# Test: Accessing a missing key in a dictionary should raise KeyError
def test_key_error():
    data = {"name": "Reshma"}
    # Accessing a key that doesn't exist ("age") should raise KeyError
    with pytest.raises(KeyError) as e:
        value = data["age"]
    # Error message will show the missing key (with quotes)
    assert "'age'" in str(e.value)

# Test: Accessing an invalid index in a list should raise IndexError
def test_index_error():
    items = [1, 2, 3]
    # Index 5 doesn't exist in a list of length 3
    with pytest.raises(IndexError) as e:
        item = items[5]
    # Common error message when index is out of range
    assert "list index out of range" in str(e.value)

# Test: Converting a non-numeric string to int should raise ValueError
def test_value_error():
    # Trying to convert a string that is not a number
    with pytest.raises(ValueError) as e:
        number = int("abc")
    # The error message will mention "invalid literal"
    assert "invalid literal" in str(e.value)

# Test: Adding incompatible types (str + int) should raise TypeError
def test_type_error():
    # You can't directly add a string and an integer
    with pytest.raises(TypeError) as e:
        result = "2" + 3
    # Message usually contains "can only concatenate str"
    assert "can only concatenate str" in str(e.value)

# Test: Trying to open a file that doesn't exist should raise FileNotFoundError
def test_file_not_found():
    # Trying to open a file that is not present in the directory
    with pytest.raises(FileNotFoundError) as e:
        open("non_existent_file.txt")
    # Error message depends on OS: handle both Linux/macOS and Windows cases
    assert "No such file or directory" in str(e.value) or "cannot find the file" in str(e.value)
