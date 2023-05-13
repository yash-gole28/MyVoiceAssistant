import requests

import webbrowser

from assistant import *

# Set up text-to-speech engine


def play_song(song_name):
    # Use YouTube Music API to search for the song and retrieve the video ID
    
    search_url = 'https://www.googleapis.com/youtube/v3/search'
    search_params = {
        'key': "AIzaSyCFguM8nuQ0c7t63aYDuQMq5cNYcOy-a5E",
        'q': song_name,
        'part': 'id',
        'type': 'video',
        'maxResults': 1
    }
    response = requests.get(search_url, params=search_params)
    results = response.json()
    video_id = results['items'][0]['id']['videoId']

    # Use webbrowser to open the YouTube Music video in a new tab with autoplay
    webbrowser.open_new_tab(f'https://music.youtube.com/watch?v={video_id}&autoplay=1')

    # Use text-to-speech to provide feedback to the user





# https://console.cloud.google.com/ = site for api key
