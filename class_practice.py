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

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"{self.restaurant_name} serves {self.cuisine_type} cuisine!")

    def open_restaurant(self):
        print(f"{self.restaurant_name} is Open!")
    
