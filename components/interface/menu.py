from components.interface.border import border


@border
def menu():
    # Меню приложения
    print(f'1. Добавить книгу\n'
          f'2. Удалить книгу\n'
          f'3. Найти книгу/и\n'
          f'4. Показать все книги\n'
          f'5. Изменить статус книги\n'
          f'6. Выйти из системы')