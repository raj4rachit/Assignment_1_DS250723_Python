from datetime import datetime
import json
import re

# Login Details
# Admin: email=> admin@gmail.com  password=> 123
# user: email=> user1@gmail.com  password=> 123
# user: email=> user2@gmail.com  password=> 123

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
            "password": password,
            "Role": "user"
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
                    print("1. Take Order:")
                    print("2. Your Order History")
                    print("3. Update Profile")
                    print("4. View Profile")
                    if self.logged_in_user["Role"] == "admin":
                        print("5. Admin Dashboard")
                    print("6. Logout")
                    your_choice = input("Enter your choice: ")

                    if your_choice == '2':
                        self.user_order_history()
                    elif your_choice == '3':
                        self.update_profile()
                    elif your_choice == '1':
                        if self.logged_in_user:
                            self.take_orders()
                        else:
                            print("Please log in first.")
                            return
                    elif your_choice == '4':
                        if self.logged_in_user:
                            self.display_user_profile()
                        else:
                            print("Please log in first.")
                            return
                    elif your_choice == '5':
                        if self.logged_in_user and self.logged_in_user["Role"] == "admin":
                            self.admin_dashboard()
                        else:
                            print("You are not authorized to access this dashboard.")
                    elif your_choice == '6':
                        self.logged_in_user = None
                        return
                    else:
                        print("Invalid choice. Please try again.")

        print("Login failed. Please check your email and password.")

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
        self.display_user_profile()

    def display_user_profile(self):
        if not self.logged_in_user:
            print("Please log in to view your profile.")
            return

        print("User Profile:")
        print(f"Full Name: {self.logged_in_user['full_name']}")
        print(f"Phone Number: {self.logged_in_user['phone_number']}")
        print(f"Email: {self.logged_in_user['email']}")
        print(f"Address: {self.logged_in_user['address']}")

    def display_menu(self):
        print("Menu:")
        for item in self.menu:
            print(f"{item['id']}) {item['name']} ({item['quantity']}) [INR {item['price']}]")

    def take_orders(self):
        if not self.logged_in_user:
            print("Please log in to place an order.")
            return

        while True:
            print("\nPlace Order:")
            print("1. Display Menu")
            print("2. Select Food Items (enter an array of numbers, e.g., [2, 3])")
            print("3. View Cart")
            print("4. Checkout")
            print("5. Go Back")
            order_choice = input("Enter your choice: ")

            if order_choice == '1':
                self.display_menu()
            elif order_choice == '2':
                self.select_food_items()
            elif order_choice == '3':
                self.view_cart()
            elif order_choice == '4':
                self.checkout()
            elif order_choice == '5':
                break
            else:
                print("Invalid choice. Please try again.")

    def select_food_items(self):
        if not self.menu:
            print("No food items available in the menu.")
            return

        print("Select Food Items:")
        self.display_menu()

        selected_items = []
        while True:
            try:
                user_input = input("Enter an array of food item numbers (e.g., [2, 3]) or 'done' to finish: ").strip()

                if user_input.lower() == 'done':
                    break

                selected_numbers = json.loads(user_input)
                if not isinstance(selected_numbers, list):
                    print("Invalid input. Please enter a valid array of numbers.")
                    continue

                for number in selected_numbers:
                    if 1 <= number <= len(self.menu):
                        selected_items.append(self.menu[number - 1])
                    else:
                        print(f"Invalid food item number: {number}. Please enter a valid number.")

            except ValueError:
                print("Invalid input. Please enter a valid array of numbers.")

        # Calculate the total price for the selected items, including discounts
        total_price = 0
        for item in selected_items:
            item_price = item['price']
            item_discount = item['discount']
            discounted_price = item_price - (item_price * item_discount / 100)
            item['discounted_price'] = discounted_price
            total_price += discounted_price

        # Add selected items to the user's cart
        if selected_items:
            if 'cart' not in self.logged_in_user:
                self.logged_in_user['cart'] = []

            self.logged_in_user['cart'].extend(selected_items)
            print("Food items added to the cart.")

        print(f"Total Price (with discounts applied): INR {total_price:.2f}")

    def view_cart(self):
        if not self.logged_in_user or 'cart' not in self.logged_in_user or not self.logged_in_user['cart']:
            print("Your cart is empty.")
        else:
            print("Cart Contents:")
            for item in self.logged_in_user['cart']:
                print(f"{item['name']} ({item['quantity']}) - [INR {item['discounted_price']}]")

    def checkout(self):
        if not self.logged_in_user:
            print("Please log in to place an order.")
            return

        if 'cart' not in self.logged_in_user or not self.logged_in_user['cart']:
            print("Your cart is empty. Nothing to order.")
            return

        # Calculate the total price of items in the cart
        total_price = sum(item['discounted_price'] for item in self.logged_in_user['cart'])

        print("Place Order:")
        print("Cart Contents:")
        for item in self.logged_in_user['cart']:
            print(f"{item['name']} ({item['quantity']}) - INR {item['discounted_price']}")

        print(f"Total Price: INR {total_price}")

        # Ask the user to choose a payment method
        payment_method = input("Select a payment method (1. Credit Card, 2. Cash on Delivery): ")

        if payment_method == '1':
            # Implement credit card payment logic here
            print("Payment processed with Credit Card.")
        elif payment_method == '2':
            # For Cash on Delivery, no payment processing is needed
            print("Cash on Delivery selected. Payment will be collected upon delivery.")
        else:
            print("Invalid payment method. Please select a valid payment method.")
            return

        # Record the order in the user's order history
        if 'order_history' not in self.logged_in_user:
            self.logged_in_user['order_history'] = []

        order_data = {
            'items': self.logged_in_user['cart'],
            'total_price': total_price,
            'order_date': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            'payment_method': "Cash on Delivery" if payment_method == '2' else "Credit Card"
        }

        self.logged_in_user['order_history'].append(order_data)

        # Save the order history to a JSON file
        self.save_order_history()

        # Clear the user's cart after placing the order
        self.logged_in_user['cart'] = []
        print("Order placed successfully!")

    def save_order_history(self):
        if 'order_history' not in self.logged_in_user or not self.logged_in_user['order_history']:
            return

        # Create a file name based on the user's email (you can customize this as needed)
        user_email = self.logged_in_user['email']
        order_history_file = f'order_history_{user_email}.json'

        # Write the order history to the JSON file
        with open(order_history_file, 'w') as history_file:
            json.dump(self.logged_in_user['order_history'], history_file)

    def user_order_history(self):
        if not self.logged_in_user:
            print("Please log in to view your order history.")
            return

        user_email = self.logged_in_user['email']
        order_history_file = f'order_history_{user_email}.json'

        try:
            with open(order_history_file, 'r') as history_file:
                order_history = json.load(history_file)

            if not order_history:
                print("You have no order history.")
                return

            print(f"Order History for {self.logged_in_user['full_name']} ({user_email}):")
            for i, order_data in enumerate(order_history, start=1):
                print(f"Order {i}:")
                print(f"Order Date: {order_data['order_date']}")
                print("Ordered Items:")
                for item in order_data['items']:
                    print(f"{item['name']} ({item['quantity']}) - [INR {item['discounted_price']}]")
                print(f"Total Price: INR {order_data['total_price']}")
                print()

        except FileNotFoundError:
            print("You have no order history.")

    def admin_dashboard(self):
        print("Admin Dashboard:")

        while True:
            print("\nAdmin Menu:")
            print("1. Add new food items")
            print("2. Edit food items using FoodID")
            print("3. View the list of all food items")
            print("4. Remove a food item from the menu using FoodID")
            print("5. Return to Main menu")
            admin_choice = input("Enter your choice: ")

            if admin_choice == '1':
                self.add_food_item()
            elif admin_choice == '2':
                self.edit_food_item()
            elif admin_choice == '3':
                self.food_list()
            elif admin_choice == '4':
                self.remove_food_item()
            elif admin_choice == '5':
                return
            else:
                print("Invalid choice. Please try again.")

    def add_food_item(self):
        print("Add New Food Item:")

        # Gather the new food item details from user input
        name = input("Enter the name of the food item: ")
        quantity = input("Enter the quantity (e.g., 100ml, 250gm, 4 pieces, etc.): ")
        price = input("Enter the price: INR ")
        discount = input("Enter the discount percentage: ")
        stock = input("Enter the stock amount: ")

        # Validate the input
        if not name or not quantity or not price or not discount or not stock:
            print("Error: Please fill in all the required fields.")
            return

        try:
            price = float(price)
            discount = float(discount)
            stock = int(stock)
        except ValueError:
            print("Error: Invalid input format for price, discount, or stock.")
            return

        # Generate a new FoodID automatically
        new_food_id = len(self.menu) + 1

        # Add the new food item to the menu
        new_food_item = {
            "id": new_food_id,
            "name": name,
            "quantity": quantity,
            "price": price,
            "discount": discount,
            "stock": stock
        }
        self.menu.append(new_food_item)

        # Save the updated menu to a JSON file
        with open('menu.json', 'w') as menu_file:
            json.dump({"n ": self.menu}, menu_file)

        print("New food item added to the menu successfully!")

    def edit_food_item(self):
        print("Edit Food Item:")
        self.food_list()
        food_id = input("Enter FoodID of the item to edit: ")

        # Find the food item with the provided FoodID
        found_item = None
        for item in self.menu:
            if str(item["id"]) == food_id:
                found_item = item
                break

        if found_item is None:
            print(f"Error: Food item with FoodID {food_id} not found.")
            return

        print(f"Editing food item with FoodID {food_id}:")
        print(f"Current Name: {found_item['name']}")
        new_name = input("Enter the new name (press Enter to keep current): ").strip()
        print(f"Current Quantity: {found_item['quantity']}")
        new_quantity = input("Enter the new quantity (press Enter to keep current): ").strip()
        print(f"Current Price: INR {found_item['price']}")
        new_price = input("Enter the new price (press Enter to keep current): ").strip()
        print(f"Current Discount: {found_item['discount']}%")
        new_discount = input("Enter the new discount percentage (press Enter to keep current): ").strip()
        print(f"Current Stock: {found_item['stock']}")
        new_stock = input("Enter the new stock amount (press Enter to keep current): ").strip()

        # Update the food item data if new values are provided
        if new_name:
            found_item['name'] = new_name
        if new_quantity:
            found_item['quantity'] = new_quantity
        if new_price:
            try:
                found_item['price'] = float(new_price)
            except ValueError:
                print("Error: Invalid input format for price. Price should be a number.")
                return
        if new_discount:
            try:
                found_item['discount'] = float(new_discount)
            except ValueError:
                print("Error: Invalid input format for discount. Discount should be a number.")
                return
        if new_stock:
            try:
                found_item['stock'] = int(new_stock)
            except ValueError:
                print("Error: Invalid input format for stock. Stock should be an integer.")
                return

        # Save the updated menu to a JSON file
        with open('menu.json', 'w') as menu_file:
            json.dump({"menu": self.menu}, menu_file)

        print("Food item updated successfully!")

    def food_list(self):
        print("Food List: ")
        for item in self.menu:
            print(
                f"FoodID: {item['id']}, Name: {item['name']}, Quantity: {item['quantity']}, Price: INR {item['price']}, Discount: {item['discount']}%, Stock: {item['stock']}")

    def remove_food_item(self):
        print("Remove Food Item:")
        self.food_list()
        food_id = input("Enter FoodID of the item to remove: ")

        # Find the food item with the provided FoodID
        found_item = None
        for item in self.menu:
            if str(item["id"]) == food_id:
                found_item = item
                break

        if found_item is None:
            print(f"Error: Food item with FoodID {food_id} not found.")
            return

        # Confirm the deletion with the user
        confirm_delete = input(f"Are you sure you want to remove '{found_item['name']}'? (yes/no): ").strip().lower()

        if confirm_delete == "yes":
            # Remove the food item from the menu
            self.menu.remove(found_item)

            # Save the updated menu to a JSON file
            with open('menu.json', 'w') as menu_file:
                json.dump({"menu": self.menu}, menu_file)

            print(f"Food item with FoodID {food_id} deleted successfully!")
        else:
            print(f"Deletion of '{found_item['name']}' canceled.")

    def start(self) -> object:
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
