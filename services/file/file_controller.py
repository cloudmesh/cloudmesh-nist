import connexion
import six


#from file_controller import *
from swagger_server.models.file import File  # noqa: E501
from swagger_server import util
from pymongo import MongoClient



client = MongoClient()

db = client['cm']
files = db['file']


def get_file():
    """
    :return: list all the files as a list
    """
    # ok
    return list(files.find({}, {'_id': False}))

def add_file(file=None):
    # ok
    if connexion.request.is_json:
        file = File.from_dict(file)

    files.insert(file.to_dict())
    return file


def get_file_by_name(name):
    # BUG: not yet gaurantiied there is only one name
	for element in files.find({'name':name}):
		return (element['name'],
                element['description'],
                element['value'],
                element['kind'])

