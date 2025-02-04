# Create a BankAccount class with private attributes balance.
# Add methods to deposit, withdraw, and check the balance.


class BankAccount:
    def __init__(self, owner, balance):
        self.owner= owner
        self.__balance= balance
    
    def deposit(self, amount):
        self.__balance += amount
        return f"Deposited {amount}. New balance is {self.__balance}"

    def withdraw(self, amount):
        if amount > self.__balance:
            return "Insufficient funds!"
        self.__balance -= amount
        return f"Withdrew {amount}. Remaining balance is {self.__balance}"

bank_account= BankAccount("Bob", 200)

print(bank_account.deposit(100))
print(bank_account.withdraw(100))
