# Part 2: Dictionary Operations
# Create a dictionary for student information (name, age, grade, subjects)

student = {
    "name": "Ava",
    "age": "21",
    "grade": "Senior",
    "subject": "MIS"
}

# Part 3: Dictionary Methods
# keys(): get all keys
print("Keys:", student.keys())

# values(): get all values
print("Values:", student.values())

# items(): get key-value pairs
for key, value in student.items():
    print(f"{key}: {value}")

# get(): safely access a value
print("Name:", student.get("name"))
print("Email:", student.get("email", "Email not available"))

# pop(): remove and return an item
removed_subject = student.pop("subject")
print("Removed subject:", removed_subject)

# update(): add or change multiple items
student.update({
    "age": "22",
    "subject": "Computer Science"
})
print("Updated student:", student)

# clear(): remove all items
# student.clear()
# print("After clear:", student)

# Part 4: Iterating Through Dictionaries
# Create loops to display all information in your dictionary.

# Iterate over keys
for key in student.keys():
    print("Key:", key)

# Iterate over values
for value in student.values():
    print("Value:", value)

# Iterate over key-value pairs
for key, value in student.items():
    print(f"{key}: {value}")

# Keys can also be iterated over directly
for key in student:
    print(f"{key}: {student[key]}")