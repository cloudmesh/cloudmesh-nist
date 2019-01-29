import connexion
import six


#from hadoop_controller import *
from swagger_server.models.hadoop import Hadoop  # noqa: E501
from swagger_server import util
from pymongo import MongoClient



client = MongoClient()

db = client['cm']
hadoops = db['hadoop']


def get_hadoop():
    """
    :return: list all the hadoops as a list
    """
    # ok
    return list(hadoops.find({}, {'_id': False}))

def add_hadoop(hadoop=None):
    # ok
    if connexion.request.is_json:
        hadoop = Hadoop.from_dict(hadoop)

    hadoops.insert(hadoop.to_dict())
    return hadoop


def get_hadoop_by_name(name):
    # BUG: not yet gaurantiied there is only one name
	for element in hadoops.find({'name':name}):
		return (element['name'],
                element['deployment_type'],
                element['deployment_git'],
                element['resource_managers'],
                element['namenodes'],
                element['dataodes'],
                element['historynodes'],
                element['journalnodes'],
                element['yarn'],
                element['hdfs'])

