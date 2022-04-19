# Make a class called Restaurant. The __init__() method for Restaurant should
# store two attributes: a restaurant_name and a cuisine_type.
# Make a method called describe_restaurant() that prints these two pieces of
# information, and a method called open_restaurant() that prints a message
# indicating that the restaurant is open.
# Make an instance called restaurant from your class. Print the two attributes
# inidividually, and then call both methods.

class Restaurant:
    """Creates a restaurant class, receives restaurant_name and cuisine_type."""

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f'{self.restaurant_name} serves {self.cuisine_type} cuisine')

    def open_restaurant(self):
        print(f'{self.restaurant_name} is open!')


restaurant = Restaurant('Arandenses', 'Mexican/Tacos')
print(f'Restaurant name: {restaurant.restaurant_name}')
print(f'Cuisine type: {restaurant.cuisine_type}')
restaurant.describe_restaurant()
restaurant.open_restaurant()

print('\n\nExercise 9.2 Three Restaurants:\n')
# 9.2 Three Restaurants
restaurant1 = Restaurant('Sushi Roll', 'Japanese/(Mexican Sushi)')
restaurant2 = Restaurant('IHOP', 'American/Breakfasts')
restaurant3 = Restaurant('Dominos Pizza', 'Italian/Pizzas')

restaurant1.describe_restaurant()
restaurant2.describe_restaurant()
restaurant3.describe_restaurant()
