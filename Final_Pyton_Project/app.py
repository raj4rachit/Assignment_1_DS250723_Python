import json
import re

class FoodOrderingApp:
    def __init__(self):
        self.users = []
        self.menu = []
        self.load_users()
        self.load_menu()
        self.logged_in_user = None

    def load_users(self):
        try:
            with open('users.json', 'r') as users_file:
                user_data = json.load(users_file)
            self.users = user_data["users"]
        except FileNotFoundError:
            self.users = []

    def load_menu(self):
        try:
            with open('menu.json', 'r') as menu_file:
                menu_data = json.load(menu_file)
            self.menu = menu_data["menu"]
        except FileNotFoundError:
            self.menu = []

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
                    print("\nPlace Order:")
                    print("1. Display Menu")
                    print("2. Take Orders")
                    print("3. Your Order History")
                    print("4. Update Profile")
                    print("5. Logout")
                    your_choice = input("Enter your choice: ")

                    if your_choice == '3':
                        self.user_order_history()
                    elif your_choice == '4':
                        self.update_profile()
                    elif your_choice == '1':
                        self.display_menu()
                    elif your_choice == '2':
                        if self.logged_in_user:
                            self.take_orders()
                        else:
                            print("Please log in first.")
                            return
                    elif your_choice == '5':
                        return
                    else:
                        print("Invalid choice. Please try again.")

        print("Login failed. Please check your email and password.")

    def user_order_history(self):
        if not self.logged_in_user:
            print("Please log in to view your order history.")
            return

        print(f"Order History for {self.logged_in_user['full_name']} ({self.logged_in_user['email']}):")
        # Implement order history retrieval and display logic here
        # You may need to load order data from a separate JSON file

    def update_profile(self):
        if not self.logged_in_user:
            print("Please log in to update your profile.")
            return

        print(f"Update Profile for {self.logged_in_user['full_name']} ({self.logged_in_user['email']}):")
        # Implement profile update logic here, e.g., updating name, phone number, address, or password
        new_full_name = input("New Full Name (press Enter to keep current): ")
        new_phone_number = input("New Phone Number (press Enter to keep current): ")
        new_address = input("New Address (press Enter to keep current): ")
        new_password = input("New Password (press Enter to keep current): ")

        # Update user profile data
        if new_full_name:
            self.logged_in_user['full_name'] = new_full_name
        if new_phone_number:
            self.logged_in_user['phone_number'] = new_phone_number
        if new_address:
            self.logged_in_user['address'] = new_address
        if new_password:
            self.logged_in_user['password'] = new_password

        # Save updated user data
        self.save_users()
        print("Profile updated successfully.")

    def display_menu(self):
        print("Menu:")
        for item in menu:
            print(f"{item['id']}. {item['name']} - ${item['price']}")

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
