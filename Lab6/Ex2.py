# Write Python code that creates a list with a variety of different values. 
# Include control logic (if, elif, else) that will print different messages whether the list contains 
# fewer than 5 elements, between 5 and 10 (inclusive), and more than 10 elements. 
# Test your code on lists with several different lengths.

# Name: Ava Puaatuua
# Date: Sept. 25, 2026

numbers_list = [1, 2, 3, 4, 5, 6, 7]

if len(numbers_list) < 5:
    print("The list has fewer than 5 elements.")
elif len(numbers_list) <=10:
    print("The list has between 5 and 10 elements.")
else:
    print("The list has more than 10 elements.")
