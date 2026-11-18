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