class Library:
    """
    Represents a library that stores a list of books.
    """

    def __init__(self, books=None):
        """
        Initializes a Library instance.

        Args:
            books: An optional list of Book instances. Defaults to an empty list.
        """
        if books is None:
            self.books = []
        else:
            self.books = books

    def get_next_book_id(self):
        """
        Returns the next available ID for a new book.
        """
        if not self.books:
            return 1
        else:
            return self.books[-1].id + 1

    def get_index_by_book_id(self, book_id: int):
        """
        Returns the index of the book with the given ID.

        Args:
            book_id: The ID of the book to search for.

        Raises:
            ValueError: If no book with the given ID exists.
        """
        for index, book in enumerate(self.books):
            if book.id == book_id:
                return index
        raise ValueError("Книги с запрашиваемым id не существует")


BOOKS_DATABASE = [{"id": 1, "name": "test_name_1", "pages": 200, }, {"id": 2, "name": "test_name_2", "pages": 400, }]


class Book:
    """
    Represents a book with an ID, name, and number of pages.
    """

    def __init__(self, id_: int, name: str, pages: int):
        """
        Initializes a Book instance.

        Args:
            id_: The unique identifier of the book (integer).
            name: The title of the book (string).
            pages: The number of pages in the book (integer).
        """
        self.id = id_
        self.name = name
        self.pages = pages

    def __str__(self):
        """
        Returns a string representation of the book in the format "Книга "название_книги"".
        """
        return f'Книга "{self.name}"'

    def __repr__(self):
        """
        Returns a string representation that can be used to recreate the Book instance.
        """
        return f"Book(id_={self.id}, name='{self.name}', pages={self.pages})"


if __name__ == '__main__':
    empty_library = Library()  # инициализируем пустую библиотеку
    print(empty_library.get_next_book_id())  # проверяем следующий id для пустой библиотеки

    list_books = [Book(id_=book_dict["id"], name=book_dict["name"], pages=book_dict["pages"]) for book_dict in
                  BOOKS_DATABASE]
    library_with_books = Library(books=list_books)  # инициализируем библиотеку с книгами
    print(library_with_books.get_next_book_id())  # проверяем следующий id для непустой библиотеки

    print(library_with_books.get_index_by_book_id(1))  # проверяем индекс книги с id = 1

    try:
        print(library_with_books.get_index_by_book_id(3))  # Проверяем обработку ошибки
    except ValueError as e:
        print(e)
