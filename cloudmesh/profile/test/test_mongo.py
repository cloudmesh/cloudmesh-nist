# !/usr/bin/env python
import pymongo
import datetime
import pprint

from pymongo import MongoClient

client = MongoClient()

client = MongoClient('localhost', 27017)

db = client['cm-database']
collection = db['cm-collection']

post = {"author": "Gregor",
        "text": "entry",
        "tags": ["profile"],
        "date": datetime.datetime.utcnow()}

posts = db.posts
post_id = posts.insert_one(post).inserted_id
print(post_id)

print(db.collection_names(include_system_collections=False))

pprint.pprint(posts.find_one())

pprint.pprint(posts.find_one({"author": "Gregor"}))

print(posts.find({"author": "Gregor"}).count())
