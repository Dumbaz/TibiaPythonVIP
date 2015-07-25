from flask import Flask, request, json
from html_getter import get_url
from character_parser import parse_single_char as parse_char 
import datetime
import config
import sqlite3

# Configuration of the Flask App
DATABASE = '/tmp/tibiatest.db'
DEBUG = True
SECRET_KEY = 'some_secret_key'

app = Flask(__name__)
app.config.from_object(__name__)

tibia_url = 'https://secure.tibia.com/community/?subtopic=characters&name={0}'

def db_connect():
    sqlite3.connect(app.config['DATABASE'])

@app.route('/get_character', methods=['GET','POST'])
def get_character_by_name():
    char_arg = request.args['character']
    char_html = get_url(tibia_url.format(char_arg.replace(" ", '+')))
    char = parse_char(char_html)
    char_json = json.dumps(char)
    print(char_json)
    return char_json

if __name__ == "__main__":
    app.run()
