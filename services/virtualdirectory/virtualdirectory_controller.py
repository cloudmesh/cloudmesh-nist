import connexion
import six


#from virtualdirectory_controller import *
from swagger_server.models.virtualdirectory import Virtualdirectory  # noqa: E501
from swagger_server import util
from pymongo import MongoClient



client = MongoClient()

db = client['cm']
virtualdirectorys = db['virtualdirectory']


def get_virtualdirectory():
    """
    :return: list all the virtualdirectorys as a list
    """
    # ok
    return list(virtualdirectorys.find({}, {'_id': False}))

def add_virtualdirectory(virtualdirectory=None):
    # ok
    if connexion.request.is_json:
        virtualdirectory = Virtualdirectory.from_dict(virtualdirectory)

    virtualdirectorys.insert(virtualdirectory.to_dict())
    return virtualdirectory


def get_virtualdirectory_by_name(name):
    # BUG: not yet gaurantiied there is only one name
	for element in virtualdirectorys.find({'name':name}):
		return (element['name'],
                element['description'],
                element['value'],
                element['kind'])

