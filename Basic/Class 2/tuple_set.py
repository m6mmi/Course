# list_var = []
# dictionary_var = {'key': 'value'}
# tuple_var = ()
# set_var = {'value', 'value', 'value'}

# Tuple --> Immutable data structure
magic_list = ('dog', 'cat', 2000, 5, True)

print(magic_list.count('dog'))
print(magic_list.index('dog'))
print(magic_list[2])


# # Set
# emty_list = list()
# emty_set = set()

the_set = {'dog', 'cat', 'elephant'}
# Adding value
the_set.add('mouse')
print(the_set)
# Removing values
the_set.remove('mouse')
print(the_set)
# Advantage is if you add something then it will remove duplicate.
the_set.add('cat')
print(the_set)

# example to use set variable usefuly
example_list = [1,1,1,1,1,2,3,5,6,7,8,4,3,2,4,6,7]
print(example_list)
# Remove duplicates
print(list(set(example_list)))
# Reverse and remove duplicates
new_list = list(set(example_list))
new_list.reverse()
print(new_list)