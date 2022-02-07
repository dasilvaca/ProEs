from pymongo import MongoClient
import certifi
def connect(col):
    ca = certifi.where()
    conn_str = "mongodb+srv://m001-student:m001-mongodb-basics@sandbox.rtlur.mongodb.net/retryWrites=true&w=majority"
    mongoClient = MongoClient(conn_str, tlsCAFile=ca)
    db = mongoClient['proesdb'][col]
    '''
    mongoClient = MongoClient("localhost",27017)
    db = mongoClient["proesdb"][col]
    '''
    return db