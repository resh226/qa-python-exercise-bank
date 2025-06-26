#----------------------------------------------------------------------------------------------------
#A simple Wallet class to simulate real-world balance operations
#-----------------------------------------------------------------------------------------------------

class Wallet:
    def __init__(self):
        self._balance = 0  # Private attribute by naming convention, variable with underscore as suffix considered as private

    def deposit(self, amount):
        self._balance += amount

    def withdraw(self, amount):
        if amount > self._balance:
            raise ValueError("Insufficient balance") #raise is a built-in Python keyword used to manually throw an exception.This is part of your application logic (not a test), and it's used to enforce a business rule.
        self._balance -= amount

    # @property is a decorator used to make a method act like an attribute (no parentheses needed).
    # It makes your class easier and safer to use — and hides internal logic from the outside world (this is encapsulation).
    @property
    def balance(self):
        return self._balance