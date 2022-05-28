from pymongo import MongoClient
import json

def initiate_database():
    client = MongoClient("mongodb://localhost:27017")
    db = client["Architecture_MS_Forecast_Database"]
    col = db["Products"]

    with open('json_productdata.json') as json_file:
        data = json.load(json_file)
        print(data)
    col.insert_many(data)

    col = db["Forecasts"]

    with open('json_forecastdata.json') as json_file:
        data = json.load(json_file)
        print(data)
    col.insert_many(data)



if __name__ == '__main__':
    initiate_database()