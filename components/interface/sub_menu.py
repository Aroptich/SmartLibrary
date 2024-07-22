import os

from components.interface.border import border

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