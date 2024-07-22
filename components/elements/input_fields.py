def input_fields() -> tuple:
    """Функция полей ввода. Возвращает кортеж"""
    title = input('Введите название книги: ')
    author = input('Введите автора книги: ')
    year = int(input('Введите год издания книги: '))
    return title, author, year