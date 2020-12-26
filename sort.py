
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import os
from dotenv import load_dotenv
import os
load_dotenv()
client_id = os.environ.get('CLIENT_ID')
client_secret = os.environ.get('CLIENT_SECRET')
user_id = os.environ.get('user_id')
authorization_token = os.environ.get('authorization_token')

sp_lib_read = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id= client_id,
                                               client_secret=client_secret,
                                               redirect_uri="https://linda-playlists.herokuapp.com/", #replace with our website url
                                               scope="user-library-read"))


def get_saved_tracks():
    results = sp_lib_read.current_user_saved_tracks(limit=50)
    for idx, item in enumerate(results['items']):
        track = item['track']
        last_50_saved_tracks = idx, track['artists'][0]['name'], " – ", track['name']
        return last_50_saved_tracks


