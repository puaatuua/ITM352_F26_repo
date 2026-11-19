# Sports Quiz Web App

A Flask quiz application that lets users select a sports category and difficulty level. Questions are randomized, answers receive difficulty-based points, and the results page shows overall and category-specific scores.

## Features

- Category and difficulty selection
- Randomized questions and answer choices
- Easy, Medium, and Hard difficulty scoring
- Immediate feedback after each answer
- Overall and category score summaries
- HTML templates using Jinja2
- CSS enhancements

## Technologies

- Python
- Flask
- HTML
- CSS
- JavaScript
- Jinja2
- JSON

## Project Structure

```text
Asst3/
├── quiz_webapp.py
├── questions.json
├── scores.json
├── static/
│   ├── style.css
└── templates/
    ├── index.html
    ├── setup.html
    ├── quiz.html
    ├── question_result.html
    └── result.html
```

## Setup Instructions

1. Open a terminal and enter the project folder:

```bash
cd Asst3
```

2. Create and activate a virtual environment:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

3. Install Flask and pytest:

```bash
python3 -m pip install flask pytest
```

4. Start the server:

```bash
python3 quiz_webapp.py
```

5. Open `http://127.0.0.1:5050/`


## Usage

```markdown
## Using the Quiz

1. Open the home page.
2. Select a sports category and difficulty.
3. Choose an answer and submit it.
4. Review the immediate feedback and explanation.
5. Continue through the remaining questions.
6. Review overall and category scores on the results page.

## Scoring

- Easy question: 1 point
- Medium question: 2 points
- Hard question: 3 points

Category totals use the same difficulty-point system.

## REST API

Retrieve questions:

```text
GET /api/questions
GET /api/questions?category=Basketball
GET /api/questions?difficulty=Medium

Retrieve scores:
GET /api/scores

Store a score:
POST /api/scores
Content-Type: applicaiton/json