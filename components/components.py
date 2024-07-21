import os

from db_json import DataBase
from models.book import Book


def title_app():
    print(f'{"#" * 52}\n'
          f'{"#" * 6}{"SMART LIBRARY".center(40)}{"#" * 6}\n'
          f'{"#" * 52}')


def border(func):
    """Функция-декратор. Рисует рамку вокруг меню"""

    def wrapper(*args, **kwargs):
        print('-' * 52)
        res = func(*args, **kwargs)
        print('-' * 52)
        return res

    return wrapper


@border
def menu():
    # Меню приложения
    print(f'1. Добавить книгу\n'
          f'2. Удалить книгу\n'
          f'3. Найти книгу/и\n'
          f'4. Показать все книги\n'
          f'5. Изменить статус книги\n'
          f'6. Выйти из системы')


@border
def sub_menu() -> bool:
    print(f'| 1. Выйти в главное меню | 2. Выйти из приложения |')
    print('-' * 52)
    # Меню действия
    action = input('Выберите действие, указав цифру от 1 или 2: ')
    if action == '1':
        # Очищает экран
        os.system('cls')
        return True
    elif action == '2':
        # Очищает экран
        os.system('cls')
        return False


def input_fields() -> tuple:
    """Функция полей ввода. Возвращает кортеж"""
    title = input('Введите название книги: ')
    author = input('Введите автора книги: ')
    year = int(input('Введите год издания книги: '))
    return title, author, year


def settings():
    db = DataBase()
    return db


def add_book(number: str) -> bool | None:
    """Функция добавления книги. Принимает число ввиде строки"""
    db = settings()
    if str(number) == '1':
        # Ввод данных
        # Очищает экран
        os.system('cls')
        title_app()
        print('Добавление новой книги'.center(50))
        flag = True
        while flag:
            title, author, year = input_fields()
            # проверка на существование книги в реестре
            if all([db.search_title(title), db.search_author(author), db.search_year(year)]):
                # Очищает экран
                os.system('cls')
                title_app()
                print(f'Книга "{title}-{author}-{year}" уже существует\n'
                      f'Введите данные новой книги')
            else:
                flag = False
        db.recording(Book(title, author, year))
        print('Книга сохранена в реестре')
        result = sub_menu()
        return result


def del_book(number: str):
    # Очищает экран
    os.system('cls')
    title_app()
    db = DataBase()
    print("Удаление книги из реестра происходит по ее 'id'")
    id = int(input('Введите "id" книги: '))
    del_book = db.remove(id)
    if del_book is not None:
        print(f'Книга {del_book} удалена из реестра')
        result = sub_menu()
        return result
    result = sub_menu()
    return result
