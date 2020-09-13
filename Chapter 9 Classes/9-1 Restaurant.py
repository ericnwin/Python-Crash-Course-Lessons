'''
9-1. Restaurant: Make a class called Restaurant . The __init__() method for
Restaurant should store two attributes: a restaurant_name and a cuisine_type .
Make a method called describe_restaurant() that prints these two pieces of
information, and a method called open_restaurant() that prints a message indi-
cating that the restaurant is open.
Make an instance called restaurant from your class. Print the two attri-
butes individually, and then call both methods.
'''


class Restaurant:
    def __init__(self, name, cuisine_type):
        self.name = name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"The restaurant's name is {self.name}")
        print(f"It's known for it's {self.cuisine_type} food!")

    def open_restaurant(self):
        print(f"\nWe're now open for business! Thank you for waiting!")


restaurant = Restaurant("Porto's Bakery", "Cuban")
print(restaurant.name)
print(restaurant.cuisine_type)

restaurant.describe_restaurant()
restaurant.open_restaurant()

restaurant2 = Restaurant("In N Out", "American Burgers")
restaurant3 = Restaurant("Malibu Seafood", "Seafood")

restaurant2.describe_restaurant()
restaurant3.open_restaurant()
restaurant3.describe_restaurant()
