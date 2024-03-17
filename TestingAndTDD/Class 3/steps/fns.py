def read_file(file_name):# read data from file
    with open(file_name, 'r') as f:
        participants = f.readline()
        results = f.readlines()

    # create a list from a result in file
    return [line.strip().replace(' ', ',').split(',') for line in results]


def process_data(input_list):
    # remove a result where is 0 steps day
    clean_records = [line for line in input_list if '0' not in line[2:]]

    # empty list for results
    out_list = []

    # iterate through lines and make a list with student grade and total distance in km
    for i in clean_records:
        # calculate total steps for each line
        total_steps = 0
        grade = int(i[0])
        step_length = int(i[1])
        for steps in i[2:]:
            total_steps += int(steps)
            # calculate distance for each student (/100 = meters) (/1000 = km)
        student_distance = round(total_steps * step_length / 100 / 1000, 2)
        # Add line to an out list. If same grade then add results
        out_list.append([grade, student_distance])

    # Temporary dictionary's to sum distance and how many times
    temp_dict = {}
    count = {}
    # Iterate through a list and use grade as key and distance as value
    for key, value in out_list:
        # Count how many times grades are present. If key is already in the list, then add +1
        count[key] = count.get(key, 0) + 1
        # For each key, add distance as value. If key(grade) is already in the dictionary, then add to existing value
        temp_dict[key] = temp_dict.get(key, 0) + value

    # Create a final list from dictionary's created before
    return [[key, count[key], temp_dict[key]] for key in temp_dict]


def write_data(out_file_name, clean_data):
    # Create a new file and write a list in to it line by line
    with open(out_file_name, 'w') as f:
        for i in clean_data:
            f.write(f'{str(i[0])} {str(i[1])} {str(i[2])}\n')


if __name__ == "__main__":
    data = (read_file("u1.txt"))
    processed_data = process_data(data)
    write_data("u1.results.txt", processed_data)
