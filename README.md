# 📰 Python SQL Project: Authors, Articles & Magazines

This project models relationships between **Authors**, **Articles**, and **Magazines** using **raw SQL** and Python. It simulates a simple publication system where authors can write articles for different magazines.

---

## 🧠 Features

- Add and view authors, magazines, and articles
- Fetch all articles by a specific author
- Fetch all articles in a specific magazine
- Fetch all authors who’ve written for a specific magazine
- Built using raw SQL queries (no ORM)

---

## 🗃️ Database Schema

### Tables:
**Authors**
- `id` (Primary Key)
- `name`
- `bio`

**Magazines**
- `id` (Primary Key)
- `name`
- `category`

**Articles**
- `id` (Primary Key)
- `title`
- `content`
- `author_id` (Foreign Key)
- `magazine_id` (Foreign Key)

### Relationships:
- One **Author** can write many **Articles**
- One **Magazine** can contain many **Articles**
- Each **Article** is linked to one **Author** and one **Magazine**

