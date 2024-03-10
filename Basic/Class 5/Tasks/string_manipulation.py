text = ("Cupcake ipsum dolor sit amet cupcake jelly. Jelly-o I love jujubes biscuit liquorice. "
        "Candy canes chocolate bar I love donut lemon drops. "
        "Cake jelly-o topping lemon drops marshmallow chocolate bar gingerbread.")


def modify(original):
    return original.replace(" ", "_").lower()


print(modify(text))
