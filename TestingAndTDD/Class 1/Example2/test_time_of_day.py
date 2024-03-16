import pytest
import time_of_day


@pytest.mark.parametrize("test_hour, test_result", [(6, 'Morning'), (11, 'Day'), (19, 'Evening'), (23, 'Night'), (4, 'Night')])
def test_what_time(test_hour, test_result):
    assert time_of_day.what_time(test_hour) == test_result
