from triangle.triangle import Triangle
import pytest


class TestTrianglePtest:

    @pytest.mark.parametrize("a, b, c",
                             [(7, 8, 9), (9, 7, 8)])
    def test_triangle_eq(self, a, b, c):
        first = Triangle(a, b, c)
        second = Triangle(9, 8, 7)
        assert first == second

    def test_triangle_lt(self):
        first = Triangle(7, 8, 9)
        second = Triangle(9, 10, 11)
        assert first < second

    def test_triangle_right(self, right_triangle):
        assert right_triangle.is_right_triangle()

    def test_triangle_rb(self, rb_triangle):
        assert rb_triangle.two_sides_eq()

    @pytest.mark.parametrize("a, b, c",
                             [(7, 8, 9), (9, 7, 8)])
    def test_triangle_rb_2(self, rb_triangle, a, b, c):
        assert rb_triangle.two_sides_eq()
        first = Triangle(a, b, c)
        second = Triangle(9, 8, 7)
        assert first == second
