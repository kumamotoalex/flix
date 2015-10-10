from flask import Flask, request, jsonify

rest = Flask(__name__)
NUM_MOVIES = 
NUM_CATEGORIES = 
PREFERENCE_MATRIX = 

# CREATE USER
@rest.route('/makeuser', methods = ['POST'])
def create_user():

# SEND PREFERENCES
@rest.route('/sendscore', methods = ['POST'])
def send_preferences():

# GET PREFERENCES
@rest.route('/getpreferences/<int:user_id>', methods = ['GET'])
def get_preferences():

# GET MATCHES
@rest.route('/getmatches/<int:user_id>', methods = ['GET'])
def get_matches():

if __name__ == 'main':
	rest.run(debug=True)