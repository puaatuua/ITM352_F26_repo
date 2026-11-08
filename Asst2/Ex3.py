# Workshop, part 3

# Name: Ava Puaatuua
# Date: Nov. 6, 2026

import pandas as pd
import ssl
import time

#Temporary fix
ssl._create_default_https_context = ssl._create_unverified_context

# Write a function load_csv() that loads a CSV file into a dataframe. 
# It should indicate the file is being loaded and when it is successfully loaded and the time it took to load. 
def load_csv(filepath):
    print(f"Loading CSV file from: {filepath}")
    start_time = time.time()

    try:
        df = pd.read_csv(filepath,engine='pyarrow',on_bad_lines='skip') # Use the pyarrow backend to skip bad rows
        end_time = time.time()
        load_time = end_time - start_time
        print(f"CSV file loaded successfully in {load_time:.2f} seconds.")
        return df

    except Exception as e:
        print("Error reading the CSV file:", e)
        return None


def display_initial_rows(data):
    # Ask the user how many initial rows to show and print them.

    while True:
        response = input(f'\nHow many initial rows would you like to see? '
                         f'(1-{len(data)} or "all" to see all rows): ').strip().lower()

        if response == 'all':
            print(data)
            return

        try:
            num_rows = int(response)
        except ValueError:
            print(f'Invalid input "{response}". Please enter a whole number or "all".')
            continue

        if num_rows < 1:
            print("Please enter a number greater than 0.")
            continue

        if num_rows > len(data):
            print(f"Only {len(data)} rows available; showing all of them.")
            continue

        print(data.head(num_rows))
        return
    


def main():
    csv_file = 'https://drive.google.com/uc?id=1ujY0WCcePdotG2xdbLyeECFW9lCJ4t-K&export=download'
    # csv_file = "junk.csv"  # Intentionally incorrect path to test error handling
    sales_data = load_csv(csv_file)

    if sales_data is None:
        return

    # describe the dataframe field data types
    print("\nData types of the dataframe fields:")
    print(sales_data.dtypes)

    try:
        while True:
            display_initial_rows(sales_data)

            again = input("\nWould you like to see more rows? (y/n): ").strip().lower()
            if again != 'y':
                print("Exiting.")
                break
    except (KeyboardInterrupt, EOFError):
        print("\nExiting.")


if __name__ == "__main__":
    main()
