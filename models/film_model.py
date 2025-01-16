class FilmModel:
    def __init__(self, title, release_date, director, planets):
        self.title = title
        self.release_date = release_date
        self.director = director
        self.planets = planets
        self.created_at = None
        self.updated_at = None

    def to_dict(self):
        return {
            "title": self.title,
            "release_date": self.release_date,
            "director": self.director,
            "planets": self.planets,
            "created_at": self.created_at,
            "updated_at": self.updated_at,
        }
