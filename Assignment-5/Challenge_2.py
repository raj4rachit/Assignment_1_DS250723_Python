# Implement a Calculator Class

class Calculator:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def add(self):
        return self.num1 + self.num2

    def subtract(self):
        return self.num2 - self.num1

    def multiply(self):
        return self.num1 * self.num2

    def divide(self):
        if self.num1 == 0:
            return "Division by zero is not allowed."
        return self.num2 / self.num1

# Input values from the user
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Create a Calculator object with user input
obj = Calculator(num1, num2)

# Perform operations and display results
add_result = obj.add()
subtract_result = obj.subtract()
multiply_result = obj.multiply()
divide_result = obj.divide()

print(f"Addition result: {add_result}")
print(f"Subtraction result: {subtract_result}")
print(f"Multiplication result: {multiply_result}")
print(f"Division result: {divide_result}")
