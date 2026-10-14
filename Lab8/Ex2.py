# This program calculates the minimum number of coins needed to make change for an amount given by the user

# Name: Ava Puaatuua
# Date: Oct. 14, 2026

total_cents = int(input("Enter the total amount of change in cents: "))
change_dict = {}
coins = [25, 10, 5, 1]

for coin in coins:
    count = total_cents // coin
    if count > 0:
        change_dict[coin] = count
        total_cents -= count * coin

print("Change given: ", change_dict)
