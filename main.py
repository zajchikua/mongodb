__author__ = 'Anastasiya'
import json_interface as ji
from pymongo import MongoClient
# establishing connection
client = MongoClient('localhost', 27017)
db = client.pymongo_test

db.collection.drop()
# populating
p = ji.Populator(client, 'pymongo_test')
p.populate('/Users/Anastasiya/mongo/source.json')

# retrieving
r = ji.Retriever('/Users/Anastasiya/mongo/out', client, 'pymongo_test', ['first_name', 'last_name', 'city','phone'])

print(r.get('Dima'))