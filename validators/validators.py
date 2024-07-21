from datetime import datetime
def valid_year(year: int) -> int:
    """Функция проверяет на валидность год"""
    try:
        if not str(year).isdigit() or not isinstance(year, int):
            raise ValueError(f'Год издания книги должен быть целым числом')
        elif len(str(year)) != 4 or 1000 <= year <= datetime.now().year:
            raise ValueError(f'Год издания книги должен быть в диапазоне от "1000" до "{datetime.now().year}"')
        return year
    except Exception as err:
        print(err)


def valid_title(title: str)-> str:
    """Функция проверяет на валидность заголовок. В случае не пройденной проверки вызывает исключение,
     в противном случае возвращает заголовок"""
    try:
        if not isinstance(title, str):
            raise ValueError(f'Заголовок должен быть строкового типа')
        return title.capitalize()
    except Exception as err:
        print(err)

def valid_author(author: str)-> str:
    """Функция проверяет на валидность автора. В случае не пройденной проверки вызывает исключение,
     в противном случае возвращает заголовок"""
    try:
        if not isinstance(author, str):
            raise ValueError(f'Автор должен быть строкового типа')
        return author.capitalize()
    except Exception as err:
        print(err)

