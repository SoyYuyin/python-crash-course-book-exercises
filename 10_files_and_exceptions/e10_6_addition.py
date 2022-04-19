# One common problem when prompting for numerical input occurs when people provide text instead of numbers. When you try to convert the input to an int, you’ll get a ValueError. Write a program that prompts for two numbers. Add them together and print the result. Catch the TypeError if either input value is not a number, and print a friendly error message. Test your program by entering two numbers and then by entering some text instead of a number.

print("Sum two numbers\n")
try:
    a = int(input('Enter first number: '))
    b = int(input('Enter second number: '))
except ValueError:
    print('Error: Please enter number values')
else:
    print(a+b)
