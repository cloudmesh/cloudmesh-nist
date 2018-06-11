import connexion
import six
import uuid

#from profile_controller import *
from swagger_server.models.profile import Profile  # noqa: E501
from swagger_server import util
from pymongo import MongoClient
# Connect to the MongoDB, change the connection string per your MongoDB environment
client = MongoClient(port=27017)
# Set the db object to point to the business database
db=client.profiles
# Showcasing the count() method of find, count the total number of 5 ratings


def get_profile_by_uuid(uuid):
    """get_profile_by_uuid
    Returns a general description of a user  # noqa: E501
    :param uuid: uuid of user
    :type id: str
    :rtype: PROFILE
    """
    item = get_profile_by_uuid_mongo(uuid)
    return Profile(item[0],item[1],item[2],item[3],item[4],item[5],item[6],item[7])
def profiles_get():  # noqa: E501
    """profiles_get

    Returns a list of general description of users  # noqa: E501

    :rtype: List[PROFILE]
    """
    listOfProfile = []
    items = get_profile()
    for element in items:
        listOfProfile.append(Profile(element[0],
                                     element[1],
                                     element[2],
                                     element[3],
                                     element[4],
                                     element[5],
                                     element[6],
                                     element[7]))
    return listOfProfile

def get_profile():
	l = list()
	for element in db.Profile.find():
		l.append((element['uuid'], 
                  element['username'], 
                  element['context'],
                  element['description'],
                  element['firstname'],
                  element['lastname'],
                  element['publickey'],
                  element['email']))
	return l

def get_profile_by_uuid_mongo(uuid):
	for element in db.Profile.find({'uuid':uuid}):
		return (element['uuid'], 
                element['username'], 
                element['context'],
                element['description'],
                element['firstname'],
                element['lastname'],
                element['publickey'],
                element['email'])

def add_profile_mongo(uuid, username,context,description,firstname, lastname,publickey):
	db.Profile.insert({"uuid":uuid, 
                       "username":username,
                       "context":context, 
                       "description":description, 
                       "firstname":firstname, 
                       "lastname":lastname,
                       "publickey":publickey,
                       "email":"gregor@iu.edu"})
	return "add a new profile successfully"

def add_profile(profile=None):
    print (profile)
    uuid = str(uuid.uuid4())
    if connexion.request.is_json:
        profile = Profile.from_dict(connexion.request.get_json())
    print (profile)
    return profile
