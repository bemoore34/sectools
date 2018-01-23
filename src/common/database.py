import pymongo

__author__ = 'bmoore'

# This object is a specific thing - for a specific database. It is not a template or model. The URI is always going
# to be the same.


class Database(object):
    URI = "mongodb://127.0.0.1:27017"
    DATABASE = None

    @staticmethod  # Note - we will need to call this at the beginning of our program.
    def initialize():
        client = pymongo.MongoClient(Database.URI)
        Database.DATABASE = client['sectools']

    @staticmethod
    def insert(collection, data):
        Database.DATABASE[collection].insert(data)

    @staticmethod
    def find(collection, query):
        return Database.DATABASE[collection].find(query)

    @staticmethod
    def find_one(collection, query):
        return Database.DATABASE[collection].find_one(query)

    @staticmethod
    def update(collection, query, data):
        Database.DATABASE[collection].update(query, data, upsert=True)

    @staticmethod
    def remove(collection, query):
        Database.DATABASE[collection].remove(query)
