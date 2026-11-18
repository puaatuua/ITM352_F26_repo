# Application to manage the quiz webapp
# Name: Ava Puaatuua
# Date: Nov. 16, 2026

from flask import Flask, render_template, request, redirect, url_for, session
import json
import random

app = Flask(__name__)
app.secret_key = 'key123'

def load_questions(filepath='questions.json'):
    # Load questions from the questions.json file
    try:
        with open(filepath, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        print(f"Error: {filepath} not found.")
        return {}

def prepare_questions(all_questions, category="All", difficulty="Easy"):
    # Filter questions based on category and difficulty
    filtered = [
        q for q in all_questions
        if q.get("difficulty", "").lower() == difficulty.lower()
        and (category.lower() == "all" or q.get("category", "").lower() == category.lower())
    ]

    # Shuffle question order
    random.shuffle(filtered)

    # Create copies so shuffling options doesn't mutate the original list
    quiz_questions = []
    for q in filtered:
        q_copy = q.copy()
        options_copy = q["options"].copy()
        random.shuffle(options_copy)
        q_copy["options"] = options_copy
        quiz_questions.append(q_copy)

    return quiz_questions

@app.route("/")
def home():
    return render_template("index.html")

@app.route('/quiz', methods=['GET', 'POST'])
def quiz():
    if request.method == 'POST':
        question = session.get('question')

        if question is None:
            return redirect(url_for('quiz'))

        user_answer = request.form.get('answer')

        if not user_answer:
            return redirect(url_for('quiz'))

        correct = user_answer == question['answer']

        feedback = (
            "Correct!"
            if correct
            else f"The correct answer is {question['answer']}."
        )

        return render_template(
            'question_result.html',
            feedback=feedback,
            correct=correct,
            user_answer=user_answer,
            correct_answer=question['answer'],
            explanation=question['explanation']
        )

    all_questions = load_questions()
    quiz_questions = prepare_questions(
        all_questions,
        category="All",
        difficulty="Medium"
    )

    if not quiz_questions:
        return "No matching questions found.", 404

    question = quiz_questions[0]
    session['question'] = question

    return render_template('quiz.html', question=question)

@app.route('/result')
def result():
    # Calculate and display the user's score
    score = 1  # Example score for demonstration
    return render_template('result.html', score=score)

if __name__ == "__main__":
    app.run(debug=True)
