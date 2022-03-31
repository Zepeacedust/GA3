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

def test_two_numbers_a():
    assert add("1,1") == 2


def test_two_numbers_b():
    assert add("1,0") == 1


def test_two_numbers_c():
    assert add("53,15") == 68
    
def test_multiple_numbers_a():
    assert add("1,1,1") == 3


def test_multiple_numbers_b():
    assert add("1,0,1") == 2


def test_multiple_numbers_c():
    assert add("53,15,1") == 69


def test_newline_delimiter():
    assert add("1,1\n1") == 3
