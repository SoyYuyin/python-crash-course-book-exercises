# Write a while loop that prompts users for their name. When they enter their name, print a greeting to the screen and add a line recording their visit in a file called guest_book.txt. Make sure each entry appears on a new line in the file.

from datetime import datetime

print('Type "quit" to exit the program.\n\n')

while True:
    name = input('Please enter your name: ')
    if name == 'quit':
        break
    else:
        print(f'\nWelcome {name}!')

        with open('guest_book.txt', 'a') as f:
            f.write(f'{datetime.now().isoformat()}, {name}\n')

        print(f'\nYou have been added to the guestbook...\n')

        print('Current guest book (guest_book.txt):\n')
        with open('guest_book.txt') as f:
            print(f.read())
