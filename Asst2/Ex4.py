# Workshop, part 4

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
    


def show_average_sales_by_region(data):
    """Pivot average sales (quantity * unit_price) by region, with state and sale type sub-columns"""
    required = ['sales_region', 'customer_state', 'order_type', 'quantity', 'unit_price']
    missing = [col for col in required if col not in data.columns]
    if missing:
        print("Missing required columns:", ", ".join(missing))
        return

    sales = data.assign(sales=data["quantity"] * data["unit_price"])
    pivot_table = pd.pivot_table(
        sales,
        index="sales_region",
        columns=["customer_state", "order_type"],
        values="sales",
        aggfunc="mean",
        fill_value=0
    )
    print("\nAverage sales by region, by state and sale type:")
    with pd.option_context("display.width", 200, "display.max_columns", None):
        print(pivot_table.round(2))



def exit_program(data=None):
    print("Exiting the program. Goodbye!")
    raise SystemExit(0)



menu_options = (
   ("Show the first n rows of sales data", display_initial_rows),
   ("Show the average sales by region", show_average_sales_by_region),
   ("Exit the program", exit_program)
)


def display_menu():
    """Show the menu and return a valid selection as an index into menu_options."""
    while True:
        print("\nSales Data Menu:")
        for number, (description, _) in enumerate(menu_options, start=1):
            print(f"{number}. {description}")

        choice = input(f'Select an option (1-{len(menu_options)}): ').strip()
        if choice.isdigit() and 1 <= int(choice) <= len(menu_options):
            return int(choice) - 1
        print(f'Invalid selection "{choice}". Please enter a number between 1 and {len(menu_options)}.')



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
            selection = display_menu()
            _, action = menu_options[selection]
            action(sales_data)

    except (KeyboardInterrupt, EOFError):
        print("\nExiting.")


if __name__ == "__main__":
    main()
