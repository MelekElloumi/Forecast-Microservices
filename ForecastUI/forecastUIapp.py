from flask import Flask, render_template, flash, redirect, url_for, session, request, json
from pymongo import MongoClient
import requests

def create_app(name):

    app = Flask(name)

    @app.route('/')
    def index():
        return render_template('home.html')

    @app.route('/planning')
    def planning():
        return render_template('planning.html')

    @app.route('/products')
    def products():
        res = requests.get('http://localhost:5001/products')
        data= json.loads(res.text)
        print(data)
        return render_template('products.html',data=data)

    @app.route('/login', methods=['GET'])
    def login():
        username = request.args.get('username', default="none", type=str)
        password = request.args.get('password', default='none', type=str)
        CONNECTION_STRING = "mongodb://localhost:27017"
        client = MongoClient(CONNECTION_STRING)
        db = client["Architecture_MS_Security"]
        col = db["Users"]
        user=col.find_one({"username":username})
        response={}
        if (user!=None):
            if password==user["password"]:
                response["loggedin"]=True
                response["message"] = "Logged in successfully"
            else:
                response["loggedin"]=False
                response["error"] = "Uncorrect password"
        else:
            response["loggedin"]=False
            response["error"] = "User not found"
        return response

    return app



def main( ):
    app = create_app(__name__)
    app.secret_key = 'secret123'
    app.run(port=5002)

if __name__ == '__main__':
    main()