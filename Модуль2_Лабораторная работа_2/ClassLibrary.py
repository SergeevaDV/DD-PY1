


BOOKS_DATABASE = [
    {
        "id": 1,
        "name": "test_name_1",
        "pages": 200,
    },
    {
        "id": 2,
        "name": "test_name_2",
        "pages": 400,
    }
]


class Book:
    """Класс Книги"""
    def __init__(self, id: int, name: str, pages: int):
        """

        :param id: индификатор
        :param name: название
        :param pages: страницы
        """
        self.name = name
        self.id = id
        self.pages = pages


class Library:
    """Класс Библиотека"""
    def __init__(self, books=None):
        """

        :param books: список книг
        """
        if books is None:
            books = []
        self.books = books

    def get_next_book_id(self):
        if not self.books:
            return 1
        else:
            return self.books[-1].id + 1

    def get_index_by_book_id(self, id: int):
        for i, index in enumerate(self.books, start=0):
            if index == id:
                return i
            if not index:
                raise ValueError




if __name__ == '__main__':
    empty_library = Library()  # инициализируем пустую библиотеку
    print(empty_library.get_next_book_id())  # проверяем следующий id для пустой библиотеки

    list_books = [
        Book(id=book_dict["id"], name=book_dict["name"], pages=book_dict["pages"]) for book_dict in BOOKS_DATABASE
    ]
    library_with_books = Library(books=list_books)  # инициализируем библиотеку с книгами
    print(library_with_books.get_next_book_id())  # проверяем следующий id для непустой библиотеки

    print(library_with_books.get_index_by_book_id(1))  # проверяем индекс книги с id = 1
