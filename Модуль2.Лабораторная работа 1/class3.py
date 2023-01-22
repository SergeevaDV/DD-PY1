import doctest
from typing import Union
class BodyCondition:
    def __init__(self, temperature: Union[int, float], well_being: bool, mood: bool):
        """
        Данная программа помогает определить на базовом уровне состояние организма.
        :param temperature: Температура организма на данный момент
        :param well_being: Самочувствие
        :param mood: Настроение
        """
        if not isinstance(temperature, (int, float)):
            raise TypeError("Температура может быть только типа int или float ")
        if temperature <= 30 or temperature >= 40:
            raise ValueError("Температура не может быть меньше 30 или превышать 40")
        """
        В данном случае рассматриваем температуру человека.
        """
        self.temperature = temperature

        self.well_being = None
        self.well_being_boby()

        self.mood = None
        self.mood_body()

    def well_being_boby(self) -> bool:
        """
        Определяем самочувствие, если True - то все хорошо, если Flase - плохо(есть какие-то отклонения).
        :return: Хорошо ли человек чувствует себя
        """
        ...
    def mood_body(self) -> bool:
        """
        Определяем настроение человека, если True - то все хорошо, если Flase - плохо(есть какие-то отклонения).

        :return: Является ли настроение отличным
        """
        ...
    def temperature_body(self, elevated_temperature: Union[int, float]):
        """
        В этой функции рассматриваем повышение температуры и при какой температуре нужно обращаться к врачу.
        :param elevated_temperature: разница между повышенной температурой и нормальной
        За нормальную температуру будет считать до 37 градусов.
        :return: Получение значения повышенной температуры.
        При повышенной температуры лучше вызвать врача
        >>> temperature += elevated_temperature
        >>> temperature.temperature_body()
        """
if __name__ == "__main__":
    doctest.testmod()
    pass
