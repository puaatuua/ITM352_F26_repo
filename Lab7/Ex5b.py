# Iterate through two tuples you create of your top 5 favorite celebrities and their corresponding ages
# Then, append the values to two lists and store the lists as values in a dictionary with keys “celebrities” and “ages.”

# Name: Ava Puaatuua
# Date: Oct. 3, 2026

# Do it without loops
celebs = ("Aaron Rodgers", "Jordan Love", "Bryan Woo", "LeBron James", "Tom Brady")
ages = (43, 25, 26, 38, 45)

celebrities = list(celebs)
ages = list(ages)

celebrity_dict = {
    "celebrities": celebrities,
    "ages": ages
}

print(celebrity_dict)