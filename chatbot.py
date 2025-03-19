from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

# Initialize ChatBot
chatbot = ChatBot('TeluguBot')

# Train the chatbot with basic conversations
trainer = ChatterBotCorpusTrainer(chatbot)
trainer.train("chatterbot.corpus.english")

# Function to get chatbot response
def get_bot_response(user_input):
    response = chatbot.get_response(user_input)
    return response.text
