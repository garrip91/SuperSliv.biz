import pytest
from utils import has_r


def test_has_r_with():
    assert has_r("канарейка") == True, "Ожидается True"

def test_has_r_without():
    assert has_r("василий") == False, "Ожидается False"

def test_has_r_wrong_type():
    with pytest.raises(TypeError):
        has_r(1)
