# Create a simple Flask app to retrieve memes from the meme API.
# Present the meme and the meme source (subreddit) to the user. Refresh the meme every 10 seconds.

# Name: Ava Puaatuua
# Date: Nov. 12, 2026

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():