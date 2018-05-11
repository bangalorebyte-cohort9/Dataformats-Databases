#!/usr/bin/env python3

import pymongo
import datetime
import pprint


client = pymongo.MongoClient('localhost',27017)

db = client.test_database

# Post is a document
post = {"author": "Mike",
         "text": "My first blog post!",
         "tags": ["mongodb", "python", "pymongo"],
         "date": datetime.datetime.utcnow()}

posts = db.posts # Collection

post_id = posts.insert_one(post).inserted_id

pprint.pprint(posts.find())
pprint.pprint(posts.find_one())
pprint.pprint(posts.find_one({"author": "Mike"}))
