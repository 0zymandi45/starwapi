from flask import Blueprint, request
from utils.http_return_codes import HttpReturnCodes
from services.planet_service import PlanetService

planet_blueprint = Blueprint("planets", __name__)
planet_service = PlanetService()

@planet_blueprint.route("/", methods=["GET"])
def get_planets():
    expand = request.args.get("expand")
    planets = planet_service.get_all_planets(expand)
    return HttpReturnCodes.success(data=planets)

@planet_blueprint.route("/<planet_id>", methods=["GET"])
def get_planet(planet_id):
    expand = request.args.get("expand")
    planet = planet_service.get_planet_by_id(planet_id, expand)
    if not planet:
        return HttpReturnCodes.not_found(message="Planet not found")
    return HttpReturnCodes.success(data=planet)

@planet_blueprint.route("/", methods=["POST"])
def create_planet():
    data = request.json
    result = planet_service.create_planet(data)
    return HttpReturnCodes.created(data={"id": result})

@planet_blueprint.route("/<planet_id>", methods=["PUT"])
def update_planet(planet_id):
    data = request.json
    result = planet_service.update_planet(planet_id, data)
    if not result:
        return HttpReturnCodes.not_found(message="Planet not found")
    return HttpReturnCodes.success(message="Planet updated successfully")

@planet_blueprint.route("/<planet_id>", methods=["DELETE"])
def delete_planet(planet_id):
    result = planet_service.delete_planet(planet_id)
    if not result:
        return HttpReturnCodes.not_found(message="Planet not found")
    return HttpReturnCodes.success(message="Planet deleted successfully")
