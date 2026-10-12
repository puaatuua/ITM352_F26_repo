'''
Interactive quiz system, final version
Loads questions from a JSON file, randomly selects questions, displays randomized answer choices,
and keeps track of the user's score.

The program also writes the history of scores out to a file
And adds explanations for why the correct answer is the correct answer.

Name: Ava Puaatuua
Date: Oct. 11, 2026
'''

from string import ascii_lowercase # Provides a string of lowercase letters for labeling answer choices
import random # Selects and shuffles questions and answer choices
import json # Reads questions from questions.json file

# Opens questions.json in read mode and loads the questions into the questions variable
question_file = open("questions.json", "r")
questions = json.load(question_file)

# Sets the number of questions to be asked in the quiz
NUM_QUESTIONS_PER_QUIZ = 5

# Selects random questions from the questions dictionary, up to the number specified by NUM_QUESTIONS_PER_QUIZ
def prepare_questions(questions, num_questions):
    num_questions = min(num_questions, len(questions))
    return random.sample(list(questions.items()), k=num_questions)

# Creates a dictionary that pairs letters with answer choices
def get_answer(question, alternatives):
    labeled_answers = dict(zip(ascii_lowercase, alternatives)) # zip() combines lowercase letters with answer choices

    for label, answer in labeled_answers.items():
        print(f"{label}. {answer}")

    # Asks the user for an answer until they enter a valid label (a, b, c, etc.)    
    while (answer_label := input("Choice? ").lower()) not in labeled_answers:
        print(f"Invalid choice. Please select one of {', '.join(labeled_answers.keys())}.")

    return labeled_answers[answer_label]

# Asks a question, checks the answer, and returns 1 if correct, 0 if incorrect
def ask_question(question, alternatives):    
    correct_answer = alternatives[0]
    ordered_alternatives = random.sample(alternatives, k=len(alternatives))
    answer = get_answer(question, ordered_alternatives)

    # Returning a score for the question, 1 for correct, 0 for incorrect
    if answer == correct_answer:
        print("Correct!")
        return 1
    else:
        print(f"The answer is '{correct_answer!r}', not {answer!r}.")
        return 0


# Main program logic starts here
questions = prepare_questions(questions, NUM_QUESTIONS_PER_QUIZ)

# Score starts at zero
num_correct = 0

# Main quiz loop
for num, (question, answers) in enumerate(questions, start=1):
    print(f"\nQuestion {num}: {question}")
    num_correct += ask_question(question, answers)

# Print the final score
print(f"\nYou got {num_correct} correct.")
