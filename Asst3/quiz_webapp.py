# Application to manage the quiz webapp
# Name: Ava Puaatuua
# Date: Nov. 16, 2026

from flask import Flask, render_template, request, redirect, url_for
import json

def load_questions():
    # Load questions from the questions.json file
    with open("questions.json", "r") as question_file:
        return json.load(question_file)


app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route('/quiz', methods=['GET', 'POST'])
def quiz():
    if request.method == 'POST':
        # Logic to capture the user’s answers and redirect to the result page
        return redirect(url_for('result'))
    # Load the question and options to display
    return render_template('quiz.html')  # Displays the question and options

@app.route('/result')
def result():
    # Calculate and display the user's score
    score = 1  # Example score for demonstration
    return render_template('result.html', score=score)

if __name__ == "__main__":
    app.run(debug=True)
