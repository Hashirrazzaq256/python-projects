import spotipy
import pprint
from spotipy.oauth2 import SpotifyOAuth

import requests
from bs4 import BeautifulSoup

CLIENT_ID = "f444a2bd51564125bbf2f99eb4a80f2b"
CLIENT_SECRET = "6fb5c1eeca07449bb7843ae0db68f0f7"

date = input("Which year do you want to go back in? Type the date in YYYY-MM-DD format\n")
URL = f"https://www.billboard.com/charts/hot-100/{date}/"
response = requests.get(url=URL)
content = response.text
soup = BeautifulSoup(content, "html.parser")
song_names_spans = soup.select("li ul li h3")
song_names = [song.getText().strip() for song in song_names_spans]
print(song_names)

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private playlist-modify-public",
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
        redirect_uri="https://www.example.org",
        cache_path="token.txt",
    )
)

user_id = sp.current_user()["id"]
songs_urls = []
year = date.split("-")[0]

for song in song_names:
    results = sp.search(f"track:{song}, year:{year}", type="track")
    print(results)
    try:
        url = results["tracks"]["items"][0]["uri"]
        songs_urls.append(url)
    except IndexError:
        print(f"{song} doesn't exist in Spotify, hence skipped")

# Creating playlist using user_id
playlist = sp.user_playlist_create(user=user_id, name=f"{date} Billboard 100", public=True)
sp.playlist_add_items(playlist_id=playlist['id'],items=songs_urls)
