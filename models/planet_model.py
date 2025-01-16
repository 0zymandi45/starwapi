class PlanetModel:
    def __init__(self, name, climate, diameter, population, films):
        self.name = name
        self.climate = climate
        self.diameter = diameter
        self.population = population
        self.films = films
        self.created_at = None
        self.updated_at = None

    def to_dict(self):
        return {
            "name": self.name,
            "climate": self.climate,
            "diameter": self.diameter,
            "population": self.population,
            "films": self.films,
            "created_at": self.created_at,
            "updated_at": self.updated_at,
        }
