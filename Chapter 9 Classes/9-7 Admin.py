'''
9-7. Admin: An administrator is a special kind of user. Write a class called
Admin that inherits from the User class you wrote in Exercise 9-3 (page 162)
or Exercise 9-5 (page 167). Add an attribute, privileges , that stores a list
of strings like "can add post" , "can delete post" , "can ban user" , and so on.
Write a method called show_privileges() that lists the administrator’s set of
privileges. Create an instance of Admin , and call your method.
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


user1 = Admin('eric', 'nguyen', 'ericnguyen159@gmail.com')
user1.show_privileges()

# basically if you're calling a method (function) inside a class use ()
# if calling an attribute use it's name (self.whatever)
