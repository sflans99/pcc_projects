class User:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def describe_user(self):
        print(f"First Name: {self.first_name.title()}\nLast Name: {self.last_name.title()}")

    def greet_user(self):
        print(f"Way to lock in {self.first_name.title()}.")

    def create_username(self):
        self.username = str(self.first_name) + str(self.last_name)
        print(f"Username: {self.username}")

class Privileges:
    def __init__(self, privileges):
        self.privileges = privileges

    def show_privileges(self):
        priv_str = ', '.join(map(str, self.privileges))
        print(f"List of Privileges:\n{priv_str}")

class Admin(User):
    def __init__(self, first_name, last_name, privileges):
        super().__init__(first_name, last_name)
        self.privileges = Privileges(privileges)  # Create a Privileges instance

    def show_admin_privileges(self):
        print(f"{self.first_name.title()}'s")
        self.privileges.show_privileges()  # Call show_privileges on the Privileges instance

# Example Usage
user1 = User("john", "doe")
user1.describe_user()
user1.greet_user()
user1.create_username()

print("\n--- Admin User ---")

admin1 = Admin("jane", "smith", ["can add post", "can delete post", "can ban user"])
admin1.describe_user()
admin1.greet_user()
admin1.create_username()
admin1.show_admin_privileges()