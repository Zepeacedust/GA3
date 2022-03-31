import pytest
from add import add

@pytest.fixture(autouse=True)
def run_around_tests():
    yield

def test_first_account_gets_number_1():
    assert add("") == 0
