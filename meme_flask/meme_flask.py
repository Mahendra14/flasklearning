from flask import Flask, render_template
import requests
import json

app = Flask(__name__)

def get_meme():
    url = "https://meme-api.herokuapp.com/gimme"
    response = json.loads(requests.request("GET",url).text)
    memel = response["preview"][-2]
    subreddit = response["subreddit"]
    return memel, subreddit


@app.route("/")
def index():
    meme_pic, subreddit = get_meme()
    return render_template("meme_index.html",meme_pic=meme_pic, subreddit=subreddit)
    # return "Started Learning Flask now!!"

app.run(host="0.0.0.0", port=8000)