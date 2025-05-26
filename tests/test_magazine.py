import pytest
from lib.models.magazine import Magazine
from lib.db.connection import get_connection

def test_magazine_all_returns_list():
    magazines = Magazine.all()
    assert isinstance(magazines, list)
    if magazines:
        assert hasattr(magazines[0], 'name')
        assert hasattr(magazines[0], 'category')

def test_magazine_find_by_id():
    magazine = Magazine.find_by_id(1)
    if magazine:
        assert magazine.name is not None
        assert isinstance(magazine.name, str)

