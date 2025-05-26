from lib.db.connection import get_connection

class Magazine:
    def __init__(self, id, name, category):
        self.id = id
        self.name = name
        self.category = category

    @classmethod
    def all(cls):
        conn = get_connection()
        cursor = conn.execute("SELECT * FROM magazines")
        magazines = [cls(row["id"], row["name"], row["category"]) for row in cursor.fetchall()]
        conn.close()
        return magazines

    @classmethod
    def find_by_id(cls, magazine_id):
        conn = get_connection()
        cursor = conn.execute("SELECT * FROM magazines WHERE id = ?", (magazine_id,))
        row = cursor.fetchone()
        conn.close()
        if row:
            return cls(row["id"], row["name"], row["category"])
        return None

