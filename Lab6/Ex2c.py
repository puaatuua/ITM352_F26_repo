# List of lists containing test inputs for each condition
test_cases = [
    [1, 2, 3],                  # 3 elements -> fewer than 5
    [1, 2, 3, 4, 5],            # 5 elements -> between 5 and 10 (boundary)
    [1, 2, 3, 4, 5, 6, 7],      # 7 elements -> between 5 and 10
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], # 10 elements -> between 5 and 10 (boundary)
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11] # 11 elements -> more than 10
]

# Testing the logic against each case
for test_list in test_cases:
    print(f"Testing list of length {len(test_list)}:")
    if len(test_list) < 5:
        print(" -> The list has fewer than 5 elements.")
    elif len(test_list) <= 10:
        print(" -> The list has between 5 and 10 elements.")
    else:
        print(" -> The list has more than 10 elements.")
    print("-" * 40)