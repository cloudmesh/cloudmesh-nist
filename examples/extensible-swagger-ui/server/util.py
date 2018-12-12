import json
from flask import jsonify


def json_response(data):
    """
    Transform a mongoengine query result to a json response
    """
    return jsonify(json.loads(data.to_json().replace("_id", "id")))
