#!flask/bin/python
from flask import Flask, request, jsonify
import numpy as np

rest = Flask(__name__)
NUM_MOVIES = 5
NUM_CATEGORIES = 5
PREFERENCE_MATRIX = np.identity(5)
PREFERENCE_DICT = {'Forrest Gump':0, 'Frozen':1}

# # CREATE USER - passes in user_name, URL of image
@rest.route('/makeuser', methods = ['POST'])
def create_user():
	# CREATE NEW USER
	zerolist = []
	for i in range(0, NUM_MOVIES):
		zerolist.append(0)
	user = {
        'username': request.json['username'],
        'imgurl': request.json['title'],
        'preferences': zerolist
    }
    # SEND INFO TO DATABASE


	return jsonify({'user': user}), 201


# # SEND PREFERENCES
@rest.route('/sendscore', methods = ['POST'])
def send_preferences():
	# WHAT WE NEED TO BE SENT
	u = request.json['username']
	m = request.json['movie_likes']
	d = request.json['movie_dislikes']
	s = []
	for i in range(0, NUM_MOVIES):
		s.append(0)
	for x in m:
		s[PREFERENCE_DICT[x]] = 1
	for x in d:
		s[PREFERENCE_DICT[x]] = -1
	v = calculate_score(s)
	# PUT VECTOR INTO MONGO DATABASE

	return jsonify({'score': v}), 201

# # GET PREFERENCES - return PREFERENCES, URL
@rest.route('/getpreferences/<string:username>', methods = ['GET'])
def get_preferences(username):
	# QUERY DATABASE FOR PREFERENCES



	return 

# # GET MATCHES
@rest.route('/getmatches/<string:username>', methods = ['GET'])
def get_matches(username):
	# QUERY DATABASE FOR PREFERENCE VECTOR, CALCULATE MAX CORRELATION
	return

# # Takes in a score list and returns the array of preferences - the 'preference vetor'
def calculate_score(score_list):
	invect = np.array(score_list)
	outvect = PREFERENCE_MATRIX.dot(invect)
	return outvect.tolist()



if __name__ == '__main__':
	rest.run(debug=True)