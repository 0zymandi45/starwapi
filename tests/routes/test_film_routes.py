import pytest
from mongomock import MongoClient
from app import create_app

@pytest.fixture
def app():
    app = create_app()
    app.config["TESTING"] = True
    app.mongo = MongoClient().db
    return app

@pytest.fixture
def client(app):
    return app.test_client()

@pytest.fixture
def mock_mongo(app):
    return app.mongo

def test_get_all_films(client, mock_mongo):
    mock_mongo.films.insert_many([
        {"_id": "1", "title": "Star Wars", "planets": []},
        {"_id": "2", "title": "The Empire Strikes Back", "planets": []}
    ])
    response = client.get("/films")
    assert response.status_code == 200
    assert len(response.json) == 2
    assert response.json[0]["title"] == "Star Wars"

def test_get_film_by_id(client, mock_mongo):
    mock_mongo.films.insert_one({"_id": "1", "title": "Star Wars", "planets": []})
    response = client.get("/films/1")
    assert response.status_code == 200
    assert response.json["title"] == "Star Wars"

def test_create_film(client, mock_mongo):
    data = {"title": "Star Wars", "planets": []}
    response = client.post("/films", json=data)
    assert response.status_code == 201
    assert mock_mongo.films.count_documents({}) == 1

def test_update_film(client, mock_mongo):
    mock_mongo.films.insert_one({"_id": "1", "title": "Star Wars", "planets": []})
    data = {"title": "Updated Star Wars"}
    response = client.put("/films/1", json=data)
    assert response.status_code == 200
    updated_film = mock_mongo.films.find_one({"_id": "1"})
    assert updated_film["title"] == "Updated Star Wars"

def test_delete_film(client, mock_mongo):
    mock_mongo.films.insert_one({"_id": "1", "title": "Star Wars", "planets": []})
    response = client.delete("/films/1")
    assert response.status_code == 200
    assert mock_mongo.films.count_documents({}) == 0
