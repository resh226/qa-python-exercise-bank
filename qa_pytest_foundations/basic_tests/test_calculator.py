# ----------------------------------------------------------------------------------------------------------------------------
#simple calculator test which covers basic test functions, using assert, following pytest naming conventions
# ----------------------------------------------------------------------------------------------------------------------------
def test_addition(): # pytest naming conventions for test
    result = 2 + 3
    assert result == 5 # using asser

def test_subtraction():
    result = 10 - 4
    assert result == 6

def test_multiplication():
    result = 4 * 3
    assert result == 12

def test_division():
    result = 8 / 2
    assert result == 4.0

def test_float_division():
    result = 5 / 2
    assert result == 2.5

def test_integer_division():
    result = 5 // 2
    assert result == 2

def test_modulus():
    result = 10 % 3
    assert result == 1

def test_power():
    result = 2 ** 3
    assert result == 8
