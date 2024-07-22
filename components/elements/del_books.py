import os

from components.interface.sub_menu import sub_menu
from components.interface.title import title_app
from db_json import DataBase


def del_book():
    # Очищает экран
    os.system('cls')
    title_app()
    db = DataBase()
    print('Удаление книги'.center(50))
    print("Удаление книги из реестра происходит по ее 'id'")
    id = int(input('Введите "id" книги: '))
    book = db.remove(id)
    if del_book is not None:
        print(f'Книга {book["id"]}.{book["title"]} {book["author"]} {book["year"]}  удалена из реестра')
        result = sub_menu()
        return result
    result = sub_menu()
    return result