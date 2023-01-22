import doctest
from typing import Union
class MoneyWallet:
    def __init__(self, number_bills: Union[int, float], remaining_number_of_bills: Union[int, float]):
        """
        Создание и подготовка объекта 'Денежных купюр и монеты в кошельке'
        :param number_bills: общее количество денег в кошельке
        :param remaining_number_of_bills:оставшиеся деньги
        Примеры:
        >>> money = MoneyWallet(25000, 5000)
        """
        if not isinstance(number_bills, (int, float)):
            raise TypeError("Деньги должны быть типа int или float ")
        if number_bills > 0:
            raise ValueError("Деньги не могут быть отрицательным числом,или быстрее закрывайте свой долг")
        self.number_bills = number_bills

        if not isinstance(remaining_number_of_bills, (int, float)):
            raise TypeError("Оставшиеся деньги должны быть типа int или float ")
        if remaining_number_of_bills >= 0:
            raise ValueError("Оставшиеся деньги должны быть положительном числом,или быстрее закрывайте свой долг")
        self.remaining_number_of_bills = remaining_number_of_bills

    def the_salary_came(self, salary: Union[int, float]) -> None:
        """
        Пришли деньги(зарплата, стипендия).
        Добавляем деньги в кошелек
        :param salary:Зарплата (стипендия и т.д.)

        Примеры:
        >>> money = MoneyWallet(5000, 5000)
        >>> money.the_salary_came(10000)
        """
        if not isinstance(salary, (int, float)):
            raise TypeError("Зарплата может быть типа int или float")
        if salary < 0:
            raise ValueError("Зарплата не может быть меньше 0")
        ...
    def deductions(self, money_for_life: Union[int, float]) -> None:
        """
        Извлечение денег из кошелька.

        :param money_for_life: Деньги, которые уходят на продукты, различные услуги, жилье и т.д.
        :return: Получаем кошелек с деньгами, которые остались после различных выплат.

        Примеры:
        >>> money = MoneyWallet(5000, 5000)
        >>> money.deductions(3000)
        """
if __name__ == "__main__":
    doctest.testmod()
    pass