import pytest
from bson.objectid import ObjectId
from mongomock import MongoClient
from app.repositories.film_repository import FilmRepository

@pytest.fixture
def mock_mongo():
    client = MongoClient()  
    db = client["test_db"] 
    return db


@pytest.fixture
def film_repository(mock_mongo):
    repo = FilmRepository()
    repo.films_collection = mock_mongo.films
    repo.planets_collection = mock_mongo.planets
    return repo


def test_get_all(film_repository, mock_mongo):
    mock_mongo.films.insert_many([
        {"_id": ObjectId(), "title": "Star Wars", "planets": []},
        {"_id": ObjectId(), "title": "The Empire Strikes Back", "planets": []},
    ])

    films = film_repository.get_all(expand=False)

    assert len(films) == 2
    assert films[0]["title"] == "Star Wars"
    assert films[1]["title"] == "The Empire Strikes Back"


def test_get_by_id(film_repository, mock_mongo):
    film_id = ObjectId()
    mock_mongo.films.insert_one({"_id": film_id, "title": "Star Wars", "planets": []})

    film = film_repository.get_by_id(str(film_id), expand=False)

    assert film["_id"] == str(film_id)
    assert film["title"] == "Star Wars"


def test_create(film_repository, mock_mongo):
    data = {"title": "Star Wars", "planets": []}

    film_id = film_repository.create(data)

    inserted_film = mock_mongo.films.find_one({"_id": ObjectId(film_id)})
    assert inserted_film is not None
    assert inserted_film["title"] == "Star Wars"


def test_update(film_repository, mock_mongo):
    film_id = ObjectId()
    mock_mongo.films.insert_one({"_id": film_id, "title": "Star Wars", "planets": []})

    update_data = {"title": "Star Wars: Updated"}

    success = film_repository.update(str(film_id), update_data)

    updated_film = mock_mongo.films.find_one({"_id": film_id})
    assert success is True
    assert updated_film["title"] == "Star Wars: Updated"


def test_delete(film_repository, mock_mongo):
    film_id = ObjectId()
    mock_mongo.films.insert_one({"_id": film_id, "title": "Star Wars", "planets": []})

    success = film_repository.delete(str(film_id))

    deleted_film = mock_mongo.films.find_one({"_id": film_id})
    assert success is True
    assert deleted_film is None
