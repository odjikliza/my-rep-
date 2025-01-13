import math


class GeometricFigure:
    """
    Базовый класс для геометрических фигур.
    """

    def __init__(self, name: str, color: str = "бесцветный"):
        """
        Конструктор базового класса.

        Args:
            name (str): Название фигуры.
            color (str, optional): Цвет фигуры. Defaults to "бесцветный".
        """
        self.name = name  # публичное свойство
        self._color = color  # приватное свойство, доступ ограничен

    def __str__(self) -> str:
        """
        Строковое представление фигуры.
        """
        return f"Геометрическая фигура: {self.name}, цвет: {self._color}"

    def __repr__(self) -> str:
        """
        Представление для отладки.
        """
        return f"{type(self).__name__}(name='{self.name}', color='{self._color}')"

    def area(self) -> float:
        """
        Вычисляет площадь фигуры. (базовый метод, должен быть перегружен в дочерних классах)
        """
        raise NotImplementedError("Метод area должен быть переопределен в дочернем классе.")

    def describe(self) -> str:
        """
        Возвращает общее описание фигуры.
        """
        return f"Это геометрическая фигура под названием {self.name}."


class Circle(GeometricFigure):
    """
    Класс для круга.
    """

    def __init__(self, name: str, radius: float, material: str = "неизвестный"):
        """
        Конструктор класса Circle.

        Args:
            name (str): Название круга.
            radius (float): Радиус круга.
            material (str, optional): Материал круга. Defaults to "неизвестный".
        """
        super().__init__(name, color="Синий")  # вызов конструктора родительского класса
        self._radius = radius  # _radius - инкапсуляция, для доступа используется геттер
        self.__material = material  # приватное свойство, доступ строго ограничен

    def __str__(self) -> str:
        """
        Перегруженный метод __str__ для класса Circle.
        """
        return f"Круг: {self.name}, радиус: {self._radius:.2f}, цвет: {self._color}, материал: {self.__material}"

    def __repr__(self) -> str:
        """
        Перегруженный метод __repr__ для класса Circle.
        """
        return f"Circle(name='{self.name}', radius={self._radius}, material='{self.__material}')"

    @property
    def radius(self) -> float:
        """
        Возвращает радиус круга. Геттер для инкапсулированного свойства _radius
        """
        return self._radius

    def area(self) -> float:
        """
        Переопределенный метод area для вычисления площади круга.
        """
        return math.pi * self._radius * 2

    def circumference(self) -> float:
        """
        Вычисляет длину окружности.
        """
        return 2 * math.pi * self._radius

    def describe(self) -> str:
        """
        Перегруженный метод describe для предоставления более подробного описания круга.
        """
        base_description = super().describe()  # вызов метода родительского класса
        return f"{base_description} Он имеет радиус {self._radius} и материал {self.__material}."
