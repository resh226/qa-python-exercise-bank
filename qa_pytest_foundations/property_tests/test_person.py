# ----------------------------------------------------------------------------------------------------------------------------
# Validate getter and setter behavior using the @property decorator in a Person class.
# This test ensures that class attributes can be accessed and updated using property methods,
# while enforcing data validation to prevent bad inputs.
# ----------------------------------------------------------------------------------------------------------------------------

import pytest

#Class with @property and @setter for controlled access to name
class Person:
    def __init__(self, name):
        self._name = name  # private by naming convention

    @property
    def name(self):
        # Getter method for name
        return self._name

    @name.setter
    def name(self, new_name):
        # Setter with input validation
        if not new_name.strip(): #strip() is a string method that removes leading and trailing whitespace from a string.
            raise ValueError("Name cannot be empty")
        self._name = new_name

#Test that getter and setter work correctly
def test_person_name_property():
    # Arrange
    p = Person("Reshma")

    # Act & Assert using getter
    assert p.name == "Reshma"

    # Act using setter
    p.name = "Leo"

    # Assert updated name using getter again
    assert p.name == "Leo"

#Test that setting an empty name raises ValueError
def test_person_invalid_name():
    p = Person("Reshma")

    # Try to set invalid name and expect exception
    with pytest.raises(ValueError, match="Name cannot be empty"):
        p.name = "   "  # whitespace-only string is invalid
