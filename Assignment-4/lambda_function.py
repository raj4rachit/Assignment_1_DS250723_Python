# Get user input as a number
try:
    user_input = int(input("Enter a number: "))
    
    # Create a lambda function to add 25 to the input number
    add_25 = lambda x: x + 25
    
    # Use the lambda function to add 25 to the input and print the result
    result = add_25(user_input)

    print(f"Result: {result}")

except ValueError:
    print("Invalid input. Please enter a valid number.")
