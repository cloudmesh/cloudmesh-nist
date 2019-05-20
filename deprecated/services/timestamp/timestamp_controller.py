import connexion
import six


#from timestamp_controller import *
from swagger_server.models.timestamp import Timestamp  # noqa: E501
from swagger_server import util
from pymongo import MongoClient



client = MongoClient()

db = client['cm']
timestamps = db['timestamp']


def get_timestamp():
    """
    :return: list all the timestamps as a list
    """
    # ok
    return list(timestamps.find({}, {'_id': False}))

def add_timestamp(timestamp=None):
    # ok
    if connexion.request.is_json:
        timestamp = Timestamp.from_dict(timestamp)

    timestamps.insert(timestamp.to_dict())
    return timestamp


def get_timestamp_by_name(name):
    # BUG: not yet gaurantiied there is only one name
	for element in timestamps.find({'name':name}):
		return (element['name'],
                element['description'],
                element['value'],
                element['kind'])

