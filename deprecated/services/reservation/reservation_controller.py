import connexion
import six


#from reservation_controller import *
from swagger_server.models.reservation import Reservation  # noqa: E501
from swagger_server import util
from pymongo import MongoClient



client = MongoClient()

db = client['cm']
reservations = db['reservation']


def get_reservation():
    """
    :return: list all the reservations as a list
    """
    # ok
    return list(reservations.find({}, {'_id': False}))

def add_reservation(reservation=None):
    # ok
    if connexion.request.is_json:
        reservation = Reservation.from_dict(reservation)

    reservations.insert(reservation.to_dict())
    return reservation


def get_reservation_by_name(name):
    # BUG: not yet gaurantiied there is only one name
	for element in reservations.find({'name':name}):
		return (element['name'],
                element['description'],
                element['value'],
                element['kind'])

