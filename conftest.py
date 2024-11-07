import pytest

from main import BooksCollector


@pytest.fixture(scope='function', autouse=True)
def collector():
    collector = BooksCollector()
    return collector