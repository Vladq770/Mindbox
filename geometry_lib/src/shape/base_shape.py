from abc import ABC, abstractmethod


class BaseShape(ABC):
    """Абстрактный базовый класс для геометрических фигур."""

    def __init__(self, accuracy: float = 1e-6):
        self.accuracy = accuracy

    @property
    @abstractmethod
    def area(self) -> float | int:
        """
        Площадь фигуры.

        Returns:
            Площадь фигуры.
        """

    @abstractmethod
    def _validate(self, *args, **kwargs) -> None:
        """Провалидировать параметры, при создании фигуры."""
