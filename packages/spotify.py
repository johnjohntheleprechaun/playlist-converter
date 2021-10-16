import requests
from base64 import b64encode

def get_login_url(client_id: str, scope="playlist-modify-public playlist-read-private user-library-read", redirect_uri="https://playlist-converter.johnj.repl.co/login/spotify/callback"):
    url = "https://accounts.spotify.com/authorize?response_type=code&scope={scope}&client_id={id}&redirect_uri={redirect}"
    return url.format(id=client_id, scope=scope, redirect=redirect_uri)

def encode_url(address: str, data: dict):
	url = address + "?"
	for item in data:
		url += "&{key}={value}".format(key=item, value=data[item])
	return url

def get_token(client_id: str, client_secret: str, code: str, redirect_uri: str):
	url_data = {
		"grant_type": "authorization_code",
		"code": code,
		"redirect_uri": redirect_uri,
		"client_id": client_id,
		"client_secret": client_secret
	}

	r = requests.post("https://accounts.spotify.com/api/token?", data=url_data)
	return r.json()