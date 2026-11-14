# Create a simple Flask app to retrieve memes from the meme API.
# Present the meme and the meme source (subreddit) to the user. Refresh the meme every 10 seconds.

# Name: Ava Puaatuua
# Date: Nov. 12, 2026

from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route('/')
def home():
    url = "https://meme-api.com/gimme/wholesomememes"

    response = requests.get(url)
    response_json = response.json()

    meme = response_json["url"]
    meme_source = response_json["subreddit"]

    return render_template("meme.html", meme=meme, meme_source=meme_source)
