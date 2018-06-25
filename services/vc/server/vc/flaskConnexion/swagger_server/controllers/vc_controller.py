import connexion
import six

from swagger_server.models.node import Node  # noqa: E501
from swagger_server.models.vc import VC  # noqa: E501
from swagger_server import util


def add_vc(vc=None):  # noqa: E501
    """Create a new vc

     # noqa: E501

    :param vc: The new vc to create
    :type vc: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        vc = VC.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def get_vc():  # noqa: E501
    """get_vc

    Returns all vcs # noqa: E501


    :rtype: VC
    """
    return 'do some magic!'


def get_vc_by_name(vcname):  # noqa: E501
    """get_vc_by_name

    Returns a vc by its name # noqa: E501

    :param vcname: 
    :type vcname: str

    :rtype: VC
    """
    return 'do some magic!'


def get_vc_fe_by_name(vcname):  # noqa: E501
    """get_vc_fe_by_name

    Returns the front-end node info of the specified vc # noqa: E501

    :param vcname: 
    :type vcname: str

    :rtype: Node
    """
    return 'do some magic!'


def get_vc_node_by_name(vcname, nodename):  # noqa: E501
    """get_vc_node_by_name

    Returns the specified node info of the specified vc # noqa: E501

    :param vcname: 
    :type vcname: str
    :param nodename: 
    :type nodename: str

    :rtype: Node
    """
    return 'do some magic!'
