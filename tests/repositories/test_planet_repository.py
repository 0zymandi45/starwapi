import pytest
from bson.objectid import ObjectId
from mongomock import MongoClient
from app.repositories.planet_repository import PlanetRepository


@pytest.fixture
def mock_mongo():
    client = MongoClient() 
    db = client["test_db"] 
    return db


@pytest.fixture
def planet_repository(mock_mongo):
    repo = PlanetRepository()
    repo.planets_collection = mock_mongo.planets
    repo.films_collection = mock_mongo.films
    return repo


def test_get_all(planet_repository, mock_mongo):
    mock_mongo.planets.insert_many([
        {"_id": ObjectId(), "name": "Dagobah", "films": []},
        {"_id": ObjectId(), "name": "Aldeeran", "films": []},
    ])

    planets = planet_repository.get_all(expand=False)

    assert len(planets) == 2
    assert planets[0]["name"] == "Dagobah"
    assert planets[1]["name"] == "Aldeeran"


def test_get_by_id(planet_repository, mock_mongo):
    planet_id = ObjectId()
    mock_mongo.planets.insert_one({"_id": planet_id, "name": "Dagobah", "films": []})

    planet = planet_repository.get_by_id(str(planet_id), expand=False)

    assert planet["_id"] == str(planet_id)
    assert planet["name"] == "Dagobah"


def test_create(planet_repository, mock_mongo):
    data = {"name": "Dagobah", "films": []}

    planet_id = planet_repository.create(data)

    inserted_planet = mock_mongo.planets.find_one({"_id": ObjectId(planet_id)})
    assert inserted_planet is not None
    assert inserted_planet["name"] == "Dagobah"


def test_update(planet_repository, mock_mongo):
    planet_id = ObjectId()
    mock_mongo.planets.insert_one({"_id": planet_id, "name": "Dagobah", "films": []})

    update_data = {"name": "Dagobah Updated"}

    success = planet_repository.update(str(planet_id), update_data)

    updated_planet = mock_mongo.planets.find_one({"_id": planet_id})
    assert success is True
    assert updated_planet["name"] == "Dagobah Updated"


def test_delete(planet_repository, mock_mongo):
    planet_id = ObjectId()
    mock_mongo.planets.insert_one({"_id": planet_id, "name": "Dagobah", "films": []})

    success = planet_repository.delete(str(planet_id))

    deleted_planet = mock_mongo.planets.find_one({"_id": planet_id})
    assert success is True
    assert deleted_planet is None
