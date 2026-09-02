# This program prompts the user to enter a number between 1 and 100, 
# calculates the square of that number, and then prints the result.

# Name: Ava Puaatuua
# Date: September 2, 2026

value_entered = input("Enter a number between 1 and 100: ")
value_as_integer = int(value_entered)

valueSquared = value_as_integer ** 2

print("The square of", value_as_integer, "is", valueSquared)

# Another way to print the result using an f-string
print(f"The square of {value_as_integer} is {valueSquared}")