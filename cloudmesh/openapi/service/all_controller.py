services/keystore/keystore_controller.py
import connexion
import six


#from key_controller import *
from swagger_server.models.key import Key  # noqa: E501
from swagger_server import util
from pymongo import MongoClient



client = MongoClient()

db = client['cm']
keys = db['key']


def get_key():
    """
    :return: list all the keys as a list
    """
    # ok
    return list(keys.find({}, {'_id': False}))

def add_key(key=None):
    # ok
    if connexion.request.is_json:
        key = Key.from_dict(key)

    keys.insert(key.to_dict())
    return key


def get_key_by_name(name):
    # BUG: not yet gaurantiied there is only one name
	for element in keys.find({'name':name}):
		return (element['name'],
                element['description'],
                element['value'],
                element['kind'])

services/profile/profile_controller.py
import connexion
import six
import uuid

#from profile_controller import *
from swagger_server.models.profile import Profile  # noqa: E501
from swagger_server import util
from pymongo import MongoClient



client = MongoClient()

db = client['cm']
profiles = db['profile']



def get_profile():
    """
    :return: list all the profiles as a list
    """
    # ok
    return list(profiles.find({}, {'_id': False}))


def add_profile(profile=None):
    # ok
    uid = str(uuid.uuid4())
    profile["uuid"] = uid
    if connexion.request.is_json:
        profile = Profile.from_dict(profile)

    profiles.insert(profile.to_dict())
    """
    db.Profile.insert({"uuid": profile.uuid,
                       "username": profile.username,
                       "context": profile.context,
                       "description": profile.description,
                       "firstname": profile.firstname,
                       "lastname": profile.lastname,
                       "publickey": profile.publickey,
                       "email": profile.email})
    """
    return profile





def get_profile_by_uuid(uuid):
    # BUG: does not gurantee more than one with same uuid
    """get_profile_by_uuid
    Returns a general description of a user  # noqa: E501
    :param uuid: uuid of user
    :type id: str
    :rtype: PROFILE
    """
    for element in profiles.find({'uuid': uuid}):
        return (element['uuid'],
                element['username'],
                element['context'],
                element['description'],
                element['firstname'],
                element['lastname'],
                element['publickey'],
                element['email'])


    return Profile(element[0],
                   element[1],
                   element[2],
                   element[3],
                   element[4],
                   element[5],
                   element[6],
                   element[7])

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



