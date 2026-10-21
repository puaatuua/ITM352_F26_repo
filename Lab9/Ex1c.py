# Using the .read() method, read the names from the names.txt file 
# and print out the names as well as a count of how many names there are altogether. 

# Name: Ava Puaatuua
# Date: Oct. 21, 2026

with open("names.txt") as file_object:
    contents = file_object.read()
    print(contents)
    contents_list = contents.split('\n')
    print(f"Number of names: {len(contents_list)}")
    for name in contents_list:
        print(name)
