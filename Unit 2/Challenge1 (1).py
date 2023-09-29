class BankAccount:
    def _init_(self, account_number, account_holder_name, initial_balance=0):
        self.__account_number = account_number
        self.__account_holder_name = account_holder_name
        self.__account_balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self.__account_balance += amount
            return f"Deposited ${amount}. New balance is ${self.__account_balance}"
        else:
            return "Invalid deposit amount."

    def withdraw(self, amount):
        if 0 < amount <= self.__account_balance:
            self.__account_balance -= amount
            return f"Withdrew ${amount}. New balance is ${self.__account_balance}"
        else:
            return "Invalid withdrawal amount or insufficient balance."

    def display_balance(self):
        return f"Account Balance for {self._account_holder_name}: ${self._account_balance}"

# Testing the BankAccount class
if _name_ == "_main_":
    account = BankAccount("123456789", "John Doe", 1000)

    print(account.display_balance())  # Display initial balance
    print(account.deposit(500))        # Deposit $500
    print(account.withdraw(200))       # Withdraw $200
    print(account.display_balance())  # Display updated balance