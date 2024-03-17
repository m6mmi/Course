import fns

# Read data from file
data = fns.read_file("u1.txt")

# Remove lines where there is 0-steps day and sum distances by grade
processed_data = fns.process_data(data)

# Write data to file
fns.write_data("u1.results.txt", processed_data)
