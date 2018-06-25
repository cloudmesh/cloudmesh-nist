import connexion
import six


#from alias_controller import *
from swagger_server.models.alias import Alias  # noqa: E501
from swagger_server import util
from pymongo import MongoClient



client = MongoClient()

db = client['cm']
aliass = db['alias']


def get_alias():
    """
    :return: list all the aliass as a list
    """
    # ok
    return list(aliass.find({}, {'_id': False}))

def add_alias(alias=None):
    # ok
    if connexion.request.is_json:
        alias = Alias.from_dict(alias)

    aliass.insert(alias.to_dict())
    return alias


def get_alias_by_name(name):
    # BUG: not yet gaurantiied there is only one name
	for element in aliass.find({'name':name}):
		return (element['name'],
                element['description'],
                element['value'],
                element['kind'])

