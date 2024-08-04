import pymongo
from constants.config import MONGODB_URL


class MongoManager:
    __instances = {}

    def __new__(cls, db):
        if db not in cls.__instances:
            cls.__instances[db] = super().__new__(cls)
            cls.__instances[db].__initialized = False
        return cls.__instances[db]

    def __init__(self, db):
        if self.__initialized:
            return
        self.__initialized = True

        self.db = db
        self.connection_str = MONGODB_URL
        self.__client = pymongo.MongoClient(self.connection_str)
        self.__database = self.__client[self.db]

    def insert_one(self, collection_name, data):
        collection = self.__database[collection_name]
        collection.insert_one(data)

    def insert_many(self, collection_name, data, options={}):
        collection = self.__database[collection_name]
        collection.insert_many(data, **options)

    def upsert_many(self, collection_name, data):
        collection = self.__database[collection_name]
        collection.bulk_write(data)

    def update_one(self, collection_name, filter, data):
        collection = self.__database[collection_name]
        collection.update_one(filter, data)

    def update_many(self, collection_name, filter, data):
        collection = self.__database[collection_name]
        collection.update_many(filter, data)

    def delete_many(self, collection_name, filter={}):
        collection = self.__database[collection_name]
        collection.delete_many(filter)

    def find_one(self, collection_name, filter={}):
        collection = self.__database[collection_name]
        return collection.find_one(filter)

    def find(
        self,
        collection_name,
        filter={},
        projection=None,
        sort=None,
        offset=0,
        limit=None,
    ):
        collection = self.__database[collection_name]
        result = collection.find(filter, projection)
        if sort:
            result = result.sort(*sort)
        if offset:
            result = result.skip(offset)
        if limit:
            result = result.limit(limit)
        return list(result)

    def aggregate(self, collection_name, filter={}):
        collection = self.__database[collection_name]
        return collection.aggregate(filter)

    def distinct(self, collection_name, filed, filter={}):
        collection = self.__database[collection_name]
        return collection.distinct(filed, filter)
