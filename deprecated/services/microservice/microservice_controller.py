import connexion
import six


#from microservice_controller import *
from swagger_server.models.microservice import Microservice  # noqa: E501
from swagger_server import util
from pymongo import MongoClient



client = MongoClient()

db = client['cm']
microservices = db['microservice']


def get_microservice():
    """
    :return: list all the microservices as a list
    """
    # ok
    return list(microservices.find({}, {'_id': False}))

def add_microservice(microservice=None):
    # ok
    if connexion.request.is_json:
        microservice = Microservice.from_dict(microservice)

    microservices.insert(microservice.to_dict())
    return microservice


def get_microservice_by_name(name):
    # BUG: not yet gaurantiied there is only one name
	for element in microservices.find({'name':name}):
		return (element['name'],
                element['description'],
                element['value'],
                element['kind'])

