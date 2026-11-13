# Create a simple HTML Flask application that displays a welcome message

# Name: Ava Puaatuua
# Date: Nov. 12, 2026

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "Welcome to Ava’s website!"

if __name__ == '__main__':
    app.run(debug=True)
