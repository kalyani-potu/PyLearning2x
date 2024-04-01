import pytest

@pytest.fixture
def sample_data():
    data = [1,2,3,4,5]
    return data

def test_1(sample_data):
    assert len(sample_data)==5

def test_2(sample_data):
    assert len(sample_data) !=4
    assert 3 in sample_data