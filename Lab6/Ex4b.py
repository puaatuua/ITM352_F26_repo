# This program uses a function to check if a given year is a leap year or not

# Name: Ava Puaatuua
# Date: Sept. 25, 2026

def isLeapYear(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return "Leap year"
            else:
                return "Not a leap year"
        else:
            return "Leap year"
    else:
        return "Not a leap year"

year = int(input("Enter a year: "))
result = isLeapYear(year)
print(f"{year} is {result}.")