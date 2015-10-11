import os 
import datetime
import pymongo
import json
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
		if (user == iterUser["username"]):
			return iterUser["preferences"]
	return 0

#Given an user and a newVector, we change the preference vector of the specified user
#@param user - user who's preference we change
#@param newVector - new preference vector for our specified user
#@return true if we can change the preference vector false otherwise
def changePreference(user, newVector):
	for iterUser in user_collection.find():
		if (user == iterUser["username"]):
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
		if (user == iterUser["username"]):
			return iterUser["address"]
	return 0

#Given an user and a new address string we change the user's address
#@param user - user who's address we want to change
#@param address - new address for the user
#@return 1 if we can change the address 0 otherwise
def changeAddress(user, newAddress):
	for iterUser in user_collection.find():
		if (user == iterUser["username"]):
			user_collection.update(
				{"username" : iterUser["username"]},
				{ "$set" : {"address" : newAddress}},
				upsert = True
				)
			return 1
	return 0

#Given an user, return the array of other users who want to chill
def returnChills(user):
	for iterUser in user_collection.find():
		if (user == iterUser["username"]):
			return iterUser["matches"]
	return 0

#Given an user and an userToAppend, we append the userToAppend to user's matches array
def insertChills(user, userToAppend):
	for iterUser in user_collection.find():
		if (user == iterUser["username"]):
			tempChillArray = iterUser["matches"]
			if (userToAppend in tempChillArray):
				return 0
			else:
				tempChillArray.append(userToAppend)
				user_collection.update(
				{"username" : iterUser["username"]},
				{ "$set" : {"matches" : tempChillArray}},
				upsert = True
				)
				return 1
	return 0

#Returns all members within our database represented as a string array of member usernames
# @return an array of strings
def returnMemberArray():
	returned = []
	for iterUser in user_collection.find():
		returned.append(iterUser["username"])
	return returned

############################################
#ALL METHOD BELOW ARE STRICTLY FOR TESTING!#
############################################
def workWithMemberArray():
	trollAround = returnMemberArray()
	for members in trollAround:
		print(isinstance(members, basestring))
		print(members)
		print(getPreference(members))


def printAll():
	for iterUser in user_collection.find():
		print(iterUser["username"])

def printAllPreferences():
	for iterUser in user_collection.find():
		print(iterUser["preferences"])

def massCreate():
	toAdd = ["james", "john", "rick", "abraham", "erika", "bobby", "ariele", "daniel", "andrew", "margie", "jason", "jay", "edward", "sum", "alex", "bowen"]
	count = 0
	for people in toAdd:
		newUser = {"username" : people, "img" : "img.jpg", "preferences" : [count]}
		addUser(newUser)
		count = count + 1



