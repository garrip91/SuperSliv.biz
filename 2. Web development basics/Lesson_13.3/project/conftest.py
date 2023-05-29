import pytest
from movie_dao import MovieDAO


@pytest.fixture()
def movie_dao():
    movie_dao_instance = MovieDAO()
    return movie_dao_instance

@pytest.fixture()
def correct_keys():
    the_keys = {"title", "trailer", "year", "rating", "pk"}
    return the_keys
