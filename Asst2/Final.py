# Final version of the Asst2 code, including individual requirements 4 & 6

# Name: Ava Puaatuua
# Date: Nov. 8, 2026

import pandas as pd
import ssl
import time

# Temporary fix
ssl._create_default_https_context = ssl._create_unverified_context

def load_csv(filepath):
    '''Loads a CSV file into a dataframe, indicating that the file is being loaded and when it is successfully loaded, along with the time it took to load.'''
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
        '''response = input(f'\nHow many initial rows would you like to see? '
                         f'(1-{len(data)} or "all" to see all rows): ').strip().lower()'''

        response = input(f"""\nEnter rows to display: 
                         \n- Enter a number 1 to {len(data)},
                         \n- To see all rows, enter "all"
                         \n- To skip preview, press Enter
                         \nYour choice:
                         """).strip().lower()

        if response == 'all':
            print(data)
            return

        if response == '':
            print("Skipping preview of initial rows.")
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
    


def calculate_total_sales_by_region_and_order_type(data):
    """Aggregate sales bt region, with columns defined by order_type (Retail or Wholesale)"""
    required = ['sales_region', 'order_type', 'quantity', 'unit_price']
    missing = [col for col in required if col not in data.columns]
    if missing:
        print("Missing required columns:", ", ".join(missing))
        return

    sales = data.assign(sales=data["quantity"] * data["unit_price"])
    pivot_table = pd.pivot_table(
        sales,
        index="sales_region",
        columns="order_type",
        values="sales",
        aggfunc="sum",
        fill_value=0
    )
    print("\nTotal sales by region and order type:")
    with pd.option_context("display.width", 200, "display.max_columns", None):
        return pivot_table.round(2)




def calculate_average_sales_by_region(data):
    """Aggregate sales by region with sub-colums showing the average sales by state and by sale type (Retail or Wholesale)"""
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
        return pivot_table.round(2)




def calculate_sales_by_customer_type_and_order_type_by_state(data):
    """Pivot table with sub-rows showing sales by customer type and order type, with state sub-columns"""
    required = ['customer_state', 'customer_type', 'order_type', 'quantity', 'unit_price']
    missing = [col for col in required if col not in data.columns]
    if missing:
        print("Missing required columns:", ", ".join(missing))
        return

    sales = data.assign(sales=data["quantity"] * data["unit_price"])
    pivot_table = pd.pivot_table(
        sales,
        index=["customer_type", "order_type"],
        columns="customer_state",
        values="sales",
        aggfunc="sum",
        fill_value=0
    )
    print("\nTotal sales by customer type and order type, by state:")
    with pd.option_context("display.width", 200, "display.max_columns", None):
        return pivot_table.round(2)



def calculate_total_sales_quantity_and_price_by_region_and_product(data):
    """Pivot sales by region and product, summing the quantity and sales price per row"""
    required = ['sales_region', 'produce_name', 'quantity', 'unit_price']
    missing = [col for col in required if col not in data.columns]
    if missing:
        print("Missing required columns:", ", ".join(missing))
        return

    sales = data.assign(sales=data["quantity"] * data["unit_price"])
    pivot_table = pd.pivot_table(
        sales,
        index=["sales_region", "produce_name"],
        columns=None,
        values=["quantity", "sales"],
        aggfunc="sum",
        fill_value=0
    )
    print("\nTotal sales by region and product:")
    with pd.option_context("display.width", 200, "display.max_columns", None):
        return pivot_table.round(2)




def calculate_total_sales_quantity_and_price_by_customer_type(data):
    """Pivot sales by order and customer type, summing the quantity and sales price per row"""
    required = ['customer_type', 'order_type', 'quantity', 'unit_price']
    missing = [col for col in required if col not in data.columns]
    if missing:
        print("Missing required columns:", ", ".join(missing))
        return

    sales = data.assign(sales=data["quantity"] * data["unit_price"])
    pivot_table = pd.pivot_table(
        sales,
        index=["customer_type", "order_type"],
        columns=None,
        values=["quantity", "sales"],
        aggfunc="sum",
        fill_value=0
    )
    print("\nTotal sales by customer type and order type:")
    with pd.option_context("display.width", 200, "display.max_columns", None):
        return pivot_table.round(2)




def calculate_max_min_sales_price_by_category(data):
    """Pivot sales by category and show the max and min sales price per row"""
    required = ['product_category', 'unit_price']
    missing = [col for col in required if col not in data.columns]
    if missing:
        print("Missing required columns:", ", ".join(missing))
        return

    pivot_table = pd.pivot_table(
        data,
        index="product_category",
        values="unit_price",
        aggfunc=["max", "min"]
    )
    print("\nMax and min sales price by category:")
    with pd.option_context("display.width", 200, "display.max_columns", None):
        return pivot_table.round(2)



def show_employees_by_region(data):
    """Print the number of unique employees in each sales region."""
    counts = data.groupby('sales_region')['employee_id'].nunique()
    print('\nNumber of employees by region:')
    print(counts.to_string())



def generate_custom_pivot_table(data):
    """Interactively build and display a pivot table."""
    print(f'\nCustom table')
    row_options = list(data.columns)
    rows = get_user_selection(row_options, "\nSelect rows (required):", required=True)

    col_options = [col for col in row_options if col not in rows]
    cols = get_user_selection(col_options, "\n Select columns (optional, Enter to skip):")

    value_options = list(data.select_dtypes(include=['number']).columns)
    if not value_options:
        print('No numeric columns available to aggregate.')
        return
    values = get_user_selection(value_options, "\nSelect value to aggregate:", required=True, single=True)

    agg_options = ['sum', 'mean', 'count']
    agg_func = get_user_selection(agg_options, "\nSelect aggregation function:", required=True, single=True)[0]

    try:
        pivot_table = pd.pivot_table(
            data,
            index=rows,
            columns=cols if cols else None,
            values=values,
            aggfunc=agg_func,
            fill_value=0 # Add fill_value=0 to handle missing values in the pivot table
        )
    except Exception as e:
        print("Could not create the pivot table:", e)
        return

    print("\nCustom pivot table:")
    return pivot_table


def compare_two_pivot_tables(data):
    """Get two analytics results and compare them side by side"""

    # Display the available analytics options for the user to choose from
    analytics = [
        ("Total sales by region and order type", calculate_total_sales_by_region_and_order_type),
       ("Average sales by region with average sales by state and sale type", calculate_average_sales_by_region),
       ("Sales by customer type and order type by state", calculate_sales_by_customer_type_and_order_type_by_state),
       ("Total sales quantity and price by region and product", calculate_total_sales_quantity_and_price_by_region_and_product),
       ("Total sales quantity and price by customer type", calculate_total_sales_quantity_and_price_by_customer_type),
       ("Max and min sales price of sales by category", calculate_max_min_sales_price_by_category),
       ("Number of unique employees by region", show_employees_by_region),
    ]

    # Prompt the user for the first analytic to compare
    print("\nChoose the first analytic:")
    for number, (description, _) in enumerate(analytics, start=1):
        print(f"{number}. {description}")

    first_number = int(input("Enter the number: "))
    first_description, first_function = analytics[first_number - 1] # -1 because Python indexes lists from 0

    # Prompt the user for the second analytic to compare
    print("\nChoose the second analytic:")
    for number, (description, _) in enumerate(analytics, start=1):
        print(f"{number}. {description}")

    second_number = int(input("Enter the number: "))
    second_description, second_function = analytics[second_number - 1] # -1 because Python indexes lists from 0

    first_rows = select_data_rows(data)
    second_rows = select_data_rows(data)

    first_table = first_function(first_rows)
    second_table = second_function(second_rows)

    if first_table is None or second_table is None:
        print("The analytics could not be calculated.")
        return

    first_table = flatten_columns(first_table)
    second_table = flatten_columns(second_table)

    # Combine the two pivot tables side by side for comparison
    comparison = pd.concat(
        [first_table, second_table],
        axis=1, # Place the two tables beside each other
        keys=[first_description, second_description] # Label the two sections
    )

    print("\nComparison of the two analytics:")
    with pd.option_context("display.width", 200,
                           "display.max_columns", None):
        print(comparison.round(2))



# This code was generated using Copilot with the prompt: "How can I make a function to prompt the user to select rows from a dataframe, allowing them to enter ranges (e.g., 1-10) or individual row numbers (e.g., 1,4,7), and return the selected rows as a new dataframe?"
def select_data_rows(data):
    '''Let the user choose which df rows an analytic should use'''
    while True:
        response = input(
            f"Enter rows to use, such as 1-10 or 1,4,7 "
            f"(1-{len(data)}): "
        ).strip()

        try:
            selected_rows = set() # Use a set to avoid duplicates

            for part in response.split(","): # Separate the input by commas to handle individual numbers and ranges
                part = part.strip()

                if "-" in part:
                    start_text, end_text = part.split("-", 1)
                    start = int(start_text.strip())
                    end = int(end_text.strip())

                    if start > end:
                        raise ValueError

                    selected_rows.update(range(start, end + 1))
                else:
                    selected_rows.add(int(part))

            if not selected_rows or any(
                row < 1 or row > len(data)
                for row in selected_rows
            ):
                raise ValueError # reject empty or out-of-bounds selections

            indexes = [row - 1 for row in sorted(selected_rows)] # Convert row numbers for pandas
            return data.iloc[indexes] # return only the selected rows

        except ValueError:
            print(
                f"Invalid input: {response!r}. "
                "Enter values such as 1-10 or 1,4,7."
            )


def flatten_columns(table):
    flattened = []

    for column in table.columns:
        if isinstance(column, tuple):
            flattened.append(" | ".join(str(value) for value in column))
        else:
            flattened.append(str(column))

    result = table.copy()
    result.columns = flattened
    return result



def exit_program(data=None):
    print("Exiting the program. Goodbye!")
    raise SystemExit(0)



def get_user_selection(options, prompt, required=False, single=False): 
    """Prompt for comma-separated option numbers and return the chosen options.
    
    Re-prompts on invalid input. An empty entry returns [] unless required."""
    
    while True:
        print(prompt)
        for i, option in enumerate(options):
            print(f"{i+1}. {option}") 
            
        choice = input("Enter the number(s) of your choice(s), separated by commas: ").strip()
        if not choice:
            if required:
                print("A selection is required.")
                continue
            return []

        try:
            indexes = [int(i) for i in choice.split(',')]
        except ValueError:
            print("Invalid input. Please enter numbers separated by commas.")
            continue

        if any(i < 1 or i > len(options) for i in indexes):
            print(f'Each number must be between 1 and {len(options)}.')
            continue

        selected = list(dict.fromkeys(options[i-1] for i in indexes))  # Remove duplicates while preserving order
        if single and len(selected) != 1:
            print("Please select exactly one option.")
            continue
        return selected



menu_options = (
   ("Show the first n rows of sales data", display_initial_rows),
   ("Total sales by region and order type", calculate_total_sales_by_region_and_order_type),
   ("Average sales by region with average sales by state and sale type", calculate_average_sales_by_region),
   ("Sales by customer type and order type by state", calculate_sales_by_customer_type_and_order_type_by_state),
   ("Total sales quantity and price by region and product", calculate_total_sales_quantity_and_price_by_region_and_product),
   ("Total sales quantity and price by customer type", calculate_total_sales_quantity_and_price_by_customer_type),
   ("Max and min sales price of sales by category", calculate_max_min_sales_price_by_category),
   ("Number of unique employees by region", show_employees_by_region),
   ("Create a custom pivot table", generate_custom_pivot_table),
   ("Compare two pivot tables", compare_two_pivot_tables),
   ("Exit the program", exit_program)
)



def display_menu():
    """Show the menu and return a valid selection as an index into menu_options."""
    while True:
        print("\n--- Sales Data Dashboard ---")
        for number, (description, _) in enumerate(menu_options, start=1):
            print(f"{number}. {description}")

        choice = input(f'Select an option (1-{len(menu_options)}): ').strip()
        if choice.isdigit() and 1 <= int(choice) <= len(menu_options):
            return int(choice) - 1
        print(f'Invalid selection "{choice}". Please enter a number between 1 and {len(menu_options)}.')



def main():
    csv_file = (
        "https://drive.google.com/uc?"
        "id=1ujY0WCcePdotG2xdbLyeECFW9lCJ4t-K&export=download"
    )

    sales_data = load_csv(csv_file)

    if sales_data is None:
        return

    print("\nData types of the dataframe fields:")
    print(sales_data.dtypes)

    try:
        while True:
            selection = display_menu()
            _, action = menu_options[selection]

            if action in (
                display_initial_rows,
                compare_two_pivot_tables,
                exit_program,
            ):
                result = action(sales_data)
            else:
                selected_data = select_data_rows(sales_data)
                result = action(selected_data)

            if result is not None:
                print(result)

    except (KeyboardInterrupt, EOFError):
        print("\nExiting.")


if __name__ == "__main__":
    main()
