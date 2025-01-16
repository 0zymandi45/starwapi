import pytest
from app.controllers.planets_controller import get_all_planets, get_planet_by_id, create_planet, update_planet, delete_planet
from flask import Flask, jsonify, request

@pytest.fixture
def mock_planet_service(mocker):
    return mocker.patch("app.services.planet_service.PlanetService")

@pytest.fixture
def app():
    app = Flask(__name__)
    app.config["TESTING"] = True
    return app

def test_get_all_planets(mock_planet_service):
    mock_planet_service.get_all.return_value = [
        {"_id": "1", "name": "Earth", "films": []},
        {"_id": "2", "name": "Mars", "films": []}
    ]
    response = get_all_planets()
    assert response.status_code == 200
    assert len(response.json) == 2
    assert response.json[0]["name"] == "Earth"

def test_get_planet_by_id(mock_planet_service):
    mock_planet_service.get_by_id.return_value = {"_id": "1", "name": "Earth", "films": []}
    response = get_planet_by_id("1")
    assert response.status_code == 200
    assert response.json["name"] == "Earth"

def test_create_planet(mock_planet_service):
    mock_planet_service.create.return_value = "1"
    data = {"name": "Earth", "films": []}
    with request.json_context(json=data):
        response = create_planet()
    assert response.status_code == 201
    assert response.json["id"] == "1"

def test_update_planet(mock_planet_service):
    mock_planet_service.update.return_value = True
    data = {"name": "Updated Earth"}
    with request.json_context(json=data):
        response = update_planet("1")
    assert response.status_code == 200

def test_delete_planet(mock_planet_service):
    mock_planet_service.delete.return_value = True
    response = delete_planet("1")
    assert response.status_code == 200

