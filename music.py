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

scope = 'user-read-private user-read-playback-state user-modify-playback-state'
token = util.prompt_for_user_token(
    username, scope, client_id=client_id, client_secret=client_secret, redirect_uri=redirect_uri)
sp = spotipy.Spotify(auth=token)

# Get ID of the first device available

devices = sp.devices()
device_id = None
if devices['devices']:
    device_id = devices['devices'][0]['id']

# play a song


def play_track(track_name):
    results = sp.search(q='track:' + track_name, type='track')
    if results['tracks']['items']:
        tracks_uri = results['tracks']['items'][0]['uri']
        if device_id:
            sp.start_playback(device_id=device_id, uris=[tracks_uri])
        else:
            print("No device available")

#pause a song
def pause_playback():
    sp.pause_playback()

#resume a  song
def resume_playback():
    sp.resume_playback()

#skip to the next song

def next_track():
    sp.next_track()

#Add a play button

import tkinter as tk
from threading import Thread

class MusicPlayerGUI:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Music Player")
        self.window.geometry('300x100')
        self.track_name_entry = tk.Entry(self.window, width=30)
        self.track_name_entry.pack(pady=10)
        self.play_button = tk.Button(self.window, text="Play", command=self.play_track_thread)
        self.play_button.pack(pady=10)

    def play_track_thread(self):
        # Run play_track in a separate thread to avoid blocking the GUI
        Thread(target=self.play_track, args=(self.track_name_entry.get(),)).start()

    def play_track(self, track_name):
        play_track(track_name)   

#start the GUI
gui = MusicPlayerGUI()
gui.window.mainloop()





