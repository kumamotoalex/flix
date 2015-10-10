#!flask/bin/python
from flask import Flask, request, jsonify
import numpy as np

rest = Flask(__name__)
NUM_MOVIES = 5
NUM_CATEGORIES = 5
PREFERENCE_MATRIX = np.identity(5)

# # CREATE USER - passes in user_name, URL of image
# @rest.route('/makeuser', methods = ['POST'])
# def create_user():
# 	return


# # SEND PREFERENCES
# @rest.route('/sendscore', methods = ['POST'])
# def send_preferences():
# 	return

# # GET PREFERENCES - return URL
@rest.route('/getpreferences/<string:user_name>', methods = ['GET'])
def get_preferences(user_name):
	# QUERY DATABASE

	return 

# # GET MATCHES
@rest.route('/getmatches/<string:user_name>', methods = ['GET'])
def get_matches(user_name):
	# QUERY DATABASE
	r = calculate_score([1,0,0,0,0])
	return str(r).strip('[]')

#Takes in a score list and returns the array of preferences - the 'preference vetor'
def calculate_score(score_list):
	invect = np.array(score_list)
	outvect = PREFERENCE_MATRIX.dot(invect)
	return outvect.tolist()



if __name__ == '__main__':
	rest.run(debug=True)