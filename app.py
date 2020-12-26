'''imports'''
from flask import Flask, redirect, url_for, render_template, request, session
from function import genre, decade, track, length, popularity
from werkzeug.datastructures import ImmutableMultiDict
from dotenv import load_dotenv
import os
load_dotenv()


#client_id = os.environ.get('CLIENT_ID')
#client_secret = os.environ.get('CLIENT_SECRET')
#user_id = os.environ.get('user_id')
#redirect_uri = os.environ.get('SPOTIPY_REDIRECT_URI')

client_id = os.getenv('CLIENT_ID')
client_secret = os.getenv('CLIENT_SECRET')
user_id = os.getenv('user_id')
redirect_uri = os.getenv('SPOTIPY_REDIRECT_URI')
genius_key = os.getenv('genius_key')
g_client_id = os.getenv('g_client_id')
g_client_secret = os.getenv('g_client_secret')

from createplaylist import *
from spotifyclient import *


'''instance flask web application'''
app = Flask(__name__)
app.secret_key = "qsdfghjklm"

'''define pages on app'''

@app.route("/page_player_pres", methods=["POST","GET"])
def playlist_pres():
    widget = session.get('playlist_id_widget')
    genre = session.get('genre')
    decade = session.get('decade')
    length = session.get('length')
    popularity = session.get('popularity')
    playlist_name = session.get('playlist_name')
    return render_template("page_player_pres.html", widget=widget, genre=genre, decade=decade, length=length, popularity=popularity, playlist_name=playlist_name)

@app.route("/page_player", methods=["POST","GET"])
def page_player():
    widget = session.get('playlist_id_widget')
    genre = session.get('genre')
    decade = session.get('decade')
    length = session.get('length')
    popularity = session.get('popularity')
    playlist_name = session.get('playlist_name')
    return render_template("page_player.html", widget=widget, genre=genre, decade=decade, length=length, popularity=popularity, playlist_name=playlist_name)

@app.route("/error", methods=["POST","GET"])
def error():
    return render_template("error.html")


@app.route("/", methods=["POST","GET"])
def center():
    genres = genre()
    decades = decade()
    tracks = track()
    lengths = length()
    popularities = popularity()
    return render_template("center.html", genres=genres, decades=decades, tracks = tracks, lengths = lengths, popularities = popularities)


@app.route("/algo_input", methods=["POST","GET"])
def algo_input():
    if request.method == "POST":
        req = request.form
        genre, decade, length, popularity, playlist_name = req.values()
        #specify function to input front-end and return html page
        if filter_data(genre, decade, length, popularity) is False:
            return redirect("/error")
        playlist_id = get_playlist_id(playlist_name)
        session['playlist_id_widget'] = playlist_id
        session['genre'] = genre
        session['decade'] = decade
        session['length'] = length
        session['popularity'] = popularity
        session['playlist_name'] = playlist_name
        add_items_to_playlist(genre, decade, length, popularity, playlist_name, playlist_id)
        return redirect("/page_player")

    return render_template("error.html")

@app.route("/karaoke", methods=["POST","GET"])
def get_lyrics():
    session['playlist_id_widget']= playlist_id
    songs = GetLyrics(client_id, client_secret, user_id,playlist_id, genius_key)
    song_lyrics = songs.get_lyrics()
    return song_lyrics


'''run app'''
if __name__ == "__main__":
    app.run(debug=False)

