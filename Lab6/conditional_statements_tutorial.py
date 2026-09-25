# Conditional Statements Tutorial

# Name: Ava Puaatuua
# Date: Sept. 24, 2026

# Part 2: Boolean Expressions and Comparisons
# Create conditional statements that check user age, grades, or weather conditions.
user_age = 20
if user_age >= 18:
    print("You are an adult.")

user_grade = 85
if user_grade >= 90:
    print("You got an A!")
elif user_grade >= 80:
    print("You got a B!")
else:
    print("You got a C or lower.")

weather_condition = "sunny"
if weather_condition == "sunny":
    print("It's a great day for a walk!")
elif weather_condition == "rainy":
    print("Don't forget your umbrella!")

# Part 3: Multiple Conditions with elif
# Create a grade calculator that assigns letter grades based on numeric scores.
grade = 92
if grade >= 90:
    print("You got an A!")
elif grade >= 80:
    print("You got a B!")
elif grade >= 70:
    print("You got a C!")

else:
    print("You got a D or lower.")

# Part 4: Nested Conditional Statements
# Create a program that determines shipping costs based on weight and destination.
weight = 4
destination = "domestic"

if destination == "domestic":
    if weight <= 5:
        shipping_cost = 5
    else:
        shipping_cost = 10
else:
    if weight <= 5:
        shipping_cost = 15
    else:
        shipping_cost = 25

print(f"Shipping cost: ${shipping_cost}")

# Part 5: Conditional Statements with Data Structures
# Validate user input for a registration form.

