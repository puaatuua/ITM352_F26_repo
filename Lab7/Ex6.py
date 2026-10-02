# Write code that will try to append an input from the user to the tuple that you created in Exercise 3 
# and print out the appended tuple.

# Name: Ava Puaatuua
# Date: Oct. 2, 2026

# Tuple from Exercise 3
data = ("hello", 10, "goodbye", 3, "goodnight", 5)
'''
user_input = input("Enter a value to append to the tuple: ")
print("Appended tuple:", data.append(user_input))
'''

# Modify your code using try and except statements to handle this error, 
# reporting to the user that an attempt was made to append a value to the tuple. 
# Get the error from the exception and print this with the report.

'''
try:
    user_input = input("Enter a value to append to the tuple: ")
    data.append(user_input)
except Exception as error:
    print("An attempt was made to append a value to the tuple.")
    print("Error:", error)
    '''

# Instead of reporting an error in the exception, handle it by creating a new tuple 
# by adding the input to the tuple and then assigning it back to the variable holding the tuple. 
# The program should not exit and will continue to the end printing out the appended tuple.

try:
    user_input = input("Enter a value to append to the tuple: ")
    data += (user_input,)
    print("Appended tuple:", data)
except:
    