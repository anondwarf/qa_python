# coding=utf-8
import random

import pytest

import helper
from main import BooksCollector


class TestBooksCollector:

    def test_init_books_genre_default_values(self, collector: BooksCollector) -> None:
        """
        Проверка дефолтного значения books_genre

        :param collector: Фикстура из conftest.py
        """
        assert len(collector.books_genre) == 0

    def test_init_favorites_default_values(self, collector: BooksCollector) -> None:
        """
        Проверка дефолтного значения favorites

        :param collector: Фикстура из conftest.py
        """
        assert len(collector.favorites) == 0

    @pytest.mark.parametrize(
        "genre", [["Фантастика", "Ужасы", "Детективы", "Мультфильмы", "Комедии"]]
    )
    def test_init_genre_default_values(
        self, collector: BooksCollector, genre: list[str]
    ) -> None:
        """
        Проверка дефолтного значения genre

        :param collector: Фикстура из conftest.py
        :param genre: Параметризация теста
        """
        assert collector.genre == genre

    @pytest.mark.parametrize("genre_age_rating", [["Ужасы", "Детективы"]])
    def test_init_genre_age_rating_default_value(
        self, collector: BooksCollector, genre_age_rating: list[str]
    ) -> None:
        """
        Проверка дефолтного значения genre_age_rating
        :param collector: Фикстура из conftest.py
        :param genre_age_rating: Параметризация теста
        """
        assert collector.genre_age_rating == genre_age_rating

    @pytest.mark.parametrize(
        "name",
        [
            helper.generate_random_string(1),
            helper.generate_random_string(2),
            helper.generate_random_string(random.randint(3, 38)),
            helper.generate_random_string(39),
            helper.generate_random_string(40),
        ],
    )
    def test_add_new_book_acceptable_length_name(
        self, collector: BooksCollector, name: str
    ) -> None:
        """
        Проверка метода add_new_book, попытка добавления книг

        :param collector: Фикстура из conftest.py
        :param name: Параметризация теста, используется функция
        `helper.generate_random_string` для генерации строки
        """
        collector.add_new_book(name)
        assert name in collector.books_genre

    @pytest.mark.parametrize(
        "books_genre, name",
        [
            (
                helper.generate_random_books_genre(random.randint(1, 15), True),
                helper.generate_random_string(random.randint(1, 40)),
            ),
            (
                helper.generate_random_books_genre(random.randint(1, 15), False),
                helper.generate_random_string(random.randint(1, 40)),
            ),
        ],
    )
    def test_add_new_book_books_genre_not_empty(
        self, collector: BooksCollector, name: str, books_genre: dict[str, str]
    ) -> None:
        """
        Проверка того что при добавлении в не пустой словарь `books_genre`,
        новой книги - старые не удаляются

        :param collector: Фикстура из conftest.py
        :param name: Параметризация теста
        :param books_genre: Параметризация теста
        """
        init_length = len(books_genre)
        collector.books_genre = books_genre
        collector.add_new_book(name)
        assert len(collector.books_genre) == init_length + 1

    @pytest.mark.parametrize(
        "name",
        [
            "",
            helper.generate_random_string(41),
            helper.generate_random_string(42),
            helper.generate_random_string(random.randint(43, 100)),
        ],
    )
    def test_add_new_book_negative_length_name(
        self, collector: BooksCollector, name: str
    ) -> None:
        """
        Проверка метода add_new_book, ввод недопустимых значений

        :param collector: Фикстура из conftest.py
        :param name: Параметризация теста
        """
        collector.add_new_book(name)
        assert len(collector.books_genre) == 0

    @pytest.mark.parametrize(
        "books_genre",
        [
            helper.generate_random_books_genre(random.randint(1, 15), False),
            helper.generate_random_books_genre(random.randint(1, 15), False),
        ],
    )
    def test_set_book_genre_exist_books(
        self, collector: BooksCollector, books_genre: dict[str, str]
    ) -> None:
        """
        Проверка метода set_book_genre, установка жанра книге

        :param collector: Фикстура из conftest.py
        :param books_genre: Параметризация теста
        """
        collector.books_genre = books_genre
        book_name = next(iter(books_genre))
        set_genre = random.choice(collector.genre)
        collector.set_book_genre(book_name, set_genre)
        assert collector.books_genre.get(book_name) == set_genre

    @pytest.mark.parametrize(
        "name",
        [
            helper.generate_random_string(random.randint(1, 40)),
            helper.generate_random_string(random.randint(1, 40)),
        ],
    )
    def test_set_book_genre_missing_book(
        self, collector: BooksCollector, name: str
    ) -> None:
        """
        Проверка метода set_book_genre, попытка установка жанра книге,
        отсутствующей в books_genre

        :param collector: Фикстура из conftest.py
        :param name: Параметризация теста
        """
        collector.set_book_genre(name, collector.genre[0])
        assert len(collector.books_genre) == 0

    @pytest.mark.parametrize(
        "books_genre, genre",
        [
            (
                helper.generate_random_books_genre(random.randint(1, 15), False),
                helper.generate_random_string(random.randint(1, 40)),
            ),
            (
                helper.generate_random_books_genre(random.randint(1, 15), False),
                helper.generate_random_string(random.randint(1, 40)),
            ),
        ],
    )
    def test_set_book_genre_missing_genre(
        self, collector: BooksCollector, books_genre: dict[str, str], genre: str
    ) -> None:
        """
        Проверка метода set_book_genre, попытка добавление несуществующего
        жанра в genre

        :param collector: Фикстура из conftest.py
        :param books_genre: Параметризация теста
        :param genre: Параметризация теста
        """
        name_book = list(books_genre.keys())[0]
        collector.set_book_genre(name_book, genre)
        assert collector.books_genre.get(name_book) is None

    @pytest.mark.parametrize(
        "books_genre",
        [
            helper.generate_random_books_genre(random.randint(1, 15), True),
            helper.generate_random_books_genre(random.randint(1, 15), True),
        ],
    )
    def test_get_book_genre(
        self, collector: BooksCollector, books_genre: dict[str, str]
    ) -> None:
        """
        Проверка метода get_book_genre, получение жанра существующей книги с
        указанным жанром

        :param collector: Фикстура из conftest.py
        :param books_genre: Параметризация теста
        """
        collector.books_genre = books_genre
        assert collector.get_book_genre(next(iter(books_genre))) == books_genre.get(
            next(iter(books_genre))
        )

    @pytest.mark.parametrize(
        "name",
        [
            helper.generate_random_string(random.randint(1, 40)),
            helper.generate_random_string(random.randint(1, 40)),
        ],
    )
    def test_get_book_genre_empty_book(
        self, collector: BooksCollector, name: str
    ) -> None:
        """
        Проверка метода get_book_genre, получение жанра по книге которой нет в
        books_genre

        :param collector: Фикстура из conftest.py
        :param name: Параметризация теста
        """
        assert collector.get_book_genre(name) is None

    @pytest.mark.parametrize(
        "books_genre",
        [
            helper.generate_random_books_genre(random.randint(1, 15), True),
            helper.generate_random_books_genre(random.randint(1, 15), True),
        ],
    )
    def test_get_books_with_specific_genre_count_genre(
        self, collector: BooksCollector, books_genre: dict[str, str]
    ) -> None:
        """
        Проверка метода get_books_with_specific_genre, получения списка книг
        по заданному жанру

        :param collector: Фикстура из conftest.py
        :param books_genre: Параметризация теста
        """
        collector.books_genre = books_genre
        random_genre: str = random.choice(list(collector.books_genre.values()))
        count_genre_init = sum(
            1 for value in books_genre.values() if value == random_genre
        )
        assert (
            len(collector.get_books_with_specific_genre(random_genre))
            == count_genre_init
        )

    @pytest.mark.parametrize(
        "books_genre",
        [
            helper.generate_random_books_genre(random.randint(1, 15), True),
            helper.generate_random_books_genre(random.randint(1, 15), True),
        ],
    )
    def test_get_books_with_specific_genre_data_comparison(
        self, collector: BooksCollector, books_genre: dict[str, str]
    ) -> None:
        """
        Проверка, что при вызове метода `get_books_with_specific_genre`
        возвращенный список корректен.

        :param collector: Фикстура возвращающая BooksCollector.
        :param books_genre: Параметризация теста, генерируется случайный dict books_genre
        """
        collector.books_genre = books_genre
        random_genre: str = random.choice(list(collector.books_genre.values()))
        assert collector.get_books_with_specific_genre(random_genre) == [
            key for key, value in books_genre.items() if value == random_genre
        ]

    @pytest.mark.parametrize("genre", ["Фантастика"])
    def test_get_books_with_specific_genre_negative(
        self, collector: BooksCollector, genre: str
    ) -> None:
        """
        Проверка метода get_books_with_specific, получение списка книг по
        существующему жанру, когда список книг пустой

        :param collector: Фикстура из conftest.py
        :param genre: Параметризация теста
        """
        assert collector.get_books_with_specific_genre(genre) == []

    @pytest.mark.parametrize(
        "books_genre",
        (
            [
                helper.generate_random_books_genre(random.randint(1, 15), True),
                helper.generate_random_books_genre(random.randint(1, 15), False),
            ],
        ),
    )
    def test_get_books_genre(
        self, collector: BooksCollector, books_genre: dict[str, str]
    ) -> None:
        """
        Проверка модуля get_books_genre, на то что возвращает словарь

        :param collector: Фикстура из conftest.py
        :param books_genre: Параметризация теста
        """
        collector.books_genre = books_genre
        assert collector.get_books_genre() == books_genre

    @pytest.mark.parametrize(
        "books_genre",
        [
            helper.generate_random_books_genre(random.randint(1, 15), True),
            helper.generate_random_books_genre(random.randint(1, 15), True),
        ],
    )
    def test_get_books_for_children_match_items(
        self,
        collector: BooksCollector,
        books_genre: dict[str, str],
    ) -> None:
        """
        Проверка метода get_books_for_children, проверка возвращает ли метод
        список книг исключая книг с взрослым жанром

        :param collector: Фикстура из conftest.py
        """
        collector.books_genre = books_genre
        set_not_children_genre = set(collector.genre_age_rating)
        match_books: list[str] = []
        for key, value in books_genre.items():
            if value not in set_not_children_genre:
                match_books.append(key)
        assert collector.get_books_for_children() == match_books

    @pytest.mark.parametrize(
        "books_genre",
        [
            helper.generate_random_books_genre(random.randint(5, 15), True),
            helper.generate_random_books_genre(random.randint(5, 15), True),
        ],
    )
    def test_get_books_for_children_count_books(
        self, collector: BooksCollector, books_genre: dict[str, str]
    ) -> None:
        """
        Проверка, что при вызове функции `get_books_for_children`, количество
        книг в списке корректно.

        :param collector: Фикстура возвращающая BooksCollector.
        :param books_genre: Параметризация теста, генерируется случайный dict books_genre
        """
        collector.books_genre = books_genre
        set_not_children_genre = set(collector.genre_age_rating)
        match_books: list[str] = []
        for key, value in books_genre.items():
            if value not in set_not_children_genre:
                match_books.append(key)
        assert len(collector.get_books_for_children()) == len(match_books)

    @pytest.mark.parametrize(
        "books_genre",
        [
            helper.generate_random_books_genre(random.randint(1, 15), True),
            helper.generate_random_books_genre(random.randint(1, 15), False),
        ],
    )
    def test_add_book_in_favorites_count_book(
        self, collector: BooksCollector, books_genre: dict[str, str]
    ) -> None:
        """
        Проверка метода add_book_in_favorites, попытка добавить книгу в
        избранное

        :param collector: Фикстура из conftest.py
        :param books_genre: Параметризация теста
        """
        collector.books_genre = books_genre
        choice_book = random.choice(list(collector.books_genre.keys()))
        collector.add_book_in_favorites(choice_book)
        assert len(collector.favorites) == 1

    @pytest.mark.parametrize(
        "books_genre",
        [
            helper.generate_random_books_genre(random.randint(1, 15), True),
            helper.generate_random_books_genre(random.randint(1, 15), False),
        ],
    )
    def test_add_book_in_favorites_data_comparison(
        self, collector: BooksCollector, books_genre: dict[str, str]
    ) -> None:
        """
        Проверка, что при добавлении книги в избранное, она добавляется в
        список.

        :param collector: Фикстура возвращающая BooksCollector.
        :param books_genre: Параметризация теста, генерирует случайный dict books_genre
        """
        collector.books_genre = books_genre
        choice_book = random.choice(list(collector.books_genre.keys()))
        collector.add_book_in_favorites(choice_book)
        assert choice_book in collector.favorites

    @pytest.mark.parametrize(
        "books_genre, name",
        [
            (
                helper.generate_random_books_genre(random.randint(1, 15), True),
                helper.generate_random_string(random.randint(1, 40)),
            ),
            (
                helper.generate_random_books_genre(random.randint(1, 15), True),
                helper.generate_random_string(random.randint(1, 40)),
            ),
        ],
    )
    def test_add_book_in_favorites_missing_name(
        self, collector: BooksCollector, books_genre: dict[str, str], name: str
    ) -> None:
        """
        Проверка метода add_book_in_favorites, попытка добавить в избранное
        книгу, отсутствующую в books_genre

        :param collector: Фикстура из conftest.py
        :param books_genre: Параметризация теста
        :param name: Параметризация теста
        """
        collector.books_genre = books_genre
        collector.add_book_in_favorites(name)
        assert collector.favorites == []

    @pytest.mark.parametrize(
        "books_genre",
        [
            helper.generate_random_books_genre(random.randint(1, 15), True),
            helper.generate_random_books_genre(random.randint(1, 15), False),
        ],
    )
    def test_add_book_in_favorites_name_in_favorites(
        self,
        collector: BooksCollector,
        books_genre: dict[str, str],
    ) -> None:
        """
        Проверка метода add_book_in_favorites, попытка добавить в избранное
        книгу которая уже в избранном

        :param collector: Фикстура из conftest.py
        """
        collector.books_genre = books_genre
        choice_book = random.choice(list(books_genre.keys()))
        collector.favorites = [choice_book]
        init_length = len(collector.favorites)
        collector.add_book_in_favorites(choice_book)
        assert len(collector.favorites) == init_length

    @pytest.mark.parametrize(
        "favorites",
        [
            helper.generate_random_favorite_list(random.randint(1, 15)),
            helper.generate_random_favorite_list(random.randint(1, 15)),
        ],
    )
    def test_delete_book_from_favorites_length(
        self, collector: BooksCollector, favorites: list[str]
    ) -> None:
        """
        Проверка, что при удалении книги из списка избранного, размер списка
        изменяется.

        :param collector: Фикстура возвращающая BooksCollector.
        :param favorites: Параметризация теста, генерируется рандомный список избранного.
        """
        collector.favorites = favorites
        init_length = len(collector.favorites)
        choice_book = random.choice(list(favorites))
        collector.delete_book_from_favorites(choice_book)
        assert len(collector.favorites) == (init_length - 1)

    @pytest.mark.parametrize(
        "favorites",
        [
            helper.generate_random_favorite_list(random.randint(1, 15)),
            helper.generate_random_favorite_list(random.randint(1, 15)),
        ],
    )
    def test_delete_book_from_favorites_data_comparison(
        self, collector: BooksCollector, favorites: list[str]
    ) -> None:
        """
        Проверка, что при удалении книги из избранного, она удаляется.

        :param collector: Фикстура возвращающая BooksCollector.
        :param favorites: Параметризация теста, генерируется рандомный список избранного.
        """
        collector.favorites = favorites
        choice_book = random.choice(list(favorites))
        collector.delete_book_from_favorites(choice_book)
        assert choice_book is not collector.favorites

    @pytest.mark.parametrize(
        "favorites, name",
        [
            (
                helper.generate_random_favorite_list(random.randint(1, 15)),
                helper.generate_random_string(random.randint(1, 40)),
            ),
            (
                helper.generate_random_favorite_list(random.randint(1, 15)),
                helper.generate_random_string(random.randint(1, 40)),
            ),
        ],
    )
    def test_delete_book_from_favorites_missing_name_length(
        self, collector: BooksCollector, favorites: list[str], name: str
    ) -> None:
        """
        Проверка, что при попытке удалить книгу из списка избранного,
        которой в нем нет, сам длина списка избранного не изменяется.

        :param collector: Фикстура возвращающая BooksCollector.
        :param favorites: Параметризация теста, генерируется рандомный список избранного.
        :param name: Параметризация теста, генерируется случайная строка.
        """
        collector.favorites = favorites
        init_length = len(collector.favorites)
        collector.delete_book_from_favorites(name)
        assert len(collector.favorites) == init_length

    @pytest.mark.parametrize(
        "favorites",
        [
            helper.generate_random_favorite_list(random.randint(1, 15)),
            helper.generate_random_favorite_list(random.randint(1, 15)),
        ],
    )
    def test_delete_book_from_favorites_missing_name_data_comparison(
        self, collector: BooksCollector, favorites: list[str]
    ) -> None:
        """
        Проверка, что при попытке удалении из списка избранного книги,
        которой в нем нет - элементы списка не изменяются.

        :param collector: Фикстура возвращающая BooksCollector.
        :param favorites: Параметризация теста, генерируется рандомный список избранного.
        """
        collector.favorites = favorites
        choice_book = random.choice(list(favorites))
        collector.delete_book_from_favorites(choice_book)
        assert collector.favorites == favorites
