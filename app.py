from flask import Flask, session, Response, jsonify
from flask_bootstrap import Bootstrap
from flask import render_template
from flask import request
#from pymongo import MongoClient
#from collections import defaultdict
#from random import randrange
#from sys import exc_info

#import plyplus
#import re
#import glob
import json
#import codediff
#import datetime
#import dateutil.parser
#from urllib import urlencode 
#from urllib import quote_plus

#import pprint

#pretty printer config
#pp = pprint.PrettyPrinter(indent=2)

app = Flask(__name__)
app.secret_key = 'abc'
Bootstrap(app)
DEBUG = True

# Initialize the database connection
#DB_HOST = 'localhost'
#DB_PORT = 27017
#db_client = MongoClient(DB_HOST,DB_PORT)

#=======================================================
# Colors / Tone dictionary 
#=======================================================
# Steve Zieverink 2004
music_color = {'C':'bcdf39','C#':'149032','D':'1b9081','D#':'1b0d82','E':'7f087c','F':'d71386','F#':'6e0d45','G':'a00c08','G#':'fa0b0c','A':'f78010','A#':'ecf086','B':'f5f43c'}
 
#Newton -> D.D. Jameson
music_color = {'C':('fa0a0c',261.63),'C#':('f44712',277.18),'D':('f78010',293.66),'D#':('f4d23b',311.13),'E':('f5f43b',329.63),'F':('149033',349.23),'F#':('1b9081',369.99),'G':('1c0d82',392.0),'G#':('4b0e7d',415.3),'A':('7f087c',440.0),'A#':('a61586',466.16),'B':('d71386',493.88)}

music_color = [('C','#fa0a0c',261.63),('C#','#f44712',277.18),('D','#f78010',293.66),('D#','#f4d23b',311.13),('E','#f5f43b',329.63),('F','#149033',349.23),('F#','#1b9081',369.99),('G','#1c0d82',392.0),('G#','#4b0e7d',415.3),('A','#7f087c',440.0),('A#','#a61586',466.16),('B','#d71386',493.88)]
#music_color = {'C':'fa0a0c','C#':'f44712','D':'f78010','D#':'f4d23b','E':'f5f43b','F':'149033','F#':'1b9081','G':'1c0d82','G#':'4b0e7d','A':'7f087c','A#':'a61586','B':'d71386'}

#=======================================================
# Views 
#=======================================================
@app.route('/all_notes')
def all_notes():
    """All colors/tones available for testing"""
    
    return render_template('all_notes.html',colors=music_color,)
    #return response

@app.route('/guess_notes')
def guess_notes():
    """Guessing notes layout """
    
    return render_template('guess_notes.html',colors=music_color,)
    #return response

#=======================================================
# Start the web service on the local host
#=======================================================
if __name__ == "__main__":
    app.run(host='0.0.0.0',debug=True,port=5010)
