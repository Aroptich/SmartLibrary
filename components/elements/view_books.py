import os

from components.interface.sub_menu import sub_menu
from components.interface.title import title_app
from db_json import DataBase


def veiw_books():
    """Функция для отображения всех книг библиотеки"""
    # Очищает экран
    os.system('cls')
    db = DataBase()
    title_app()
    print('Список книг'.center(50))
    # Все записи библиотеки
    books = db.reading()
    if len(books.values()) == 0:
        print('В библиотеке нет книг')
    for book in books.values():
        print(f'{book["id"]}. {book["title"]} {book["author"]} {book["year"]}')
    result = sub_menu()
    return result