# coding=utf-8
import pytest

from main import BooksCollector


@pytest.fixture(scope="function", autouse=True)
def setup():
    collector = BooksCollector()
    return collector


# TODO создать фикстуры для генерации тестов
