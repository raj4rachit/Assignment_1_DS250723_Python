while True:
    inputStr = input("Enter the String: ")
    if inputStr.strip():
        inputStr = str(inputStr)
        break
    else:
        print("Input cannot be empty.")

# using loop
reverseString = ""
for char in inputStr:
    reverseString = char + reverseString

print("Reversed word:", reverseString)

# another way
reverseString = inputStr[::-1]
print("Reversed word:", reverseString)