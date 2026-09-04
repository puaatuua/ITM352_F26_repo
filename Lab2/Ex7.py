# This program converts temperature in Fahrenheit to Celsius.

# Name: Ava Puaatuua
# Date: September 4, 2026

fahrenheit_input = input("Enter a temperature in Fahrenheit: ")
fahrenheit_float = float(fahrenheit_input)

celsius_value = (fahrenheit_float - 32) * 5 / 9

celsius_value = round(celsius_value, 2)

print("You entered: ", fahrenheit_float)
print("The temperature in Celsius is: ", celsius_value)