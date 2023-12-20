import pymongo
from pymongo.database import Database

DB_URI = 'mongodb://localhost:27017'
DB_NAME = 'eve'


def DB() -> Database:
    """ 连接数据库 """
    conn = pymongo.MongoClient(DB_URI)
    db = conn.get_database(DB_NAME)
    return db
