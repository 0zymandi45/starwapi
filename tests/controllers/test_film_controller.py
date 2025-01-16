import pytest
from unittest.mock import MagicMock
from app.controllers.films_controller import get_all_films, get_film_by_id, create_film, update_film, delete_film
from flask import Flask, jsonify, request

@pytest.fixture
def mock_film_service(mocker):
    return mocker.patch("app.services.film_service.FilmService")

@pytest.fixture
def app():
    app = Flask(__name__)
    app.config["TESTING"] = True
    return app

def test_get_all_films(mock_film_service):
    mock_film_service.get_all.return_value = [
        {"_id": "1", "title": "Star Wars", "planets": []},
        {"_id": "2", "title": "The Empire Strikes Back", "planets": []}
    ]
    response = get_all_films()
    assert response.status_code == 200
    assert len(response.json) == 2
    assert response.json[0]["title"] == "Star Wars"

def test_get_film_by_id(mock_film_service):
    mock_film_service.get_by_id.return_value = {"_id": "1", "title": "Star Wars", "planets": []}
    response = get_film_by_id("1")
    assert response.status_code == 200
    assert response.json["title"] == "Star Wars"

def test_create_film(mock_film_service):
    mock_film_service.create.return_value = "1"
    data = {"title": "Star Wars", "planets": []}
    with request.json_context(json=data):
        response = create_film()
    assert response.status_code == 201
    assert response.json["id"] == "1"

def test_update_film(mock_film_service):
    mock_film_service.update.return_value = True
    data = {"title": "Updated Star Wars"}
    with request.json_context(json=data):
        response = update_film("1")
    assert response.status_code == 200

def test_delete_film(mock_film_service):
    mock_film_service.delete.return_value = True
    response = delete_film("1")
    assert response.status_code == 200
