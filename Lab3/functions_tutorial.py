# This program is a tutorial on functions in Python.

# Name: Ava Puaatuua
# Date: September 7, 2026


# Part 2: Creating Your First Functions
# Function with no parameters
def greet():
    print("Hello! Welcome to the functions tutorial.")

greet()

# Function with one parameter
def greet_user(name):
    print(f"Hello, {name}! Welcome to the functions tutorial.")

greet_user("Ava")

# Function with multiple parameters
def greet_user_with_age(name, age):
    print(f"Hello, {name}! You are {age} years old. Welcome to the functions tutorial.")

greet_user_with_age("Ava", 21)

# Function with a default parameter
def greet_user_with_default(name="Guest"):
    print(f"Hello, {name}! Welcome to the functions tutorial.")

greet_user_with_default()


# Part 3: Return Values and Function Output
# Return a number from a function
def add_numbers(a, b):
    return a + b

answer = add_numbers(5, 10)
print(f"The sum of 5 and 10 is: {answer}")

# Return a string from a function
def create_greeting(name):
    return f"Hello, {name}! Welcome to the functions tutorial."

greeting = create_greeting("Ava")
print(greeting)

# Return a list from a function
def get_favorite_colors():
    return ["blue", "green", "red"]

favorite_colors = get_favorite_colors()
print(favorite_colors)



# Part 4: Function Scope and Variables
# Function with local variable
def calculate_area(length, width):
    area = length * width  # local variable
    return area

area = calculate_area(5, 10)
print(f"The area of the rectangle is: {area}")

# Function with global variable
global_variable = "I am a global variable."

def print_global_variable():
    print(global_variable)  # accessing global variable

print_global_variable()



# Part 5: Practical Function Examples
# Function to perform a mathematical calculation
def calculate_square(number):
    return number ** 2

result = calculate_square(int(input("Enter a number to calculate its square: ")))
print(f"The square of the number is: {result}")

# Function to return the length of a string
def get_string_length(string):
    return len(string)

length = get_string_length("Hello, World!")

# Function to process a string
def count_words(string):
    words = string.split()
    return len(words)

total_words = count_words("This is a sample string with several words.")
print(f"The total number of words in the string is: {total_words}")



# Assessment Challenge
# 1. A function that calculates the area of a rectangle
def calculate_rectangle_area(length, width):
    return length * width

print(f"The area of the rectangle is: {calculate_rectangle_area(5, 10)}")

# 2. A function that determines if a number is even or odd
def is_even_or_odd(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"

print(f"The number 7 is: {is_even_or_odd(7)}")

# 3. A function that takes a list and returns the largest number
def find_largest_number(numbers):
    return max(numbers)

largest_number = find_largest_number([3, 5, 2, 8, 1])
print(f"The largest number in the list is: {largest_number}")

# 4. A function with default parameters for greeting users
def greet_user_with_default_params(name="Guest", age=0):
    print(f"Hello, {name}! You are {age} years old. Welcome to the functions tutorial.")

greet_user_with_default_params("Ava", 21)