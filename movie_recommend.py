import requests

def get_telugu_movies():
    api_key = "70296e194b4c20b4df37bef25ab934c7"  # Your actual TMDB API Key
    url = f"https://api.themoviedb.org/3/discover/movie?api_key={api_key}&with_original_language=te"

    headers = {
        "Content-Type": "application/json"
    }

    response = requests.get(url, headers=headers).json()

    if "results" in response:
        return [movie["title"] for movie in response["results"][:5]]
    else:
        return [f"API Error: {response.get('status_message', 'Unknown error')}"]
