from components.interface.border import border
@border
def menu_status():
    print(f'| 1. "В наличии"{" "*10} | 2. "Выдана"{" "*10} |')