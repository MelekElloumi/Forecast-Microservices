from flask import Flask, render_template, flash, redirect, url_for, session, request, json
from functools import wraps
from pymongo import MongoClient
import requests

def create_app(name):

    app = Flask(name)

    @app.route('/')
    def index():
        return render_template('home.html')

        # User login

    @app.route('/login', methods=['POST'])
    def login():
        username = request.form["username"]
        password = request.form["password"]

        res = requests.get(f'http://localhost:5000/login?username={username}&password={password}')
        data = json.loads(res.text)
        if data['loggedin']:
            session['logged_in'] = True
            flash(data['message'], 'success')
            return redirect(url_for('index'))
        else:
            return render_template('login.html', error=data['error'])

    def is_logged_in(f):
        @wraps(f)
        def wrap(*args, **kwargs):
            if 'logged_in' in session:
                return f(*args, **kwargs)
            else:
                flash('Unauthorized, Please login', 'danger')
                return render_template('login.html')
        return wrap

    @app.route('/logout')
    @is_logged_in
    def logout():
        session.clear()
        flash('Logged out successfully', 'success')
        return redirect(url_for('index'))

    @app.route('/planning')
    @is_logged_in
    def planning():
        return render_template('planning.html')

    @app.route('/products')
    @is_logged_in
    def products():
        res = requests.get('http://localhost:5001/products')
        data= json.loads(res.text)
        return render_template('products.html',data=data)

    @app.route('/forecasts/<int:product_id>')
    @is_logged_in
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