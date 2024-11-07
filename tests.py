# coding=utf-8
import pytest


from main import BooksCollector


class TestBooksCollector:

    def test_init_books_genre(self, collector):
        assert len(collector.books_genre) == 0

    def test_init_favorites(self, collector):
        assert len(collector.favorites) == 0

    def test_init_genre(self, collector):
        assert len(collector.genre) == 5
        assert collector.genre == [
            "Фантастика",
            "Ужасы",
            "Детективы",
            "Мультфильмы",
            "Комедии",
        ]

    def test_init_genre_age_rating(self, collector):
        assert len(collector.genre_age_rating) == 2
        assert collector.genre_age_rating == ["Ужасы", "Детективы"]

    @pytest.mark.parametrize("name", ["Хорошая книга"])
    def test_add_new_book_positive_one_book(self, collector, name):
        collector.add_new_book(name)
        assert len(collector.books_genre) == 1
        assert name in collector.books_genre

    @pytest.mark.parametrize(
        "first_book, second_book", [("Первая хорошая книга", "Вторая хорошая книга")]
    )
    def test_add_new_book_positive_two_books(self, collector, first_book, second_book):
        collector.add_new_book(first_book)
        collector.add_new_book(second_book)
        assert len(collector.books_genre) == 2
        assert first_book in collector.books_genre
        assert second_book in collector.books_genre

    @pytest.mark.parametrize("name", [""])
    def test_add_new_book_negative_empty_name(self, collector, name):
        collector.add_new_book(name)
        assert len(collector.books_genre) == 0

    def test_add_new_book_negative_len_name(self, collector):
        name = "a" * 41
        collector.add_new_book(name)
        assert len(collector.books_genre) == 0

    @pytest.mark.parametrize("name", ["Хорошая книга"])
    def test_set_book_genre_positive_one_book(self, collector, name):
        collector.add_new_book(name)
        collector.set_book_genre(name, collector.genre[0])
        assert len(collector.books_genre) == 1
        assert collector.books_genre.get(name) == collector.genre[0]

    @pytest.mark.parametrize(
        "first_book, second_book", [("Первая хорошая книга", "Вторая хорошая книга")]
    )
    def test_set_book_genre_negative_two_books(
        self, collector, first_book, second_book
    ):
        collector.add_new_book(first_book)
        collector.add_new_book(second_book)
        collector.set_book_genre(first_book, collector.genre[0])
        collector.set_book_genre(second_book, collector.genre[1])
        assert len(collector.books_genre) == 2
        assert collector.books_genre.get(first_book) == collector.genre[0]
        assert collector.books_genre.get(second_book) == collector.genre[1]

    @pytest.mark.parametrize("name", ["Плохая книга"])
    def test_set_book_genre_negative_missing_book(self, collector, name):
        collector.set_book_genre(name, collector.genre[0])
        assert len(collector.books_genre) == 0

    @pytest.mark.parametrize("name, genre", [("Хорошая книга", "Плохой жанр")])
    def test_set_book_genre_negative_missing_genre(self, collector, name, genre):
        collector.add_new_book(name)
        collector.set_book_genre(name, genre)
        assert collector.books_genre.get(name) == ""

    @pytest.mark.parametrize("books_genre", [{"Хорошая книга": "Фантастика"}])
    def test_get_book_genre_positive(self, collector, books_genre):
        collector.books_genre = books_genre
        assert collector.get_book_genre(next(iter(books_genre))) == books_genre.get(
            next(iter(books_genre))
        )

    @pytest.mark.parametrize("name", ["Хорошая книга"])
    def test_get_book_genre_negative_empty_genre(self, collector, name):
        assert collector.get_book_genre(name) is None

    @pytest.mark.parametrize("genre_first, genre_second", [("Фантастика", "Ужасы")])
    @pytest.mark.parametrize(
        "books_genre",
        [
            {
                "Первая хорошая книга": "Фантастика",
                "Вторая хорошая книга": "Фантастика",
                "Третья хорошая книга": "Ужасы",
            }
        ],
    )
    def test_get_books_with_specific_genre_positive(
        self, collector, books_genre, genre_first, genre_second
    ):
        collector.books_genre = books_genre
        assert len(collector.get_books_with_specific_genre(genre_first)) == 2
        assert collector.get_books_with_specific_genre(genre_first) == [
            "Первая хорошая книга",
            "Вторая хорошая книга",
        ]
        assert len(collector.get_books_with_specific_genre(genre_second)) == 1
        assert collector.get_books_with_specific_genre(genre_second) == [
            "Третья хорошая книга"
        ]
