import os

from components.elements.add_book import add_book
from components.elements.del_books import del_book
from components.elements.search_books import search_books
from components.elements.set_status import set_status
from components.elements.view_books import veiw_books
from components.interface.menu import menu
from components.interface.title import title_app
from db_json import DataBase



def app():
    # Очищает экран
    os.system('cls')
    start = True
    while start:
        db = DataBase()
        title_app()
        menu()
        # Меню действия
        menu_action = input('Выберите действие, указав цифру от 1 до 6: ')
        # Добавление книги
        if menu_action == '1':
            flag = add_book(menu_action)
            if flag:
                continue
            else:
                break
        # Удаление книги
        elif menu_action == '2':
            flag = del_book()
            if flag or None:
                continue
            else:
                break
        # Поиск книг по заголовку/автору/году издания
        elif menu_action == '3':
            flag = search_books()
            if flag:
                continue
            else:
                break
        # Отображения всех книг библиотеки
        elif menu_action == '4':
            flag = veiw_books()
            if flag:
                continue
            else:
                break
        # Изменение статуса книг
        elif menu_action == '5':
            flag = set_status()
            if flag:
                continue
            else:
                break
        elif menu_action == '6':
            # Очищает экран
            os.system('cls')
            start = False

    # Очищает экран
    os.system('cls')


if __name__ == '__main__':
   app()
