# Interactive quiz system, third version
# Make QUESTIONS a dictionary, to include multiple answer options and 
# an indication of the correct option

# Name: Ava Puaatuua
# Date: Oct. 8, 2026

questions = {
    "What is the capital of France? ": ["Paris", "Toulouse", "Lyon", "Marseille"],
    "What is the capital of Germany? ": ["Berlin", "Hamburg", "Munich", "Cologne"],
    "What is the capital of Italy? ": ["Rome", "Milan", "Naples", "Turin"],
    }

for question, answers in questions.items():
    correct_answer = answers[0]
    for answer in answers:
        print(f"- {answer}")
        
    answer = input(f"{question} ")
    if answer == correct_answer:
        print("Correct!")
    else:
        print(f"The answer is '{correct_answer}', not {answer!r}.")