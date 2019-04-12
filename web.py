from flask import Flask
from flask import jsonify
from flask import request
from flask_pymongo import PyMongo
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

app.config['MONGO_DBNAME'] = 'viewstats'
app.config['MONGO_URI'] = 'mongodb://localhost:27017/viewstats'

mongo = PyMongo(app)

@app.route('/', methods=['GET'])
def index():
  return 'Viewstats backend is working !!!'

@app.route('/commercants', methods=['GET'])
def get_all_commercants():
  commercant = mongo.db.commercants
  output = []
  for s in commercant.find():
    output.append({'nom' : s['nom'], 'adresse' : s['adresse'], 'revenu' : s['Revenu']})
  return jsonify(output)
