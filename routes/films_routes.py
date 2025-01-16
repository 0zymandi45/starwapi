from flask import Blueprint, request
from utils.http_return_codes import HttpReturnCodes
from services.films_service import FilmService

film_blueprint = Blueprint("films", __name__)
film_service = FilmService()

@film_blueprint.route("/", methods=["GET"])
def get_films():
    expand = request.args.get("expand")
    films = film_service.get_all_films(expand)
    return HttpReturnCodes.success(data=films)

@film_blueprint.route("/<film_id>", methods=["GET"])
def get_film(film_id):
    expand = request.args.get("expand")
    film = film_service.get_film_by_id(film_id, expand)
    if not film:
        return HttpReturnCodes.not_found(message="Film not found")
    return HttpReturnCodes.success(data=film)

@film_blueprint.route("/", methods=["POST"])
def create_film():
    data = request.json
    result = film_service.create_film(data)
    return HttpReturnCodes.created(data={"id": result})

@film_blueprint.route("/<film_id>", methods=["PUT"])
def update_film(film_id):
    data = request.json
    result = film_service.update_film(film_id, data)
    if not result:
        return HttpReturnCodes.not_found(message="Film not found")
    return HttpReturnCodes.success(message="Film updated successfully")

@film_blueprint.route("/<film_id>", methods=["DELETE"])
def delete_film(film_id):
    result = film_service.delete_film(film_id)
    if not result:
        return HttpReturnCodes.not_found(message="Film not found")
    return HttpReturnCodes.success(message="Film deleted successfully")
