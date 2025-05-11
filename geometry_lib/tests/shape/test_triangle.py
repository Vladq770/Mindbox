import pytest

from src.shape.triangle import Triangle


class TestTriangle:
    @pytest.mark.parametrize(
        "sides, exception",
        [
            ((1, 2, 3), "Triangle with the given sides cannot exist"),
            ((1, 2, 4), "Triangle with the given sides cannot exist"),
            ((3, 2, 1), "Triangle with the given sides cannot exist"),
            ((4, 2, 1), "Triangle with the given sides cannot exist"),
            ((-1, 2, 1), "Incorrect side value"),
            ((0, 2, 2), "Incorrect side value"),
            ((1, -1.0, 1), "Incorrect side value"),
            ((2, 2, 0.0), "Incorrect side value"),
        ],
    )
    def test_validate_triangle(self, sides, exception):
        with pytest.raises(ValueError, match=exception):
            Triangle(*sides)

    @pytest.mark.parametrize(
        "sides",
        [
            (1, 2, 2),
            (1, 2.0, 2.0),
            (3, 4, 5),
            (1, 2, 2.99999),
        ],
    )
    def test_get_area(self, sides):
        triangle = Triangle(*sides)
        p = sum(sides) / 2
        assert (
            triangle.area
            == (p * (p - sides[0]) * (p - sides[1]) * (p - sides[2])) ** 0.5
        )

    def test_default_accuracy(self):
        triangle = Triangle(1, 1, 1)
        assert triangle.accuracy == 1e-6

    def test_custom_accuracy(self):
        triangle = Triangle(1, 1, 1, accuracy=0.01)
        assert triangle.accuracy == 0.01

    @pytest.mark.parametrize(
        "sides, is_right",
        [
            ((1, 2, 2), False),
            ((3, 4, 5), True),
            ((1, 2.1, 2), False),
            ((3.0, 4, 5.0000000000000001), True),
            ((3.0, 4, 5.001), False),
        ],
    )
    def test_is_right(self, sides, is_right):
        triangle = Triangle(*sides)
        assert triangle.is_right == is_right
