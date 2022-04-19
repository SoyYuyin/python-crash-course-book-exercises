# Start with your program form Exercise 9.1 (page 162).
# Add an attribute called number_served with a default value of 0. Create an
# instance called restaurant from this class. Print the number of customers the
# restaurant has served, and then change this value and print it again.
#   Add a method called set_number_served() that lets you set the number
# of customers that have been served. Call this method with a new number and
# print the value again.
#   Add a method called increment_number_served() that lets you increment the
# number of customers who've been served. Call this method with any number you
# like that could represent how many customers were served in, say, a day of
# bussiness.


class Restaurant:
    """Creates a restaurant class, receives restaurant_name and cuisine_type."""

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print(f'{self.restaurant_name} serves {self.cuisine_type} cuisine')

    def open_restaurant(self):
        print(f'{self.restaurant_name} is open!')

    def set_number_served(self, number_customers):
        self.number_served = number_customers

    def increment_number_served(self, customers_increment):
        self.number_served += customers_increment


my_restaurant = Restaurant('Arandenses', 'Mexican/Tacos')
my_restaurant.describe_restaurant()
print(f'Customers served: {my_restaurant.number_served}')

my_restaurant.set_number_served(3000)
print(f'Customers served: {my_restaurant.number_served}')

my_restaurant.increment_number_served(50)
print(f'Customers served: {my_restaurant.number_served}')
