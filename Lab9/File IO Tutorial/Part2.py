# Part 2: Reading Files
# Create a text file and practice different reading methods.

# read()
with open('example.txt', 'r') as file:
    content = file.read()
    print("Read entire file:")
    print(content)

# readline()
with open('example.txt', 'r') as file:
    print("\nRead first line:")
    first_line = file.readline()
    print(first_line)

# readlines()
with open('example.txt', 'r') as file:
    print("\nRead all lines into a list:")
    lines = file.readlines()
    print(lines)

# Reading with a for loop
with open('example.txt', 'r') as file:
    print("\nRead file line by line using a for loop:")
    for line in file:
        print(line.strip())