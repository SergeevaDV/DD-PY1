BOOKS_DATABASE = [
    {
        "id_": 1,
        "name": "test_name_1",
        "pages": 200,
    },
    {
        "id_": 2,
        "name": "test_name_2",
        "pages": 400,
    }
]
class Book:
    """Класс книги."""
    def __init__(self, id_: int, name: str, pages: int):
        """

        :param id_: идентификатор книги
        :param name: Название книги
        :param pages: Количество страниц в книге
        """
        self.name = name
        self.id_ = id_
        self.pages = pages

    def __str__(self) -> str:
        """ Метод __str__ возвращает строку"""
        return f'Книга "{self.name}"'
    def __repr__(self) -> str:
        """Метод __repr__ возвращает валидную python строку, по которой можно инициализировать точно такой же экземпляр."""
        return f'Book(id_={self.id_!r}, name={self.name!r}, pages={self.pages!r})'

if __name__ == '__main__':
    # инициализируем список книг
    list_books = [
        Book(id_=book_dict["id_"], name=book_dict["name"], pages=book_dict["pages"]) for book_dict in BOOKS_DATABASE
    ]
    for book in list_books:
        print(book)  # проверяем метод __str__

    print(list_books)  # проверяем метод __repr__
