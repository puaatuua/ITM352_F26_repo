# Flask tutorial

# Name: Ava Puaatuua
# Date: Nov. 12, 2026

from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, World."

@app.route("/about")
def about():
    return "<h1>About this app</h1>"

@app.route("/contact")
def contact():
    return "<h1>Contact us at example@email.com</h1>"

@app.route("/user/<username>")
def greet_user(username):
    return render_template("hello.html", username=username)

