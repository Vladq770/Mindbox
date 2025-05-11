from src.shape.base_shape import BaseShape


class Triangle(BaseShape):
    """Класс, описывающий треугольник."""

    def __init__(
        self,
        a_side: float | int,
        b_side: float | int,
        c_side: float | int,
        accuracy: float = 1e-6,
    ):
        self._validate(a_side, b_side, c_side)
        super().__init__(accuracy=accuracy)
        self.a_side = a_side
        self.b_side = b_side
        self.c_side = c_side

    @property
    def area(self) -> float:
        """
        Получить площадь треугольника.

        Returns:
            Площадь треугольника.
        """
        p = (self.a_side + self.b_side + self.c_side) / 2
        return (p * (p - self.a_side) * (p - self.b_side) * (p - self.c_side)) ** 0.5

    @property
    def is_right(self) -> bool:
        """
        Является ли треугольник прямоугольным.

        Returns:
            True: Треугольник прямоугольный.
            False: Иначе.
        """
        sides = [self.a_side, self.b_side, self.c_side]
        sides.sort()
        return abs(sides[0] ** 2 + sides[1] ** 2 - sides[2] ** 2) < self.accuracy

    def _validate(
        self, a_side: float | int, b_side: float | int, c_side: float | int
    ) -> None:
        """
        Провалидировать стороны треугольника.

        Raises:
            ValueError: 1. Если сторона меньше или равна 0.
                        2. Если значения сторон не соответствуют свойству треугольника.
        """
        sides = [a_side, b_side, c_side]

        for side in sides:
            if side <= 0:
                raise ValueError(
                    f"Incorrect side value: {side}. Value must be positive"
                )

        sides.sort()
        if sides[-1] >= sides[0] + sides[1]:
            raise ValueError(f"Triangle with the given sides cannot exist: {sides}")
