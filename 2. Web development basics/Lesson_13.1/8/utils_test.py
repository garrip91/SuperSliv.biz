import pytest
from utils import sum_of_two


sum_of_two_parameters = [(0, 0, 0), (1, 1, 2), (-10, 10, 0)]

@pytest.mark.parametrize("first, second, expected", sum_of_two_parameters)
def test_sum_of_two(first, second, expected):
    assert sum_of_two(first, second) == expected
