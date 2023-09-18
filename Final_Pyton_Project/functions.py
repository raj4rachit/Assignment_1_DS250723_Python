import json

class admin:
    def __init__(self):
        self.data = {}
        with open("user_info.json", "r") as file:
            data = json.load(file)
            if data:
                self.data = data

    def display_users(self):
        for k, v in self.data.items():
            print("Users ------>", k)
            for i, j in v.items():
                print(i, "----->", j)

            print("-------------------------------------")

    def add_user(self):
        dict = {}
        dict["Name"] = input("Enter the User name: ")
        dict["email"] = input("Enter the email address: ")
        dict["password"] = input("Enter the password")
        dict["Role"] = 'user'

        keys = list(self.data.keys())
        if len(keys) > 0:
            new_key = int(keys[-1]) + 1
        else:
            new_key = "01"
        self.data[str(new_key)] = dict

        with open("user_info.json", "w") as file:
            json.dump(self.data, file)
            print("User Added successfully!!!")

    def update_user(self):
        pass

    def delete_user(self):
        pass


class user:
    def __init__(self):
        self.data = {}
        self.food_data = {}
        with open("food_list.json", "r") as file:
            food_data = json.load(file)
            if food_data:
                self.food_data = food_data

        self.user_data = {}
        with open("user_info.json", "r") as file:
            data = json.load(file)
            if data:
                self.user_data = data

    def user_sign_in(self, email, password):
        flag = False
        for k, v in self.user_data:
            if v['email'] == email:
                if v['password'] == password:
                    flag = True
                    return True
        if flag == False:
            return False

    def user_signup(self):
        data = {}
        data['Name'] = input("Enter your name")
        data['email'] = input("Enter your email")
        data['Password'] = input("Create a strong password")
        data["Role"] = 'user'
        with open("user_info.json", "w") as file:
            keys = list(self.user_data.keys())
        if len(keys) > 0:
            new_key = int(keys[-1]) + 1
        else:
            new_key = "01"
        self.user_data[str(new_key)] = data

        with open("user_info.json", "w") as file:
            json.dump(self.user_data, file)
            print("Signed up successfully!!!")

    def display_food_items(self):
        for k, v in self.food_data.items():
            print("Foods ------>", k)
        for i, j in v.items():
            print(i, "----->", j)
            print("-------------------------------------")

    def add_to_cart(self):
        pass

    def order(self):
        pass

    def update_profile(self):
        pass

    def view_order_history(self):
        pass
