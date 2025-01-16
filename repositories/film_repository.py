from bson.objectid import ObjectId
from app import mongo

class FilmRepository:
    def get_all(self, expand: bool = False):
        films = list(mongo.db.films.find())
        for film in films:
            film['_id'] = str(film['_id'])
            if expand:
                film['planets'] = [
                    {
                        "_id": str(planet["_id"]),
                        "name": planet["name"],
                        "climate": planet.get("climate"),
                        "population": planet.get("population")
                    }
                    for planet_id in film.get('planets', [])
                    if (planet := mongo.db.planets.find_one({'_id': ObjectId(planet_id)}))
                ]
        return films

    def get_by_id(self, film_id, expand: bool = False):
        film = mongo.db.films.find_one({"_id": ObjectId(film_id)})
        if film:
            film['_id'] = str(film['_id'])
            if expand:
                film['planets'] = [
                    {
                        "_id": str(planet["_id"]),
                        "name": planet["name"],
                        "climate": planet.get("climate"),
                        "population": planet.get("population")
                    }
                    for planet_id in film.get('planets', [])
                    if (planet := mongo.db.planets.find_one({'_id': ObjectId(planet_id)})) is not None
                ]

        return film

    def create(self, data):
        result = mongo.db.films.insert_one(data)
        return str(result.inserted_id)

    def update(self, film_id, data):
        result = mongo.db.films.update_one({"_id": ObjectId(film_id)}, {"$set": data})
        return result.matched_count > 0

    def delete(self, film_id):
        result = mongo.db.films.delete_one({"_id": ObjectId(film_id)})
        return result.deleted_count > 0
