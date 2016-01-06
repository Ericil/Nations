import utils
form flask import FLask, render_template, request, redirect, url_for
app = Flask(__name__)
@app.route("/")
def intro():

@app.route("/login", methods = ["GET", "POST"])
def login:

@app.route("/play/<username>", methods = ["GET", "POST"])
def play:

if __name__ = "__main__":
    app.debug = True
    app.run()
