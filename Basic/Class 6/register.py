# import text codecs for utf-8
import codecs
# import os to check if file exists
import os
# define file name variable used in program
file_name = "entries.txt"


class Entry:
    def __init__(self, id, name='', age='', city='', potato_count=''):
        self.id = id
        self.name = name
        self.age = age
        self.city = city
        self.potato_count = potato_count

    # define how data is writen to file
    def form_entry(self):
        return f"{self.id}, {self.name}, {self.age}, {self.city}, {self.potato_count}\n"

    # ask user data in each line and assign to object
    def get_user_data(self):
        print("Provide the following information please: ")
        self.name = input("Name: ")
        self.age = input("Age: ")
        self.city = input("City: ")
        self.potato_count = input("Potatoes consumed: ")

    def announcement(self):
        print(f"The participant {self.name}, aged {self.age} years old, coming from {self.city} have "
              f"destroyed {self.potato_count} potatoes!")


# greeting
print("Hello to the great potato eating competition!")
# define id counter variable
id_counter = 0
# define empty entries list
entries = []

# Check if the file already exists. If not, then create a new one. This will be faster than "with open" for bigger files
if os.path.exists(file_name):
    pass
else:
    with open(file_name, "w"):
        print(f"{file_name} will be created after exit and save.")
        pass

# open file and use utf-8 coding
with codecs.open(file_name, "r+", "utf-8") as f:
    # in the first line read key values
    headers = f.readline()
    # if there are no key values, then create them
    if headers == "":
        f.write("id, name, age, city, potato_count\n")
    else:
        # create a list of values where each line in text file is separate value
        records = f.readlines()
        # create an object from lines read before
        for record in records:
            # remove any empty spaces and commas
            line = record.strip().split(",")
            # append values to object and add an object to a previously created empty list
            entries.append(Entry(line[0], line[1], line[2], line[3], line[4]))

# assign value to id_counter for later use
id_counter = int(line[0])
# before continuing, create variable last_id so that code will write only new values in file.
last_id = id_counter


while True:
    # ask user input
    user_action = input("a - Add an entry\n"
                        "v - View the entries\n"
                        "x - Exit and save\n"
                        ">>> ")
    # add a new object
    if user_action.lower() == 'a':
        # add +1 to the last known id for a new object
        id_counter += 1
        # assign id to a temporary object
        entry = Entry(id_counter)
        # call class function to get user data and add them to a temporary object accordingly
        entry.get_user_data()
        # append a temporary object to an entry list
        entries.append(entry)
    # announce each object from a list in console
    elif user_action.lower() == "v":
        for entry in entries:
            entry.announcement()
    # exit from loop
    elif user_action.lower() == 'x':
        break

# open file to append with utf-8 codecs
with codecs.open(file_name, "a", "utf-8") as f:
    # go through a list of an object
    for entry in entries:
        # If entry.id > last id already in the file:
        # compare last id in file with id's that will be entered. If id is not in file, then write new line in file
        if int(entry.id) > last_id:
            f.write(entry.form_entry())

# output after exiting program
print("You have earned one beer! ")
