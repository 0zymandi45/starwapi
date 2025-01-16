import pytest
from app import create_app
from app.repositories.planet_repository import PlanetRepository
from mongomock import MongoClient


@pytest.fixture
def app():
    app = create_app()
    app.config["TESTING"] = True
    app.config["MONGO_URI"] = "mongomock://localhost" 
    return app

@pytest.fixture
def mock_mongo(app):
    with app.app_context():
        app.mongo = MongoClient().db
        yield app.mongo
