# coding=utf-8
import random
import string


def generate_random_string(length: int) -> str:
    """
    Генератор строки случайными символами, длины переданной в параметры.

    :param length: Длина строки.
    :return: Случайная строка.
    """
    letters = string.ascii_letters
    return "".join(random.choice(letters) for _ in range(length))


def generate_random_books_genre(
    number_of_entries: int, with_genre: bool
) -> dict[str, str]:
    """
    Генератор books_genre.

    :param number_of_entries: Кол-во книг в словаре.
    :param with_genre: С указанием genre или нет.
    :return: Возвращается наполненный случайными данными список.
    """
    books_genre: dict[str, str] = {}
    genre: list[str] = ["Фантастика", "Ужасы", "Детективы", "Мультфильмы", "Комедии"]
    if with_genre:
        for _ in range(number_of_entries):
            book_name = generate_random_string(random.randint(1, 40))
            books_genre[book_name] = random.choice(genre)
        return books_genre
    else:
        for _ in range(number_of_entries):
            book_name = generate_random_string(random.randint(1, 40))
            books_genre[book_name] = ""
        return books_genre


def generate_random_favorite_list(number_of_entries: int) -> list[str]:
    """
    Генератор favorite_list.

    :param number_of_entries: Количество книг в списке.
    :return: Список случайно длин, со случайным наполнением.
    """
    favorite_list: list[str] = []
    for _ in range(number_of_entries):
        favorite_list.append(generate_random_string(random.randint(1, 40)))
    return favorite_list
