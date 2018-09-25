#!/usr/bin/env python

import connexion
import flask
from pprint import pprint
import yaml
import os
from decorator import decorator

# load credentials from config file
creds = {}
dir = os.path.dirname(__file__)
file = os.path.join(dir, "secconf.yaml")
with open(file, 'r') as f:
    try:
        credconf = yaml.load(f)
        if 'httpbasicauth' in credconf:
            for userpass in credconf["httpbasicauth"]:
                [(key, value)] = userpass.items()
                creds[key] = value
        if 'apikey' in credconf:
            for apikeypair in credconf['apikey']:
                [(key, value)] = apikeypair.items()
                creds[key] = value
        pprint (creds)
    except yaml.YAMLError as exc:
        print(exc)

def ERROR_401(error):
    return flask.Response(error, 401, {'WWWAuthenticate':'Basic realm="Login Required"'})

def check_basicauth(username, password):
    '''This function is called to check if a username /
    password combination is valid.'''
    return username in creds and password == creds[username]

def check_apikeyauth(apikey, apisecret):
    '''This function is called to check if an apikey /
    api secret combination is valid.'''
    return apikey in creds and apisecret == creds[apikey]

@decorator
def basic_auth(f, *args, **kwargs):
    '''http basic auth decorator'''
    auth = flask.request.authorization
    #pprint (auth)
    if not auth or not check_basicauth(auth.username, auth.password):
        return ERROR_401('ERROR: Invalid username/password for http basic auth')
    return f(*args, **kwargs)

@decorator
def apikey_auth(f, *args, **kwargs):
    '''apikey-secret auth decorator'''
    apikey = flask.request.headers.get('API-Key')
    apisecret = flask.request.headers.get('API-Secret')
    #print(apikey, apisecret)
    if not check_apikeyauth(apikey, apisecret):
        return ERROR_401('ERROR: apikey auth failed')
    return f(*args, **kwargs)
