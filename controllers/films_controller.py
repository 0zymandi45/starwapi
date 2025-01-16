from flask import jsonify, request
from services.films_service import FilmService

film_service = FilmService()

def get_films():
    try:
        expand = request.args.get("expand")
        films = film_service.get_all_films(expand)
        return jsonify(films), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def get_film(film_id):
    try:
        expand = request.args.get("expand")
        film = film_service.get_film_by_id(film_id, expand)
        if not film:
            return jsonify({"error": "Film not found"}), 404
        return jsonify(film), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def create_film():
    try:
        data = request.json
        result = film_service.create_film(data)
        return jsonify({"id": result}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def update_film(film_id):
    try:
        data = request.json
        result = film_service.update_film(film_id, data)
        if not result:
            return jsonify({"error": "Film not found"}), 404
        return jsonify({"message": "Film updated successfully"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def delete_film(film_id):
    try:
        result = film_service.delete_film(film_id)
        if not result:
            return jsonify({"error": "Film not found"}), 404
        return jsonify({"message": "Film deleted successfully"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
