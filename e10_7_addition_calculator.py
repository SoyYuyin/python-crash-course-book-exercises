# Wrap your code from Exercise 10-6 in a while loop so the user can continue entering numbers even if they make a mistake and enter text instead of a number.

print("Sum of two integers\n")
while True:
    try:
        a = int(input('Enter first number: '))
        b = int(input('Enter second number: '))
    except ValueError:
        print('Error: Invalid number values. Please try again')
    else:
        print(a+b)
        break
