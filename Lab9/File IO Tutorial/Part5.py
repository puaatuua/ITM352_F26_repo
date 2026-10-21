# Part 5: Working with CSV Files
# Create a CSV file with student data and practice reading/writing it

# Writing CSV manually
students = [
    ["name", "age", "grade"],
    ["Alice", 20, "A"],
    ["Bob", 22, "B"],
    ["Charlie", 21, "C"]
]

with open("students.csv", "w", encoding="utf-8") as file:
    for row in students:
        file.write(",".join(map(str, row)) + "\n")

# Reading CSV manually
with open("students.csv", "r", encoding="utf-8") as file:
    for line in file:
        print(line.strip().split(","))

# Reading CSV with the csv module
import csv

with open("students.csv", "r", encoding="utf-8") as file:
    reader = csv.reader(file)
    print("\nReading CSV using csv module:")
    for row in reader:
        print(row)

# Reading rows as dictionaries
with open("students.csv", "r", newline="", encoding="utf-8") as file:
    reader = csv.DictReader(file)
    print("\nReading CSV as dictionaries:")
    for row in reader:
        print(row)

# Writing CSV with csv.writer
with open("students.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["name", "age", "grade"])
    writer.writerow(["David", 23, "A"])
    writer.writerow(["Eva", 20, "B"])

# Writing CSV with csv.DictWriter
with open("students.csv", "w", newline="", encoding="utf-8") as file:
    fieldnames = ["name", "age", "grade"]
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerow({"name": "Frank", "age": 21, "grade": "C"})
    writer.writerow({"name": "Grace", "age": 22, "grade": "B"})

