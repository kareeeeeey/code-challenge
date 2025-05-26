# lib/debug.py
from lib.db.connection import get_connection
from lib.models.author import Author
from lib.models.magazine import Magazine
from lib.models.article import Article

# You can use this for testing your models manually
if __name__ == '__main__':
    import ipdb; ipdb.set_trace()

    # Example: Create and save a new author
    new_author = Author(name="Cynthia")
    new_author.save()

    # Example: Find an author by name
    found_authors = Author.find_by_name("Cynthia")
    print(found_authors)

    # Example: Add a magazine and article
    mag = Magazine(name="Daily Boost", category="Wellness")
    mag.save()
    new_author.add_article(magazine=mag, title="Start Your Day Right")

    # Example: View author’s articles
    print(new_author.articles())

    # Exit debugging
    # exit()

