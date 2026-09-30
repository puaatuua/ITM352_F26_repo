# Write Python code that executes a for loop that examines every element of the tuple (“hello,” 10; “goodbye,” 3; “goodnight,” 5). 
# Within the loop, use an if statement to count how many of the elements are strings. 
# After the loop completes, print out a message stating how many strings are in the tuple.

# Name: Ava Puaatuua
# Date: Sept. 20, 2026


data = ("hello", 10, "goodbye", 3, "goodnight", 5)

string_count = 0

for item in data:
    if type(item) == str:
        string_count += 1

print(f'There are {string_count} strings in the data tuple.')