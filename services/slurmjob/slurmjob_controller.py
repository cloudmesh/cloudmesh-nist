import connexion
import six


#from batchjob_controller import *
from swagger_server.models.batchjob import Batchjob  # noqa: E501
from swagger_server import util
from pymongo import MongoClient



client = MongoClient()

db = client['cm']
batchjobs = db['batchjob']


def get_slurmjob():
    """
    :return: list all the batchjobs as a list
    """
    # ok
    return list(slurmjobs.find({}, {'_id': False}))

def add_batchjob(slurmjob=None):
    # ok
    if connexion.request.is_json:
        slurmjob = Slurmjob.from_dict(slurmjob)

    batchjobs.insert(slurmjob.to_dict())
    return slurmjob


def get_batchjob_by_name(name):
    # BUG: not yet gaurantiied there is only one name
	for element in slurmjobs.find({'name':name}):
		return (element['name'],
                element['suffix'],
                element['remote_path'],
                element['kind'])

