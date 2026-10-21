# Part 4: File Modes and Context Managers
# Rewrite your file operations using with statements.

# Writing to a file without using 'with' statement
file = open('Part4_output.txt', 'w', encoding='utf-8')
file.write("This is the first line.\n")

# Writing to a file using 'with' statement
with open('Part4_output.txt', 'w', encoding='utf-8') as file:
    file.write("This is the first line.\n")
    file.write("This is the second line.\n")

