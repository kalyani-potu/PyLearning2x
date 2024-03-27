import pytest
def test_sub():
    assert 3-2 == 1

@pytest.mark.smoke
def test_sub1():
    assert 2-2 !=0

@pytest.mark.reg
def test_sub2():
    assert 10-2 !=0

@pytest.mark.reg
def test_sub3():
    assert 5-1==4