import pytest
from triangle.triangle import Triangle


@pytest.fixture()
def right_triangle():
    right_tr = Triangle(6, 6, 6)
    yield right_tr
    del right_tr


@pytest.fixture(params=[(3, 3, 4), (8, 8, 10)])
def rb_triangle(request):
    rb_tr = Triangle(request.param[0], request.param[1], request.param[2])
    yield rb_tr
    del rb_tr
