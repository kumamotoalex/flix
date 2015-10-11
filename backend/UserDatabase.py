import os 
import datetime
import pymongo
from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.user_database
user_collection = db.user_collection

#Adds an user to our Mongo Database
#@param user - user to add to our database, must be a python dictionary
#@return void there is no return
def addUser(user):
	toAdd = user
	append_id = user_collection.insert(user)


#Given an user, we return his or her preference vector
#@param user - user who's preference vector we want to receive
#@return the preference vector for the given user 0 if the user is not in our database
def getPreference(user):
	for iterUser in user_collection.find():
		if (user["username"] == iterUser["username"]):
			return iterUser["preferences"]
	return 0

#Given an user and a newVector, we change the preference vector of the specified user
#@param user - user who's preference we change
#@param newVector - new preference vector for our specified user
#@return true if we can change the preference vector false otherwise
def changePreference(user, newVector):
	for iterUser in user_collection.find():
		if (user["username"] == iterUser["username"]):
			user_collection.update(
				{"username" : iterUser["username"]},
				{ "$set" : {"preferences" : newVector}},
				upsert = True
				)
			return 1
	return 0
 
#Given an user we will return his address as a string
#@param user - user who's address we want
#@return string - the address of the user's current location or 0 if the user is not in our database
def returnAddress(user):
	for iterUser in user_collection.find():
		if (user["username"] == iterUser["username"]):
			return iterUser["address"]
	return 0

#Given an user and a new address string we change the user's address
#@param user - user who's address we want to change
#@param address - new address for the user
#@return 1 if we can change the address 0 otherwise
def changeAddress(user, newAddress):
	for iterUser in user_collection.find():
		if (user["username"] == iterUser["username"]):
			user_collection.update(
				{"username" : iterUser["username"]},
				{ "$set" : {"address" : newAddress}},
				upsert = True
				)
			return 1
	return 0




