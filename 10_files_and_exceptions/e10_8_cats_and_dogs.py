# Make two files, cats.txt and dogs.txt. Store at least three names of cats in the first file and three names of dogs in the second file. Write a program that tries to read these files and print the contents of the file to the screen. Wrap your code ina try-except block to catch the FileNotFound error, and print a friendly message if a file is missing. Move one of the files to a different location on your system, and make sure the code in the except block executes properly.

cats_filename = 'catss.txt'  # misspelled on purpose to raise FileNotFound error
dogs_filename = 'dogs.txt'

try:
    with open(cats_filename) as f:
        cat_names = f.read()

    with open(dogs_filename) as f:
        dog_names = f.read()

except FileNotFoundError:
    # pass   # uncomment this to fail silently and delete/comment print below
    print('File specified does not exist.')

else:
    print(cat_names)
    print(dog_names)
