# qa_python

<!-- TOC -->
* [qa_python](#qa_python)
  * [Доп методы](#доп-методы)
    * [helper.py](#helperpy)
      * [generate_random_string](#generate_random_string)
      * [generate_random_books_genre](#generate_random_books_genre)
      * [generate_random_favorite_list](#generate_random_favorite_list)
  * [Реализованные тесты](#реализованные-тесты)
    * [Метод `_init_`](#метод-_init_)
    * [Метод `add_new_book`](#метод-add_new_book)
    * [Метод `set_book_genre`](#метод-set_book_genre)
    * [Метод `get_book_genre`](#метод-get_book_genre)
    * [Метод `get_books_with_specific_genre`](#метод-get_books_with_specific_genre)
    * [Метод `get_books_genre`](#метод-get_books_genre)
    * [Метод `get_books_for_children`](#метод-get_books_for_children)
    * [Метод `add_book_in_favorites`](#метод-add_book_in_favorites)
    * [Метод `delete_book_from_favorites`](#метод-delete_book_from_favorites)
<!-- TOC -->

## Доп методы

### helper.py

####  generate_random_string

Генерируется строка из случайных символов, различного регистра. Длина указывается в параметре `number_of_entries: int`.

#### generate_random_books_genre

Генерируется словарь books_genre, как с указанием `genre`, так и без (в зависимости от указанного параметра 
`with_genre: bool`). Длина словаря указывается в параметре `number_of_entries: int`.

#### generate_random_favorite_list

Генерируется случайный список избранного. Длина указывается в параметре `number_of_entries: int`.

## Реализованные тесты

### Метод `_init_`

* `test_init_books_genre` - проверка дефолтного значения books_genre
* `test_init_favorites` - проверка дефолтного значения favorites
* `test_init_genre` - проверка дефолтного значения genre
* `test_init_genre_age_rating` - проверка дефолтного значения genre_age_rating

### Метод `add_new_book`

* `test_add_new_book_acceptable_length_name` - попытка добавить книгу при корректных значениях `name`
* `test_add_new_book_negative_length_name` - попытка добавить книгу при не корректных значениях `name`

### Метод `set_book_genre`

* `test_set_book_genre_exist_books` - попытка установки существующего жанра книге, которая входит в словарь `books_genre`
* `test_set_book_genre_missing_book` - попытка установки существующего жанра книге, которая не входит в словарь `books_genre`
* `test_set_book_genre_missing_genre` - попытка установки не существующего жанра книге, которая входит в словарь `books_genre`

### Метод `get_book_genre`

* `test_get_book_genre` - попытка получения жанра существующей книги
* `test_get_book_genre_empty_book` - попытка получения жанра не существующей книги

### Метод `get_books_with_specific_genre`

* `test_get_books_with_specific_genre` - попытка получения списка книг по заданному жанру
* `test_get_books_with_specific_genre_negative` - попытка получения списка книг по заданному жанру, когда список книг пустой

### Метод `get_books_genre`

* `test_get_books_genre` - попытка получения словаря `get_books_genre`

### Метод `get_books_for_children`

* `test_get_books_for_children` - попытка получить массив книг без ограничения по возрасту

### Метод `add_book_in_favorites`

* `test_add_book_in_favorites_existing_name` - попытка добавить книгу, входящую в словарь `books_genre`, в список избранного
* `test_add_book_in_favorites_missing_name` - попытка добавить книгу, отсутствующую в словаре `books_genre`, в список избранного
* `test_add_book_in_favorites_name_in_favorites` - попытка добавить книгу, входящую в словарь `books_genre`, которая уже находится в избранном

### Метод `delete_book_from_favorites`

* `test_delete_book_from_favorites` - попытка удаления книги из избранного
* `test_delete_book_from_favorites_empty_favorites` - попытка удалить книгу из избранного, когда список избранного пуст