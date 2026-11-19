# Application to manage the quiz webapp
# Name: Ava Puaatuua
# Date: Nov. 16, 2026

from flask import Flask, render_template, request, redirect, url_for, session
from flask import jsonify
from datetime import datetime
from pathlib import Path
import json
import random

app = Flask(__name__)
app.secret_key = 'key123'

SCORE_FILE = Path(app.root_path) / "scores.json"

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
    # Handle the case where the json file is not found    
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



def load_scores():
    if not SCORE_FILE.exists():
        return []

    try:
        with open(SCORE_FILE, "r", encoding="utf-8") as file:
            content = file.read()

            if not content.strip():
                return []

            return json.loads(content)

    except json.JSONDecodeError:
        print(f"Error: {SCORE_FILE} contains invalid JSON.")
        return []



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

    # Handle form submission
    if request.method == "POST":
        category = request.form["category"]
        difficulty = request.form["difficulty"]

        # Filter questions based on selected category and difficulty
        filtered_questions = [
            question for question in all_questions
            if question["category"].lower() == category.lower()
            and question["difficulty"].lower() == difficulty.lower()
        ]

        if not filtered_questions:
            return "No questions matched these options.", 400

        random.shuffle(filtered_questions) # Shuffle the filtered questions

        session["questions"] = filtered_questions # Store the filtered questions in the session
        session["question_index"] = 0 # Track the current question index
        session["score"] = 0 # Initialize the score to 0

        session["category_scores"] = {category: 0}

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
        session["score_saved"] = False  # Initialize the score saved flag

        return redirect(url_for("quiz")) # Redirect to the quiz page after setting up the session

    return render_template(
        "setup.html",
        categories=categories,
        difficulties=["Easy", "Medium", "Hard"]
    )



@app.route('/quiz', methods=['GET', 'POST'])
def quiz():
    # Handle POST request when the user submits an answer
    if request.method == 'POST':
        # Retrieve the previously displayed question from the session
        question = session.get('question')
        user_answer = request.form.get('answer')
        correct = user_answer == question['answer']

        if correct:
            points = DIFFICULTY_POINTS[question['difficulty']]

            # Update the overall score
            session["score"] = session.get("score", 0) + points

            category = question['category']
            # Update the category scores
            category_scores = session.get("category_scores", {})
            category_scores[category] = category_scores.get(category, 0) + points
            session["category_scores"] = category_scores

        session['question_index'] = session.get('question_index', 0) + 1 # Advance the question index
        is_finished = session['question_index'] >= len(session['questions'])
        # If the quiz is finished, redirect to the result page
        if is_finished:
            return redirect(url_for('result'))
        # Otherwise, set the next question in the session
        session['question'] = session['questions'][session['question_index']]

        return render_template(
            'question_result.html',
            correct=correct,
            user_answer=user_answer,
            correct_answer=question['answer'],
            explanation=question['explanation']
        )

    # Handle GET request when the user accesses the quiz page
    if 'questions' not in session:
        all_questions = load_questions()
        session['questions'] = prepare_questions(
            all_questions,
            category="All",
            difficulty="Medium"
        )
        session['question_index'] = 0
        session['score'] = 0

    question_index = session['question_index'] # Get the current question index from the session
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
    # Read values from the session to display the final results
    score = session.get("score", 0)
    total = session.get("difficulty_total", 0)
    category_scores = session.get("category_scores", {})
    category_totals = session.get("category_totals", {})

    if not session.get("score_saved", False):
        # Load existing scores from the scores.json file
        scores = load_scores()

        # Append the new score with timestamp
        scores.append({
            "timestamp": datetime.now().isoformat(),
            "category": session.get("category"),
            "difficulty": session.get("difficulty"),
            "score": score,
            "total": total,
            "category_scores": category_scores,
            "category_totals": category_totals
        })

        with open(SCORE_FILE, 'w', encoding="utf-8") as file:
            json.dump(scores, file, indent=2)

        session["score_saved"] = True  # Mark the score as saved to prevent duplicates

    # Pass the values to Jinja
    return render_template(
        "result.html",
        score=score,
        total=total,
        category_scores=category_scores,
        category_totals=category_totals
    )



@app.route("/api/questions", methods=["GET"])
def api_questions():
    questions = load_questions()

    category = request.args.get("category")
    difficulty = request.args.get("difficulty")

    if category:
        questions = [
            question for question in questions
            if question["category"].lower() == category.lower()
        ]

    if difficulty:
        questions = [
            question for question in questions
            if question["difficulty"].lower() == difficulty.lower()
        ]

    public_questions = [
        {
            "question": question["question"],
            "options": question["options"],
            "category": question["category"],
            "difficulty": question["difficulty"]
        }
        for question in questions
    ]

    return jsonify(public_questions)



@app.route("/api/scores", methods=["GET"])
def api_get_scores():
    return jsonify(load_scores())


@app.route("/api/scores", methods=["POST"])
def api_store_score():
    data = request.get_json(silent=True)

    if not data:
        return jsonify({"error": "JSON data is required"}), 400

    score = data.get("score")
    total = data.get("total")

    if not isinstance(score, int) or not isinstance(total, int):
        return jsonify({
            "error": "score and total must be integers"
        }), 400

    if total < 1 or score < 0 or score > total:
        return jsonify({"error": "Invalid score"}), 400

    scores = load_scores()

    entry = {
        "timestamp": datetime.now().isoformat(),
        "score": score,
        "total": total
    }

    scores.append(entry)

    with open(SCORE_FILE, "w", encoding="utf-8") as file:
        json.dump(scores, file, indent=2)

    return jsonify(entry), 201



if __name__ == "__main__":
    app.run(debug=True, port=5050) # Use port 5050 to avoid conflicts with other applications
