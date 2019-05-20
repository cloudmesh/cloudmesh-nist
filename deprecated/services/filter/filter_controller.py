import connexion
import six


#from filter_controller import *
from swagger_server.models.filter import Filter  # noqa: E501
from swagger_server import util
from pymongo import MongoClient



client = MongoClient()

db = client['cm']
filters = db['filter']


def get_filter():
    """
    :return: list all the filters as a list
    """
    # ok
    return list(filters.find({}, {'_id': False}))

def add_filter(filter=None):
    # ok
    if connexion.request.is_json:
        filter = Filter.from_dict(filter)

    filters.insert(filter.to_dict())
    return filter


def get_filter_by_name(name):
    # BUG: not yet gaurantiied there is only one name
	for element in filters.find({'name':name}):
		return (element['name'],
                element['description'],
                element['value'],
                element['kind'])

