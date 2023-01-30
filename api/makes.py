from flask import Blueprint, request, jsonify, render_template
import requests
from flask_restful import Api, Resource
from __init__ import app


# Creating a Flask blueprint and API routing
makes_api = Blueprint('makes_api', __name__ ,
                    url_prefix='/api/makes')

# API instance from flask_restful
api = Api(makes_api)

# Get request for the API
def carMakes():
    global makes_api  
    try: cars_info
    except: cars_info = None
       
    url = "https://car-api2.p.rapidapi.com/api/makes"
    querystring = {"direction":"asc","sort":"id"}

    headers = {
	"X-RapidAPI-Key": "d3a3e94748msh74bb629320d5734p160ceajsn7f28f4859ea2",
	"X-RapidAPI-Host": "car-api2.p.rapidapi.com"
    }
    response = requests.request("GET", url, headers=headers, params=querystring)
    cars_info = response
    return response

# Get method + json of the response
class CarsInfo(Resource):
    def get(self):
        response = carMakes()
        return response.json()

class postMake(Resource):
    def post(self):
        body = request.get_json()
        car_make = body.get('make')
        if car_make:
            # Saving the make to the database
            return jsonify({"message": "Car make added successfully"}), 201
        else:
            # Return an error message
            return jsonify({"error": "Invalid request"}), 400


api.add_resource(CarsInfo, '/')
api.add_resource(postMake, '/create')


if __name__ == '__main__':
    app.run(debug=True)