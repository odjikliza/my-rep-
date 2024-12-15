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


BOOKS_DATABASE = [{"id": 1, "name": "test_name_1", "pages": 200, }, {"id": 2, "name": "test_name_2", "pages": 400, }]

if __name__ == '__main__':
    # инициализируем список книг
    list_books = [Book(id_=book_dict["id"], name=book_dict["name"], pages=book_dict["pages"]) for book_dict in
                  BOOKS_DATABASE]
    for book in list_books:
        print(book)  # проверяем метод str

    print(list_books)  # проверяем метод repr
