from flask import Flask, request, jsonify

app = Flask(__name__)

# Home Route (Main Page)
@app.route("/", methods=["GET"])
def home():
    return jsonify({"message": "Welcome to the Telugu Movie & Song Chatbot API!"})

# Chatbot Route (Main Functionality)
@app.route("/chat", methods=["POST"])
def chat():
    data = request.json
    user_message = data.get("message", "").lower()

    if "movie" in user_message:
        return jsonify({"response": "Here are some Telugu movies: RRR, Baahubali, Pushpa, KGF"})
    elif "song" in user_message:
        return jsonify({"response": "Here are some Telugu songs: Srivalli, Naatu Naatu, Butta Bomma"})
    else:
        return jsonify({"response": "I can recommend Telugu movies and songs!"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
