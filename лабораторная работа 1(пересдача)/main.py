from task_1 import Car, Book, BankAccount  # Импортируем классы из первого задания

if __name__ == "__main__":
    # Инстанцируем объекты классов
    car = Car("Toyota", "Camry", 2015)
    book = Book("1984", "George Orwell", 328)
    account = BankAccount("123456", 100.0)

    # Проверка методов класса Car
    try:
        # Попробуем создать машину с некорректным годом
        invalid_car = Car("Ford", "Mustang", 1800)  # Год меньше 1886
    except ValueError as e:
        print(f'Ошибка: {e}')

    try:
        # Попробуем обновить модель на некорректное значение (например, на None)
        car.update_model(None)
    except TypeError as e:
        print('Ошибка: неправильные данные')

    # Проверка методов класса Book
    try:
        # Попробуем создать книгу с некорректным количеством страниц
        invalid_book = Book("The Catcher in the Rye", "J.D. Salinger", -10)  # Количество страниц отрицательное
    except ValueError as e:
        print(f'Ошибка: {e}')

    try:
        # Попробуем прочитать больше страниц, чем есть в книге
        book.read(400)
    except ValueError as e:
        print(f'Ошибка: {e}')

    # Проверка методов класса BankAccount
    try:
        # Попробуем внести отрицательную сумму
        account.deposit(-50)
    except ValueError as e:
        print(f'Ошибка: {e}')

    try:
        # Попробуем снять больше средств, чем есть на счете
        account.withdraw(200)
    except ValueError as e:
        print(f'Ошибка: {e}')
