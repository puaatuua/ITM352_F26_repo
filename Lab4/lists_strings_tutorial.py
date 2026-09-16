# Part 2: List Operations and Methods

favorite_movies = ["Spider-Man", "Inception", "The Matrix", "Interstellar", "The Dark Knight"] # List of five favorite movies
favorite_movies.append("The Lord of the Rings")  # Adding a new movie to the list
favorite_movies.insert(2, "Pulp Fiction")  # Inserting a movie at index 2
favorite_movies.remove("Inception")  # Removing a movie from the list
favorite_movies.pop()  # Removing the last movie from the list
favorite_movies.sort()  # Sorting the list of favorite movies in alphabetical order
favorite_movies.reverse()  # Reversing the order of the list
print(favorite_movies)  # Display the updated list of favorite movies

# Part 3: List Indexing and Slicing
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

# Indexing practice
print(numbers[0]) # Get the first item
print(numbers[-1]) # Get the last item
print(numbers[5]) # Get the item at index 5
print(numbers[-3]) # Get the third item from the end

# Slicing practice
print(numbers[0:5]) # Get the first five items
print(numbers[-5:]) # Get the last five items
print(numbers[3:8]) # Get items from index 3 to 7
print(numbers[5:]) # Get items from index 5 to the end
print(numbers[:10]) # Get items from the start to index 9
print(numbers[0::2]) # Get all even indexed items
print(numbers[1::2]) # Get all odd indexed items
print(numbers[::-1]) # Get all items in reverse order
print(numbers[-10::-1]) # Get the last ten items in reverse order
print(numbers[15:4:-1]) # Get items from index 15 to 5 in reverse order
print(numbers[::]) # Get all items in the list

# Part 4: String Fundamentals

# Example personal information
name = "John Doe"
email = "john.doe@example.com"
phone_number = "123-456-7890"
city = "New York"
birth_year = "1990"

# Practice exercises
print(name.upper()) # Print the person's name in uppercase
print(email.lower()) # Print the person's email in lowercase
address = "   123 Example Street   "
print(address.strip()) # Remove the extra spaces from the address string
print(name.split()) # Split the name into a list of first and last name
first_name = name.split()[0] # Get the first name from the split list
print(f"{first_name}.{birth_year}") # Create a username by combining the first name and birth year

# Assessment Challenge

# Store a list of student names
student_names = ["Alice", "Bob", "Charlie", "David", "Eva"]

# Store a list of their grades
student_grades = [85, 92, 78, 90, 88]

# Use string formatting to display each student's information
print("Student Information:")

for name, grade in zip(student_names, student_grades):
    print(f"Name: {name}, Grade: {grade}")

# Demonstrate list sorting and manipulation
student_names.sort()  # Sort the student names alphabetically
print("\nSorted Student Names:")
print(student_names)

student_names.insert(2, "Frank")  # Insert a new student name at index 2
print(student_names)

# Show the difference between lists and tuples with examples
list_example = ["red", "blue", "green"]
list_example.append("yellow")
list_example[0] = "purple"
print("List Example:", list_example)

# A tuple cannot be modified
tuple_example = ("red", "blue", "green")

print("\nTuple example:")
print(tuple_example)
