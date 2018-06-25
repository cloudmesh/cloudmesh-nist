import connexion
import six


#from database_controller import *
from swagger_server.models.database import Database  # noqa: E501
from swagger_server import util
from pymongo import MongoClient



client = MongoClient()

db = client['cm']
databases = db['database']


def get_database():
    """
    :return: list all the databases as a list
    """
    # ok
    return list(databases.find({}, {'_id': False}))

def add_database(database=None):
    # ok
    if connexion.request.is_json:
        database = Database.from_dict(database)

    databases.insert(database.to_dict())
    return database


def get_database_by_name(name):
    # BUG: not yet gaurantiied there is only one name
	for element in databases.find({'name':name}):
		return (element['name'],
                element['description'],
                element['value'],
                element['kind'])

