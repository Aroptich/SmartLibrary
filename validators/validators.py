from datetime import datetime
def valid_year(year: int):
    """Функция проверяет на валидность год"""
    try:
        if not str(year).isdigit() or not isinstance(year, int):
            raise ValueError(f'Год издания книги должен быть целым числом')
        elif len(str(year)) != 4 or 1000 <= year <= datetime.now().year:
            raise ValueError(f'Год издания книги должен быть в диапазоне от "1000" до "{datetime.now().year}"')
    except Exception as err:
        print(err)


