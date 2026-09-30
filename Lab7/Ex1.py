# Use a for-statement to create a list of elements that are the odd numbers between 1 and 50.

# Name: Ava Puaatuua
# Date: Sept. 30, 2026

# Use range() and an if-statement in a “traditional” for loop
""" 
for number in range(1, 51):
    if number % 2 == 1:
        print(number) 
"""


odd_nums = []

for num in range(1, 51):
    if num % 2 != 0:
        odd_nums.append(num)

print(odd_nums)

