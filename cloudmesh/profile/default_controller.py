import connexion
import six
#from profile_controller import *
from swagger_server.models.profile import PROFILE  # noqa: E501
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
    return PROFILE(item[0],item[1],item[2],item[3],item[4],item[5],item[6],item[7])
def profiles_get():  # noqa: E501
    """profiles_get

    Returns a list of general description of users  # noqa: E501

    :rtype: List[PROFILE]
    """
    listOfProfile = []
    items = get_profile()
    for each in items:
        listOfProfile.append(PROFILE(each[0],each[1],each[2],each[3],each[4],each[5],each[6],each[7]))
    return listOfProfile

def get_profile():
	l = list()
	for each in db.Profile.find():
		l.append((each['uuid'], each['username'], each['context'],each['description'],each['firstname'],each['lastname'],each['publickey'],each['email']))
	return l

def get_profile_by_uuid_mongo(uuid):
	for each in db.Profile.find({'uuid':uuid}):
		return (each['uuid'], each['username'], each['context'],each['description'],each['firstname'],each['lastname'],each['publickey'],each['email'])

def add_profile_mongo(uuid, username,context,description,firstname, lastname,publickey):
	db.Profile.insert({"uuid":uuid, "username":username,"context":context, "description":description, "firstname":firstname, "lastname":lastname, "publickey":publickey,"email":"yy@iu.edu"})
	return "add a new profile successfully"


def add_profile(uuid, username,context,description,firstname, lastname,publickey, email):
	return PROFILE(uuid,username,context,description,firstname,lastname,publickey,email)
