class BankAccount:
    def __init__(self, owner, initial_balance=0):
        self.owner = owner
        self.__balance = initial_balance  # private variable

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited {amount}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount > self.__balance:
            print("Insufficient funds.")
        elif amount <= 0:
            print("Withdrawal amount must be positive.")
        else:
            self.__balance -= amount
            print(f"Withdrew {amount}")

    def get_balance(self):
        return self.__balance

    def set_balance(self, new_balance):
        if new_balance >= 0:
            self.__balance = new_balance
            print(f"new balance is {self.__balance}")
        else:
            print("Balance cannot be negative.")


# ----- Main -----
if __name__ == "__main__":
    account = BankAccount("Reshma", 1000)

    account.deposit(500)
    account.withdraw(200)
    print(f"🔍 Current balance: {account.get_balance()}")
    account.set_balance(1000)

    account.withdraw(2000)  # Try overdraw
    account.deposit(-50)    # Try invalid deposit
