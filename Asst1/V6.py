# Interactive quiz system, sixth version
# Randomize the order of questions and order of the answer alternatives per question

# Name: Ava Puaatuua
# Date: Oct. 9, 2026

from string import ascii_lowercase
import random

questions = {
    "What is the capital of France? ": ["Paris", "Toulouse", "Lyon", "Marseille"],
    "What is the capital of Germany? ": ["Berlin", "Hamburg", "Munich", "Cologne"],
    "What is the airspeed of an unladen swallow?": ["10", "12", "8", "15"],
    "What is the capital of Italy? ": ["Rome", "Milan", "Naples", "Turin"],
    }

NUM_QUESTIONS_PER_QUIZ = 5

num_questions = min(NUM_QUESTIONS_PER_QUIZ, len(questions))
selected_questions = random.sample(list(questions.items()), k=num_questions)

num_correct = 0

for num, (question, answers) in enumerate(questions.items(), start=1):
    correct_answer = answers[0]
    print(f"\nQuestion {num}: {question}")

    sorted_answers = sorted(answers)
    labeled_answers = dict(zip(ascii_lowercase, sorted_answers))

    for label, answer in labeled_answers.items():
        print(f"{label}. {answer}")
        
    while (answer_label := input("Choice? ").lower()) not in labeled_answers:
        print(f"Invalid choice. Please select one of {', '.join(labeled_answers.keys())}.")

    answer = labeled_answers.get(answer_label)

    if answer == correct_answer:
        print("Correct!")
        num_correct += 1
    else:
        print(f"The answer is '{correct_answer!r}', not {answer!r}.")

print(f"\nYou got {num_correct} out of {len(questions)} correct.")
