'''
9-8. Privileges: Write a separate Privileges class. The class should have one
attribute, privileges , that stores a list of strings as described in Exercise 9-7.
Move the show_privileges() method to this class. Make a Privileges instance
as an attribute in the Admin class. Create a new instance of Admin and use your
method to show its privileges.
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


class Admin(User):
    def __init__(self, first_name, last_name, email):
        super().__init__(first_name, last_name, email)
        self.privileges = Privileges()


class Privileges:
    def __init__(self, privileges=[]):
        self.privileges = [
            "can add post",
            "can delete post",
            "can ban user",
            "can change user access"
        ]

    def show_privileges(self):
        print("Here's what an Admin can do:")
        for privilege in self.privileges:
            print("\t", privilege)


user1 = Admin("Booty", "Ass", 'bootyeater69@gmail.com')

user1.privileges.show_privileges()
