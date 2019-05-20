import connexion
import six


#from containers_controller import *
from swagger_server.models.containers import Containers  # noqa: E501
from swagger_server import util
from pymongo import MongoClient



client = MongoClient()

db = client['cm']
containerss = db['containers']


def get_containers():
    """
    :return: list all the containerss as a list
    """
    # ok
    return list(containerss.find({}, {'_id': False}))

def add_containers(containers=None):
    # ok
    if connexion.request.is_json:
        containers = Containers.from_dict(containers)

    containerss.insert(containers.to_dict())
    return containers


def get_containers_by_name(name):
    # BUG: not yet gaurantiied there is only one name
	for element in containerss.find({'name':name}):
		return (element['name'],
                element['version'],
                element['label'],
                element['type'],
                element['definition'],
                element['imgURI'],
                element['tags'])

