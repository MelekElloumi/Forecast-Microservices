from pymongo import MongoClient

def initiate_database():
    client = MongoClient("mongodb://localhost:27017")
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

if __name__ == '__main__':
    initiate_database()