from repositories.planet_repository import PlanetRepository
from datetime import datetime, timezone

class PlanetService:
    def __init__(self):
        self.repository = PlanetRepository()

    def get_all_planets(self, expand):
        return self.repository.get_all(expand)

    def get_planet_by_id(self, planet_id, expand):
        return self.repository.get_by_id(planet_id, expand)

    def create_planet(self, data):
        timestamps = {"created_at": datetime.now(timezone.utc), "updated_at": datetime.now(timezone.utc)}
        data.update(timestamps)
        return self.repository.create(data)

    def update_planet(self, planet_id, data):
        data.update({"updated_at": datetime.now(timezone.utc)})
        return self.repository.update(planet_id, data)

    def delete_planet(self, planet_id):
        return self.repository.delete(planet_id)
