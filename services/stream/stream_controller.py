import connexion
import six


#from stream_controller import *
from swagger_server.models.stream import Stream  # noqa: E501
from swagger_server import util
from pymongo import MongoClient



client = MongoClient()

db = client['cm']
streams = db['stream']


def get_stream():
    """
    :return: list all the streams as a list
    """
    # ok
    return list(streams.find({}, {'_id': False}))

def add_stream(stream=None):
    # ok
    if connexion.request.is_json:
        stream = Stream.from_dict(stream)

    streams.insert(stream.to_dict())
    return stream


def get_stream_by_name(name):
    # BUG: not yet gaurantiied there is only one name
	for element in streams.find({'name':name}):
		return (element['name'],
                element['description'],
                element['value'],
                element['kind'])

