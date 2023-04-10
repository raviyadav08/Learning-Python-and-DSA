import mathlib
import pytest

@pytest.mark.cal
def test_calc_total():
    total = mathlib.calc_total(4,5)
    assert total == 9

@pytest.mark.cal
def test_calc_multiply():
    result = mathlib.calc_multiply(10,3)
    assert result == 30

@pytest.mark.dummy
def test_dummy():
    assert True

