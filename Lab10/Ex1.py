# Analyze an array of tuples using numpy

# Name: Ava Puaatuua
# Date: Oct. 23, 2026

import numpy as np

# Create an array of typles of household income and percentiles.
hh_income = [
    (10, 14629),
    (20, 25600),
    (30, 37002),
    (40, 50000),
    (50, 63179),
    (60, 79542),
    (70, 100162),
    (80, 130000),
    (90, 184292)
]

hh_income_array = np.array(hh_income) # Convert the list to a NumPy array

# Report the dimensions of the array and the number of elements in the array
print(f"Dimensions of the array: {hh_income_array.ndim}")
print(f"Number of elements in the array: {hh_income_array.size}")

for i in range(hh_income_array.shape[0]): # shape[0] gives the number of rows in the array
    percentile, income = hh_income_array[i]
    print(f"Percentile: {percentile}, Income: ${income}")

# Print the two columns using 2D indexing
'''
for i in range (hh_income_array.shape[0]):
    print(hh_income_array[i, 0], hh_income_array[i, 1])
'''

print("\nTotal income of each percentile group:")
for i in range(len(hh_income_array)):
    percentile, income = hh_income_array[i]
    total_income = percentile * income
    print(f"Percentile {hh_income_array[i][0]}: ${total_income:,}")
    