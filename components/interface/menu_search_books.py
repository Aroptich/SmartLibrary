from components.interface.border import border

@border
def menu_search_books():
    """Функция меню поиска книг"""
    print(f'Найти книгу по:\n'
          f'1. Заголовку\n'
          f'2. Автору\n'
          f'3. Году издания')