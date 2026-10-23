# Read a file of quiz questions and save as a dictionary

# Name: Ava Puaatuua
# Date: Oct. 23, 2026

import json
filename = "quiz_questions.json"
with open(filename, "r") as file:
    questions = json.load(file)

print(questions)
