__author__ = 'Anastasiya'
import json
import os

# TODO implement clear DB (erase true-flase)
class Populator:
     def __init__(self, client, dbname):
        self.db = client[dbname]


     def populate(self, jsonpath):
         filehandle = open(jsonpath, mode='r')
         data = json.load(filehandle)
         filehandle.close()
         self.db.posts.insert_many(data['records'])
         return


class Retriever:
    def __init__(self, dpath, client, dbname, keys):
        self.dpath = dpath
        self.db = client[dbname]
        self.keys = keys

    def get(self, first_name):
        # get the record by the 1st name
        record = self.db.posts.find_one({'first_name': first_name})

        # check if the record is in the dictionary
        if not isinstance(record, dict):
            return 'Record not found'
        for key in self.keys:
            if key not in record:
                return 'Key %s is missing' % key

        # delete '_id' from the returned dictionary
        record.pop('_id')

        # write the results of the query to the file, defined in open()
        filehandle = open(os.path.join(self.dpath, 'record.json'), mode='w')
        json.dump(record, filehandle)
        filehandle.close()
        return ''
