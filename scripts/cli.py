import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from lib.db.connection import get_connection
from lib.db.seed import seed_database
from scripts.run_queries import (
    authors_for_magazine,
    magazines_with_multiple_authors,
    article_count_per_magazine,
    most_prolific_author
)

def print_help():
    print("""
Available Commands:
  help                - Show this help message
  seed                - Seed the database with test data
  list authors        - List all authors
  list magazines      - List all magazines
  list articles       - List all articles
  authors <magazine_id> - List authors for a specific magazine ID
  multi_author_mags   - List magazines with multiple authors
  article_counts      - Show article count per magazine
  prolific_author      - Show the most prolific author
  exit                - Exit the CLI
""")

def list_authors():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM authors")
    authors = [dict(row) for row in cursor.fetchall()]
    conn.close()
    if not authors:
        print("No authors found.")
    for author in authors:
        print(f"ID: {author['id']}, Name: {author['name']}")

def list_magazines():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM magazines")
    magazines = [dict(row) for row in cursor.fetchall()]
    conn.close()
    if not magazines:
        print("No magazines found.")
    for magazine in magazines:
        print(f"ID: {magazine['id']}, Name: {magazine['name']}, Category: {magazine['category']}")

def list_articles():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT a.id, a.title, auth.name AS author_name, m.name AS magazine_name
        FROM articles a
        JOIN authors auth ON a.author_id = auth.id
        JOIN magazines m ON a.magazine_id = m.id
    """)
    articles = [dict(row) for row in cursor.fetchall()]
    conn.close()
    if not articles:
        print("No articles found.")
    for article in articles:
        print(f"ID: {article['id']}, Title: {article['title']}, Author: {article['author_name']}, Magazine: {article['magazine_name']}")

def main():
    print("Welcome to the Article Database CLI. Type 'help' for commands.")
    while True:
        try:
            command = input("> ").strip().lower()
            parts = command.split()

            if command == "help":
                print_help()

            elif command == "seed":
                print("Seeding database...")
                seed_database()

            elif command == "list authors":
                list_authors()

            elif command == "list magazines":
                list_magazines()

            elif command == "list articles":
                list_articles()

            elif parts[0] == "authors" and len(parts) == 2:
                try:
                    magazine_id = int(parts[1])
                    authors = authors_for_magazine(magazine_id)
                    if not authors:
                        print(f"No authors found for magazine ID {magazine_id}.")
                    for author in authors:
                        print(f"ID: {author['id']}, Name: {author['name']}")
                except ValueError:
                    print("Error: Magazine ID must be a number.")

            elif command == "multi_author_mags":
                magazines = magazines_with_multiple_authors()
                if not magazines:
                    print("No magazines with multiple authors found.")
                for mag in magazines:
                    print(f"ID: {mag['id']}, Name: {mag['name']}, Category: {mag['category']}")

            elif command == "article_counts":
                counts = article_count_per_magazine()
                if not counts:
                    print("No magazines found.")
                for item in counts:
                    print(f"Magazine: {item['name']}, Article Count: {item['article_count']}")

            elif command == "prolific_author":
                author = most_prolific_author()
                if author:
                    print(f"Most Prolific Author: ID: {author['id']}, Name: {author['name']}")
                else:
                    print("No authors found.")

            elif command == "exit":
                print("Goodbye!")
                break

            else:
                print("Unknown command. Type 'help' for available commands.")

        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    main()