import connexion
import six


#from batchjob_controller import *
from swagger_server.models.batchjob import Batchjob  # noqa: E501
from swagger_server import util
from pymongo import MongoClient



client = MongoClient()

db = client['cm']
batchjobs = db['batchjob']


def get_batchjob():
    """
    :return: list all the batchjobs as a list
    """
    # ok
    return list(batchjobs.find({}, {'_id': False}))

def add_batchjob(batchjob=None):
    # ok
    if connexion.request.is_json:
        batchjob = Batchjob.from_dict(batchjob)

    batchjobs.insert(batchjob.to_dict())
    return batchjob


def get_batchjob_by_name(name):
    # BUG: not yet gaurantiied there is only one name
	for element in batchjobs.find({'name':name}):
		return (element['name'],
                element['description'],
                element['value'],
                element['kind'])

