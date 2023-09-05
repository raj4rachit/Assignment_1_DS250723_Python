# Function to triple a number
def triple_number(num):
    return num * 3

# Get a list of integers from the user
numbers = []
while True:
    try:
        user_input = input("Enter an integer (or 'done' to finish): ")
        if user_input.lower() == 'done':
            break
        num = int(user_input)
        numbers.append(num)
    except ValueError:
        print("Invalid input. Please enter a valid integer.")

# Use map() to triple all numbers in the list
tripled_numbers = list(map(triple_number, numbers))

# Print the original and tripled lists
print("Original numbers:", numbers)
print("Tripled numbers:", tripled_numbers)
