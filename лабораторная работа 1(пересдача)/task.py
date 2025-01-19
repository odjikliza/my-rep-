class Car:
    def __init__(self, make: str, model: str, year: int):
        """
        Инициализация объекта Car.

        :param make: Производитель автомобиля.
        :param model: Модель автомобиля.
        :param year: Год выпуска автомобиля (должен быть >= 1886).
        :raises ValueError: Если год выпуска меньше 1886.
        """
        if year < 1886:
            raise ValueError("Год выпуска должен быть не ранее 1886 года.")
        self.make = make
        self.model = model
        self.year = year

    def get_age(self) -> int:
        """
        Вычисляет возраст автомобиля.

        :return: Возраст автомобиля в годах.
        >>> car = Car("Toyota", "Camry", 2015)
        >>> car.get_age()
        8
        """
        from datetime import datetime
        current_year = datetime.now().year
        return current_year - self.year

    def update_model(self, new_model: str) -> None:
        """
        Обновляет модель автомобиля.

        :param new_model: Новая модель автомобиля.
        """
        self.model = new_model


class Book:
    def __init__(self, title: str, author: str, pages: int):
        """
        Инициализация объекта Book.

        :param title: Название книги.
        :param author: Автор книги.
        :param pages: Количество страниц (должно быть положительным числом).
        :raises ValueError: Если количество страниц <= 0.
        """
        if pages <= 0:
            raise ValueError("Количество страниц должно быть положительным числом.")
        self.title = title
        self.author = author
        self.pages = pages

    def read(self, pages_read: int) -> str:
        """
        Читает указанное количество страниц.

        :param pages_read: Количество страниц для чтения (должно быть <= количества страниц в книге).
        :raises ValueError: Если pages_read > pages.
        :return: Статус чтения.

        >>> book = Book("1984", "George Orwell", 328)
        >>> book.read(50)
        'Вы прочитали 50 страниц.'
        """
        if pages_read > self.pages:
            raise ValueError("Нельзя прочитать больше страниц, чем есть в книге.")
        return f'Вы прочитали {pages_read} страниц.'

    def get_info(self) -> str:
        """
        Возвращает информацию о книге.

        :return: Строка с информацией о книге.

        >>> book = Book("1984", "George Orwell", 328)
        >>> book.get_info()
        '1984, автор: George Orwell, страницы: 328'
        """
        return f'{self.title}, автор: {self.author}, страницы: {self.pages}'


class BankAccount:
    def __init__(self, account_number: str, balance: float = 0.0):
        """
        Инициализация объекта BankAccount.

        :param account_number: Номер счета (должен быть строкой).
        :param balance: Начальный баланс (по умолчанию 0.0).
        """
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount: float) -> float:
        """
        Вносит деньги на счет.

        :param amount: Сумма для внесения (должна быть положительной).
        :raises ValueError: Если сумма <= 0.
        :return: Новый баланс счета.

        >>> account = BankAccount("123456")
        >>> account.deposit(100)
        100.0
        """
        if amount <= 0:
            raise ValueError("Сумма для внесения должна быть положительной.")
        self.balance += amount
        return self.balance

    def withdraw(self, amount: float) -> float:
        """
        Снимает деньги со счета.

        :param amount: Сумма для снятия (должна быть положительной и <= текущему балансу).
        :raises ValueError: Если сумма <= 0 или больше текущего баланса.
        :return: Новый баланс счета.

        >>> account = BankAccount("123456", 200)
        >>> account.withdraw(50)
        150.0
        """
        if amount <= 0: