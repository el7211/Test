import pytest

def test_area(my_rectangle):
    assert my_rectangle.area() == 200


def test_perimeter(my_rectangle):
    assert my_rectangle.perimeter() == 60

def test_not_eqal(my_rectangle, wierd_rectangle):
    assert my_rectangle != wierd_rectangle