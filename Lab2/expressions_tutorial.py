## My age in days
age = 21
print("My age in days is:",age * 365)

## Monthly expenses if I spend $50 per week
weekly_spending = 50
print("My monthly expenses are:",weekly_spending * 52 / 12)

## How many hours I've been alive
hours_in_a_day = 24
days_in_a_year = 365
print("Hours I've been alive:",age * days_in_a_year * hours_in_a_day)

## My GPA on a 100-point scale if it's currently on a 4.0 scale
gpa_4_scale = 3.7
gpa_100_scale = gpa_4_scale * 25
print("My GPA on a 100-point scale is:", gpa_100_scale)

## Days since I was born
birth_year = 2005
current_year = 2026
print("Days since I was born:", (current_year - birth_year) * 365)

## Weeks since I graduated high school
graduation_year = 2023
print("Weeks since I graduated high school:", (current_year - graduation_year) * 52)

## How much money I spend on gas per month if I drive 200 miles per week and my car gets 25 miles per gallon, with gas costing $3.50 per gallon
miles_per_week = 200
miles_per_gallon = 25
gas_price_per_gallon = 3.50
gallons_per_week = miles_per_week / miles_per_gallon
monthly_gas_expense = gallons_per_week * gas_price_per_gallon * 4
print("My monthly gas expense is:", monthly_gas_expense)

## How much caffiene I consume per week if I drink 2 cups of coffee per day, with each cup containing 95 mg of caffeine
cups_per_day = 2
caffeine_per_cup = 95
caffeine_per_week = cups_per_day * caffeine_per_cup * 7
print("My weekly caffeine consumption is:", caffeine_per_week, "mg")

## How many seconds I've been alive
seconds_in_a_minute = 60
minutes_in_an_hour = 60
hours_in_a_day = 24
days_in_a_year = 365
seconds_alive = age * days_in_a_year * hours_in_a_day * minutes_in_an_hour
print("Seconds I've been alive:", seconds_alive)

## Personal profile
name = "Ava Puaatuua"
hometown = "Honolulu, Hawaii"
print("My name is", name, "and I am from", hometown)

## Email signature
major = "MIS"
graduation_year = 2028
email_signature = f"{name}\n{major} Major\nClass of {graduation_year}"
print("Email signature:\n", email_signature)

## 5 arithmetic expressions showing different operators
# addition, subtraction, multiplication, division, and exponentiation
print("5 + 3 =", 5 + 3)
print("10 - 4 =", 10 - 4)
print("6 * 7 =", 6 * 7)
print("15 / 3 =", 15 / 3)
print("2 ** 8 =", 2 ** 8)

## 3 string expressions using concatenation and f-strings
# Concatenation, f-string, and format method
print("Hello, " + name + "!")
print(f"Welcome, {name}!")
print("You are from {}.".format(hometown))

## 4 boolean expressions using comparison and logical operators
# Comparison and logical operators
print("Is your age greater than 20?", age > 20)
print("Is your GPA higher than 3.5?", gpa_4_scale > 3.5)
print("Is your hometown Honolulu?", hometown == "Honolulu, Hawaii")
print("Is your major MIS or Computer Science?", major == "MIS" or major == "Computer Science")

## 2 complex expressions that demonstrate operator precedence
# Operator precedence
print("(5 + 3) * 2 =", (5 + 3) * 2)
print("5 + 3 * 2 =", 5 + 3 * 2)