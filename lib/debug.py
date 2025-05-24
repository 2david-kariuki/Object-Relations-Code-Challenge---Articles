# lib/debug.py
from lib.models.author import Author
from lib.models.magazine import Magazine
from lib.models.article import Article
from lib.db.seed import seed_database

def debug():
    seed_database()
    print("Database seeded. Try the following:")
    print("author = Author.find_by_id(1)")
    print("author.articles()")
    print("author.magazines()")
    print("magazine = Magazine.find_by_id(1)")
    print("magazine.contributors()")
    import code
    code.interact(local=locals())

if __name__ == "__main__":
    debug()