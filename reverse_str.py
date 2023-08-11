while True:
    inputStr = input("Enter the String: ")
    if inputStr.strip():  # Check if the input is not empty after stripping whitespace
        try:
            inputStr = str(inputStr)
            break  # Break the loop if a valid integer is provided
        except ValueError:
            print("Please enter a valid string.")
    else:
        print("Input cannot be empty.")

# using loop
reversed_word = ""
for char in inputStr:
    reversed_word = char + reversed_word

print("Reversed word:", reversed_word)

# another way
reversed_word = inputStr[::-1]
print("Reversed word:", reversed_word)