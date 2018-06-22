import connexion
import six

from swagger_server.models.vc import VC # noqa: E501
from swagger_server.models.node import Node
from swagger_server.models.nic import NIC
from swagger_server import util
from pymongo import MongoClient


client = MongoClient()

db = client['cm']
vcs = db['vc']


def get_vc():
    """
    :return: list all the vcs as a list
    """
    # ok
    return list(vcs.find({}, {'_id': False}))


def add_vc(vc=None):
    # ok
    if connexion.request.is_json:
        vc = VC.from_dict(vc)

    vcs.insert(vc.to_dict())
    return vc

def get_vc_by_name(vcname):  # noqa: E501
    """get_vc_by_name

    Returns a vc by its name # noqa: E501

    :param vcname:
    :type vcname: str

    :rtype: VC
    """
    return vcs.find({"name": "%s" % vcname}, {'_id': False})[0]


def get_vc_fe_by_name(vcname):  # noqa: E501
    """get_vc_fe_by_name

    Returns the front-end node info of the specified vc # noqa: E501

    :param vcname:
    :type vcname: str

    :rtype: Node
    """
    return vcs.find({"name": "%s" % vcname}, {'_id': False})[0]["fe"]


def get_vc_node_by_name(vcname, nodename):  # noqa: E501
    """get_vc_node_by_name

    Returns the specified node info of the specified vc # noqa: E501

    :param vcname:
    :type vcname: str
    :param nodename:
    :type nodename: str

    :rtype: Node
    """
    nodes = vcs.find({"name": "%s" % vcname}, {'_id': False})[0]["nodes"]
    found = False
    ret = {}
    for node in nodes:
        nodeobj = Node.from_dict(node)
        if nodeobj.name == nodename:
            found = True
            ret = nodeobj
            print (ret)
            break
    return ret
