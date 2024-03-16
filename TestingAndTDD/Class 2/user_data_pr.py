def prepare_data(file):
    headers = file.readline().strip().split(',')
    content = file.readlines()
    result_list = []

    for line in content:
        record = line.strip().split(',')
        content_with_headers = {}
        for index, value in enumerate(record):
            content_with_headers[headers[index]] = value
        result_list.append(content_with_headers)

    return result_list


with open('real.csv', 'r') as f:
    print(prepare_data(f))
