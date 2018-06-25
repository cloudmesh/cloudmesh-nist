import connexion
import six


#from user_controller import *
from swagger_server.models.user import User  # noqa: E501
from swagger_server import util
from pymongo import MongoClient



client = MongoClient()

db = client['cm']
users = db['user']


def get_user():
    """
    :return: list all the users as a list
    """
    # ok
    return list(users.find({}, {'_id': False}))

def add_user(user=None):
    # ok
    if connexion.request.is_json:
        user = User.from_dict(user)

    users.insert(user.to_dict())
    return user


def get_user_by_name(name):
    # BUG: not yet gaurantiied there is only one name
	for element in users.find({'name':name}):
		return (element['name'],
                element['description'],
                element['value'],
                element['kind'])

