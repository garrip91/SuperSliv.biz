import pytest
from movie_dao import MovieDAO


class TestMovieDAO:
    
    def test_load_data_is_list_of_dicts(self, movie_dao):
        data = movie_dao.load_data()
        assert type(data) == list, "Data is not a list"
        assert len(data) > 0, "Data is empty"
        movie = data[0]
        assert type(movie) == dict, "Data items are not a dict"

    ######

    def test_get_by_id_exist(self, movie_dao):
        movie_1 = movie_dao.get_by_id(1)
        assert type(movie_1) == dict, "Item is not a dict"

    def test_get_by_id_correct_keys(self, movie_dao, correct_keys):
        movie_1 = movie_dao.get_by_id(1)
        movie_keys = set(movie_1.keys())
        assert movie_keys == correct_keys, "Incorrect set of keys"

    def test_get_by_id_not_exist(self, movie_dao):
        movie_1 = movie_dao.get_by_id(-1)
        assert movie_1 is None, "Request for non existent movie should return None"
    
    @pytest.mark.parametrize("movie_id, movie_name", [(1, "Йеллоустоун"), (2, "Омерзительная восьмёрка"), (3, "Вооружён и очень опасен")])
    def test_get_by_id_values(self, movie_dao, movie_id, movie_name):
        movie = movie_dao.get_by_id(movie_id)
        assert movie.get("title") == movie_name

    ######

    def test_get_by_period_returns_list(self, movie_dao):
        movies_found = movie_dao.get_by_period(0, 3000)
        assert type(movies_found) == list

    def test_get_by_period_exist(self, movie_dao):
        movies_found = movie_dao.get_by_period(2015, 2018)
        assert len(movies_found) == 2

    def test_get_by_period_not_exist(self, movie_dao):
        movies_found = movie_dao.get_by_period(-2, -1)
        assert movies_found == []

    def test_get_by_period_all(self, movie_dao):
        movies_all = movie_dao.load_data()
        movies_found = movie_dao.get_by_period(0, 3000)
        assert len(movies_found) == len(movies_all)

    def test_get_by_period_keys_correct(self, movie_dao, correct_keys):
        one_movie = movie_dao.get_by_period(2015, 2015)[0]
        movie_keys = set(one_movie.keys())
        assert movie_keys == correct_keys, "Incorrect set of keys"
