# ----------------------------------------------------------------------------------------------------------------------------
# Shared fixtures go here
# conftest.py standard pytest configuration file used to define:Shared fixtures, Hooks, Global test setups
# ----------------------------------------------------------------------------------------------------------------------------

import pytest
# From the file wallet.py inside the fixture_tests folder, import the Wallet class so I can use it here."
from fixture_tests.wallet import Wallet

# Define a fixture to provide a reusable Wallet object for tests
@pytest.fixture
def wallet():
    """
    Fixture to create a new Wallet instance for each test.
    Using fixtures avoids repeating setup logic in every test case.
    """
    return Wallet()
