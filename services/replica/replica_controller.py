import connexion
import six


#from replica_controller import *
from swagger_server.models.replica import Replica  # noqa: E501
from swagger_server import util
from pymongo import MongoClient



client = MongoClient()

db = client['cm']
replicas = db['replica']


def get_replica():
    """
    :return: list all the replicas as a list
    """
    # ok
    return list(replicas.find({}, {'_id': False}))

def add_replica(replica=None):
    # ok
    if connexion.request.is_json:
        replica = Replica.from_dict(replica)

    replicas.insert(replica.to_dict())
    return replica


def get_replica_by_name(name):
    # BUG: not yet gaurantiied there is only one name
	for element in replicas.find({'name':name}):
		return (element['name'],
                element['fielname'],
                element['endpoint'],
                element['checksum'],
                element['size'],
                element['timestamp'])

