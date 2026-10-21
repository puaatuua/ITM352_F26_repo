# Part 3: Writing Files
# Create programs that write different types of data to files.


with open('Part3_output.txt', "w", encoding="utf-8") as file:
    file.write("First line\n")
    file.write("Second line\n")
    file.write("Third line\n")

number = 15
with open('Part3_output.txt', "a", encoding="utf-8") as file:
    file.write(f"Appending a number: {number}\n")

list = ["Item 1", "Item 2", "Item 3"]
with open('Part3_output.txt', "a", encoding="utf-8") as file:
    file.write("Appending a list:\n")
    for item in list:
        file.write(f"{item}\n")

try:
   with open("Part3_output.txt", "x", encoding="utf-8") as file:
       file.write("This file was created safely.\n")
except FileExistsError:
   print("The file already exists.")
