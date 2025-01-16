from unittest.mock import MagicMock
import pytest
from app.services.planet_service import PlanetService


@pytest.fixture
def mock_planet_repository():
    return MagicMock()


@pytest.fixture
def planet_service(mock_planet_repository):
    service = PlanetService()
    service.repository = mock_planet_repository
    return service


def test_get_all(planet_service, mock_planet_repository):
    mock_planet_repository.get_all.return_value = [
        {"_id": "1", "name": "Earth", "films": []},
        {"_id": "2", "name": "Mars", "films": []},
    ]

    planets = planet_service.get_all(expand=False)

    assert len(planets) == 2
    assert planets[0]["name"] == "Earth"
    assert planets[1]["name"] == "Mars"
    mock_planet_repository.get_all.assert_called_once_with(expand=False)


def test_get_by_id(planet_service, mock_planet_repository):
    mock_planet_repository.get_by_id.return_value = {"_id": "1", "name": "Earth", "films": []}

    planet = planet_service.get_by_id("1", expand=False)

    assert planet["_id"] == "1"
    assert planet["name"] == "Earth"
    mock_planet_repository.get_by_id.assert_called_once_with("1", expand=False)


def test_create(planet_service, mock_planet_repository):
    mock_planet_repository.create.return_value = "1"
    data = {"name": "Earth", "films": []}

    planet_id = planet_service.create(data)

    assert planet_id == "1"
    mock_planet_repository.create.assert_called_once_with(data)


def test_update(planet_service, mock_planet_repository):
    mock_planet_repository.update.return_value = True
    update_data = {"name": "Updated Earth"}

    success = planet_service.update("1", update_data)

    assert success is True
    mock_planet_repository.update.assert_called_once_with("1", update_data)


def test_delete(planet_service, mock_planet_repository):
    mock_planet_repository.delete.return_value = True

    success = planet_service.delete("1")

    assert success is True
    mock_planet_repository.delete.assert_called_once_with("1")
