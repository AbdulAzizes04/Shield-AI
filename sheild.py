from flask import Flask, request, jsonify
import random
import re
import urllib.parse
import requests
from flask_cors import CORS
import urllib.parse
app = Flask(__name__)
CORS(app)
def google_search(query):
    search_url = f"https://www.google.com/search?q={urllib.parse.quote(query)}"
    return f'<a href="{search_url}" target="_blank">Search Google for "{query}"</a>'


def get_response(user_input):
    responses = {
        "hello": ["Hello! What is your name?", "Hi, what is your name?"],
        "what about you?": ["I am Sheild, a voice-assistant chatbot.", "I am Sheild."],
        "sheild can i ask you something":["yaah!,you may ask anything ..."],
        "can i ask you something":["yaah!,you may ask anything ..."],
        "what about you": ["I am Sheild, a voice-assistant chatbot.", "I am Sheild."],
        "tell about you": ["I am Sheild, a voice-assistant chatbot.", "I am Sheild."],
        "tell me about yourself": ["I am Sheild, a voice-assistant chatbot.", "I am Sheild."],
        "hi": ["Hello! What is your name?", "Hi, what is your name?"],
        "hey": ["Hello! What is your name?", "Hi, what is your name?"],
        "good morning": ["Good morning! What is your name?"],
        "good afternoon": ["Good afternoon! What is your name?"],
        "good evening": ["Good evening! What is your name?"],
        "good night": ["Good night! What is your name?"],
        "how are you": ["I am doing great, how about you?"],
        "i am good": ["Nice to hear that!", "Good to hear that!"],
        "i am fine": ["Nice to hear that!", "Good to hear that!"],
        "i am okay": ["Nice to hear that!", "Good to hear that!"],
        "i am bad": ["I am sorry to hear that!"],
        "i am sad": ["I am sorry to hear that!"],
        "i am happy": ["Nice to hear that!", "Good to hear that!"],
        "can you help me": ["Yes, I can help you. What do you need help with?"],
        "what can you do": ["I can help you in many ways. Just ask me anything."],
        "who invented you": ["I was created by a team of developers Azizes.Shaik and Dharma Teja Varma."],
        "who are your creator": ["I was created by a team of developers Azizes.Shaik and Dharma Teja Varma."],
        "who created you": ["I was created by a team of developers Azizes.Shaik and Dharma Teja Varma."],
        "who are your developer": [" i was created by a team of developers Azizes.Shaik and Dharma Teja Varma."],
        "who is your developer": [" i was created by a team of developers Azizes.Shaik and Dharma Teja Varma."],
        "why were you created": ["I was created to help people in many ways."],
        "what is your purpose": ["I was created to help people in many ways."],
        "what is your goal": ["I was created to help people in many ways."],
        "why you created":["i was created to help people in many ways."],
        "great": ["Nice to hear that!", "Good to hear that!"],
        "introduce yourself": ["I am Sheild, a voice-assistant chatbot."],
        "how are you?": ["I am doing great, how about you?"],
        "i am fine": ["Nice to hear that!"],
        "what is special in you": ["I am a chatbot, I can help you in many ways."],
        "what is your name": ["My name is Sheild."],
        "what is your age": ["I am a chatbot, I don't have an age."],
        "what is (a+b)^2": ["a^2 + b^2 + 2ab"],
        "what is (a-b)^2": ["a^2 + b^2 - 2ab"],
        "what is (a+b)(a-b)": ["a^2 - b^2"],
        "what is your favorite color": ["I like pink color."],
        "what is your fav color": ["I like pink color."],
        "what is your favorite food": ["I like biryani."],
        "what is your favorite game": ["I like cricket."],
        "what is your fav movie": ["I like Bahubali, Bahubali 2, Jersey, and many others depending on my mood."],
        "what is your fav food": ["I like biryani."],
        "what is your fav game": ["I like cricket."],
        "what is your favorite movie": ["I like Bahubali, Bahubali 2, Jersey, and many others depending on my mood."],
        "can you suggest me a good movie to watch": ["Bahubali", "Dangal", "3 Idiots", "Kabir Singh", "RRR", "Avengers"],
    }
    
    user_input = user_input.lower()
    match = re.match(r"my name is (.+)", user_input)
    if match:
        return f"Hello {match.group(1)}, how are you today?"
    
    if user_input in responses:
        return random.choice(responses[user_input])
    else:
        return google_search(user_input)

@app.route("/", methods=["GET"])
def home():
    return "Welcome to the Chatbot API!"

@app.route("/chat", methods=["POST"])
def chat():
    user_message = request.json.get("message")
    return jsonify({"response": get_response(user_message)})

if __name__ == "__main__":
    app.run(port=5000, debug=True)
