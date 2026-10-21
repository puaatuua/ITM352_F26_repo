# Read the entire file using readlines()

# Name: Ava Puaatuua
# Date: Oct. 21, 2026

with open("names.txt", "r") as file_object:
    names = file_object.readlines()
    print(f"Number of names: {len(names)}")
    for name in names:
        print(name.strip())
