'''
9-6. Ice Cream Stand: An ice cream stand is a specific kind of restaurant. Write
a class called IceCreamStand that inherits from the Restaurant class you wrote
in Exercise 9-1 (page 162) or Exercise 9-4 (page 167). Either version of
the class will work; just pick the one you like better. Add an attribute called
flavors that stores a list of ice cream flavors. Write a method that displays
these flavors. Create an instance of IceCreamStand , and call this method.
'''


class Restaurant:
    def __init__(self, name, cuisine_type):
        self.name = name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print(f"The restaurant's name is {self.name}")
        print(f"It's known for it's {self.cuisine_type} food!")

    def open_restaurant(self):
        print(f"\nWe're now open for business! Thank you for waiting!")

    def set_number_served(self, number_served):
        self.number_served = number_served

    def increment_number_served(self, new_customers):
        self.number_served += new_customers


class IceCreamStand(Restaurant):
    # flavors = []

    def __init___(self, name, cuisine_type):
        super().__init__(name, cuisine_type)
        self.name = name
        self.cuisine_type = cuisine_type
        self.number_served = 1
        self.flavors = []

    def add_flavor(self, new_flavor):
        self.flavors.append(new_flavor)
        print(f"Just added {new_flavor}!")

    def print_flavors(self):
        print("Here are the flavors we serve: ")
        for flavor in self.flavors:
            print("\t", flavor)


Dreyers = IceCreamStand("Dreyers", "Ice Cream")

Dreyers.flavors = ["vanilla"]
print(Dreyers.flavors)

Dreyers.add_flavor("chocolate")
print(Dreyers.flavors)
Dreyers.print_flavors()
