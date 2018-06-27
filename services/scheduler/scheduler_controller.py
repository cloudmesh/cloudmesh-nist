import connexion
import six


#from scheduler_controller import *
from swagger_server.models.scheduler import Scheduler  # noqa: E501
from swagger_server import util
from pymongo import MongoClient


client = MongoClient()

db = client['cm']
schedulers = db['scheduler']


def get_scheduler():
    """
    :return: list all the schedulers as a list
    """
    # ok
    return list(schedulers.find({}, {'_id': False}))

def add_scheduler(scheduler=None):
    # ok
    if connexion.request.is_json:
        scheduler = Scheduler.from_dict(scheduler)

    schedulers.insert(scheduler.to_dict())
    return scheduler


def get_scheduler_by_name(name):
    # BUG: not yet gaurantiied there is only one name
	for element in schedulers.find({'name':name}):
		return (element['name'],
                element['description'],
                element['value'],
                element['kind'])

