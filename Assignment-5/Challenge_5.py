# Handling a Bank Account

class Account:
    def __init__(self, title=None, balance=0):
        self.title = title
        self.balance = balance

    def withdrawal(self, amount):
        self.balance -= amount

    def deposit(self, amount):
        self.balance += amount

    def getBalance(self):
        return self.balance

class SavingsAccount(Account):
    def __init__(self, title=None, balance=0, interestRate=0):
        super().__init__(title, balance)
        self.interestRate = interestRate

    def interestAmount(self):
        return (self.balance * self.interestRate) / 100


raw_text = u"\u20B9"
# Create a SavingsAccount object
demo1 = SavingsAccount("Ashish", 2000, 5)

# Test deposit and withdrawal methods
deposit_balance = float(input("Enter the deposit amount: "))
demo1.deposit(deposit_balance)
# Display the current balance
balance = demo1.getBalance()
print(f"\nCurrent Balance: {raw_text}{balance}")

withdrawal_balance = float(input("\nEnter the withdrawal amount: "))
demo1.withdrawal(withdrawal_balance)
# Display the current balance
balance = demo1.getBalance()
print(f"\nCurrent Balance: {raw_text}{balance}")

# Calculate and display the interest amount
interest = demo1.interestAmount()
print(f"\nInterest ({demo1.interestRate}%) Amount: {raw_text}{interest}")
