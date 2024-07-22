#Подумать как возвращаться в меню поиска и делать заново поиск
import os

from components.interface.menu_search_books import menu_search_books
from components.interface.sub_menu import sub_menu
from components.interface.title import title_app
from db_json import DataBase
from validators.validators import valid_year


def search_books():
    """Функция для поиска книг в реестре по заголовку/автору/году издания"""
    # Очищает экран
    os.system('cls')
    title_app()
    print('Поиск книги по заголовку/автору/году'.center(50))
    db = DataBase()
    # Поиск книги по заголовку/автору/году
    menu_search_books()
    # Меню действия
    sub_action = input('Выберите действие, указав цифру от 1 до 3: ')
    if sub_action == '1':
        # Очищает экран
        os.system('cls')
        title_app()
        print('Поиск книги по заголовку/автору/году'.center(50))
        title = input('Введите название книги: ')
        search_book = db.search_title(title)
        if len(search_book) == 0:
            print(f'Книга/и с названием "{title}" не найдена/ы')
        else:
            print(f'Книга/и {search_book} найдена/ы')
        result = sub_menu()
        return result
        #надо что-то дописать чтобы продолжить поиск
    elif sub_action == '2':
        # Очищает экран
        os.system('cls')
        title_app()
        print('Поиск книги по заголовку/автору/году'.center(50))
        author = input('Введите автора книги: ')
        search_book = db.search_author(author)
        if len(search_book) == 0:
            print(f'Книга/и с автором "{author}" не найдена/ы')
        else:
            print(f'Книга/и {search_book} найдена/ы')
        result = sub_menu()
        return result
    elif sub_action == '3':
        # Очищает экран
        os.system('cls')
        title_app()
        print('Поиск книги по заголовку/автору/году'.center(50))
        year = input('Введите год издания книги: ')
        valid_year(year)
        search_book = db.search_year(year)
        if len(search_book) == 0:
            print(f'Книга/и с годом издания "{year}" не найдена/ы')
        else:
            print(f'Книга/и {search_book} найдена/ы')
        result = sub_menu()
        return result