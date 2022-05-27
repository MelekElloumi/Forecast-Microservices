import sqlite3

from pymongo import MongoClient

def initiate_database():
    CONNECTION_STRING = "mongodb://localhost:27017"
    client = MongoClient(CONNECTION_STRING)
    db = client["Architecture_MS_Security"]
    col = db["Users"]
    data=[
        {
        "username":"Melek",
        "password":"Elloumi"
        },
        {
            "username": "admin",
            "password": "admin"
        },
        {
            "username": "root",
            "password": "root"
        }
    ]
    col.insert_many(data)

def create_db():
    connection = sqlite3.connect('database.db')
    cur = connection.cursor()
    cur.execute("DROP TABLE IF EXISTS User")
    cur.execute(
        "CREATE TABLE User (ID INTEGER PRIMARY KEY, USERNAME TEXT NOT NULL, PASSWORD TEXT NOT NULL);")
    cur.execute(
        "INSERT INTO User (USERNAME,PASSWORD) VALUES ('admin','admin'),('root','root'),('melek','elloumi');")
    connection.commit()
    print("Done")
    connection.close()

if __name__ == '__main__':
    #create_db()
    initiate_database()