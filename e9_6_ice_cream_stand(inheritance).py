# Ice Cream Stand: An ice cream stand is a specific kind of restaurant. Write
# a class called IceCreamStand that inherits from the Restaurant class you wrote
# in Exercise 9.1 (page 162) or Exercise 9.4 (page 167). Either version of the
# class will work; just pick the one you like better. Add an attribute called
# flavors that stores a list of ice cream flavors. Write a method that displays
# these flavors. Create an instance of IceCreamStand, and call this method.

# import Restaurant class form exercise 9.4

class Restaurant():
    """Creates a restaurant class, receives restaurant_name and cuisine_type."""

    def __init__(self, name, cuisine_type):
        """Initialize the restaurant."""
        self.name = name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        """Display a summary of the restaurant."""
        print(f'{self.name} serves {self.cuisine_type}')

    def open_restaurant(self):
        """Display a message that the restaurant is open."""
        print(f'{self.name} is open!')

    def set_number_served(self, number_served):
        """Allow user to set the number of customers that have been served."""
        self.number_served = number_served

    def increment_number_served(self, customers_increment):
        """Allow user to increment the number of customers served."""
        self.number_served += customers_increment


class IceCreamStand(Restaurant):
    """Represent an ice cream stand."""

    def __init__(self, name, cuisine_type='ice cream'):
        """
        Initialize attributes of the parent class (Restaurant).
        Then initializa attributes specific to an Ice Cream Stand.
        """
        super().__init__(name, cuisine_type)
        self.flavors = []

    def available_flavors(self):
        """Displays available flavors neatly printed."""
        print('Available flavors:')
        for flavor in self.flavors:
            print(f'\t- {flavor.title()}')


dannys = IceCreamStand("Danny's Cream Pies", "Ice Cream")
dannys.flavors = ['vanilla', 'chocolate',
                  'lemon', 'strawberry',
                  'cookies & cream', 'cream pie']

dannys.describe_restaurant()
dannys.open_restaurant()
dannys.available_flavors()
