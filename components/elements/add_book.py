import os

from components.elements.input_fields import input_fields
from components.interface.sub_menu import sub_menu
from components.interface.title import title_app

from db_json import DataBase
from models.book import Book


def add_book(number: str) -> bool | None:
    """Функция добавления книги. Принимает число ввиде строки"""
    db = DataBase()
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