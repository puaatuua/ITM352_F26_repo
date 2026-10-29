# Select only properties that have 500 or more units. 
# Drop some unnecessary columns and print the first 10 rows

# Name: Ava Puaatuua
# Date: Oct. 28, 2026

import pandas as pd

# Read in the CSV file and create a dataframe
homes_df = pd.read_csv("homes_data.csv")

# Print the dimensions of the dataframe
print(f"Dimensions: {homes_df.shape}")

# Show the first 10 rows of the dataframe
print(f"First 10 rows:\n{homes_df.head(10)}")

# Only keep properties with more than 500 units and drop the easement column

df_big = homes_df[homes_df['units'] >= 500]
df_big = df_big.drop(columns=['easement'])
print(df_big.head(10))

# Look at the data types
print(df_big.info())

# Coerce land_sqft, gross_sqft, and sale_price to numeric
df_big['land_sqft'] = pd.to_numeric(df_big['land_sqft'], errors='coerce')
df_big['gross_sqft'] = pd.to_numeric(df_big['gross_sqft'], errors='coerce')
df_big['sale_price'] = pd.to_numeric(df_big['sale_price'], errors='coerce')

# We have some null values. Drop these.
df_big = df_big.dropna()

# Now drop duplicate records.
df_big = df_big.drop_duplicates()

# Filter out 0 sales
df_big = df_big[df_big['sale_price'] > 0]
print("After filtering out 0 sales...")
print(df_big.info())
print(df_big.head(10))