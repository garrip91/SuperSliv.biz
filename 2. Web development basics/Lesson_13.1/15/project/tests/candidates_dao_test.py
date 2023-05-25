import pytest
from app.candidates.dao.candidates_dao import CandidateDAO


# Нам пригодится экземпляр DAO, так что мы создадим его в фикстуре,
# но пригодится нам это только 1 раз, поэтому выносить его в conftest мы не будем:
@pytest.fixture()
def candidates_dao():
    candidates_dao_instance = CandidateDAO("./data/candidates.json")
    return candidates_dao_instance


# Задаём, какие ключи ожидаем получить от кандидата:
keys_should_be = {"pk", "name", "position"}


class TestCandidateDao:

    def test_get_all(self, candidates_dao):
        """Проверяем, верный ли список кандидатов возвращается"""
        candidates = candidates_dao.get_all()
        assert type(candidates) == list, "возвращается не список"
        assert len(candidates) > 0, "возвращается пустой список"
        assert set(candidates[0].keys()) == keys_should_be, "Неверный список"
    
    def test_get_by_id(self, candidates_dao):
        """Проверяем, верный ли кандидат возвращается при запросе одного кандидата"""
        candidate = candidates_dao.get_by_pk(1)
        assert(candidate["pk"] == 1), "возвращается неправильный кандидат"
        assert set(candidate.keys()) == keys_should_be, "Неверный список кандидатов"
