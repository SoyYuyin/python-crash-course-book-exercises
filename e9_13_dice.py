# Make a class Die with one attribute called sides, which has a
# default value of 6. Write a method called roll_die() that
# prints a random number between 1 and the number of sides the
# die has. Make a 6-sided die and roll it 10 times.

from random import randint


class Die():
    """A class representing a dice."""

    def __init__(self, sides=6):
        self.sides = sides

    def roll_die(self):
        return randint(1, self.sides)


my_normal_dice = Die()
my_10_sided_dice = Die(10)
my_20_sided_dice = Die(20)

print('\n6 sided die rolled 10 times')
for i in range(10):
    print(f'roll #{i}, result:{my_normal_dice.roll_die()}')


print('\n10 sided die rolled 10 times')
for i in range(10):
    print(f'roll #{i}, result:{my_10_sided_dice.roll_die()}')

print('\n20 sided die rolled 10 times')
for i in range(10):
    print(f'roll #{i}, result:{my_20_sided_dice.roll_die()}')


# $ python e9_13_dice.py

# 6 sided die rolled 10 times
# roll #0, result:3
# roll #1, result:3
# roll #2, result:1
# roll #3, result:5
# roll #4, result:4
# roll #5, result:4
# roll #6, result:3
# roll #7, result:6
# roll #8, result:3
# roll #9, result:3

# 10 sided die rolled 10 times
# roll #0, result:1
# roll #1, result:3
# roll #2, result:3
# roll #3, result:1
# roll #4, result:3
# roll #5, result:4
# roll #6, result:9
# roll #7, result:4
# roll #8, result:3
# roll #9, result:4

# 20 sided die rolled 10 times
# roll #0, result:19
# roll #1, result:15
# roll #2, result:10
# roll #3, result:18
# roll #4, result:14
# roll #5, result:20
# roll #6, result:10
# roll #7, result:12
# roll #8, result:20
# roll #9, result:2
