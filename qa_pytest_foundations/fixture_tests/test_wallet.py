# ----------------------------------------------------------------------------------------------------------------------------
# To test operations on a Wallet class (wallet.py) like checking balance, making deposits, and preventing direct access
# to internal state. To avoid repeating object setup in each test, you'll use a @pytest.fixture to create a
# reusable wallet instance in conftest.py.In this test_wallet.py we directly use the fixture wallet to do operations
# ----------------------------------------------------------------------------------------------------------------------------

import pytest   # needed for fixtures

# Test initial balance is 0
# The wallet is passed from fixture specified in conftest.py
def test_wallet_starts_empty(wallet):
    # Here we directly called balance instead of balance() as balance is having @property decorator
    assert wallet.balance == 0

#Test deposit operation
def test_deposit(wallet):
    wallet.deposit(100)
    assert wallet.balance == 100

#Test withdraw operation
def test_withdraw(wallet):
    wallet.deposit(200)
    wallet.withdraw(50)
    assert wallet.balance == 150

#Test withdrawing more than available balance raises error
def test_withdraw_insufficient_funds(wallet):
    with pytest.raises(ValueError, match="Insufficient balance"):
        wallet.withdraw(50)

#Test direct modification is not allowed
def test_wallet_balance_is_read_only(wallet):
    with pytest.raises(AttributeError):
        wallet.balance = 500  # Should raise because balance is a @property without setter
