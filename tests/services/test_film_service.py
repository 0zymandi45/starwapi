from unittest.mock import MagicMock
import pytest
from app.services.films_service import FilmService

@pytest.fixture
def mock_film_repository():
    return MagicMock()

@pytest.fixture
def film_service(mock_film_repository):
    service = FilmService()
    service.repository = mock_film_repository
    return service


def test_get_all(film_service, mock_film_repository):
    mock_film_repository.get_all.return_value = [
        {"_id": "1", "title": "Star Wars", "planets": []},
        {"_id": "2", "title": "The Empire Strikes Back", "planets": []},
    ]

    films = film_service.get_all(expand=False)

    assert len(films) == 2
    assert films[0]["title"] == "Star Wars"
    assert films[1]["title"] == "The Empire Strikes Back"
    mock_film_repository.get_all.assert_called_once_with(expand=False)

def test_get_by_id(film_service, mock_film_repository):
    mock_film_repository.get_by_id.return_value = {"_id": "1", "title": "Star Wars", "planets": []}

    film = film_service.get_by_id("1", expand=False)

    assert film["_id"] == "1"
    assert film["title"] == "Star Wars"
    mock_film_repository.get_by_id.assert_called_once_with("1", expand=False)

def test_create(film_service, mock_film_repository):
    mock_film_repository.create.return_value = "1"
    data = {"title": "Star Wars", "planets": []}

    film_id = film_service.create(data)

    assert film_id == "1"
    mock_film_repository.create.assert_called_once_with(data)

def test_update(film_service, mock_film_repository):
    mock_film_repository.update.return_value = True
    update_data = {"title": "Star Wars Updated"}

    success = film_service.update("1", update_data)

    assert success is True
    mock_film_repository.update.assert_called_once_with("1", update_data)

def test_delete(film_service, mock_film_repository):
    mock_film_repository.delete.return_value = True

    success = film_service.delete("1")

    assert success is True
    mock_film_repository.delete.assert_called_once_with("1")
