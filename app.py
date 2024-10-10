from flask import Flask, request, render_template, jsonify
from datetime import date
import requests
import random
from dotenv import load_dotenv
import os

# This loads our apikey from the variable API_KEY in the .env.local file
api_key = os.getenv('API_KEY')
host = "ai-translate.p.rapidapi.com"
load_dotenv('.env.local')

def list_all_languages():
    # We will fill this out in a second
    pass

def translatetext():
    # We will fill this out in a second
    pass


#### Defining Flask App
app = Flask(__name__)

#### Saving Date today in 2 different formats
datetoday = date.today().strftime("%m_%d_%y")
datetoday2 = date.today().strftime("%d-%B-%Y")

#### Our main page

### Our translate page

### Other endpoints

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


