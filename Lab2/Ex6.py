# This program converts weight in pounds to kilograms using one line of code.

# Name: Ava Puaatuua
# Date: September 4, 2026

#print("The weight in kilograms is: ", float(input("Enter weight in pounds: "))*0.453592)

KG_TO_POUNDS = 0.453592
weight_in_pounds = input("Enter weight in pounds: ")
weight_in_pounds_float = float(weight_in_pounds)
weight_in_kilograms = weight_in_pounds_float * KG_TO_POUNDS

print("You entered: ", weight_in_pounds_float)
print("The weight in kilograms is: ", weight_in_kilograms)