import pytest


@pytest.fixture()
def text_1():
    # 6 vowels
    return "AAA eeE kkK"


@pytest.fixture()
def text_2():
    # 102 vowels
    return ("Cake gummies sweet donut dessert ice cream sweet roll chupa chups biscuit. Chocolate cake lemon drops "
            "tootsie roll tootsie roll soufflé bonbon cotton candy topping lollipop. Ice cream soufflé macaroon "
            "dessert lemon drops dragée dragée fruitcake. Cake candy canes biscuit chocolate chupa chups danish candy "
            "chocolate icing.")
