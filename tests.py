# coding=utf-8
import pytest


class TestBooksCollector:

    def test_init_books_genre(self, setup):
        """Проверка дефолтного значения books_genre"""
        assert isinstance(setup.books_genre, dict) == True
        assert len(setup.books_genre) == 0

    def test_init_favorites(self, setup):
        """Проверка дефолтного значения favorites"""
        assert isinstance(setup.favorites, list) == True
        assert len(setup.favorites) == 0

    @pytest.mark.parametrize(
        "genre", [["Фантастика", "Ужасы", "Детективы", "Мультфильмы", "Комедии"]]
    )
    def test_init_genre(self, setup, genre):
        """Проверка дефолтного значения genre"""
        assert isinstance(setup.genre, list) == True
        assert len(setup.genre) == 5
        assert setup.genre == genre

    @pytest.mark.parametrize("genre_age_rating", [["Ужасы", "Детективы"]])
    def test_init_genre_age_rating(self, setup, genre_age_rating):
        """Проверка дефолтного значения genre_age_rating"""
        assert isinstance(setup.genre_age_rating, list) == True
        assert len(setup.genre_age_rating) == 2
        assert setup.genre_age_rating == genre_age_rating

    @pytest.mark.parametrize("name", ["Первая хорошая книга", "Вторая хорошая книга"])
    def test_add_new_book_acceptable_length_name(self, setup, name):
        """Проверка метода add_new_book,
        попытка добавления книг"""
        setup.add_new_book(name)
        assert len(setup.books_genre) == 1
        assert name in setup.books_genre

    @pytest.mark.parametrize("name", ["", "a" * 42])
    def test_add_new_book_negative_length_name(self, setup, name):
        """Проверка метода add_new_book,
        ввод недопустимых значений"""
        setup.add_new_book(name)
        assert len(setup.books_genre) == 0

    @pytest.mark.parametrize(
        "books_genre", [{"Хорошая книга": ""}, {"Еще одна хорошая книга": ""}]
    )
    def test_set_book_genre_exist_books(self, setup, books_genre):
        """Проверка метода set_book_genre,
        установка жанра книге"""
        setup.books_genre = books_genre
        book_name = next(iter(books_genre))
        setup.set_book_genre(book_name, setup.genre[0])
        assert len(setup.books_genre) == 1
        assert setup.books_genre.get(book_name) == setup.genre[0]

    @pytest.mark.parametrize("name", ["Плохая книга", "Еще плохая одна книга"])
    def test_set_book_genre_missing_book(self, setup, name):
        """Проверка метода set_book_genre,
        попытка установка жанра книге, отсутствующей в books_genre"""
        setup.set_book_genre(name, setup.genre[0])
        assert len(setup.books_genre) == 0

    @pytest.mark.parametrize(
        "books_genre, genre",
        [
            ({"Первая хорошая книга": ""}, "Роман"),
            ({"Вторая хорошая книга": ""}, "Научпок"),
        ],
    )
    def test_set_book_genre_missing_genre(self, setup, books_genre, genre):
        """Проверка метода set_book_genre,
        попытка добавление несуществующего жанра в genre"""
        name_book = list(books_genre.keys())[0]
        setup.set_book_genre(name_book, genre)
        assert setup.books_genre.get(name_book) is None

    @pytest.mark.parametrize(
        "books_genre",
        [{"Хорошая книга": "Фантастика"}, {"Еще одна хорошая книга": "Детективы"}],
    )
    def test_get_book_genre(self, setup, books_genre):
        """Проверка метода get_book_genre, получение жанра существующей книги с указанным жанром"""
        setup.books_genre = books_genre
        assert setup.get_book_genre(next(iter(books_genre))) == books_genre.get(
            next(iter(books_genre))
        )

    @pytest.mark.parametrize("name", ["Плохая книга", "Еще одна плохая книга"])
    def test_get_book_genre_empty_book(self, setup, name):
        """Проверка метода get_book_genre, получение жанра
        по книге которой нет в books_genre"""
        assert setup.get_book_genre(name) is None

    @pytest.mark.parametrize(
        "genre, books_genre",
        [
            (
                "Фантастика",
                {
                    "Первая хорошая книга": "Фантастика",
                    "Вторая хорошая книга": "Фантастика",
                    "Третья хорошая книга": "Ужасы",
                },
            ),
            (
                "Детективы",
                {
                    "Четвертая хорошая книга": "Детективы",
                    "Пятая хорошая книга": "Детективы",
                    "Шестая хорошая книга": "Комедии",
                },
            ),
        ],
    )
    def test_get_books_with_specific_genre(self, setup, books_genre, genre):
        """Проверка метода get_books_with_specific_genre,
        получения списка книг по заданному жанру"""
        setup.books_genre = books_genre
        assert len(setup.get_books_with_specific_genre(genre)) == 2
        assert setup.get_books_with_specific_genre(genre) == [
            key for key, value in books_genre.items() if value == genre
        ]

    @pytest.mark.parametrize("genre", ["Фантастика"])
    def test_get_books_with_specific_genre_negative(self, setup, genre):
        """Проверка метода get_books_with_specific,
        получение списка книг по существующему жанру, когда список книг пустой"""
        assert setup.get_books_with_specific_genre(genre) == []

    @pytest.mark.parametrize(
        "books_genre, name",
        (
            [
                {
                    "Первая хорошая книга": "Фантастика",
                    "Вторая хорошая книга": "Фантастика",
                    "Третья хорошая книга": "Ужасы",
                },
                "Первая хорошая книга",
            ],
        ),
    )
    def test_get_books_genre(self, setup, books_genre, name):
        """Проверка модуля get_books_genre,
        на то что возвращает словарь"""
        setup.books_genre = books_genre
        assert isinstance(setup.get_books_genre(), dict) == True
        assert (setup.get_books_genre() == books_genre) == True

    @pytest.mark.parametrize(
        "books_genre, books_list",
        (
            [
                {
                    "Первая хорошая книга": "Фантастика",
                    "Вторая хорошая книга": "Фантастика",
                    "Третья взрослая книга": "Ужасы",
                },
                ["Первая хорошая книга", "Вторая хорошая книга"],
            ],
        ),
    )
    def test_get_books_for_children(self, setup, books_genre, books_list):
        """Проверка метода get_books_for_children,
        проверка возвращает ли метод список книг исключая книг с взрослым жанром"""
        setup.books_genre = books_genre
        assert isinstance(setup.get_books_for_children(), list) == True
        assert len(setup.get_books_for_children()) == 2
        assert setup.get_books_for_children() == books_list

    @pytest.mark.parametrize(
        "books_genre, name",
        [
            (
                {
                    "Первая хорошая книга": "Фантастика",
                    "Вторая хорошая книга": "Фантастика",
                    "Третья взрослая книга": "Ужасы",
                },
                "Первая хорошая книга",
            ),
            (
                {
                    "Четвертая взрослая книга": "Детективы",
                    "Вторая хорошая книга": "Мультфильмы",
                    "Первая хорошая книга": "Комедии",
                },
                "Вторая хорошая книга",
            ),
        ],
    )
    def test_add_book_in_favorites_existing_name(self, setup, books_genre, name):
        """Проверка метода add_book_in_favorites,
        попытка добавить книгу в избранное"""
        setup.books_genre = books_genre
        setup.add_book_in_favorites(name)
        assert len(setup.favorites) == 1
        assert name in setup.favorites

    @pytest.mark.parametrize(
        "books_genre, name",
        [
            (
                {
                    "Первая хорошая книга": "Фантастика",
                    "Вторая хорошая книга": "Фантастика",
                    "Третья взрослая книга": "Ужасы",
                },
                "Шестая хорошая книга",
            ),
            (
                {
                    "Четвертая взрослая книга": "Детективы",
                    "Вторая хорошая книга": "Мультфильмы",
                    "Первая хорошая книга": "Комедии",
                },
                "Моя хорошая книга",
            ),
        ],
    )
    def test_add_book_in_favorites_missing_name(self, setup, books_genre, name):
        """Проверка метода add_book_in_favorites,
        попытка добавить в избранное книгу, отсутствующую в books_genre"""
        setup.books_genre = books_genre
        setup.add_book_in_favorites(name)
        assert setup.favorites == []

    @pytest.mark.parametrize(
        "books_genre, favorites, name",
        [
            (
                {
                    "Первая хорошая книга": "Фантастика",
                    "Вторая хорошая книга": "Фантастика",
                    "Третья взрослая книга": "Ужасы",
                },
                ["Первая хорошая книга"],
                "Первая хорошая книга",
            ),
            (
                {
                    "Моя хорошая книга": "Детективы",
                    "Вторая хорошая книга": "Мультфильмы",
                    "Первая хорошая книга": "Комедии",
                },
                ["Моя хорошая книга"],
                "Моя хорошая книга",
            ),
        ],
    )
    def test_add_book_in_favorites_name_in_favorites(
        self, setup, books_genre, favorites, name
    ):
        """Проверка метода add_book_in_favorites,
        попытка добавить в избранное книгу которая уже в избранном"""
        setup.books_genre = books_genre
        setup.favorites = favorites
        init_length = len(setup.favorites)
        setup.add_book_in_favorites(name)
        assert len(setup.favorites) == init_length

    @pytest.mark.parametrize(
        "favorites, name",
        [
            (["Первая книга", "Вторая книга"], "Первая книга"),
            (["Четвертая книга", "Пятая книга"], "Пятая книга"),
        ],
    )
    def test_delete_book_from_favorites(self, setup, favorites, name):
        """Проверка метода delete_book_from_favorites,
        попытка удалить книгу присутствующую в favorites"""
        setup.favorites = favorites
        init_length = len(setup.favorites)
        setup.delete_book_from_favorites(name)
        assert len(setup.favorites) == (init_length - 1)
        assert name is not setup.favorites

    @pytest.mark.parametrize(
        "favorites, name",
        [
            (["Первая книга", "Вторая книга"], "Пятая книга"),
            (["Четвертая книга", "Пятая книга"], "Первая книга"),
        ],
    )
    def test_delete_book_from_favorites_empty_favorites(self, setup, favorites, name):
        """Проверка метода delete_book_from_favorites,
        попытка удалить из списка избранного книги, которой в ней нет"""
        setup.favorites = favorites
        init_length = len(setup.favorites)
        setup.delete_book_from_favorites(name)
        assert len(setup.favorites) == init_length
        assert setup.favorites == favorites
