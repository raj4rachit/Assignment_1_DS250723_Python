import json
import re

class FoodOrderingApp:
    def __init__(self):
        self.users = []
        self.load_users()
        self.logged_in_user = None

    def load_users(self):
        try:
            with open('users.json', 'r') as users_file:
                user_data = json.load(users_file)
            self.users = user_data["users"]
        except FileNotFoundError:
            self.users = []

    def save_users(self):
        with open('users.json', 'w') as users_file:
            json.dump({"users": self.users}, users_file)

    def is_valid_email(self, email):
        # Use a regular expression to validate the email format
        email_pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
        return re.match(email_pattern, email)

    def register_user(self):
        print("User Registration:")
        full_name = input("Full Name: ")
        phone_number = input("Phone Number: ")
        email = input("Email: ")
        address = input("Address: ")
        password = input("Password: ")

        # Basic input validation
        if not full_name or not phone_number or not email or not address or not password:
            print("Please fill in all the required fields.")
            return

        # Check if email is already registered
        for user in self.users:
            if user["email"] == email:
                print("Email already registered. Please use a different email.")
                return

        # Validate email format
        if not self.is_valid_email(email):
            print("Invalid email format. Please enter a valid email address.")
            return

        user = {
            "full_name": full_name,
            "phone_number": phone_number,
            "email": email,
            "address": address,
            "password": password
        }
        self.users.append(user)
        self.save_users()
        print("Registration successful!")

    def login(self):
        print("User Login:")
        email = input("Email: ")
        password = input("Password: ")

        # Basic input validation
        if not email or not password:
            print("Please provide both email and password.")
            return

        for user in self.users:
            if user["email"] == email and user["password"] == password:
                self.logged_in_user = user
                print("Logged in as:", self.logged_in_user["full_name"])

                while True:
                    print("\n:")
                    print("1. Display Menu")
                    print("2. Take Orders")
                    print("3. Your Order History")
                    print("4. Update Profile")
                    print("5. Logout")
                    choice = input("Enter your choice: ")

                    if choice == '1':
                        self.register_user()
                    elif choice == '2':
                        self.login()
                    elif choice == '3':
                        self.display_menu()
                    elif choice == '4':
                        if self.logged_in_user:
                            self.take_orders()
                        else:
                            print("Please log in first.")
                    elif choice == '5':
                        break
                    else:
                        print("Invalid choice. Please try again.")

        print("Login failed. Please check your email and password.")

    def display_menu(self):
        # Add your menu display logic here
        pass

    def take_orders(self):
        # Add your order taking logic here
        pass

    def calculate_total(self):
        # Add your total calculation logic here
        pass

    def start(self):
        while True:
            print("\nWelcome My Food App:")
            print("1. Register")
            print("2. Log in")
            print("3. Display Menu")
            print("4. Take Orders")
            print("5. Quit")
            choice = input("Enter your choice: ")

            if choice == '1':
                self.register_user()
            elif choice == '2':
                self.login()
            elif choice == '3':
                self.display_menu()
            elif choice == '4':
                if self.logged_in_user:
                    self.take_orders()
                else:
                    print("Please log in first.")
            elif choice == '5':
                break
            else:
                print("Invalid choice. Please try again.")

if __name__ == "__main__":
    app = FoodOrderingApp()
    app.start()
