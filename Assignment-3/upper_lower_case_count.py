def countUpperLower(input_str):
    upper_count = 0
    lower_count = 0

    for char in input_str:
        if char.isupper():
            upper_count += 1
        elif char.islower():
            lower_count += 1
    
    return upper_count, lower_count

# Take input from the user
user_input = input("Enter a string: ")

upper, lower = countUpperLower(user_input)
print("Number of upper case letters: ", upper)
print("Number of lower case letters: ", lower)
