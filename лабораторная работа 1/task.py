class Book:
    """
    Класс, описывающий книгу.

    Attributes:
        title (str): Название книги.
        author (str): Автор книги.
        pages (int): Количество страниц. Должно быть положительным числом.
    """

    def __init__(self, title: str, author: str, pages: int):
        """
        Инициализация объекта класса Book.

        Args:
            title (str): Название книги.
            author (str): Автор книги.
            pages (int): Количество страниц.

        Raises:
            ValueError: Если количество страниц не положительное число.
        """
        if pages <= 0:
            raise ValueError("Количество страниц должно быть положительным числом.")
        self.title: str = title
        self.author: str = author
        self.pages: int = pages

    def get_info(self) -> str:
        """
        Возвращает информацию о книге в виде строки.

        Returns:
            str: Информация о книге.

        >>> book = Book("Python для начинающих", "Иван Иванов", 200)
        >>> book.get_info()
        'Название: Python для начинающих, Автор: Иван Иванов, Страниц: 200'
        """
        return f"Название: {self.title}, Автор: {self.author}, Страниц: {self.pages}"

    def read_chapter(self, chapter_number: int, chapters_count: int = 10) -> None:
        """
        "Читает" главу книги.

        Args:
            chapter_number (int): Номер главы.
            chapters_count (int, optional): Общее количество глав в книге. Defaults to 10.

        Raises:
            ValueError: Если номер главы вне допустимого диапазона.
        """
        if not 1 <= chapter_number <= chapters_count:
            raise ValueError("Номер главы вне допустимого диапазона.")
        print(f"Читаю главу {chapter_number}")


class BankAccount:
    """
    Класс, описывающий банковский счет.

    Attributes:
        owner (str): Владелец счета.
        balance (float): Баланс счета. Не может быть отрицательным.
    """

    def __init__(self, owner: str, balance: float = 0.0):
        """
        Инициализация объекта класса BankAccount.

        Args:
            owner (str): Владелец счета.
            balance (float, optional): Начальный баланс. Defaults to 0.0.

        Raises:
            ValueError: Если начальный баланс отрицательный.
        """
        if balance < 0:
            raise ValueError("Начальный баланс не может быть отрицательным.")
        self.owner: str = owner
        self.balance: float = balance

    def deposit(self, amount: float) -> float:
        """
        Вносит средства на счет.

        Args:
            amount (float): Сумма вклада. Должна быть положительной.

        Returns:
            float: Новый баланс счета.

        Raises:
            ValueError: Если сумма вклада не положительна.

        >>> account = BankAccount("Петр Петров", 100.0)
        >>> account.deposit(50.0)
        150.0
        """
        if amount <= 0:
            raise ValueError("Сумма вклада должна быть положительной.")
        self.balance += amount
        return self.balance

    def withdraw(self, amount: float) -> float:
        """
        Снимает средства со счета.

        Args:
            amount (float): Сумма снятия.

        Returns:
            float: Новый баланс счета.

        Raises:
            ValueError: Если сумма снятия превышает баланс счета.
        """
        if amount > self.balance:
            raise ValueError("Недостаточно средств на счете.")
        self.balance -= amount
        return self.balance


class SocialNetworkPost:
    """
    Класс, описывающий пост в социальной сети.

    Attributes:
        author (str): Автор поста.
        text (str): Текст поста.
        likes (int): Количество лайков. Не может быть отрицательным.
    """

    def __init__(self, author: str, text: str):
        """
        Инициализация объекта класса SocialNetworkPost.

        Args:
            author (str): Автор поста.
            text (str): Текст поста.
        """
        self.author: str = author
        self.text: str = text
        self.likes: int = 0

    def add_like(self) -> int:
        """
        Добавляет один лайк к посту.

        Returns:
            int: Новое количество лайков.

        >>> post = SocialNetworkPost("Василий Пупкин", "Привет, мир!")
        >>> post.add_like()
        1
        """
        self.likes += 1
        return self.likes

    def display_post(self, show_likes: bool = True) -> str:
        """
        Выводит информацию о посте.

        Args:
            show_likes (bool, optional): Отображать ли количество лайков. Defaults to True.

        Returns:
            str: Информация о посте.
        """
        post_info = f"Автор: {self.author}\nТекст: {self.text}"
        if show_likes:
            post_info += f"\nЛайки: {self.likes}"
        return post_info
