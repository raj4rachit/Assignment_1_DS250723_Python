# Get a list of numbers from the user
numbers = []
while True:
    try:
        user_input = input("Enter a number (or 'done' to finish): ")
        if user_input.lower() == 'done':
            break
        num = int(user_input)  # Convert input to int
        numbers.append(num)
    except ValueError:
        print("Invalid input. Please enter a valid number.")

# Use map() to square all numbers in the list
squared_numbers = list(map(lambda x: x ** 2, numbers))

# Print the original and squared lists
print("Original numbers:", numbers)
print("Squared numbers:", squared_numbers)
