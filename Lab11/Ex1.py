# Read the CSV file from the URL using exception handling and convert the data types using the pyarrow data type backend. 
# Have it skip bad lines read in. 

# Name: Ava Puaatuua
# Date: Oct. 29, 2026

import pandas as pd
import ssl

csv_file = 'https://drive.google.com/file/d/1ujY0WCcePdotG2xdbLyeECFW9lCJ4t-K/view?usp=drive_link'

# Temporary fix
ssl._create_default_https_context = ssl._create_unverified_context

try:
    df = pd.read_csv(csv_file,engine='pyarrow',on_bad_lines='skip')
    print(df.head())
except Exception as e:
    print("Error reading the CSV file:", e)
