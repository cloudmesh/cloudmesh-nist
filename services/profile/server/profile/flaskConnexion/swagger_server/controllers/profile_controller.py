import connexion
import six

from swagger_server.models.profile import Profile  # noqa: E501
from swagger_server import util


def add_profile(profile=None):  # noqa: E501
    """Create a new profile

     # noqa: E501

    :param profile: The new profile to create
    :type profile: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        profile = Profile.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def get_profile():  # noqa: E501
    """get_profile

    Returns all general description users # noqa: E501


    :rtype: Profile
    """
    return 'do some magic!'


def get_profile_by_uuid(uuid):  # noqa: E501
    """get_profile_by_uuid

    Returns a general description of a user # noqa: E501

    :param uuid: 
    :type uuid: str

    :rtype: Profile
    """
    return 'do some magic!'
