# Create an algorithm to determine if a number entered by a user exists in an array of numbers. 
# For example, you can use the array: 

# Name: Ava Puaatuua
# Date: Oct. 14, 2026

searchMe  = [ 2, 5, 7, 11, 15, 22, 27, 30, 34, 41, 55, 57, 58, 60, 77]

def search_array(array, number):
    for i in range(len(array)):
        if array[i] == number:
            return True
    return False

number = int(input("Enter a number to search for: "))
if search_array(searchMe, number):
    print("The number", number, "is in the array.")
else:
    print("The number", number, "is not in the array.")
