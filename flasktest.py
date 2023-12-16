from flask import Flask

# saying flask that everything it needs to run the app is in here
app = Flask(__name__)

@app.route("/")
def index():
    return "Started Learning Flask now!!"

# by telling it to run at 0.0.0.0 we are specifying it to run at all addresses.
app.run(host="0.0.0.0", port=8000)