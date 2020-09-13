'''
9-5. Login Attempts: Add an attribute called login_attempts to your User
class from Exercise 9-3 (page 162). Write a method called increment_login
_attempts() that increments the value of login_attempts by 1. Write another
method called reset_login_attempts() that resets the value of login_attempts
to 0.
Make an instance of the User class and call increment_login_attempts()
several times. Print the value of login_attempts to make sure it was incremented
properly, and then call reset_login_attempts() . Print login_attempts again to
make sure it was reset to 0.
'''


class User:
    def __init__(self, first_name, last_name, email):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.login_attempts = 0

    def describe_user(self):
        print("Here's the user info:")
        print(f"\t{self.first_name}\n\t{self.last_name}\n\t{self.email}")

    def greet_user(self):
        full_name = f"{self.first_name} {self.last_name}"
        print(f"Hello welcome {full_name}")

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0


new_user = User('Eric', 'Nguyen', 'ericnguyen159@gmail.com')

new_user.describe_user()
new_user.greet_user()

new_user.increment_login_attempts()

new_user.increment_login_attempts()
new_user.increment_login_attempts()
new_user.increment_login_attempts()
print(new_user.login_attempts)

new_user.reset_login_attempts()
print(new_user.login_attempts)
