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

        user_answer = request.form.get('answer')
        correct = user_answer == question['answer']

        if correct:
            session['score'] = session.get('score', 0) + 1

        session['question_index'] = session.get('question_index', 0) + 1
        is_finished = session['question_index'] >= len(session['questions'])

        if is_finished:
            return redirect(url_for('result'))

        session['question'] = session['questions'][session['question_index']]

        return render_template(
            'question_result.html',
            correct=correct,
            user_answer=user_answer,
            correct_answer=question['answer'],
            explanation=question['explanation']
        )

    if 'questions' not in session:
        all_questions = load_questions()
        session['questions'] = prepare_questions(
            all_questions,
            category="All",
            difficulty="Medium"
        )
        session['question_index'] = 0
        session['score'] = 0

    question_index = session['question_index']
    questions = session['questions']

    if question_index >= len(questions):
        return redirect(url_for('result'))

    session['question'] = questions[question_index]

    return render_template(
        'quiz.html',
        question=session['question']
    )

@app.route('/result')
def result():
    score = session.get('score', 0)
    total = len(session.get('questions', []))

    session.pop('questions', None)
    session.pop('question_index', None)
    session.pop('question_index', None)
    session.pop('score', None)

    return render_template(
        'result.html',
        score=score,
        total=total
    )

if __name__ == "__main__":
    app.run(debug=True)
