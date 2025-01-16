from repositories.film_repository import FilmRepository
from datetime import datetime, timezone

class FilmService:
    def __init__(self):
        self.repository = FilmRepository()

    def get_all_films(self, expand):
        return self.repository.get_all(expand)

    def get_film_by_id(self, film_id, expand):
        return self.repository.get_by_id(film_id, expand)

    def create_film(self, data):
        timestamps = {"created_at": datetime.now(timezone.utc), "updated_at": datetime.now(timezone.utc)}
        data.update(timestamps)
        return self.repository.create(data)

    def update_film(self, film_id, data):
        data.update({"updated_at": datetime.now(timezone.utc)})
        return self.repository.update(film_id, data)

    def delete_film(self, film_id):
        return self.repository.delete(film_id)
