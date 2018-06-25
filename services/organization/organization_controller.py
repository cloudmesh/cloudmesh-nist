import connexion
import six


#from organization_controller import *
from swagger_server.models.organization import Organization  # noqa: E501
from swagger_server import util
from pymongo import MongoClient



client = MongoClient()

db = client['cm']
organizations = db['organization']


def get_organization():
    """
    :return: list all the organizations as a list
    """
    # ok
    return list(organizations.find({}, {'_id': False}))

def add_organization(organization=None):
    # ok
    if connexion.request.is_json:
        organization = Organization.from_dict(organization)

    organizations.insert(organization.to_dict())
    return organization


def get_organization_by_name(name):
    # BUG: not yet gaurantiied there is only one name
	for element in organizations.find({'name':name}):
		return (element['name'],
                element['description'],
                element['value'],
                element['kind'])

