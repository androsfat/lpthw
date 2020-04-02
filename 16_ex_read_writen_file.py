''' Need to tun the file like:
python3 16_ex_read_written_file.py new_file.txt
'''
from sys import argv

script, filename = argv

print("We are going to read the file of exercise 16.")
print("Content of file is:")

file = open(filename)
print(file.read())

print("Closing file...")
file.close()
