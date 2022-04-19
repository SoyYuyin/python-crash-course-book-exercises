# Make a class called User. Create two attributes called first_name and
# last_name, and then create several other attributes that are typically stored
# in a user profile. Make a method called describe_user() that prints a summary
# of the user's information. Make a nother method called greet_user() that
# prints a personalized greeting to the user.
#   Create several instances represetnting different users, and call both
# methods for each user.

class User:
    def __init__(self, first_name, last_name, email, username, premium):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.username = username
        self.premium = premium

    def describe_user(self):
        print(f'\nName: {self.first_name}\
            \nLast name: {self.last_name}\
            \nemail: {self.email}\
            \nUsername: {self.username}\
            \nIs Premium: {self.premium}')

    def greet_user(self):
        print(f'Hello {self.username}!')


user1 = User('Eugenio', 'Martinez', 'yuyin@gmail.com', 'Yuyin', False)
user2 = User('Mon', 'Ortuño', 'mon@gmail.com', 'Monbon', True)


user1.describe_user()
user1.greet_user()
user2.describe_user()
user2.greet_user()
