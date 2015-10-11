#!flask/bin/python
from flask import Flask, request, jsonify, abort
import numpy as np

rest = Flask(__name__)
NUM_MOVIES = 5
NUM_CATEGORIES = 5
NUM_MATCHES = 1
PREFERENCE_MATRIX = np.identity(5)
PREFERENCE_DICT = {'Forrest Gump':0, 'Frozen':1, 'Star Wars':2, 'Parent Trap':3,'The Notebook':4}

# ----------------WORK AROUND DATABASE---------------------
database = [
    {
        'username': 'kevinj',
        'imgurl': 'images/kevinj.jpeg',
        'preferences': [0,1,1,0,1] 
    },
    {
        'username': 'abrahaml',
        'imgurl': 'images/abrahaml.jpeg',
        'preferences': [1,0,0,1,0] 
    }
]
# ---------------------------------------------------------


# # CREATE USER - passes in user_name, URL of image
@rest.route('/makeuser', methods = ['POST'])
def create_user():
	# CREATE NEW USER
	zerolist = []
	for i in range(0, NUM_MOVIES):
		zerolist.append(0)

	user = {
        'username': request.json['username'],
        'imgurl': request.json['imgurl'],
        'preferences': zerolist
    }
 #    # SEND INFO TO DATABASE
	database.append(user)

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
	for x in database:
		if x['username'] == u:
			x['preferences'] = v
			return jsonify({'score': v}), 201
	abort(404)
	# return jsonify({'mild success':'yay'}), 201
	

# # GET PREFERENCES - return PREFERENCES, URL
@rest.route('/getpreferences/<string:username>', methods = ['GET'])
def get_preferences(username):
	# QUERY DATABASE FOR PREFERENCES in return
	for x in database:
		if x['username'] == username:
			return jsonify({'preferences': x['preferences']})
	abort(404)

# # GET MATCHES
@rest.route('/getmatches/<string:username>', methods = ['GET'])
def get_matches(username):
	# QUERY DATABASE FOR PREFERENCE VECTOR, CALCULATE MAX CORRELATION
	results = {}
	returnjson = []
	p = None
	for x in database:
		if x['username'] == username:
			p = numpy.array(x['preferences'])
	for y in database:
		if y['username'] != username:
			comparison = numpy.array(y['preferences'])
			results[y['username']] = comparison.dot(p)
	# Put the top results into returnjson
	for i in range(0,NUM_MATCHES):
		name = max(stats.iteritems(), key=operator.itemgetter(1))[0]
		returnjson.append(name)
		results.pop(name)

	return jsonify({'matches':returnjson})

# # Takes in a score list and returns the array of preferences - the 'preference vetor'
def calculate_score(score_list):
	invect = np.array(score_list)
	outvect = PREFERENCE_MATRIX.dot(invect)
	return outvect.tolist()



if __name__ == '__main__':
	rest.run(debug=True)