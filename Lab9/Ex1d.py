# Read a file of names one line at a time and print each name

# Name: Ava Puaatuua
# Date: Oct. 21, 2026

with open("names.txt", "r") as file_object:
    while (line := file_object.readline()):
        print(line.strip())
