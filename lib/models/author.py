from lib.db.connection import get_connection

class Author:
    def __init__(self, id, name, email):
        self.id = id
        self.name = name
        self.email = email

    @classmethod
    def all(cls):
        conn = get_connection()
        cursor = conn.execute("SELECT * FROM authors")
        authors = [cls(row['id'], row['name'], row['email']) for row in cursor.fetchall()]
        conn.close()
        return authors

    @classmethod
    def find_by_id(cls, author_id):
        conn = get_connection()
        cursor = conn.execute("SELECT * FROM authors WHERE id = ?", (author_id,))
        row = cursor.fetchone()
        conn.close()
        if row:
            return cls(row['id'], row['name'], row['email'])
        return None
