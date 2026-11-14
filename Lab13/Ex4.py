# Use Flask to create a "skeleton" of the quiz game.

# Name: Ava Puaatuua
# Date: Nov. 13, 2026

from flask import Flask, render_template, request

app = Flask(__name__)

QUESTIONS = [
    {
        "question": "Which NFL quarterback holds the record for the most Super Bowl wins?",
        "choices": ["Tom Brady", "Joe Montana", "Peyton Manning", "John Elway"],
        "answer": "Tom Brady",
    },
    {
        "question": "Which city's NFL team is nicknamed the 'Cheeseheads' by their fans?",
        "choices": ["Green Bay (Packers)", "Chicago (Bears)", "Minnesota (Vikings)", "Detroit (Lions)"],
        "answer": "Green Bay (Packers)",
    },
    {
        "question": "How many points is a touchdown worth in American football?",
        "choices": ["6", "7", "8", "3"],
        "answer": "6",
    },
    {
        "question": "What is the name of the trophy awarded to the NFL Super Bowl champion?",
        "choices": ["Vince Lombardi Trophy", "Pete Rozelle Trophy", "Lamar Hunt Trophy", "George Halas Trophy"],
        "answer": "Vince Lombardi Trophy",
    },
    {
        "question": "In what year was Super Bowl I played?",
        "choices": ["1967", "1968", "1969", "1970"],
        "answer": "1967",
    },
    {
        "question": "Which team plays its home games at Lambeau Field?",
        "choices": ["Green Bay Packers", "Los Angeles Rams", "Baltimore Ravens", "Seattle Seahawks"],
        "answer": "Green Bay Packers",
    },
    {
        "question": "In what year did the AFL and NFL officially merge into a single league?",
        "choices": ["1970", "1966", "1980", "1990"],
        "answer": "1970",
    }
]



@app.route("/")
def home():
    return render_template("quiz.html", question=QUESTIONS[0], question_number=1)


@app.route("/answer", methods=["POST"])
def answer():
    selected_answer = request.form.get("answer")
    correct_answer = QUESTIONS[0]["answer"]

    if selected_answer == correct_answer:
        result = "Correct!"
    else:
        result = "Incorrect."

    return render_template("result.html", result=result)


if __name__ == "__main__":
    app.run(debug=True)
