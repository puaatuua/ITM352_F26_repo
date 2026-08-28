"""
Simple Calculator Program
Performs basic math operations: add, subtract, multiply, divide
Includes error handling for division by zero
"""

def add(x, y):
    """Add two numbers"""
    return x + y


def subtract(x, y):
    """Subtract two numbers"""
    return x - y


def multiply(x, y):
    """Multiply two numbers"""
    return x * y


def divide(x, y):
    """Divide two numbers with error handling"""
    if y == 0:
        raise ValueError("Cannot divide by zero!")
    return x / y


def main():
    """Main function to run the calculator"""
    print("=" * 40)
    print("        Simple Calculator")
    print("=" * 40)
    
    # Get user inputs
    try:
        num1 = float(input("\nEnter first number: "))
        num2 = float(input("Enter second number: "))
    except ValueError:
        print("Error: Please enter valid numbers!")
        return
    
    # Display operation choices
    print("\nChoose an operation:")
    print("1. Add (+)")
    print("2. Subtract (-)")
    print("3. Multiply (*)")
    print("4. Divide (/)")
    
    # Get operation choice
    choice = input("\nEnter operation (1/2/3/4): ")
    
    # Perform calculation based on choice
    try:
        if choice == '1':
            result = add(num1, num2)
            operation = "+"
        elif choice == '2':
            result = subtract(num1, num2)
            operation = "-"
        elif choice == '3':
            result = multiply(num1, num2)
            operation = "*"
        elif choice == '4':
            result = divide(num1, num2)
            operation = "/"
        else:
            print("Error: Invalid choice! Please select 1, 2, 3, or 4.")
            return
        
        # Display result
        print("\n" + "=" * 40)
        print(f"Result: {num1} {operation} {num2} = {result}")
        print("=" * 40 + "\n")
        
    except ValueError as e:
        print(f"\nError: {e}")


if __name__ == "__main__":
    main()
