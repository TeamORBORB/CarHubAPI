from flask import Blueprint, request, jsonify, render_template
import requests
from flask_restful import Api, Resource
from __init__ import app

# Creating a Flask blueprint and API routing
years_api = Blueprint('years_api', __name__ ,
                    url_prefix='/api/years')

# API instance from flask_restful
api = Api(years_api)

# Get request for the API - provided by RapidAPI
def carYears():
    global years_api  
    try: cars_info
    except: cars_info = None
       
    url = "https://car-api2.p.rapidapi.com/api/years"

    headers = {
	"X-RapidAPI-Key": "d3a3e94748msh74bb629320d5734p160ceajsn7f28f4859ea2",
	"X-RapidAPI-Host": "car-api2.p.rapidapi.com"
    }
    response = requests.request("GET", url, headers=headers)
    cars_info = response
    return response

# Get method + json of the response
class CarsInfo(Resource):
    def get(self):
        response = carYears()
        return response.json()

# Endpoint that allows a specific car to be searched using the ID provided by the API - from Car Data API
    # def car_specific(self, id):
    #     response = carYears()
    #     cars_data = response.json()
    #     for car in cars_data:
    #         if car['id'] == id:
    #             return jsonify(car)

api.add_resource(CarsInfo, '/')

if __name__ == '__main__':
    app.run(debug=True)