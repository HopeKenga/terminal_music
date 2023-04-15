import os
import spotipy
import spotipy.util as util
from dotenv import load_dotenv


# Load the environment file
load_dotenv()

# Authenticate with the Spotify API
username = os.getenv("SPOTIFY_USERNAME")
client_id = os.getenv("SPOTIFY_CLIENT_ID")
client_secret = os.getenv("SPOTIFY_CLIENT_SECRET")
redirect_uri = os.getenv("SPOTIFY_REDIRECT_URI")

scope='user-read-private user-read-playback-state user-modify-playback-state'
token = util.prompt_for_user_token(username, scope, client_id=client_id, client_secret=client_secret, redirect_uri=redirect_uri)
sp = spotipy.Spotify(auth=token)

#play a song
def play_track(track_name):
    results = sp.search(q='track:' + track_name, type='track')
    if results['tracks'] ['items'] :
        tracks_uri = results['tracks']['items'][0]['uri']
        sp.start_playback(uris=[tracks_uri])

#pause a song
def pause_playback():
    sp.pause_playback()

#resume a  song
def resume_playback():
    sp.resume_playback()

#skip to the next song
def next_track():
    sp.next_track()
    
