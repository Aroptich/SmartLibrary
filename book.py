class Book:
    __id = 1
    __status = 'в наличии'


    def __init__(self, title: str, author: str, year:int):
        self.id = self.__id
        self.title = title.capitalize()
        self.author = author.capitalize()
        self.year = year
        self.status = Book.__status
        Book.__id += 1


    def __repr__(self):
        return (f'id: "{self.__id}", title: "{self.title}", author: "{self.author}",'
                f'status: "{self.__status}"')


