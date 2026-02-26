def test_username(sample_user):
    assert sample_user['name'] == 'Hari'

def test_lists(num_list_print):
    assert num_list_print[3] == 4