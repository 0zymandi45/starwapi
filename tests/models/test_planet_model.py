import pytest
from app.models.planet_model import Planet

@pytest.fixture
def planet_data():
    return {
        "_id": "1",
        "name": "Tatooine",
        "films": ["film_1", "film_2"]
    }

def test_planet_model_initialization(planet_data):
    planet = Planet(**planet_data)

    assert planet._id == planet_data["_id"]
    assert planet.name == planet_data["name"]
    assert planet.films == planet_data["films"]

def test_planet_model_to_dict(planet_data):
    planet = Planet(**planet_data)
    planet_dict = planet.to_dict()

    assert planet_dict["_id"] == planet_data["_id"]
    assert planet_dict["name"] == planet_data["name"]
    assert planet_dict["films"] == planet_data["films"]

def test_planet_model_update(planet_data):
    planet = Planet(**planet_data)
    update_data = {"name": "Dagobah", "films": ["film_3"]}

    planet.update(update_data)

    assert planet.name == "Dagobah"
    assert planet.films == ["film_3"]
