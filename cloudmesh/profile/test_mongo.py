import pymongo
import datetime
import pprint

from pymongo import MongoClient
client = MongoClient()

client = MongoClient('localhost', 27017)


db = client['test-database']
collection = db['test-collection']

post = {"author": "Mike",
        "text": "My first blog post!",
        "tags": ["mongodb", "python", "pymongo"],
        "date": datetime.datetime.utcnow()}

posts = db.posts
post_id = posts.insert_one(post).inserted_id
print (post_id)


print (db.collection_names(include_system_collections=False))

pprint.pprint(posts.find_one())

pprint.pprint(posts.find_one({"author": "Mike"}))

print (posts.find({"author": "Mike"}).count())
