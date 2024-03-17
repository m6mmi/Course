def calculate_distance(steps_cm, length):
    steps_meters = [step / 100 * length for step in steps_cm]  # Convert steps from centimeters to meters
    distance_km = sum(steps_meters) / 1000  # Convert total steps from meters to kilometers
    return distance_km


def process_entries(input_filename, output_filename):
    grade_data = {}  # Dictionary to store grade-wise valid entries and distance covered.
    with open(input_filename, 'r') as input_file:
        num_participants = int(input_file.readline().strip())  # number of lines is the number of participants
        for _ in range(num_participants):
            grade, step_length, *steps = map(int, input_file.readline().split())
            if 0 not in steps:  # If steps entry for at least 1 day is not 0
                distance_covered = calculate_distance(steps, step_length)
                if grade in grade_data:
                    grade_data[grade]['count'] += 1
                    grade_data[grade]['distance'] += distance_covered
                else:
                    grade_data[grade] = {'count': 1, 'distance': distance_covered}
        # Write results to the output file
    with open(output_filename, 'w') as output_file:
        for grade, data in grade_data.items():
            output_file.write(f"{grade} {data['count']} {data['distance']:.2f}\n")


# Example usage:
process_entries("u1.txt", "u1result_1.txt")
