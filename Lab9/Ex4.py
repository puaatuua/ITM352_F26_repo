# Modify the program to calculate the total of all fares, the average of those fares, 
# and the maximum trip distance (based on the Trip Miles field) for records that have fares 
# greater than 10 dollars. 

# Name: Ava Puaatuua
# Date: Oct. 23, 2026

import csv

filename = "../taxi_1000.csv"

with open(filename, "r") as file:
    csv_reader = csv.reader(file)

    # Initializing variables to hold the total fare, max distance, average fare, and number of rows
    total_fare = 0.0 # Running total of all fares
    max_distance = 0.0 # Greatest trip distance found
    average_fare = 0.0 # Calculated after all rows are processed
    num_rows = 0 # Counts the header and data rows
    num_records = 0 # Counts the number of records with fares greater than $10

    # Processing the header row
    for row in csv_reader:
        if num_rows == 0:

            fare_index = row.index('Fare') # Get the index of the fare column
            distance_index = row.index('Trip Miles') # Get the index of the distance column
            num_rows += 1
            continue

        # Reading each taxi record
        if (num_rows > 0):
            fare = float(row[fare_index])
            distance = float(row[distance_index])

        if fare > 10: # Only process records with fares greater than $10
            total_fare += fare
            num_records += 1 # Increment the count of records with fares greater than $10
            # Finding the longest trip
            if distance > max_distance: 
                max_distance = distance

        num_rows += 1 # Counting rows, including the header row

        if num_records > 0:
            average_fare = total_fare / num_records # Calculate the average fare for records with fares greater than $10    

print(f"Total fare: ${total_fare:.2f}")
print(f"Average fare: ${average_fare:.2f}")
print(f"Max trip distance: {max_distance:.2f} miles")