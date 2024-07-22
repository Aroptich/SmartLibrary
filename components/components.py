import os

from db_json import DataBase
from models.book import Book
from validators.validators import valid_year


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

#Подумать как возвращаться в меню добавления книги и производить добавление книги заново
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


def del_book():
    # Очищает экран
    os.system('cls')
    title_app()
    db = DataBase()
    print('Удаление книги'.center(50))
    print("Удаление книги из реестра происходит по ее 'id'")
    id = int(input('Введите "id" книги: '))
    del_book = db.remove(id)
    if del_book is not None:
        print(f'Книга {del_book} удалена из реестра')
        result = sub_menu()
        return result
    result = sub_menu()
    return result

@border
def menu_search_books():
    """Функция меню поиска книг"""
    print(f'Найти книгу по:\n'
          f'1. Заголовку\n'
          f'2. Автору\n'
          f'3. Году издания')

#Подумать как возвращаться в меню поиска и делать заново поиск
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

def set_status():
    """Функция изменения статуса книги"""
    # Очищает экран
    os.system('cls')
    title_app()
    db = DataBase()
    print('Изменение статуса'.center(50))
    print("Изменение статуса книги в реестре происходит по ее 'id'")
    id = int(input('Введите "id" книги: '))
    if len(db.detail_book(id)) == 0:
        print(f'Книги с "{id}" не сушествует')
    else:
        book = db.detail_book(id)
        print(f'{book["id"]}. {book["title"]} {book["author"]} {book["year"]}')
    # изменение статуса
    print(f'1. "В наличии"\n'
          f'2. "Выдана"')
    # Меню действия
    sub_action = input('Выберите действие, указав цифру от 1 или 2: ')
    if sub_action == '1':
        status = 'Выдана'
    elif sub_action == '2':
        status = "В наличии"
    status_book = db.change_status(id, status)
    if status_book is None:
        print(f'Книга c id:{id} не найдена')
    else:
        print(f'Статус книги "{status_book["title"]} {status_book["author"]} '
              f'{status_book["year"]}" изменен на "{status}"')
    result = sub_menu()
    return result

