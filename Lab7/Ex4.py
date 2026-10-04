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
        print(f"This purchase {purchase} is over budget!")
    else:
        print(f"This purchase {purchase} is within budget.")

# Create a function for this and write test cases for this and use them to test the function.
def check_budget(purchases, budget):
    for purchase in purchases:
        if purchase > budget:
            print(f"This purchase {purchase} is over budget!")
        else:
            print(f"This purchase {purchase} is within budget.")

# Test cases
def test_check_purcahses(list_of_purcahses, list_of_budgets):
    for purchases, budget in zip(list_of_purcahses, list_of_budgets):
        print(f"Testing with purchases: {purchases} and budget: {budget}")
        check_budget(purchases, budget)
        print()
