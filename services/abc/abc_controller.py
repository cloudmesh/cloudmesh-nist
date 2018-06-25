import connexion
import six


#from abc_controller import *
from swagger_server.models.abc import Abc  # noqa: E501
from swagger_server import util
from pymongo import MongoClient



client = MongoClient()

db = client['cm']
abcs = db['abc']


def get_abc():
    """
    :return: list all the abcs as a list
    """
    # ok
    return list(abcs.find({}, {'_id': False}))

def add_abc(abc=None):
    # ok
    if connexion.request.is_json:
        abc = Abc.from_dict(abc)

    abcs.insert(abc.to_dict())
    return abc


def get_abc_by_name(name):
    # BUG: not yet gaurantiied there is only one name
	for element in abcs.find({'name':name}):
		return (element['name'],
                element['description'],
                element['value'],
                element['kind'])

