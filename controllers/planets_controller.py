from flask import jsonify, request
from services.planet_service import PlanetService

planet_service = PlanetService()

def get_planets():
    try:
        expand = request.args.get("expand")
        planets = planet_service.get_all_planets(expand)
        return jsonify(planets), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def get_planet(planet_id):
    try:
        expand = request.args.get("expand")
        planet = planet_service.get_planet_by_id(planet_id, expand)
        if not planet:
            return jsonify({"error": "Planet not found"}), 404
        return jsonify(planet), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def create_planet():
    try:
        data = request.json
        result = planet_service.create_planet(data)
        return jsonify({"id": result}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def update_planet(planet_id):
    try:
        data = request.json
        result = planet_service.update_planet(planet_id, data)
        if not result:
            return jsonify({"error": "Planet not found"}), 404
        return jsonify({"message": "Planet updated successfully"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def delete_planet(planet_id):
    try:
        result = planet_service.delete_planet(planet_id)
        if not result:
            return jsonify({"error": "Planet not found"}), 404
        return jsonify({"message": "Planet deleted successfully"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
