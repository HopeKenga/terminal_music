import spotipy
import spotipy.util as util
from dotenv import as load_dotenv

# Load the environment file
load_dotenv()

# Authenticate with the Spotify API
username = os.getenv("SPOTIFY_USERNAME")
client_id = os.getenv("SPOTIFY_CLIENT_ID")
client_secret = os.getenv("SPOTIFY_CLIENT_SECRET")
redirect_uri = os.getenv("SPOTIFY_REDIRECT_URI")

scope='user-read-private user-read-playback-state user-modify-playback-state'
token=util.prompt_for_user_token(username, scope, client_id=client_id, client_secret=client_secret, redirect_uri=redirect_uri)


