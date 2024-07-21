from db_json import DataBase



def border(func):
    """Функция-декратор. Рисует рамку вокруг меню"""
    def wrapper(*args, **kwargs):
        print('-'*50)
        func(*args, **kwargs)
        print('-' * 50)
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


def title_app():
    # Заставка приложения
    print(f'{"#" * 50}\n'
          f'{"#" * 5}{"SMART LIBRARY".center(40)}{"#" * 5}\n'
          f'{"#" * 50}')

def settings():
    db = DataBase()
    return db