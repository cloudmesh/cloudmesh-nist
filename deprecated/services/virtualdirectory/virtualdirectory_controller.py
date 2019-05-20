import connexion
import six


#from virtualdirectory_controller import *
from swagger_server.models.virtualdirectory import Virtualdirectory  # noqa: E501
from swagger_server import util
from swagger_server.conf import basic_auth, apikey_auth
from pymongo import MongoClient


client = MongoClient()

db = client['cm']
virtualdirectorys = db['virtualdirectory']

@basic_auth
def get_virtualdirectory():
    """
    :return: list all the virtualdirectorys as a list
    """
    # ok
    return list(virtualdirectorys.find({}, {'_id': False, "credential": False}))

@apikey_auth
def add_virtualdirectory(virtualdirectory=None):
    # ok
    if connexion.request.is_json:
        virtualdirectory = Virtualdirectory.from_dict(virtualdirectory)

    virtualdirectorys.insert(virtualdirectory.to_dict())
    return virtualdirectory

@basic_auth
def get_virtualdirectory_by_name(name):
    # BUG: not yet gaurantiied there is only one name
    virtd = virtualdirectorys.find({'name':name})[0]
    flist = None
    #
    # ftp://archive.ubuntu.com/ubuntu/dists/bionic-updates/main/installer-amd64/current/images/netboot/
    '''
    from ftplib import FTP
    ftp = FTP('ftp.debian.org')     # connect to host, default port
    ftp.login()                     # user anonymous, passwd anonymous@
    '230 Login successful.'
    ftp.cwd('debian')               # change into "debian" directory
    '250 Directory successfully changed.'
    ftp.retrlines('LIST')
    '226 Directory send OK.'
    '''
    if virtd["protocol"] == 'ftp':
        from ftplib import FTP
        ftp = FTP(virtd["host"])  # connect to host, default port
        ftp.login(virtd["credential"]["username"], virtd["credential"]["password"])  # user anonymous, passwd anonymous@
        ftp.cwd(virtd["location"])  # change into directory
        files = []
        flist = ftp.retrlines('LIST', files.append)
        flist = files
    elif virtd["protocol"] == 'ssh':
        flist = "NOT Implemented yet!"
    else:
        flist = "NOT Implemented yet!"
    return flist

