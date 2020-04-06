from sys import argv

# Expecting an argument when running this script
script, input_file = argv

# Print the whole file
def print_all(f):
    print(f.read())


def rewind(f):
    f.seek(0)


# Read a specific line from the file
def print_a_line(line_count, f):
    print(line_count, f.readline())


# Open file for reading
current_file = open(input_file)

print("First let's print the whole file:\n")
print_all(current_file)

print("Now let's rewind, kind of like a tape.")
rewind(current_file)

print("Let's print 3 lines:")
current_line = 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)
