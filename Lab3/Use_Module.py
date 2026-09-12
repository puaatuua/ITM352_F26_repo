# This program uses the module HandyMath to perform various mathematical operations

# Name: Ava Puaatuua
# Date: September 11, 2026

import HandyMath
from HandyMath import max, min, exponent

number1 = float(input("Enter the first number: "))
number2 = float(input("Enter the second number: "))

print(f"The midpoint is {HandyMath.midpoint(number1, number2)}")
print(f"The square root of the square of {number1} is "
      f"{HandyMath.squareroot(number1 ** 2)}")
print(f"{number1} raised to the exponent {number2} is "
      f"{HandyMath.exponent(number1, number2)}")
print(f"The maximum is {max(number1, number2)}")
print(f"The minimum is {min(number1, number2)}")

print(HandyMath.describe_function(min, 8, 5))
print(HandyMath.describe_function(max, 8, 5))
print(HandyMath.describe_function(exponent, 2, 3))