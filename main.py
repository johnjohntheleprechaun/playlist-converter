from flask import Flask, render_template, redirect, request
from packages import spotify
import os

CLIENT_ID = os.environ["client_id"]
CLIENT_SECRET = os.environ["client_secret"]
REDIRECT_URI = os.environ["redirect_uri"]

app = Flask(__name__)

@app.route("/")
def homepage():
    return render_template('homepage/index.html') #Return the homepage HTML

@app.route("/login")
def login():
    return "Work in progress..."

@app.route("/login/spotify")
def spotify_login(): #get user authorization code in order to get access token
	url_data = {
		"client_id": CLIENT_ID,
		"redirect_uri": REDIRECT_URI,
		"response_type": "code"
	}
	url = spotify.encode_url("https://accounts.spotify.com/authorize", url_data) #Encode the URL with the data objects
	return redirect(url)

@app.route("/login/spotify/callback", methods=["GET", "POST"])
def callback():
	code = request.args.get('code') #Extract code from GET request
	token = spotify.get_token(CLIENT_ID, CLIENT_SECRET, code, REDIRECT_URI) #Get access token from spotify
	return token

app.run("0.0.0.0")