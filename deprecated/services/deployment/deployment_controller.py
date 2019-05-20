import connexion
import six


#from deployment_controller import *
from swagger_server.models.deployment import Deployment  # noqa: E501
from swagger_server import util
from pymongo import MongoClient



client = MongoClient()

db = client['cm']
deployments = db['deployment']


def get_deployment():
    """
    :return: list all the deployments as a list
    """
    # ok
    return list(deployments.find({}, {'_id': False}))

def add_deployment(deployment=None):
    # ok
    if connexion.request.is_json:
        deployment = Deployment.from_dict(deployment)

    deployments.insert(deployment.to_dict())
    return deployment


def get_deployment_by_name(name):
    # BUG: not yet gaurantiied there is only one name
	for element in deployments.find({'name':name}):
		return (element['name'],
                element['description'],
                element['value'],
                element['kind'])

