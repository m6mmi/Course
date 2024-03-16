def prepare_data(file):
    # Read the first line from file as headers and make a list from these. Remove empty spaces and split where ',' is.
    headers = file.readline().strip().split(',')
    # Read the rest of the files as data
    content = file.readlines()
    # New empty list.
    result_list = []
    # Iterate through data
    for line in content:
        # For each line in content, create a list
        record = line.strip().split(',')
        # New empty directory for every value in content
        content_with_headers = {}
        # Iterate through values in a list
        for index, value in enumerate(record):
            # Add key: value pair in a new empty dictionary
            content_with_headers[headers[index]] = value
        # Append newly created dictionary to a directory list
        result_list.append(content_with_headers)

    return result_list


def filter_underage(people_list):
    # Iterate through a directory list
    for index, person in enumerate(people_list):
        # Check if age value in directory is under 18 years. If it is then remove it from a list
        if int(person['age']) < 18:
            people_list.pop(index)

    return people_list


with open('real.csv', 'r') as f:
    new_list = prepare_data(f)
    filter_underage(new_list)
    print(new_list)

