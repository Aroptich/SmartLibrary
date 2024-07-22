import json
import os

from models.book import Book
from validators.validators import is_valid

class DataBase:
    """Класс DataBase реализует чтение/запись данных в формате JSON"""

    __name_db = 'db.json'
    __data = {}

    def __init__(self):

        if not os.path.exists(self.__name_db):
            data = is_valid(self.__data)
            # tmp_data = json.dumps(self.__data)
            # tmp_data = json.loads(str(tmp_data))
            with open(self.__name_db, 'w', encoding="utf-8") as file:
                json.dump(data, file,
                          ensure_ascii=False, indent=4)

    def recording(self, data: object) -> None:
        """Метод записывает данные в файл JSON"""
        tmp_data = self.reading()
        tmp_data[str(data.id)] = data.__dict__
        record_data = is_valid(tmp_data)
        # value = json.dumps(tmp_data)
        # value = json.loads(str(value))
        with open(self.__name_db, 'w', encoding='utf-8') as file:
            json.dump(record_data, file,
                      ensure_ascii=False, indent=4)


    def reading(self) -> dict:
        """Метод считывает данные из файла "db.json" и возвращает словарь с данными книг"""
        with open(self.__name_db, 'r', encoding='utf-8') as file:
            templates = json.loads(file.read())
        return templates

    def remove(self, id: int):
        """Метод считывает данные из файла "db.json, удаляет запись по "id" """
        try:
            tmp_data = self.reading()
            if len(tmp_data) == 0:
                raise ValueError('Реестр книг пуст')
            del_data = tmp_data.pop(str(id))
            data = is_valid(tmp_data)
            # value = json.dumps(tmp_data)
            # value = json.loads(str(value))
            with open(self.__name_db, 'w', encoding='utf-8') as file:
                json.dump(data, file,
                          ensure_ascii=False, indent=4)
            return del_data
        except Exception as err:
            print(err)

    def change_status(self, id: int, status: str):
        """Метод позволяет изменять статус книги"""
        try:
            tmp_data = self.reading()
            book = tmp_data.pop(str(id))
            book['status'] = status
            tmp_data[str(id)] = book
            data = is_valid(tmp_data)
            with open(self.__name_db, 'w', encoding='utf-8') as file:
                json.dump(data, file, sort_keys=True,
                          ensure_ascii=False, indent=4)
            return book
        except Exception as err:
            print(err)


    def search_title(self, title: str):
        """Метод позволяет осуществлять поиск по заголовку книги"""
        try:
            tmp_data = self.reading()
            books = list(tmp_data.values())
            list_books = []
            for book in books:
                if book['title'] == title.capitalize():
                    list_books.append(tmp_data[str(book['id'])])
            return list_books
        except Exception as err:
            print(err)

    def search_author(self, author: str):
        """Метод позволяет осуществлять поиск по автору книги"""
        try:
            tmp_data = self.reading()
            books = list(tmp_data.values())
            list_books = []
            for book in books:
                if book['author'] == author.capitalize():
                    list_books.append(tmp_data[str(book['id'])])
            return list_books
        except Exception as err:
            print(err)

    def search_year(self, year: int):
        """Метод позволяет осуществлять поиск по году издания книги"""
        try:
            tmp_data = self.reading()
            books = list(tmp_data.values())
            list_books = []
            for book in books:
                if book['year'] == year:
                    list_books.append(tmp_data[str(book['id'])])
            return list_books
        except Exception as err:
            print(err)

    def detail_book(self, id: int) -> dict:
        """Метод принимает "id" и возвращает данные книги"""
        try:
            tmp_data = self.reading()
            if len(tmp_data) != 0:
                book = tmp_data.get(str(id))
                return book
            raise ValueError('Реестр книг пуст')
        except Exception as err:
            print(err)


# if __name__ == '__main__':
#     db = DataBase()
#     print(db.reading())
#     db.recording(Book('asdadad', 'adada', 2015))
#     print(db.reading())
#     db.recording(Book('hjfhj', 'ghdhf', 2018))
#     print(db.reading())
#     db.recording(Book('bcvnfg', 'xcvxb', 2000))
#     print(db.reading())
#     db.recording(Book('ukgp[hsh', 'xcCWEF', 15))
#     # # print(db.remove(3))
#     # print(db.reading())
#     # print(db.change_status(2, 'ывф'))
#     print(db.reading())
#     print(db.search_title('hjfhj'))
#     print(db.search_author('adada'))
#     # print(db.search_year(2000))




