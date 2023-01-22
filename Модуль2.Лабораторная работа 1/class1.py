import doctest
from typing import Union


def classic_skiing(height: int, additional_length_classic: int):
    """
    С помощью этой функции можно подобрать классические лыжи под ваш рост ( в этом случае рассматриваются взрослые рост от 155 см).
    Чтобы узнать какая длина лыж вам подойдет, то нужно к вашему росту прибавить добовочную длину ( + 5-15 см к росту).
    :param height: Рост человека(ваш рост)
    :param additional_length_classic: Добавочная длина лыж. Вданном случае будем использовать среднее 10 см.
    :return: Подбор длинны лыж индивидуально для каждого человека
    Примеры:
    >>> length = height + additional_length_classic
    >>> ski = Ski(4.4, length)
    """
    if not isinstance(height, int):
        raise TypeError("Рост должен быть типа int")
    if height >=155 or height <= 272:
        raise ValueError("Рост взрослого не должен быть меньше 155 или выше 272")
    ...


class Ski:
    def __init__(self, width: Union[int, float], length: Union[int, float]):
        """
        Создание и подготовка объекта Лыжи
        :param width: ширина лыж
        :param length: длина
        Ширина спортивных лыж обычно не больше 44мм=4,4см, прогулочные лыжи обычнопоширине 50мм, туристические или бэккантри лыжи 60-70 мм.
        В данном случае мы будем рассматривать длину и ширину беговых лыж.

        Пример:
        >>> ski = Ski(4.4, 185)
        """
        if not isinstance(width, Union[int, float]):
            raise TypeError("Ширина лыж должна быть типа int или float")
        if width < 4.4:
            raise ValueError("Ширина спортивных лыж не может быть меньше 4.4 см ")
        self.width = width

        if not isinstance(length, (int, float)):
            raise TypeError("Длина лыж должна быть типа int или float")
        if length <= 0:
            raise ValueError("Длина лыж должна быть положительной ")
        self.length = length

    def abult(self) -> bool:
        """
        В данном методе выясняем является ли человек взрослым (то есть человек,который выше 155)
        :return: Является ли человек выше 155 см, если нет, то нужно смотреть другие параметры(например, для детей)
        >>> ski = Ski(4.4, 165)
        >>> ski.abult()
        """
        ...


def skis_for_skating(self, height: int, additional_length_skating: int):
        """
        С помощью этой функции можно подобрать лыжи для конькового хода под ваш рост ( в этом случае рассматриваются взрослые рост от 155 см).
        Чтобы узнать какая длина лыж вам подойдет, то нужно к вашему росту прибавить добовочную длину ( + 20-30 см к росту).
        :param height: Рост человека(ваш рост)
        :param additional_length_skating: Добавочная длина лыж. Вданном случае будем использовать среднее 25 см.
        :return: Подбор длинны лыж индивидуально для каждого человека
        Примеры:
        >>> length = height + additional_length_skating
        >>> ski = Ski(4.4, 195)
        """
        if not isinstance(height, int):
            raise TypeError("Рост должен быть типа int")
        if height >=155 or height <= 272:
            raise ValueError("Рост взрослого не должен быть меньше 155 или выше 272")
        ...
if __name__ == "__main__":
    doctest.testmod()
    pass
