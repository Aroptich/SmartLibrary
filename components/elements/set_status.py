import os

from components.interface.menu_status import menu_status
from components.interface.sub_menu import sub_menu
from components.interface.title import title_app
from db_json import DataBase


def set_status():
    """Функция изменения статуса книги"""
    # Очищает экран
    os.system('cls')
    title_app()
    db = DataBase()
    print('Изменение статуса'.center(50))
    print("Изменение статуса книги в реестре происходит по ее\n'id'")
    id = int(input('Введите "id" книги: '))
    if len(db.detail_book(id)) == 0:
        print(f'Книги с "{id}" не сушествует')
    else:
        book = db.detail_book(id)
        print(f'{book["id"]}. {book["title"]} {book["author"]} {book["year"]}')
    # изменение статуса
    menu_status()
    # Меню действия
    sub_action = input('Выберите действие, указав цифру от 1 или 2: ')
    if sub_action == '1':
        status = 'Выдана'
        os.system('cls')
        title_app()
    elif sub_action == '2':
        status = "В наличии"
        os.system('cls')
        title_app()
    status_book = db.change_status(id, status)
    if status_book is None:
        print(f'Книга c id:{id} не найдена')
    else:
        print(f'Статус книги "{status_book["title"]} {status_book["author"]} '
              f'{status_book["year"]}"\n изменен на "{status}"')
    result = sub_menu()
    return result
