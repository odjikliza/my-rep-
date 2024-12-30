class Book:
    """Базовый класс книги."""

    def __init__(self, name: str, author: str):
        if not isinstance(name, str):
            raise TypeError("Имя книги должно быть строкой.")
        if not isinstance(author, str):
            raise TypeError("Имя автора должно быть строкой.")
        self._name = name
        self._author = author

    def __str__(self) -> str:
        return f"Книга '{self._name}'. Автор: {self._author}"

    def __repr__(self) -> str:
        return f"{type(self).__name__}(name={self._name!r}, author={self._author!r})"

    @property
    def name(self) -> str:
        return self._name

    @property
    def author(self) -> str:
        return self._author



class PaperBook(Book):
    """Класс бумажной книги."""

    def __init__(self, name: str, author: str, pages: int):
        super().__init__(name, author)
        self.pages = pages

    @property
    def pages(self):
        return self._pages

    @pages.setter
    def pages(self, value):
        if not isinstance(value, int):
            raise TypeError("Количество страниц должно быть целым числом.")
        if value <= 0:
            raise ValueError("Количество страниц должно быть больше нуля.")
        self._pages = value

    def __str__(self):
        return f"Бумажная книга {self.name}. Автор {self.author}, {self.pages} страниц."


class AudioBook(Book):
    """Класс аудиокниги."""

    def __init__(self, name: str, author: str, duration: float):
        super().__init__(name, author)
        self.duration = duration

    @property
    def duration(self):
        return self._duration

    @duration.setter
    def duration(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError("Продолжительность должна быть числом.")
        if value <= 0:
            raise ValueError("Продолжительность должна быть больше нуля.")
        self._duration = value

    def __str__(self):
        return f"Аудиокнига {self.name}. Автор {self.author}, продолжительность {self.duration:.2f} часов."


if name == "__main__":
    paper_book = PaperBook("1984", "Джордж Оруэлл", 328)
    audio_book = AudioBook("Bohemian Rhapsody", "Queen", 5.55)

    print(paper_book)
    print(audio_book)
