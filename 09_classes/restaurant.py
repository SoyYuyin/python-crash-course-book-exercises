"""A class to represent a Restaurant"""


class Restaurant():
    """A class representing a restaurant."""

    def __init__(self, name, cuisine_type):
        """Initialize the restaurant."""
        self.name = name.title()
        self.cuisine_type = cuisine_type.title()
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
