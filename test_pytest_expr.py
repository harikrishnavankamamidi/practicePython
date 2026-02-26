def test_add_func(dev_func):
    assert dev_func(1,2) == 3
    assert dev_func(10,23) == 33
    assert dev_func(18,27) == 45
