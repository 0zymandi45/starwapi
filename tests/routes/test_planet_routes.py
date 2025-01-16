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

def test_get_all_planets(client, mock_mongo):
    mock_mongo.planets.insert_many([
        {"_id": "1", "name": "Earth", "films": []},
        {"_id": "2", "name": "Mars", "films": []}
    ])
    response = client.get("/planets")
    assert response.status_code == 200
    assert len(response.json) == 2
    assert response.json[0]["name"] == "Earth"

def test_get_planet_by_id(client, mock_mongo):
    mock_mongo.planets.insert_one({"_id": "1", "name": "Earth", "films": []})
    response = client.get("/planets/1")
    assert response.status_code == 200
    assert response.json["name"] == "Earth"

def test_create_planet(client, mock_mongo):
    data = {"name": "Earth", "films": []}
    response = client.post("/planets", json=data)
    assert response.status_code == 201
    assert mock_mongo.planets.count_documents({}) == 1

def test_update_planet(client, mock_mongo):
    mock_mongo.planets.insert_one({"_id": "1", "name": "Earth", "films": []})
    data = {"name": "Updated Earth"}
    response = client.put("/planets/1", json=data)
    assert response.status_code == 200
    updated_planet = mock_mongo.planets.find_one({"_id": "1"})
    assert updated_planet["name"] == "Updated Earth"

def test_delete_planet(client, mock_mongo):
    mock_mongo.planets.insert_one({"_id": "1", "name": "Earth", "films": []})
    response = client.delete("/planets/1")
    assert response.status_code == 200
    assert mock_mongo.planets.count_documents({}) == 0
