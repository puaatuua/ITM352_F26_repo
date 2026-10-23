# Save the dictionary of quiz questions to a JSON file

# Name: Ava Puaatuua
# Date: Oct. 23, 2026

import json

questions = {
    "What is the capital of France? ": ["Paris", "Toulouse", "Lyon", "Marseille"],
    "What is the capital of Germany? ": ["Berlin", "Hamburg", "Munich", "Cologne"],
    "What is the airspeed of an unladen swallow?": ["10", "12", "8", "15"],
    "What is the capital of Italy? ": ["Rome", "Milan", "Naples", "Turin"],
    "What is the capital of Texas": ["Austin","San Antonio", "Dallas","Waco"],
    "The Last Supper was painted by which artist": ["Da Vinci","Rembrandt","Picasso","Michelangelo"],
    }

filename = "quiz_questions.json"

# Open the file in write mode and save the dictionary as JSON
with open(filename, "w") as file:
    json.dump(questions, file, indent=4)

print(f"Quiz questions saved to {filename}.")