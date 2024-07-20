import json
import os
from book import Book

class DataBase:
    """Класс DataBase реализует чтение/запись данных в формате JSON"""

    __name_db = 'db.json'
    __data = {"books": []}

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
        data1 = tmp_data['books']
        elem = data1.append(data.__dict__)
        tmp_data['books'] = data1
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




