from flask import Flask, render_template, redirect, request
from spotify import login_url

app = Flask(__name__)

@app.route("/")
def hello():
    return render_template('homepage/index.html')

@app.route("/test")
def test():
    return "redirect succesful"

@app.route("/login")
def login():
    return "SUCCESS"

@app.route("/login/spotify")
def spotify():
    return redirect(login_url("953baf82d4a7400b8c509a3aa39288d6"))

@app.route("/login/spotify/callback", methods=["GET", "POST"])
def callback():
	access_code = request.args.get('code')
	return "ummmm"

app.run("0.0.0.0")