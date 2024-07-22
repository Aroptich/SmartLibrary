def border(func):
    """Функция-декратор. Рисует рамку вокруг меню"""
    def wrapper(*args, **kwargs):
        print('-' * 52)
        res = func(*args, **kwargs)
        print('-' * 52)
        return res

    return wrapper