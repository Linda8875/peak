import requests
import json
from spotifyclient import *



def genre():
    return ['Rock', 'Soul', 'Pop', 'Classical', 'Rap', 'Jazz', 'Hip Hop', 'Folk', 'Funk', 'Country', 'Techno', 'House']

def decade():
    return ["1920's", "1930's", "1940's","1950's","1960's", "1970's", "1980's", "1990's", "2000's", "2010's", "2020's"]

def track():
    return ['123 - abc', '456 - def', '789 - ghi', 'other']

def length():
    return ['30', '60', '90']

def popularity():
    return ['Not Popular', 'Less Popular', 'Popular']

def pl_name():
    base_url = 'https://api.spotify.com/v1/me/playlists'
    headers = {'Authorization': 'Bearer ' + authorization_token}
    response = requests.get(url=base_url,headers=headers)
    pl_names = [li['name'] for li in response.json()['items']]
    return pl_names

if __name__ == '__main__':
    genre()
