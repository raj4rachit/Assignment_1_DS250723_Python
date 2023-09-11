# Implement a Banking Account

class Account:
    def __init__(self, title=None, balance=0):
        self.title = title
        self.balance = balance

class SavingsAccount(Account):
    def __init__(self, title=None, balance=0, interestRate=0):
        super().__init__(title, balance)
        self.interestRate = interestRate

# Input values from the user for Account
title_account = input("Enter the account title: ")
balance_account = float(input("Enter the account balance: "))

# Create an Account object with user input
account = Account(title_account, balance_account)

# Input values from the user for SavingsAccount
title_savings = input("Enter the savings account title: ")
balance_savings = float(input("Enter the savings account balance: "))
interest_rate = float(input("Enter the interest rate for the savings account: "))

# Create a SavingsAccount object with user input
savings_account = SavingsAccount(title_savings, balance_savings, interest_rate)

# Display account details
print("\nAccount Details:")
print(f"Title: {account.title}")
print(f"Balance: {account.balance}")

# Display savings account details
print("\nSavings Account Details:")
print(f"Title: {savings_account.title}")
print(f"Balance: {savings_account.balance}")
print(f"Interest Rate: {savings_account.interestRate}%")