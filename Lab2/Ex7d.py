# This program converts temperature in Fahrenheit to Celsius.
# Create the conversion as a function.

# Name: Ava Puaatuua
# Date: September 4, 2026

def F_to_C(fahrenheit):
    celsius = (fahrenheit - 32) * 5 / 9
    rounded_celsius = round(celsius, 2)
    return rounded_celsius

fahrenheit_input = input("Enter a temperature in Fahrenheit: ")
fahrenheit_float = float(fahrenheit_input)

celsius_value = F_to_C(fahrenheit_float)

celsius_value = round(celsius_value, 2)

print("You entered: ", fahrenheit_float)
print("The temperature in Celsius is: ", celsius_value)