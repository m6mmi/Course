cars = ["VW", "Audi", "BMW"]
print(cars)

# Adding values to the list
cars.append("Zap")
cars.append("Cupra")
print(cars)

# Lenght of car list
print(f"Cars in the list {len(cars)}")

# Joining list
cars.extend(["Nissan", "Volvo", "Opel", "VW"])
print(cars)

# Sort the list
cars.sort()
print(cars)

# Get a count of certain values
print(f"Amount VolksWagens in the list: {cars.count("VW")}")

# Index of Cupra
index_of_cupra = cars.index("Cupra")
print(f"Index of Opel is: {index_of_cupra}")

# Inserting at certaini index
cars.insert(index_of_cupra, "Opel")
print(cars)

# remove from list
cars.pop(index_of_cupra) # removes by index
cars.remove("VW") # removes by name
cars.pop() # removes last item
print(cars)

# reverse list
cars.reverse()
print(cars)

for i in cars:
    print(f"{i}", end=", ")


cars.clear()
print(f"\n\n{cars}")
