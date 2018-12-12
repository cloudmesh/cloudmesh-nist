import random
from flask import jsonify
from random import randint


def get_image():
    return jsonify("yo")


def get_image_by_name(name):
    return jsonify(name)


def add_image(image):
    return jsonify(image)

