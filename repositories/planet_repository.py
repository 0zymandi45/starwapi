from bson.objectid import ObjectId
from app import mongo

class PlanetRepository:
    def get_all(self, expand: bool = False):
        planets = list(mongo.db.planets.find())
        for planet in planets:
            planet['_id'] = str(planet['_id'])
            if expand:
                planet['films'] = [
                    {
                        "_id": str(film["_id"]),
                        "title": film["title"],
                        "director": film.get("director"),
                        "release_date": film.get("release_date")
                    }
                    for film_id in planet.get('films', [])
                    if (film := mongo.db.films.find_one({'_id': ObjectId(film_id)}))
                ]
        return planets

    def get_by_id(self, planet_id, expand: bool = False):
        planet = mongo.db.planets.find_one({"_id": ObjectId(planet_id)})
        if planet:
            planet['_id'] = str(planet['_id'])
            if expand:
                planet['films'] = [
                    {
                        "_id": str(film["_id"]),
                        "title": film["title"],
                        "director": film.get("director"),
                        "release_date": film.get("release_date"),
                        "diameter": film.get("diameter")
                    }
                    for film_id in planet.get('films', [])
                    if (film := mongo.db.films.find_one({'_id': ObjectId(film_id)})) is not None
                ]

        return planet

    def create(self, data):
        result = mongo.db.planets.insert_one(data)
        return str(result.inserted_id)

    def update(self, planet_id, data):
        result = mongo.db.planets.update_one({"_id": ObjectId(planet_id)}, {"$set": data})
        return result.matched_count > 0

    def delete(self, planet_id):
        result = mongo.db.planets.delete_one({"_id": ObjectId(planet_id)})
        return result.deleted_count > 0
