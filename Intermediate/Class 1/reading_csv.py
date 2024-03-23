import csv

with open('csv_source.csv', 'r') as f:
    read_file = csv.DictReader(f)
    headers = read_file.fieldnames
    data = [row for row in read_file]

with open('csv_output_1.csv', 'w', newline='') as output:
    writer = csv.DictWriter(output, fieldnames=headers)
    writer.writeheader()
    writer.writerows(data)



# other way
with open('csv_source.csv', 'r') as f:
    data = [row for row in csv.DictReader(f)]

with open('csv_output.csv', 'w', newline='') as output:
    headers = data[0].keys()
    writer = csv.DictWriter(output, fieldnames=headers)

    writer.writeheader()
    writer.writerows(data)