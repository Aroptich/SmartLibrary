class Book:
    __id = 1
    __status = ('в наличии', 'выдана')


    def __init__(self, title: str, author: str, year:int):
        self.id = Book.__id + 1
        self.title = title
        self.author = author
        self.year = year
        self.__status = Book.__status[0]


    def __repr__(self):
        return (f'id: "{self.__id}", title: "{self.title}", author: "{self.author}",'
                f'status: "{self.__status}"')




