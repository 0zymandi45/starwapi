import pytest
from app.models.film_model import Film

@pytest.fixture
def film_data():
    return {
        "_id": "1",
        "title": "A New Hope",
        "planets": ["planet_1", "planet_2"]
    }

def test_film_model_initialization(film_data):
    film = Film(**film_data)

    assert film._id == film_data["_id"]
    assert film.title == film_data["title"]
    assert film.planets == film_data["planets"]

def test_film_model_to_dict(film_data):
    film = Film(**film_data)
    film_dict = film.to_dict()

    assert film_dict["_id"] == film_data["_id"]
    assert film_dict["title"] == film_data["title"]
    assert film_dict["planets"] == film_data["planets"]

def test_film_model_update(film_data):
    film = Film(**film_data)
    update_data = {"title": "The Empire Strikes Back", "planets": ["planet_3"]}

    film.update(update_data)

    assert film.title == "The Empire Strikes Back"
    assert film.planets == ["planet_3"]
