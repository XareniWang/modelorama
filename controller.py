from flask import request
import json

from app import app
from elastic import *
from common import *
import service as service


@app.route('/', methods=['GET'])
def hello_world():
    return "Hello Worl!d!"

@app.route('/bulk', methods=['POST'])
def upload_cities():
    if request.files:
        file = request.files["file"]
        cities = file.read().decode('utf-8')
        cities = json.loads(cities)
        try:
            service.bulk_cities(cities)
            return "Succes bulk cities", 200
        except Exception as e:
            return str(e), 500
    
    return "Please insert a file", 400

@app.route('/search', methods=['GET'])
def search_cities():
    if "q" in request.args:
        q = request.args.get("q")
    else:
        return "Please provide the parameter 'q' with the name of the city that you want to search", 400

    lat = request.args.get("latitude")
    long = request.args.get("longitude")
    
    try:
        cities = service.search_cities(q, lat, long)
        response = {
            "search": cities
        }
        return response, 200
    except Exception as e:
        return str(e), 500
