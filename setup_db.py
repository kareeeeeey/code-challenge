import sqlite3

def setup_db():
    with sqlite3.connect('articles.db') as conn:
        with open('lib/db/schema.sql', 'r') as f:
            schema_sql = f.read()
        conn.executescript(schema_sql)
    print("Database and tables created successfully.")

if __name__ == '__main__':
    setup_db()

