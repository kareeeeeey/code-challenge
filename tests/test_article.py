import pytest
from lib.models.article import Article
from lib.db.connection import get_connection

def test_article_all_returns_list():
    articles = Article.all()
    assert isinstance(articles, list)
    if articles:
        assert hasattr(articles[0], 'title')
        assert hasattr(articles[0], 'content')
        assert hasattr(articles[0], 'author_id')
        assert hasattr(articles[0], 'magazine_id')

def test_article_find_by_id():
    article = Article.find_by_id(1)
    if article:
        assert article.title is not None
        assert isinstance(article.title, str)

