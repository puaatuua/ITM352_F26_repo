#Debugging exercise # 2
# Calculating a shopping cart
prices = [5.95, 3.00, 12.50]
total_price = 0
tax_rate = 1.08    # 8% tax 
for price in prices:
    price_with_tax = price * tax_rate
    total_price += price_with_tax

print(f"Total price (with tax): ${total_price}")
