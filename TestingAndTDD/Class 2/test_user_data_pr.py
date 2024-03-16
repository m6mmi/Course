import user_data_pr


def test_read_data(mock_file):
    with open(mock_file, 'r') as f:
        prepared_data = user_data_pr.prepare_data(f)

    assert prepared_data == [
        {'id': '1', 'first_name': 'Idaline', 'last_name': 'Murrell', 'email': 'imurrell0@yale.edu', 'gender': 'Female',
         'age': '42'}]
