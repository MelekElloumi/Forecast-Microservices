from flask import Flask, render_template, flash, redirect, url_for, session, request, json,jsonify
from pymongo import MongoClient

def create_app(name):

    app = Flask(name)

    @app.route('/products', methods=['GET'])
    def products():
        client = MongoClient("mongodb://localhost:27017")
        db = client["Architecture_MS_Forecast_Database"]
        col = db["Products"]
        products=col.find()
        response=jsonify(list(products))
        return response

    @app.route('/forecasts/<int:product_id>', methods=['GET'])
    def forecasts(product_id):
        #product_id = request.args.get('product_id', default=0, type=int)
        client = MongoClient("mongodb://localhost:27017")
        db = client["Architecture_MS_Forecast_Database"]
        col = db["Forecasts"]
        forecasts = col.find({"product_id":product_id})
        response = jsonify(list(forecasts))
        return response

    return app



def main( ):
    app = create_app(__name__)
    app.secret_key = 'secret123'
    app.run(port=5001)

if __name__ == '__main__':
    main()