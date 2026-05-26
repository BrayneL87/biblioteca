import json
import os

BOOKS_FILE = "books.json"

# Load books from file
def load_books():
    if os.path.exists(BOOKS_FILE):
        try:
            with open(BOOKS_FILE, 'r', encoding='utf-8') as file:
                return json.load(file)
        except:
            return []
    return []

# Save books to file
def save_books(books):
    with open(BOOKS_FILE, 'w', encoding='utf-8') as file:
        json.dump(books, file, indent=4, ensure_ascii=False)

# Test data - Add some sample books
def test_add_books():
    books = [
        {'title': 'Don Quijote', 'author': 'Miguel de Cervantes', 'year': 1605},
        {'title': 'Cien años de soledad', 'author': 'Gabriel García Márquez', 'year': 1967},
        {'title': 'El Quijote', 'author': 'Miguel de Cervantes', 'year': 1605},
        {'title': 'La Casa de los Espíritus', 'author': 'Isabel Allende', 'year': 1982},
        {'title': 'Ficciones', 'author': 'Jorge Luis Borges', 'year': 1944},
    ]
    save_books(books)
    print("✓ Books added successfully!")
    print_books()

def print_books():
    books = load_books()
    print("\n" + "="*80)
    print(f"{'TITLE':<30} {'AUTHOR':<25} {'YEAR':<10}")
    print("="*80)
    for book in books:
        print(f"{book['title']:<30} {book['author']:<25} {book['year']:<10}")

if __name__ == "__main__":
    test_add_books()
