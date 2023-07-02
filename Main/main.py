from flask import Flask, jsonify, abort
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import UniqueConstraint
import requests

from producer import publish

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = 'mysql://root:root@db/main'
CORS(app)

db = SQLAlchemy(app)

@app.route('/api/movies')
def index():
    req = requests.get('http://localhost:8000/api/movies')
    json = req.json()
    return req.json()

@app.route('/api/movies/<int:id>', methods=['GET'])
def rate(id):
    url = "{}/{}".format('http://localhost:8000/api/movieinfo', id)
    print("url: ", url)
    req = requests.get(url)
    print("total ratings: ", req['totalratings'])
    print("total users: ", req['totalusers'])
    print("movies: ", req.json())

    return req.json()
    #return jsonify({
    #    'message': 'success'
    #})


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
