import connexion
import six


#from nic_controller import *
from swagger_server.models.nic import Nic  # noqa: E501
from swagger_server import util
from pymongo import MongoClient



client = MongoClient()

db = client['cm']
nics = db['nic']


def get_nic():
    """
    :return: list all the nics as a list
    """
    # ok
    return list(nics.find({}, {'_id': False}))

def add_nic(nic=None):
    # ok
    if connexion.request.is_json:
        nic = Nic.from_dict(nic)

    nics.insert(nic.to_dict())
    return nic


def get_nic_by_name(name):
    # BUG: not yet gaurantiied there is only one name
	for element in nics.find({'name':name}):
		return (element['name'],
                element['description'],
                element['value'],
                element['kind'])

