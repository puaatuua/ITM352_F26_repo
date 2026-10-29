# Read in a CSV file and turn it into a pandas dataframe.
# Print out the dimensions of the data frame and show the first 10 rows

# Name: Ava Puaatuua
# Date: Oct. 28, 2026

import pandas as pd

# Read in the CSV file and create a dataframe
df = pd.read_csv("homes_data.csv")

# Print the dimensions of the dataframe
print(f"Dimensions: {df.shape}")

# Show the first 10 rows of the dataframe
print(f"First 10 rows:\n{df.head(10)}")
