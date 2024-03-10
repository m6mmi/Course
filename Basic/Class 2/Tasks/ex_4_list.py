# print 1st empty line
print()
# ask names from user
name_1 = input('Enter name to append: ').capitalize()
name_2 = input('Enter name to insert: ').capitalize()
# print empty line
print()
# create list
name_list = ['Diana', 'Tõnis', 'Indrek', 'Jaan', 'Karola']
# append name to list and check if it already exists
if name_1 in name_list:
    print(f'{name_1} is already in the list!')
else:
    name_list.append(name_1)
# insert name at the beginning and check if it already exists
if name_2 in name_list:
    print(f'{name_2} is already in the list!')
else:
    name_list.insert(0, name_2)
# sort list alphabetically
name_list.sort()
# reverse list
name_list.reverse()
# get name indexes
name_append = name_list.index(name_1)
name_insert = name_list.index(name_2)
# let's create nice print for list
x = 0
for i in name_list:
    name_index = name_list.index(i)
    x += 1
    if x == len(name_list):
        print(f"{name_index}: {i}", end="\n\n")
    else:
        print(f"{name_index}: {i}", end=", ")
# print entered name indexes in list
print(f'{name_1} appended and index is {name_append}.\n'
      f'{name_2} inserted and index is {name_insert}.')
