class Dog:
    """ Define a dog and enable the object to perform a set of commands. """

    def __init__(self, age, name, breed):
        self.age = age
        self.name = name
        self.breed = breed

    def description(self):
        print(f"{self.name} is a {self.age} year old {self.breed}!")

    def sit(self):
        print(f"{self.name} is now sitting")

    def shake(self):
        print(f"{self.name} shakes your hand")

class Restaurant:
    """9-1"""

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print(f"{self.restaurant_name} serves {self.cuisine_type} cuisine!")

    def open_restaurant(self):
        print(f"{self.restaurant_name} is Open!")

    def set_number_served(self, served):
        self.number_served = served

    def increment_number_served(self, additional_served):
        self.number_served += additional_served

    
class IceCreamStand(Restaurant):
    """9-6"""
    def __init__(self, restaurant_name, cuisine_type, flavors):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = flavors

    def all_flavors(self):
        if not self.flavors:
            return
        
        flavors_str = ", ".join(map(str, self.flavors[:-1]))
        if len(self.flavors) > 1:
            flavors_str += f", and {self.flavors[-1]}"
        
        else:
            items_str = str(self.flavors[0])

        print(f"{self.restaurant_name} is currently serving the following flavors: {flavors_str}!")


class User:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def describe_user(self):
        print(f"First Name: {self.first_name.title()}\nLast Name: {self.last_name.title()}")

    def greet_user(self):
        print(f"Way to lock in {self.first_name.title()}.")

    def create_username(self):
        self.username = str(self.first_name)+str(self.last_name)
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
        self.privileges = Privileges(privileges)
