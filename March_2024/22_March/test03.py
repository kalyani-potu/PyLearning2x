import pytest
def test_sub():
    assert 3-2 == 1

@pytest.mark.smoke
def test_sub1():
    assert 2-2 !=0