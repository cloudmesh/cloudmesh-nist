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

