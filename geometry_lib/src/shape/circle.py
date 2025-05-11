import math

from src.shape.base_shape import BaseShape


class Circle(BaseShape):
    """Класс, описывающий круг."""

    def __init__(self, radius: float | int, accuracy: float = 1e-6):
        self._validate(radius)
        super().__init__(accuracy=accuracy)
        self.radius = radius

    @property
    def area(self) -> float:
        """
        Получить площадь круга.

        Returns:
            Площадь круга.
        """
        return math.pi * self.radius**2

    def _validate(self, radius: float | int) -> None:
        """
        Провалидировать радиус.

        Raises:
            ValueError: Если радиус меньше или равен 0.
        """
        if radius > 0:
            return

        raise ValueError(f"Incorrect radius value: {radius}. Value must be positive")
