import sqlite3

def seed_data():
    with sqlite3.connect('articles.db') as conn:
        cur = conn.cursor()

        # Insert authors
        cur.execute("INSERT INTO authors (name, email) VALUES (?, ?)", ("Cynthia Leletu", "leletu1234@gmail.com"))
        cur.execute("INSERT INTO authors (name, email) VALUES (?, ?)", ("Vivian Kitaiyon", "kitaiyon1956@gmail.com"))

        # Insert magazines
        cur.execute("INSERT INTO magazines (name, category) VALUES (?, ?)", ("Tech Today", "Technology"))
        cur.execute("INSERT INTO magazines (name, category) VALUES (?, ?)", ("Health Weekly", "Health"))

        # Insert articles
        cur.execute("""
            INSERT INTO articles (title, content, author_id, magazine_id)
            VALUES (?, ?, ?, ?)
            """, ("The Future of AI", "AI is transforming everything...", 1, 1))
        cur.execute("""
            INSERT INTO articles (title, content, author_id, magazine_id)
            VALUES (?, ?, ?, ?)
            """, ("Healthy Living Tips", "Eat well and exercise regularly...", 2, 2))

        conn.commit()
    print("Seed data inserted successfully.")

if __name__ == '__main__':
    seed_data()
