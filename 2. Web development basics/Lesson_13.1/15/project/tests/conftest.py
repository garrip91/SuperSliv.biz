import pytest
import run


# Создаём фикстуру для тестирования всех вьюшек (main, candidates, vacancies):
@pytest.fixture()
def test_client():
    app = run.app
    return app.test_client()
