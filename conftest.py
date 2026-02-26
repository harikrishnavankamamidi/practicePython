import pytest

def dev_func(a,b):
    return a+b

@pytest.fixture
def num_list_print():
    return [1,2,3,4,5,6]

