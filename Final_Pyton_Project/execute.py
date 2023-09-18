while True:
    print(f"Welcome to the My Food Ordering App")
    print("Press 1. To Sign in")
    print("Press 2. To Sign up")
    choice = input("Enter your choice: ")

    if choice == "1":
        username = input("Enter a username: ")
        password = input("Enter a password: ")
        register_user(username, password)
    elif choice == "2":
        username = input("Enter your username: ")
        password = input("Enter your password: ")
        login_user(username, password)
    elif choice == "3":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")


print("Welcome to the My Food Ordering App")
print("Press 1. To Sign in")
print("Press 2. To Sign up")

# Initialize choice with an invalid value to enter the loop.
choice = 0

# Keep prompting until the user enters a valid choice (1 or 2).
while choice not in [1, 2]:
    try:
        choice = int(input("Enter your choice: "))
        if choice not in [1, 2]:
            print("Invalid choice. Please enter 1 or 2.")
    except ValueError:
        print("Invalid input. Please enter 1 or 2 as a number.")

if choice == 1:
    print("You chose to Sign in")
    # Add your Sign in code here
elif choice == 2:
    print("You chose to Sign up")
    # Add your Sign up code here
