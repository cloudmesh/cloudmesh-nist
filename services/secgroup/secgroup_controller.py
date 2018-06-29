import connexion
import six


#from secgroup_controller import *
from swagger_server.models.secgroup import Secgroup  # noqa: E501
from swagger_server import util
from pymongo import MongoClient



client = MongoClient()

db = client['cm']
secgroups = db['secgroup']


def get_secgroup():
    """
    :return: list all the secgroups as a list
    """
    # ok
    return list(secgroups.find({}, {'_id': False}))

def add_secgroup(secgroup=None):
    # ok
    if connexion.request.is_json:
        secgroup = Secgroup.from_dict(secgroup)

    secgroups.insert(secgroup.to_dict())
    return secgroup


def get_secgroup_by_name(name):
    # BUG: not yet gaurantiied there is only one name
	for element in secgroups.find({'name':name}):
		return (element['name'],
                element['description'],
                element['value'],
                element['kind'])

