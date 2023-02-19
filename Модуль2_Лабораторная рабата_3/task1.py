class Book:
    """ Базовый класс книги. """
    def __init__(self, name: str, author: str):
        """
        :param name: Название книги
        :param author: Автор
        """
        self._name = name
        self._author = author

    @property
    def name(self):
        return self._name

    @property
    def author(self):
        return self._author

    def __str__(self):
        return f"Книга {self._name}. Автор {self._author}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self._name!r}, author={self._author!r})"


class PaperBook(Book):
    """Дочерний класс.Бумажная книга."""
    def __init__(self, _name: str, _author: str, pages: int):
        """
        :param pages: Количество страниц
        """
        super().__init__(_name, _author)

        self._pages = pages

    def __str__(self):
        super().__str__()
        return f"Книга {self._name}. Автор {self._author}. Количество страниц {self._pages}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self._name!r}, author={self._author!r}, pages={self._pages!r})"

    @property
    def pages(self):
        return self._pages

    @pages.setter
    def pages(self, new_pages: int):
        if not isinstance(new_pages, int):
            raise TypeError("Страницы могут быть только типа int")
        if new_pages < 0:
            raise ValueError("Страницы долны быть положительными")


class AudioBook(Book):
    """ Дочерний класс. Аудио книга."""
    def __init__(self, _name: str, _author: str, duration: float):
        """
        :param duration: Продолжительность
        """
        super().__init__(_name, _author)
        self._duration = duration

    def __str__(self):
        super().__str__()
        return f"Книга {self._name}. Автор {self._author}. Продолжительность {self._duration} "

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self._name!r}, author={self._author!r}, pages={self.duration!r})"

    @property
    def duration(self):
        return self._duration

    @duration.setter
    def duration(self, new_duration: float):
        if not isinstance(new_duration, float):
            raise TypeError("Продолжительность должна быть типа float")
        if new_duration < 0:
            raise ValueError("Продолжительность не может быть отрицательной")
        self._duration = new_duration


book = Book("Весна", "Пушкин")
print(book)
paperboook = PaperBook("Весна", "Пушкин", 50)
print(paperboook)
audiobook = AudioBook("Весна", "Пушкин", 5.56)
print(audiobook)
