# Read the json file of taxi trip data and create a dataframe from it.
# Print summary statistics about the dataframe, as well as the median.

# Name: Ava Puaatuua
# Date: Oct. 28, 2026

import pandas as pd

# Read the json file and create a dataframe
taxi_data = pd.read_json("Taxi_Trips.json") 
print(f"Dataframe:\n{taxi_data}")

# Get summary statistics for the dataframe
summary = taxi_data.describe()
print(f"\nSummary statistics: {summary}")

# Get the median of the dataframe
median = taxi_data.median(numeric_only=True) # Calculate the median for numeric columns only
print(f"\nMedian: {median}")
