
from dotenv import load_dotenv
import os
load_dotenv()
import requests
import json
from bs4 import BeautifulSoup

g_client_id = os.getenv('g_client_id')
g_client_secret = os.getenv('g_client_secret')
client_id = os.getenv('CLIENT_ID')
client_secret = os.getenv('CLIENT_SECRET')
genius_key = os.getenv('genius_key')




def get_track_names():
    track_names = []
    for song in range(len(playlist['items'])):
        track_names.append(playlist['items'][song]['track']['name'])
    return track_names

def get_track_artists():
    track_artists = []
    for song in range(len(playlist['items'])):
        track_artists.append(playlist['items'][song]['track']['artists'][0]['name'])
    return track_artists

def request_song_info(track_name, track_artist):
    base_url = 'https://api.genius.com'
    headers = {'Authorization': 'Bearer ' + genius_key}
    search_url = base_url + '/search'
    data = {'q': track_name + ' ' + track_artist}
    response = requests.get(search_url, data=data, headers=headers)
    return response

def check_hits():
    json = response.json()
    remote_song_info = None
    for hit in json['response']['hits']:
        if track_artist.lower() in hit['result']['primary_artist']['name'].lower():
            remote_song_info = hit
            break
    return remote_song_info

def get_url():
    song_url = remote_song_info['result']['url']
    return song_url

def scrape_lyrics():
    page = requests.get(song_url)
    html = BeautifulSoup(page.text, 'html.parser')
    lyrics1 = html.find("div", class_="lyrics")
    lyrics2 = html.find("div", class_="Lyrics__Container-sc-1ynbvzw-2 jgQsqn")
    if lyrics1:
        lyrics = lyrics1.get_text()
    elif lyrics2:
        lyrics = lyrics2.get_text()
    elif lyrics1 == lyrics2 == None:
        lyrics = None
    return lyrics

def get_lyrics():
    playlist = GetLyrics.get_playlist_info()
    track_names = GetLyrics.get_track_names()
    track_artists = GetLyrics.get_track_artists()
    song_lyrics = []
    for i in range(len(track_names)):
        print("\n")
        print(f"Working on track {i}.")
        response = GetLyrics.request_song_info(track_names[i],track_artists[i])
        remote_song_info = GetLyrics.check_hits()
        if remote_song_info == None:
            lyrics = None
            print(f"Track {i} is not in the Genius database.")
        else:
            url = GetLyrics.get_url()
            lyrics = GetLyrics.scrape_lyrics()
            if lyrics == None:
                print(f"Track {i} is not in the Genius database.")
            else:
                print(f"Retrieved track {i} lyrics!")
        song_lyrics.append(lyrics)
    return song_lyrics
