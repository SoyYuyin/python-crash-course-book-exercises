# You can use a loop to see how hard it might be to win the kind
# of lottery you just modeled. Make a list or tuple called
# my_ticket. Write a loop that keeps pulling numbers until your
# ticket wins. Print a message reporting how many times the loop
# had to run to give you a winning ticket.

from random import choice


def get_random_ticket():
    """Returns a ticket randomly selected."""
    possibilities = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 'a', 'b', 'c', 'd', 'e']
    random_ticket = []

    while len(random_ticket) < 4:
        pulled_item = choice(possibilities)
        # print(f"  We pulled a {pulled_item}!")

        # check if item is already in random_ticket
        if pulled_item not in random_ticket:
            random_ticket.append(pulled_item)
    return random_ticket


def check_ticket(my_ticket, winning_ticket):
    """Returns False if any element from the one ticket is not in the other. Returns True if tickets match."""
    for element in winning_ticket:
        if element not in my_ticket:
            return False

    # We must have a winning ticket!
    return True


# my_ticket = [1, 2, 3, 4]
my_ticket = get_random_ticket()
winner = False
plays = 0

while not winner:
    plays += 1
    winning_ticket = get_random_ticket()
    if check_ticket(my_ticket, winning_ticket):
        print(f'ran {plays} times')
        print(f'winner ticket {winning_ticket},', f'my ticket {my_ticket}')
        winner = True
