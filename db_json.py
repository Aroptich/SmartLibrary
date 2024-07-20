import json
import os

from book import Book

class DataBase:
    """Класс DataBase реализует чтение/запись данных в формате JSON"""

    __name_db = 'db.json'
    __data = {}

    def __init__(self):

        if os.path.exists(self.__name_db) == False:
            tmp_data = json.dumps(self.__data)
            tmp_data = json.loads(str(tmp_data))
            with open(self.__name_db, 'w', encoding="utf-8") as file:
                json.dump(tmp_data, file,
                          ensure_ascii=False, indent=4)

    def recording(self, data: object) -> None:
        """Метод записывает данные в файл JSON"""
        tmp_data = self.reading()
        tmp_data[str(data.id)] = data.__dict__
        value = json.dumps(tmp_data)
        value = json.loads(str(value))
        with open(self.__name_db, 'w', encoding='utf-8') as file:
            json.dump(value, file,
                      ensure_ascii=False, indent=4)


    def reading(self) -> dict:
        """Метод считывает данные из файла "db.json" и возвращает словарь"""
        with open(self.__name_db, 'r', encoding='utf-8') as file:
            templates = json.loads(file.read())
        return templates

    def remove(self, id: int):
        """Метод считывает данные из файла "db.json, удаляет запись по "id" """
        tmp_data = self.reading()
        tmp_data.pop(str(id))
        value = json.dumps(tmp_data)
        value = json.loads(str(value))
        with open(self.__name_db, 'w', encoding='utf-8') as file:
            json.dump(value, file,
                      ensure_ascii=False, indent=4)

    def change_status(self, id: int, status: str):
        """Метод позволяет изменять статус книги"""
        tmp_data = self.reading()
        book = tmp_data.pop(str(id))
        book['status'] = status
        tmp_data[str(id)] = book
        value = json.dumps(tmp_data)
        value = json.loads(str(value))
        with open(self.__name_db, 'w', encoding='utf-8') as file:
            json.dump(value, file, sort_keys=True,
                      ensure_ascii=False, indent=4)


    def title_search(self, title: str):
        """Метод позволяет осуществлять поиск по заголовку книги"""
        tmp_data = self.reading()
        books = list(tmp_data.values())
        for book in books:
            if book['title'] == title:
                return tmp_data[str(book['id'])]
        raise Exception(f'Книга с заголовком "{title}" не найдена')



if __name__ == '__main__':
    db = DataBase()
    # print(db.reading())
    # db.recording(Book('asdadad', 'adada', 2015))
    # print(db.reading())
    # db.recording(Book('hjfhj', 'ghdhf', 2018))
    # print(db.reading())
    # db.recording(Book('bcvnfg', 'xcvxb', 2000))
    # print(db.reading())
    # # print(db.remove(3))
    # # print(db.reading())
    # print(db.change_status(2, 'ывф'))
    # print(db.reading())
    print(db.title_search('hjfhj'))




