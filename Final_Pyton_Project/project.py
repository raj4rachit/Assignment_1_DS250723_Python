from new_app import functions

class Application:
    def run(self):
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

if __name__ == "__main__":
    app = Application()
    app.run()
