# Part 2: The Range Function
# Create loops that count from 1 to 10, count backwards, and count by 2s

print("Counting from 1 to 10:")
for number in range (1,11):
    print(number)

print("Counting backwards from 10 to 1:")
for number in range (10,0,-1):
    print(number)

print("Counting by 2s from 0 to 10:")
for number in range (0,11,2):
    print(number)

# Part 3: Iterating Over Data Structures
# Create loops that process a list of students, a sentence, and a dictionary of grades
students = ["Alice", "Bob", "Charlie", "David"]
grades = {"Alice": 90, "Bob": 85, "Charlie": 92, "David": 88}

print("Iterating over a list of students:")
for student in students:
    print(f'Student: {student}')
    print(f'Grade: {grades[student]}')

# Part 4: While Loops
# Create a guessing game use a while loop
number_to_guess = 5
guess = input("Guess a number between 1 and 10: ")

while int(guess) != number_to_guess:
    print("Wrong! Try again.")
    guess = input("Guess a number between 1 and 10: ")
print("Correct! You guessed the number.")

# Part 5: Loop Control Statements
# Modify your previous loops to demonstrate break and continue

# Part 6: Nested Loops
# Create a multiplication table using nested loops

# Part 7: List Comprehensions
# Convert some of your earlier loops into list comprehensions

# Part 8: Advanced Iteration Techniques
