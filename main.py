# TODO Написать 3 класса с документацией и аннотацией типов
import doctest

class Table:
    def __init__(self, material: str, size: tuple[int, int]):
        """
        Создание и подготовка к работе объекта "Стол"

        :param material: Материал, из которого изготовлен стол
        :param size: Размеры стола (длина, ширина) в см

        Примеры:
        >>> table = Table("wood", (120, 80))  # инициализация экземпляра класса
        """
        if not isinstance(material, str):
            raise TypeError("Материал должен быть строкой")
        if not isinstance(size, tuple) or len(size) != 2 or not all(isinstance(x, int) and x > 0 for x in size):
            raise ValueError("Размер должен быть кортежем из двух положительных чисел")

        self.material = material
        self.size = size

    def is_wooden(self) -> bool:
        """
        Проверка, сделан ли стол из дерева.

        :return: True, если материал стола дерево, иначе False

        Примеры:
        >>> table = Table("wood", (120, 80))
        >>> table.is_wooden()
        True
        >>> table = Table("metal", (120, 80))
        >>> table.is_wooden()
        False
        """
        return self.material.lower() == "wood"

    def resize(self, new_size: tuple[int, int]) -> None:
        """
        Изменение размеров стола.

        :param new_size: Новый размер стола (длина, ширина) в см
        :raise ValueError: Если размеры некорректны

        Примеры:
        >>> table = Table("wood", (120, 80))
        >>> table.resize((150, 90))
        >>> table.size
        (150, 90)
        """
        if not isinstance(new_size, tuple) or len(new_size) != 2 or not all(isinstance(x, int) and x > 0 for x in new_size):
            raise ValueError("Размер должен быть кортежем из двух положительных чисел")
        self.size = new_size


class Tree:
    def __init__(self, height: float, age: int):
        """
        Создание и подготовка к работе объекта "Дерево"

        :param height: Высота дерева в метрах
        :param age: Возраст дерева в годах

        Примеры:
        >>> tree = Tree(5.0, 10)  # инициализация экземпляра класса
        """
        if not isinstance(height, (int, float)) or height <= 0:
            raise ValueError("Высота должна быть положительным числом")
        if not isinstance(age, int) or age < 0:
            raise ValueError("Возраст не может быть отрицательным числом")

        self.height = height
        self.age = age

    def grow(self, years: int) -> None:
        """
        Увеличение возраста и высоты дерева.

        :param years: Количество лет для роста
        :raise ValueError: Если передано некорректное количество лет

        Примеры:
        >>> tree = Tree(5.0, 10)
        >>> tree.grow(5)
        >>> tree.age
        15
        >>> tree.height
        7.5
        """
        if not isinstance(years, int) or years <= 0:
            raise ValueError("Количество лет должно быть положительным целым числом")
        self.age += years
        self.height += years * 0.5  # Допустим, дерево растет на 0.5 м в год

    def is_ancient(self) -> bool:
        """
        Проверка, является ли дерево старым (возраст > 100 лет).

        :return: True, если возраст дерева больше 100 лет, иначе False

        Примеры:
        >>> tree = Tree(5.0, 101)
        >>> tree.is_ancient()
        True
        >>> tree = Tree(5.0, 50)
        >>> tree.is_ancient()
        False
        """
        return self.age > 100


class Facebook:
    def __init__(self, user_count: int, name: str):
        """
        Создание и подготовка к работе объекта "Facebook"

        :param user_count: Количество пользователей
        :param name: Название платформы

        Примеры:
        >>> fb = Facebook(1000000, "Facebook")  # инициализация экземпляра класса
        """
        if not isinstance(user_count, int) or user_count < 0:
            raise ValueError("Количество пользователей должно быть неотрицательным целым числом")
        if not isinstance(name, str) or not name:
            raise ValueError("Название платформы должно быть непустой строкой")

        self.user_count = user_count
        self.name = name

    def add_user(self, count: int) -> None:
        """
        Добавление новых пользователей.

        :param count: Количество добавляемых пользователей
        :raise ValueError: Если количество добавляемых пользователей отрицательное

        Примеры:
        >>> fb = Facebook(1000000, "Facebook")
        >>> fb.add_user(1000)
        >>> fb.user_count
        1001000
        """
        if not isinstance(count, int) or count < 0:
            raise ValueError("Количество добавляемых пользователей должно быть неотрицательным целым числом")
        self.user_count += count

    def remove_user(self, count: int) -> None:
        """
        Удаление пользователей.

        :param count: Количество удаляемых пользователей
        :raise ValueError: Если количество удаляемых пользователей больше текущего количества

        Примеры:
        >>> fb = Facebook(1000000, "Facebook")
        >>> fb.remove_user(500)
        >>> fb.user_count
        999500
        >>> fb.remove_user(2000000)  # вызовет ошибку
        Traceback (most recent call last):
        ...
        ValueError: Нельзя удалить больше пользователей, чем есть
        """
        if not isinstance(count, int) or count < 0:
            raise ValueError("Количество удаляемых пользователей должно быть неотрицательным целым числом")
        if count > self.user_count:
            raise ValueError("Нельзя удалить больше пользователей, чем есть")
        self.user_count -= count

if __name__ == "__main__":
    doctest.testmod()
    pass
