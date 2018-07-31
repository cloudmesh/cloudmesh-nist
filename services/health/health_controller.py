import connexion
import six


#from health_controller import *
from swagger_server.models.health import Health  # noqa: E501
from swagger_server import util
from pymongo import MongoClient



client = MongoClient()

db = client['cm']
healths = db['health']


def get_health():
    """
    :return: list all the healths as a list
    """
    # ok
    return list(healths.find({}, {'_id': False}))

def add_health(health=None):
    # ok
    if connexion.request.is_json:
        health = Health.from_dict(health)

    healths.insert(health.to_dict())
    return health


def get_health_by_name(name):
    # BUG: not yet gaurantiied there is only one name
	for element in healths.find({'name':name}):
		return (element['name'],
                element['description'],
                element['value'],
                element['kind'])

