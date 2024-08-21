from pymongo import MongoClient, errors
from bson.objectid import ObjectId

class AnimalShelter:
    """CRUD operations for Animal collection in MongoDB"""

    def __init__(self, username, password):
        # Initialize the MongoClient
        self.USER = username
        self.PASS = password
        self.HOST = 'nv-desktop-services.apporto.com'
        self.PORT = 30918
        self.DB = 'AAC'
        self.COL = 'animals'

        # Initialize the connection
        connection_string = f'mongodb://{self.USER}:{self.PASS}@{self.HOST}:{self.PORT}/{self.DB}'
        self.client = MongoClient(connection_string)
        self.database = self.client[self.DB]

    def create(self, data):
        if data:
            try:
                result = self.database.animals.insert_one(data)
                return result.acknowledged
            except errors.PyMongoError as e:
                print(f"An error occurred while inserting: {e}")
                return False
        else:
            raise Exception("Nothing to save because data parameter is empty")

    def read_all(self, query):
        try:
            cursor = self.database.animals.find(query)
            return list(cursor)
        except errors.PyMongoError as e:
            print(f"An error occurred while reading: {e}")
            return []

    def read(self, query):
        try:
            result = self.database.animals.find_one(query)
            return result
        except errors.PyMongoError as e:
            print(f"An error occurred while reading: {e}")
            return None

    def update(self, query, new_data):
        if query:
            try:
                result = self.database.animals.update_one(query, {'$set': new_data})
                return result.acknowledged
            except errors.PyMongoError as e:
                print(f"An error occurred while updating: {e}")
                return False
        else:
            raise Exception("No query provided for update")

    def delete(self, query):
        if query:
            try:
                result = self.database.animals.delete_one(query)
                return result.acknowledged
            except errors.PyMongoError as e:
                print(f"An error occurred while deleting: {e}")
                return False
        else:
            raise Exception("No query provided for delete")