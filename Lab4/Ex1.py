# Using the input() function to input three strings (first name, middle initial, and last name)
# And concatenate the strings with a space in between, in various ways.

# Name: Ava Puaatuua
# Date: Sept. 16, 2026

first = input("Enter your first name: ")
middle_initial = input("Enter your middle initial: ")
last = input("Enter your last name: ")

# Using the + operator to concatenate the strings
full_name = first + " " + middle_initial + ". " + last
print("Your full name is:",full_name)

# Using an f-string to format the output
print(f'Your full name using f-strings is: {first} {middle_initial}. {last}')

# Using the % Operator to format the output
print("Your full name using percent formatting is: %s %s. %s" % (first, middle_initial, last))

# Using the format() method to format the output
print("Your full name using format method is: {} {}. {}".format(first, middle_initial, last))

# Using the join() method to format the output
print("Your full name using list joins is:" + " ".join([first, middle_initial + ".", last]))

# Using the format() method but unpacking the list as the argument
name_parts = [first, middle_initial, last]
print("Your full name is: {} {}. {}".format(*name_parts))
