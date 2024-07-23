# SmartLibrary

## Описание
Консольное приложение для управления библиотекой книг.

Приложение позволяет добавлять, удалять, искать и отображать книги.

# Запуск приложения

> Загрузка проекта
```bash
https://github.com/Aroptich/SmartLibrary.git
cd SmartLibrary
```

> Запуск приложения

В терменале необходимо ввести следующую команду
```bash
python app.py
```

### **Вид главного меню**

Управление приложением осуществляется с клавиатуры

![main menu](components/screenshots/main_menu.png)

### **Добавить книгу**

В разделе "Добавить книгу" необходимо ввести название, 

автора и год издания книги

![add_book](components/screenshots/add_book.png)

При правильном заполнении всех полей появиться сообщение о том, 

что "книга сохранена в реестре".

После успешного добавления книги программа попросит пользователя выбрать дальнейшие действия.

![success_add_book](components/screenshots/success_add_book.png)

При добавлении книги, которая уже находится в реестре будет выдано сообщении о том, 

что такая книга уже существует и попросит пользователя ввести данные книги заново

![bad_add_book](components/screenshots/bad_add_book.png)

### **Удалить книгу**

При удалении книги, пользователь должен ввести 'id' книги.
Если 'id', который указал пользователь существует, то произойдет успешное удаление книги,

![success_del_book](components/screenshots/success_del_book.png)


а если 'id' будет указан не верно, то прилодение выдаст сообщение, 

что книги с таким 'id' в реесрте нет

![bad_del_book](components/screenshots/bad_del_book.png)


### **Найти книгу/и**

Поиск книг/и осуществляется или по заголову или по автору или по году издания.

Пользователю необходимо выбрать один из 3 вариантов

![menu_search_books](components/screenshots/menu_search_books.png)

Для поиска книги например по заголовку пользователь должен ввести полное название книги. 

При совпадении заголовка, который ввел пользователь с названием книги из БД, 

пользователь получает книгу или список книг

![success_result_search](components/screenshots/success_result_search.png)


Аналогично с вариантами поиска по автору и по году издания.

![success_result_search](components/screenshots/success_result_search.png)

### **Показать все книги**

При выборе пользователя варианта "Показать все книги", приложение выводит все книги добавленные в реестр

![search_all_books](components/screenshots/search_all_books.png)

### **Изменение статуса**

При изменении статуса книги, пользователь должен ввести 'id' книги.

Если 'id', который указал пользователь существует, то пользователю будет предложен выбор смены статуса

![search_set_status](components/screenshots/search_set_status.png)

## Архитектура приложения

```
< PROJECT ROOT >
   |
   |-- components/                 
   |    |-- elements/
   |    |      |-- add_books.py
   |    |      |-- del_books.py
   |    |      |-- input_fields.py     
   |    |      |-- search_books.py     
   |    |      |-- set_status.py     
   |    |      |-- veiw_books.py     
   |    |-- interface/
   |    |      |-- border.py
   |    |      |-- menu.py
   |    |      |-- menu_search_books.py     
   |    |      |-- menu_status.py     
   |    |      |-- sub_menu.py     
   |    |      |-- title.py  
   |    |-- screenshots/            
   |    |      |-- add_book.png
   |    |      |-- bad_add_book.png
   |    |      |-- bad_del_book.png     
   |    |      |-- main_menu.png 
   |    |      |-- menu_search_books.png
   |    |      |-- search_all_books.png     
   |    |      |-- success_add_book.png     
   |    |      |-- success_del_book.png     
   |    |      |-- success_result_search.png    
   |    |
   |-- models/ 
   |    |-- book.py   
   |-- validators/ 
   |    |-- validators.py             
   |              
   |-- app.py
   |-- db_json.py            
   |-- README.md
   |-- ************************************************* 
```