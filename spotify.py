import requests

def login_url(client_id: str, scope="playlist-modify-public", redirect_uri="http://raspberrypi.local:5000/login/spotify/callback"):
    url = "https://accounts.spotify.com/authorize?response_type=code&scope={scope}&client_id={id}&redirect_uri={redirect}"
    return url.format(id=client_id, scope=scope, redirect=redirect_uri)

def get_playlist(id: str, token: str):
    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json",
        "Authorization": "Bearer {}".format(token)
    }
    r = requests.get("https://api.spotify.com/v1/me/playlists", headers=headers)
    return r.json()