# import sys module for command line arguments
from sys import argv

# define names of arguments
script, filename = argv

# set filename to txt variable
txt = open(filename)

# print notification with the filename
print(f"Here's your file {filename}:")
# print the content of the file on screen
print(txt.read())

# asking for another file to be typed
print("Type the filename again:")
# get the input of the file showing the prompt
file_again = input('> ')

# open file and set it to a variable
txt_again = open(file_again)

# read and print file on screen
print(txt_again.read())
