# Add any number of arguments
def add_ingredients(**kwargs):
    result = 0
    for key in kwargs:
        result += kwargs[key]
        print(key, kwargs[key])
    return result


print(add_ingredients(eggs=3, spam=5, cheese=2))