'''
9-3. Users: Make a class called User . Create two attributes called first_name
and last_name , and then create several other attributes that are typically stored
in a user profile. Make a method called describe_user() that prints a summary
of the user’s information. Make another method called greet_user() that prints
a personalized greeting to the user.
Create several instances representing different users, and call both methods
for each user.
'''


class User:
    def __init__(self, first_name, last_name, email):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email

    def describe_user(self):
        print("Here's the user info:")
        print(f"\t{self.first_name}\n\t{self.last_name}\n\t{self.email}")

    def greet_user(self):
        full_name = f"{self.first_name} {self.last_name}"
        print(f"Hello welcome {full_name}")


new_user = User('Eric', 'Nguyen', 'ericnguyen159@gmail.com')

new_user.describe_user()
new_user.greet_user()
