# Iterate through a list named “recent_purchases” of your last 5 expenses (e.g. recent_purchases = [36.13, 23.87, 183.35, 22.93, 11.62]) 
# and set a budget for yourself (e.g. $50). 
# Print the message “This purchase is over budget!” if the expense is greater than your budget 
# and “This purchase is within budget” otherwise.

# Name: Ava Puaatuua
# Date: Oct. 2, 2026

recent_purchases = [36.13, 23.87, 183.35, 22.93, 11.62]
budget = 50

for purchase in recent_purchases:
    if purchase > budget:
        print("This purchase is over budget!")
    else:
        print("This purchase is within budget.")

# Create a function for this and write test cases for this and use them to test the function.
def check_budget(purchases, budget):
    for purchase in purchases:
        if purchase > budget:
            print("This purchase is over budget!")
        else:
            print("This purchase is within budget.")

# Test cases
test_purchases1 = [10, 20, 30]
test_budget1 = 25
print("\nTest Case 1:")
check_budget(test_purchases1, test_budget1)

test_purchases2 = [60, 40, 50]
test_budget2 = 55
print("\nTest Case 2:")
check_budget(test_purchases2, test_budget2)