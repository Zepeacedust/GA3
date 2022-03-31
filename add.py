import pytest
from add import add

## step 1
def test_empty_string():
    assert add("") == 0