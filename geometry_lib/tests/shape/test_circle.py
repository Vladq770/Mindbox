import math

import pytest

from src.shape.circle import Circle


class TestCircle:
    @pytest.mark.parametrize(
        "radius",
        [0, -1, 0.0, -3.33],
    )
    def test_validate_circle(self, radius):
        with pytest.raises(
            ValueError,
            match=f"Incorrect radius value: {radius}. Value must be positive",
        ):
            Circle(radius)

    @pytest.mark.parametrize(
        "radius",
        [1, 2, 3.213, 0.213],
    )
    def test_get_area(self, radius):
        circle = Circle(radius)
        assert circle.area == math.pi * radius**2

    def test_default_accuracy(self):
        circle = Circle(123)
        assert circle.accuracy == 1e-6

    def test_custom_accuracy(self):
        circle = Circle(123, accuracy=0.01)
        assert circle.accuracy == 0.01
