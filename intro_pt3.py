from class_practice import *

# my_dog = Dog(6, "Sylvester", "German Shepard")
# my_dog.description()

# restaurant = Restaurant("Kenny's", "Italian")
# restaurant.describe_restaurant()
# restaurant.open_restaurant()

# restaurant = Restaurant("Kenny's", "Italian")
# restaurant.number_served = 5
# restaurant.set_number_served(10)
# print()


# my_ice_cream_store = IceCreamStand("Sean's", "Ice Cream", ["Strawberry", "Chocolate", "Vanilla"])
# my_ice_cream_store.all_flavors()

user_1 = User("sean", "Flannery")
# user_1.describe_user()
# user_1.greet_user()

list_of_privileges = ["Can read", "Can write", "Can Delete"]
user_2 = Admin("Sean", "Flannery", list_of_privileges)
user_2.privileges.show_privileges()
