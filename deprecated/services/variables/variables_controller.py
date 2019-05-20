import connexion
import six


#from variables_controller import *
from swagger_server.models.variables import Variables  # noqa: E501
from swagger_server import util
from pymongo import MongoClient



client = MongoClient()

db = client['cm']
variabless = db['variables']


def get_variables():
    """
    :return: list all the variabless as a list
    """
    # ok
    return list(variabless.find({}, {'_id': False}))

def add_variables(variables=None):
    # ok
    if connexion.request.is_json:
        variables = Variables.from_dict(variables)

    variabless.insert(variables.to_dict())
    return variables


def get_variables_by_name(name):
    # BUG: not yet gaurantiied there is only one name
	for element in variabless.find({'name':name}):
		return (element['name'],
                element['description'],
                element['value'],
                element['kind'])

