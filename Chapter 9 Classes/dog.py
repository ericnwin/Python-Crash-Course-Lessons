'''
creating object dog with info: name and age and behavior: sit and roll over
'''
# By definition classes are capitalized in Python


class Dog:
    """ a simple attempt to model a DOG"""

    def __init__(self, name, age):
        """__init__ means to initialize and we're initializing name and age attributes"""
        self.name = name
        self.age = age

    def sit(self):
        """simulate a dog sitting in response to command"""
        print(f"{self.name} is now sitting")

    def roll_over(self):
        """simulate a dog rolling over in response to a command"""
        print(f"{self.name} is now rolling over")


my_dog = Dog('Mochi', 2)
print(my_dog.name)
print(my_dog.age)
