# Application to manage the quiz webapp
# Name: Ava Puaatuua
# Date: Nov. 16, 2026

from flask import Flask, render_template, request, redirect, url_for, session
import json
import random

app = Flask(__name__)
app.secret_key = 'key123'

DIFFICULTY_POINTS = {
    "Easy": 1,
    "Medium": 2,
    "Hard": 3
}

def load_questions(filepath='questions.json'):
    # Load questions from the questions.json file
    try:
        with open(filepath, 'r') as file:
            return json.load(file)
    # Handle the case where the file is not found    
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

@app.route("/setup", methods=["GET", "POST"])
def setup():
    all_questions = load_questions()

    categories = sorted({
        question["category"]
        for question in all_questions
    })

    if request.method == "POST":
        category = request.form["category"]
        difficulty = request.form["difficulty"]

        filtered_questions = [
            question for question in all_questions
            if question["category"].lower() == category.lower()
            and question["difficulty"].lower() == difficulty.lower()
        ]

        if not filtered_questions:
            return "No questions matched these options.", 400

        random.shuffle(filtered_questions)

        session["questions"] = filtered_questions
        session["question_index"] = 0
        session["score"] = 0

        session["category_scores"] = {
            category: 0
        }

        session["category_totals"] = {
            category: sum(
                DIFFICULTY_POINTS[question["difficulty"]]
                for question in filtered_questions
            )
        }

        session["difficulty_total"] = sum(
            DIFFICULTY_POINTS[question["difficulty"]]
            for question in filtered_questions
        )

        session["category"] = category
        session["difficulty"] = difficulty

        return redirect(url_for("quiz"))

    return render_template(
        "setup.html",
        categories=categories,
        difficulties=["Easy", "Medium", "Hard"]
    )

@app.route('/quiz', methods=['GET', 'POST'])
def quiz():
    if request.method == 'POST':
        question = session.get('question')

        user_answer = request.form.get('answer')
        correct = user_answer == question['answer']

        if correct:
            points = DIFFICULTY_POINTS[question['difficulty']]

            session["score"] = session.get("score", 0) + points

            category = question['category']
            category_scores = session.get("category_scores", {})
            category_scores[category] = category_scores.get(category, 0) + points
            session["category_scores"] = category_scores

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

@app.route("/result")
def result():
    score = session.get("score", 0)
    total = session.get("difficulty_total", 0)
    category_scores = session.get("category_scores", {})
    category_totals = session.get("category_totals", {})

    return render_template(
        "result.html",
        score=score,
        total=total,
        category_scores=category_scores,
        category_totals=category_totals
    )

if __name__ == "__main__":
    app.run(debug=True, port=5050)
