def login_url(client_id: str, scope="playlist-modify-public", redirect_uri="https://localhost:5000/login/spotify/callback"):
    url = "https://accounts.spotify.com/authorize?response_type=code&scope={scope}&client_id={id}&redirect_uri={redirect}"
    return url.format(id=client_id, scope=scope, redirect=redirect_uri)