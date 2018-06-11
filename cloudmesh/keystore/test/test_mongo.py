#! /usr/bin/env python 

import pymongo
import datetime
import pprint

from pymongo import MongoClient

client = MongoClient()

db = client['cm']
profiles = db['profile']



profile = {"author": "Gregor",
        "text": "entry",
        "tags": ["profile"],
        "date": datetime.datetime.utcnow()}



post_id = profiles.insert_one(profile).inserted_id
print(post_id)

print(db.collection_names(include_system_collections=False))

pprint.pprint(profiles.find_one())

pprint.pprint(profiles.find_one({"author": "Gregor"}))

print(profiles.find({"author": "Gregor"}).count())
