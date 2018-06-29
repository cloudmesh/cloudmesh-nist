import connexion
import six


#from flavor_controller import *
from swagger_server.models.flavor import Flavor  # noqa: E501
from swagger_server import util
from pymongo import MongoClient



client = MongoClient()

db = client['cm']
flavors = db['flavor']


def get_flavor():
    """
    :return: list all the flavors as a list
    """
    # ok
    return list(flavors.find({}, {'_id': False}))

def add_flavor(flavor=None):
    # ok
    if connexion.request.is_json:
        flavor = Flavor.from_dict(flavor)

    flavors.insert(flavor.to_dict())
    return flavor


def get_flavor_by_name(name):
    # BUG: not yet gaurantiied there is only one name
	for element in flavors.find({'name':name}):
		return (element['name'],
                element['description'],
                element['value'],
                element['kind'])

