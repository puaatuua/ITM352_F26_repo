# Read a CSV file containing window cleaning employee data and compute salary statistics.
# print info about file existence and permissions before reading the file

import csv
import os

# Check if the file exists and is readable
if not os.path.exists("window_cleaning_employees.csv"):
    print("Error: The file 'window_cleaning_employees.csv' does not exist.")
    exit(1)

if not os.access("window_cleaning_employees.csv", os.R_OK):
    print("Error: The file 'window_cleaning_employees.csv' is not readable.")
    exit(1)
else: