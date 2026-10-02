# Iterate through numbers from 1 to 10 and print the number if it is not equal to 5 (using continue) 
# and stop the loop entirely and print a message when it reaches 8 (using break)

# Name: Ava Puaatuua
# Date: Oct. 2, 2026

for number in range(1, 11):
    if number == 8:
        print("Stopping")
        break
    if number != 5:
        print(number)
        continue
    