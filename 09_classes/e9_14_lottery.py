# Make a list or tuple containing a series of 10 numbers and five
# letters. Randomly select four numbers or letters from the list
# and print a message saying that any ticket matching these four
# numbers or letters wins a prize.

# numbers can't be repeated

from random import choice

possibilities = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 'a', 'b', 'c', 'd', 'e']
winning_ticket = []

while len(winning_ticket) < 4:
    pulled_item = choice(possibilities)
    print(f"  We pulled a {pulled_item}!")

    # check if item is already in winning_ticket
    if pulled_item not in winning_ticket:
        winning_ticket.append(pulled_item)

print(winning_ticket)
