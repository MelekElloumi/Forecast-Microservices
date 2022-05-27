from flask import Flask, render_template, flash, redirect, url_for, session, request, json
from pymongo import MongoClient

def create_app(name):

    app = Flask(name)

    @app.route('/login', methods=['GET'])
    def login():
        username = request.args.get('username', default="none", type=str)
        password = request.args.get('password', default='none', type=str)
        CONNECTION_STRING = "mongodb://localhost:27017"
        client = MongoClient(CONNECTION_STRING)
        db = client["Architecture_MS_Security"]
        col = db["Users"]
        user=col.find({"username":username})
        response={}
        if (user.count()):
            if password==user["password"]:
                response["loggedin"]=True
            else:
                response["loggedin"]=False
        else:
            response["loggedin"]=False
        return response

    return app



def main( ):
    app = create_app(__name__)
    app.secret_key = 'secret123'
    app.run(port=5000)

if __name__ == '__main__':
    main()