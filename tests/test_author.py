import pytest
from lib.models.author import Author
from lib.db.connection import get_connection

def test_author_all_returns_list():
    authors = Author.all()
    assert isinstance(authors, list)
    if authors:
        assert hasattr(authors[0], 'name')
        assert hasattr(authors[0], 'email')

