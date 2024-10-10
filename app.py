from flask import Flask, request, render_template, jsonify
from datetime import date
import requests
import random
from dotenv import load_dotenv
import os

api_key = os.getenv('API_KEY')
host = "ai-translate.p.rapidapi.com"
load_dotenv('.env.local')

def list_all_languages():
    url = "https://deep-translate1.p.rapidapi.com/language/translate/v2/languages"

    headers = {
        "x-rapidapi-key": "06e9fdad13msh0c03b16263635e5p1ffbfejsnb9c6d5478224",
        "x-rapidapi-host": "deep-translate1.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers)
    return response.text

def translatetext(text,l2,l1='en'):
    url = "https://deep-translate1.p.rapidapi.com/language/translate/v2"

    payload = {
        "q": text,
        "source": l1,
        "target": l2
    }
    headers = {
	"x-rapidapi-key": "06e9fdad13msh0c03b16263635e5p1ffbfejsnb9c6d5478224",
	"x-rapidapi-host": "deep-translate1.p.rapidapi.com",
	"Content-Type": "application/json"
    }

    response = requests.post(url, json=payload, headers=headers)
    
    return response.json()


#### Defining Flask App
app = Flask(__name__)

#### Saving Date today in 2 different formats
datetoday = date.today().strftime("%m_%d_%y")
datetoday2 = date.today().strftime("%d-%B-%Y")

#### Our main page
@app.route('/')
def home():
    return render_template('home.html',datetoday2=datetoday2,res='')

@app.route('/translate',methods=['POST'])
def translate():
    input_text = request.form['sourcetext']
    targetlang = request.form['languages']
    res = translatetext(input_text, targetlang, 'en').get('data').get('translations').get('translatedText')
    return render_template('home.html',datetoday2=datetoday2,res=res)

@app.route('/random', methods=['GET'])
def random_phrase():
    phrases = {
    "phrase1": "The sun is shining brightly today.",
    "phrase2": "Coffee is the best way to start the day.",
    "phrase3": "Every day is a new opportunity.",
    "phrase4": "I love exploring new places.",
    "phrase5": "Nature is a beautiful escape.",
    "phrase6": "Reading expands the mind.",
    "phrase7": "Music can heal the soul.",
    "phrase8": "Believe in yourself and all that you are.",
    "phrase9": "Creativity takes courage.",
    "phrase10": "The journey is more important than the destination.",
    "phrase11": "Life is short, make every moment count.",
    "phrase12": "Stay curious and keep learning.",
    "phrase13": "Friendship is a treasure to cherish.",
    "phrase14": "Challenges make us stronger.",
    "phrase15": "Laughter is the best medicine.",
    "phrase16": "Kindness is free, sprinkle that stuff everywhere.",
    "phrase17": "Dream big and dare to fail.",
    "phrase18": "Adventure awaits, go find it."
}


    # Select a random phrase
    random_key = random.choice(list(phrases.keys()))
    random_value = phrases[random_key]

    return jsonify({"phrase": random_value})

#### Our main function which runs the Flask App
if __name__ == '__main__':
    app.run(debug=True)


### HELPFUL COMANDS
#
# To run our app:
# flask --app app.py --debug run
#
# You can also use the following command to run the app:
# flask run
# But this won't restart the server automatically when you make a change in the code. You will have to stop the server and run the command again.


