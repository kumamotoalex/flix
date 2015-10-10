"""Takes in a movie and returns NEW matches by UID"""
import json
from pprint import pprint
with open('players.JSON') as data_file:
    data=json.load(data_file)
def match(movie, matches):#movie is a string; matches is an array of ints (UID's)
    for user in data["Users"]:
        if movie in user["Movies"] and not user["UID"] in matches:
            matches.append(user["UID"])
    return matches
