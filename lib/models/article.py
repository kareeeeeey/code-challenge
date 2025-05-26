from lib.db.connection import get_connection

class Article:
    def __init__(self, id, title, content, author_id, magazine_id):
        self.id = id
        self.title = title
        self.content = content
        self.author_id = author_id
        self.magazine_id = magazine_id

    @classmethod
    def all(cls):
        conn = get_connection()
        cursor = conn.execute("SELECT * FROM articles")
        articles = [cls(row['id'], row['title'], row['content'], row['author_id'], row['magazine_id']) for row in cursor.fetchall()]
        conn.close()
        return articles

    @classmethod
    def find_by_id(cls, article_id):
        conn = get_connection()
        cursor = conn.execute("SELECT * FROM articles WHERE id = ?", (article_id,))
        row = cursor.fetchone()
        conn.close()
        if row:
            return cls(row['id'], row['title'], row['content'], row['author_id'], row['magazine_id'])
        return None
