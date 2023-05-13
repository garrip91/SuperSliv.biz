import pytest
from utils import double


@pytest.mark.parametrize(
    "test_input, expected",
    [(0, 0), (1, 2), (10.0, 20.0), (-3, -6), (123456789, 246913578)]
)
def test_double(test_input, expected):
    assert double(test_input) == expected
