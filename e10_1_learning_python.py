# Open a blank file in your text editor and write a few lines summarizing what you’ve learned about Python so far. Start each line with the phrase In Python you can… Save the file as learning_python.txt in the same directory as your exercises for this chapter. Write a program that reads the file and prints what you wrote three times. Print the contents once by reading in the entire file, once by looping over the file object, and once by storing the lines in a list and then working with them outside the with block.

file_name = 'learning_python.txt'

with open(file_name) as file_object:
    content = file_object.read()

print('\n\nRead using .read() method\n', content[:300])


with open(file_name) as file_object:
    print('\n\nRead using for loop on file object')
    i = 0
    for line in file_object:
        print(line.rstrip())
        i += 1
        if i == 6:
            break


with open(file_name) as file_object:
    lines = file_object.readlines()

print('\n\nCreated a list of lines by using .readlines() on file object')
print(lines[:6])
