#!flask/bin/python
from flask import Flask, request, jsonify, abort
from flask.ext.cors import CORS
import numpy as np
import operator
import UserDatabase
import prefmatrix

rest = Flask(__name__)
NUM_MOVIES = 10
CORS(rest)

NUM_CATEGORIES = 10
NUM_MATCHES = 1
PREFERENCE_MATRIX = prefmatrix.generate_prefmatrix()
PREFERENCE_DICT = {'Forrest_Gump':0, 'Frozen':1, 'Star_Wars':2, 'Parent_Trap':3,'The_Notebook':4, 'Harry_Potter':5, 'Bat_Man':6, 'Finding_Nemo':7, 'The_Hangover':8, 'Inception':9}
INDEX_DICT = {0:'Forrest_Gump', 1:'Frozen', 2:'Star_Wars', 3:'Parent_Trap',4:'The_Notebook', 5:'Harry_Potter', 6:'Bat_Man', 7:'Finding_Nemo', 8:'The_Hangover', 9:'Inception'}

# ----------------WORK AROUND DATABASE---------------------
database = [
    {
        'username': 'obama',
        'imgurl': '../img/obama.jpg',
        'preferences': [0,1,1,0,1,0,0,0,0,0] 
    },
    {
        'username': 'oskibear',
        'imgurl': '../img/oski.jpg',
        'preferences': [1,0,0,1,0,0,0,0,0,0] 
    }
]
# ---------------------------------------------------------

# # GET NOT RATED
@rest.route('/getnotrated/<string:username>', methods = ['GET'])
def get_not_rated(username):
	result = []
#  # GET INFO FROM DATABASE
	# for x in database:
	# 	if x['username'] == username:
	# 		s = x['preferences']
	# 		break
	s = UserDatabase.getPreference(username)
	i = 0
	while i < NUM_MOVIES:
		if s[i] == 0:
			result.append({"title":INDEX_DICT[i],
			               "url":"../img/"+INDEX_DICT[i] + ".jpg"})
		i += 1

	return jsonify({"notRated": result})

# # RESET A USER
@rest.route('/resetuser/<string:username>', methods = ['GET'])
def reset_user(username):
	zerolist = []
	for i in range(0, NUM_MOVIES):
		zerolist.append(0)

#  # SEND INFO TO DATABASE
	# for x in database:
	# 	if x['username'] == username:
	# 		x['preferences'] = zerolist
	# 		return jsonify({'user': x['preferences']})
	# abort(404)
	UserDatabase.changePreference(username, zerolist)
	return jsonify({'user': UserDatabase.getPreference(username)})

# # CREATE USER - passes in user_name
@rest.route('/makeuser', methods = ['POST'])
def create_user():
	# CREATE NEW USER
	zerolist = []
	for i in range(0, NUM_MOVIES):
		zerolist.append(0)

	user = {
	       'username': request.json['username'],
	       'imgurl': "../img/default.jpg",
	       'preferences': zerolist
	   }
	a = {
        'username': request.json['username'],
        'imgurl': "../img/default.jpg",
        'preferences': zerolist
    }
 #    # SEND INFO TO DATABASE
	UserDatabase.addUser(user)

	return jsonify({'user': a}), 201


# # SEND PREFERENCES
@rest.route('/sendscore', methods = ['POST'])
def send_preferences():
	# WHAT WE NEED TO BE SENT
	print(request.data)
	print(request.args)
	u = request.json['username']
	m = request.json['movie_likes']
	d = request.json['movie_dislikes']
	s = []
	
	s = UserDatabase.getPreference(u)
	# for x in database:
	# 	if x['username'] == u:
	# 		s = x['preferences']
	# 		break

	for x in m:
		s[PREFERENCE_DICT[x]] = 1
	for x in d:
		s[PREFERENCE_DICT[x]] = -1

	# PUT VECTOR INTO MONGO DATABASE
	# for x in database:
	# 	if x['username'] == u:
	# 		x['preferences'] = s
	# 		return jsonify({'score': s}), 201
	# abort(404)
	UserDatabase.changePreference(u, s)
	return jsonify({'score': UserDatabase.getPreference(s)})
	

# # # GET PREFERENCES - return PREFERENCES, URL -DEPRECATED
# @rest.route('/getpreferences/<string:username>', methods = ['GET'])
# def get_preferences(username):
# 	# QUERY DATABASE FOR PREFERENCES in return
# 	for x in database:
# 		if x['username'] == username:
# 			return jsonify({'preferences': x['preferences']})
# 	abort(404)

# # GET MATCHES
@rest.route('/getmatches/<string:username>', methods = ['GET'])
def get_matches(username):
	# QUERY DATABASE FOR PREFERENCE VECTOR, CALCULATE MAX CORRELATION - MUST CALCULATE SCORE FIRST FROM PREFERENCE VECTOR!!!!!!!!!!!!!!!!!!
	results = {}
	returnjson = []
	scorev = calculate_score(UserDatabase.getPreference(username))
	p = np.array(scorev)
	# for x in database:
	# 	if x['username'] == username:
	# 		p = np.array(x['preferences'])
	dbnames = UserDatabase.returnMemberArray()
	for y in dbnames:
		if y != username:
			comparison = np.array(calculate_score(UserDatabase.getPreference(y)))
			results[y] = comparison.dot(p)
	# # Put the top results into returnjson
	for i in range(0,NUM_MATCHES):
		name = max(results.items(), key=operator.itemgetter(1))[0]
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
