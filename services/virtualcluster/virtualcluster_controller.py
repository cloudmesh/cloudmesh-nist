import connexion
import six

from swagger_server.models.virtualcluster import VirtualCluster # noqa: E501
from swagger_server.models.node import Node
from swagger_server.models.nic import NIC
from swagger_server import util
from pymongo import MongoClient


client = MongoClient()

db = client['cm']
virtualclusters = db['virtualcluster']


def get_virtualcluster():
    """
    :return: list all the virtualclusters as a list
    """
    # ok
    return list(virtualclusters.find({}, {'_id': False}))


def add_virtualcluster(virtualcluster=None):
    # ok
    if connexion.request.is_json:
        virtualcluster = VirtualCluster.from_dict(virtualcluster)

    virtualclusters.insert(virtualcluster.to_dict())
    return virtualcluster

def get_virtualcluster_by_name(virtualclustername):  # noqa: E501
    """get_virtualcluster_by_name

    Returns a virtualcluster by its name # noqa: E501

    :param virtualclustername:
    :type virtualclustername: str

    :rtype: VirtualCluster
    """
    return virtualclusters.find({"name": "%s" % virtualclustername}, {'_id': False})[0]


def get_virtualcluster_fe_by_name(virtualclustername):  # noqa: E501
    """get_virtualcluster_fe_by_name

    Returns the front-end node info of the specified virtualcluster # noqa: E501

    :param virtualclustername:
    :type virtualclustername: str

    :rtype: Node
    """
    return virtualclusters.find({"name": "%s" % virtualclustername}, {'_id': False})[0]["fe"]


def get_virtualcluster_node_by_name(virtualclustername, nodename):  # noqa: E501
    """get_virtualcluster_node_by_name

    Returns the specified node info of the specified virtualcluster # noqa: E501

    :param virtualclustername:
    :type virtualclustername: str
    :param nodename:
    :type nodename: str

    :rtype: Node
    """
    nodes = virtualclusters.find({"name": "%s" % virtualclustername}, {'_id': False})[0]["nodes"]
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
