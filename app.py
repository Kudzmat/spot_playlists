import spotipy
from spotipy.oauth2 import SpotifyOAuth
from flask import Flask
from dotenv import load_dotenv
import os

load_dotenv()  # load the environment variables

CLIENT_ID = os.getenv('CLIENT_ID')
CLIENT_SECRET = os.getenv('CLIENT_SECRET')
SPOTIFY_REDIRECT_URI = os.getenv('SPOTIFY_REDIRECT_URI')
SPOTIFY_USER_ID = os.getenv('SPOTIFY_USER_ID')

scope = "user-library-read user-top-read playlist-modify-public user-follow-read user-library-read " \
        "playlist-read-private playlist-modify-private "

app = Flask(__name__)
app.secret_key = 'SECRET_KEY'

"""
if __name__ == '__main__':
    app.run(debug=True)
"""

import playlist
