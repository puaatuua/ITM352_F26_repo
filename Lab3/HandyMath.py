# New module containing two functions: midpoint and squareroot

# Name: Ava Puaatuua
# Date: September 11, 2026

def midpoint(number1, number2):
    return (number1 + number2) / 2

def squareroot(number):
    return number ** 0.5

def exponent(base, exponent):
    return base ** exponent

def max(num1, num2):
    return num1 if num1 > num2 else num2

def min(num1, num2):
    return num1 if num1 < num2 else num2

def describe_function(function, x, y):
    result = function(x, y)
    return f"The function {function.__name__} {x},{y} = {result}"