# Importing the necessary modules
import codecs  # Module for handling file encoding
import os      # Module for interacting with the operating system

# Define the filename for storing entries
file_name = "entries.txt"


# Define the Entry class to represent individual entries
class Entry:
    def __init__(self, id, name='', age='', city='', potato_count=''):
        """
        Initialize an Entry object with provided attributes.
        """
        self.id = id
        self.name = name
        self.age = age
        self.city = city
        self.potato_count = potato_count

    # Define a method to format entry data for writing to file
    def form_entry(self):
        """
        Format entry data as a string to be written to the file.
        """
        return f"{self.id}, {self.name}, {self.age}, {self.city}, {self.potato_count}\n"

    # Define a method to prompt the user for entry data
    def get_user_data(self):
        """
        Prompt the user to provide entry data and assign it to object attributes.
        """
        print("Provide the following information please: ")
        self.name = input("Name: ")
        self.age = input("Age: ")
        self.city = input("City: ")
        self.potato_count = input("Potatoes consumed: ")

    # Define a method to print an announcement about the entry
    def announcement(self):
        """
        Print an announcement about the entry.
        """
        print(f"The participant {self.name}, aged {self.age} years old, coming from {self.city} have "
              f"destroyed {self.potato_count} potatoes!\n")

    # Define a method to print the entry index and name
    def entry_idx(self):
        """
        Print the entry index and name.
        """
        print(f"{self.id}: {self.name}")


# Print a greeting for the user
print("Hello to the great potato eating competition!")

# Initialize variables
id_counter = 0
entries = []

# Check if the file already exists. If not, create a new one
if os.path.exists(file_name):
    pass
else:
    with open(file_name, "w"):
        print(f"{file_name} will be created after exit and save.")
        pass

# Open the file and handle utf-8 encoding
with codecs.open(file_name, "r+", "utf-8") as f:
    # Read the headers to determine if the file is empty
    headers = f.readline()
    # If the file is empty, write headers
    if headers == "":
        f.write("id, name, age, city, potato_count\n")
    else:
        # Read existing records and create Entry objects
        records = f.readlines()
        for record in records:
            line = record.strip().split(",")
            entries.append(Entry(line[0], line[1], line[2], line[3], line[4]))

# Set the id_counter to the last id in the file
id_counter = int(line[0])
last_id = id_counter

# Main loop for user interaction
while True:
    print()
    # Prompt user for action
    user_action = input("a - Add an entry\n"
                        "v - View the entries\n"
                        "x - Exit and save\n"
                        ">>> ")
    # Add a new entry
    if user_action.lower() == 'a':
        id_counter += 1
        entry = Entry(id_counter)
        entry.get_user_data()
        entries.append(entry)
    # View existing entries
    elif user_action.lower() == "v":
        print()
        for entry in entries:
            entry.entry_idx()
        print()
        while True:
            user_choice = input("Choose number\n"
                                "x - Exit to main menu\n"
                                ">>> ")
            try:
                user_choice = int(user_choice) - 1
                print()
                entries[user_choice].announcement()
            except ValueError:
                break
    # Exit the program
    elif user_action.lower() == 'x':
        break

# Append new entries to the file
with codecs.open(file_name, "a", "utf-8") as f:
    for entry in entries:
        if int(entry.id) > last_id:
            f.write(entry.form_entry())

# Exit message
print("You have earned one beer! ")
