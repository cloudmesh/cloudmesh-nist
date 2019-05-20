import connexion
import six


#from default_controller import *
from swagger_server.models.default import Default  # noqa: E501
from swagger_server import util
from pymongo import MongoClient



client = MongoClient()

db = client['cm']
defaults = db['default']


def get_default():
    """
    :return: list all the defaults as a list
    """
    # ok
    return list(defaults.find({}, {'_id': False}))

def add_default(default=None):
    # ok
    if connexion.request.is_json:
        default = Default.from_dict(default)

    defaults.insert(default.to_dict())
    return default


def get_default_by_name(name):
    # BUG: not yet gaurantiied there is only one name
	for element in defaults.find({'name':name}):
		return (element['name'],
                element['description'],
                element['value'],
                element['kind'])

