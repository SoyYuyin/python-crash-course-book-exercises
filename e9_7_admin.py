# 9.7 Admin: An administrator is a special kind of user. Write a class called
# Admin that inherits from the User class you wrote in Exercise 9.3 (page 162)
# or Exercise 9.5 (page 167). Add an attribute, "privileges", that stores a list
# of strings like "can add post", "can delete post", "can ban user", and so on.
# Write a method called show_privileges() that lists the administrator's set of
# privileges. Create an instance of Admin, and call your method.

class User():
    """Represent a simple user profile."""

    def __init__(self, first_name,
                 last_name, username, email,
                 premium):
        """Initialize the user."""
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.username = username
        self.email = email
        self.premium = premium

    def describe_user(self):
        """Display a summary of the user's profile"""
        print(f'\nName: \t\t{self.first_name}\
            \nLast name: \t{self.last_name}\
            \nemail: \t\t{self.email}\
            \nUsername: \t{self.username}\
            \nIs Premium: \t{self.premium}')

    def greet_user(self):
        """Display a personalized greeting message to the user."""
        print(f'Hello {self.username}!')


class Admin(User):
    """
    Represent aspects of User, specific to Administrators
    """

    def __init__(self, first_name, last_name, email, username, premium):
        """
        Initialize attributes of the parent class (User).
        Then initializa attributes specific to Admin types.
        """
        super().__init__(first_name, last_name, email, username, premium)
        self.privileges = []

    def show_privileges(self):
        print('\nPrivileges:')
        for privilege in self.privileges:
            print(f'- {privilege}')


admin_user = Admin('Eugenio', 'Martinez', 'yuyin@gmail.com', 'Yuyin', True)
admin_user.describe_user()
admin_user.privileges = ['can add post', 'can delete post', 'can ban user']
admin_user.show_privileges()
