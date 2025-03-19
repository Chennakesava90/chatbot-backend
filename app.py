from flask import Flask, request, jsonify
from flask_cors import CORS
from chatbot import get_bot_response
from movie_recommend import get_telugu_movies
from song_recommend import get_telugu_songs

app = Flask(__name__)
CORS(app)

@app.route('/chat', methods=['POST'])
def chat():
    data = request.json
    user_message = data.get("message")

    if "movie" in user_message.lower():
        movies = get_telugu_movies()
        return jsonify({"response": "Here are some Telugu movies:\n" + "\n".join(movies)})

    elif "song" in user_message.lower():
        songs = get_telugu_songs()
        return jsonify({"response": "Here are some Telugu songs:\n" + "\n".join(songs)})

    else:
        response = get_bot_response(user_message)
        return jsonify({"response": response})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
