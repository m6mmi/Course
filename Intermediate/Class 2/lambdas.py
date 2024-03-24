def function_sum(x):
    return x + 5


function_sum(9)

l_sum = lambda x: x + 5

l_sum(9)

# Anonymous lambda function(function has no name) --- 2 and 9 is parameter passed to lambda function
print((lambda x, y: x * y)(2, 9))

# example list
example_list = [2, 3, 4, 5, 6, 7, 8, 9, 0]

# filter
filter_result = list(filter(lambda x: x % 2 == 0, example_list))
print(filter_result)

# function map
map_result = list(map(lambda x: x + 2, example_list))
print(map_result)
list_method = [x + 2 for x in example_list]
print('function map comprehension:', list_method)

# sorting
example_list_sort = [[1, 3], [3, 1], [4, 2], [2, 4], [1, 2]]

simple_sorted = sorted(example_list)
print(simple_sorted)

# sort list by first char
simple_sorted = sorted(example_list_sort)
print(simple_sorted)

# solt list by second char
smarter_sorted = sorted(example_list_sort, key=lambda x: x[1])
print(smarter_sorted)
