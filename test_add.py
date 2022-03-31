import pytest
from add import add

## step 1 
@pytest.fixture(autouse=True)


def test_empty_add():
    assert add("") == 0


def test_single_number_a():
    assert add("1") == 1


def test_single_number_b():
    assert add("6") == 6


def test_single_number_c():
    assert add("86") == 86


def test_single_number_d():
    assert add("0") == 0
