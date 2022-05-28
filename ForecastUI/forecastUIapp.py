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
        return render_template('products.html',data=data)

    @app.route('/forecasts/<int:product_id>')
    def forecasts(product_id):
        #product_id = request.args.get('product_id', default=0, type=int)
        res = requests.get(f'http://localhost:5001/forecasts/{product_id}')
        data = json.loads(res.text)
        labels=[forecast['date'] for forecast in data]
        values= [forecast['sales'] for forecast in data]
        return render_template('forecasts.html', labels=labels, values=values)


    return app



def main( ):
    app = create_app(__name__)
    app.secret_key = 'secret123'
    app.run(port=5002)

if __name__ == '__main__':
    main()