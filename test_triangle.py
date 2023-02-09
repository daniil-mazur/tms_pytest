from triangle.triangle import Triangle


class TestTrianglePtest:

    def test_triangle_exist(self):
        assert Triangle.check_if_exist(7, 8, 100)

    def test_triangle_eq(self):
        first = Triangle(7, 8, 9)
        second = Triangle(9, 8, 7)
        assert first == second

    def test_triangle_lt(self):
        first = Triangle(7, 8, 9)
        second = Triangle(9, 10, 11)
        assert first < second

    def test_triangle_right(self, right_triangle):
        assert right_triangle.is_right_triangle()
