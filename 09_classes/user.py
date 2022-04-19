"""A collection of classes for modeling users."""


class User():
    """Represent a simple user profile."""

    def __init__(self, first_name, last_name, username, email, premium):
        """Initialize the user."""
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.username = username
        self.email = email
        self.premium = premium

    def describe_user(self):
        """Display a summary of the user's information."""
        print(f'\nName: \t\t{self.first_name}\
            \nLast name: \t{self.last_name}\
            \nemail: \t\t{self.email}\
            \nUsername: \t{self.username}\
            \nIs Premium: \t{self.premium}')

    def greet_user(self):
        """Display a personalized greeting to the user."""
        print(f'Hello {self.username}!')


class Privileges():
    """A class to store an admin's privileges."""

    def __init__(self, privileges=[]):
        self.privileges = privileges

    def show_privileges(self):
        print('\nPrivileges:')
        if self.privileges:
            for privilege in self.privileges:
                print(f'- {privilege}')
        else:
            print("Currently, this user has no provileges.")


class Admin(User):
    """
    A user with administrative privileges.
    """

    def __init__(self, first_name, last_name, email, username, premium):
        """
        Initialize attributes of the parent class (User).
        Then initialize attributes specific to Admin types.
        """
        super().__init__(first_name, last_name, email, username, premium)

        # Initialize an empty set of priviliges.
        self.privileges = Privileges()
