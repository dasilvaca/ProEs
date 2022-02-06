from pymongo import MongoClient
def connect(col):
    mongoClient = MongoClient("localhost",27017)
    db = mongoClient["proesdb"][col]
    return db