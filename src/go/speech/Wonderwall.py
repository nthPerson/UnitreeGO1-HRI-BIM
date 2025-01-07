import spotipy
from spotipy.oauth2 import SpotifyOAuth
import time
import os
from spotipy.cache_handler import CacheFileHandler

# Your Spotify API credentials
SPOTIPY_CLIENT_ID = '2b6c88a3086a404284d8a37081fbb129'
SPOTIPY_CLIENT_SECRET = '14b91a7c484c457c9dffddaf5428d477'
SPOTIPY_REDIRECT_URI = 'http://localhost:8888/callback'

# Set up cache handler
cache_path = ".spotify_cache"
cache_handler = CacheFileHandler(cache_path=cache_path)

# Set up authentication manager with cache handler
auth_manager = SpotifyOAuth(
    client_id=SPOTIPY_CLIENT_ID,
    client_secret=SPOTIPY_CLIENT_SECRET,
    redirect_uri=SPOTIPY_REDIRECT_URI,
    scope="user-modify-playback-state user-read-playback-state",
    open_browser=False,
    cache_handler=cache_handler
)

# Try to get a valid token
token_info = auth_manager.get_cached_token()

if not token_info:
    # If there's no valid token, we need to get one
    auth_url = auth_manager.get_authorize_url()
    print(f"Please go to this URL and authorize the app: {auth_url}")
    response = input("Enter the URL you were redirected to: ")
    code = auth_manager.parse_response_code(response)
    token_info = auth_manager.get_access_token(code)

# Create Spotify client
sp = spotipy.Spotify(auth_manager=auth_manager)

# Test the connection
user = sp.current_user()
print(f"Authentication successful. Logged in as: {user['display_name']}")

# Function to play a specific track
def play_specific_track(track_uri):
    try:
        # Get available devices
        devices = sp.devices()
        if not devices['devices']:
            print("No active Spotify devices found. Please open Spotify on a device.")
            return
        
        # Use the first available device
        device_id = devices['devices'][0]['id']
        
        # Play the specific track
        sp.start_playback(device_id=device_id, uris=[track_uri])
        track_info = sp.track(track_uri)
        print(f"Now playing: {track_info['name']} by {track_info['artists'][0]['name']} from the album {track_info['album']['name']}")
    except spotipy.exceptions.SpotifyException as e:
        print(f"Spotify API Error: {e}")
        if 'Premium required' in str(e):
            print("This feature requires a Spotify Premium account.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Main execution
if __name__ == "__main__":
    wonderwall_uri = "spotify:track:1qPbGZqppFwLwcBC1JQ6Vr"
    play_specific_track(wonderwall_uri)