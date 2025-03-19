import requests

def get_telugu_songs():
    api_url = f"https://itunes.apple.com/search?term=telugu&entity=song&limit=5"
    response = requests.get(api_url).json()
    songs = [song['trackName'] for song in response['results']]
    return songs
