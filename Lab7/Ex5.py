# Iterate through two tuples you create of your top 5 favorite celebrities and their corresponding ages
# Then, append the values to two lists and store the lists as values in a dictionary with keys “celebrities” and “ages.”

# Name: Ava Puaatuua
# Date: Oct. 2, 2026

celebs = ("Aaron Rodgers", "Jordan Love", "Bryan Woo", "LeBron James", "Tom Brady")
ages = (43, 25, 26, 38, 45)

celeb_list = []
for celeb in celebs:
    celeb_list.append(celeb)

ages_list = [age for age in ages]

celebs_dict = {"celebs": celeb_list, "ages": ages_list}
print(celebs_dict)
