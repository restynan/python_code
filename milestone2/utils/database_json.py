# storing  and retrieving books from a  json
import json
books_file = "books.json"


def create_book_table():
    with open(books_file, 'w') as file:
        json.dump([], file)


def add_book(name, author):
    book_new = {"name": name, "author": author, "read": False}
    books = get_books()
    books.append(book_new)
    _save_all_books(books)


def get_books():
    with open(books_file, 'r') as file:
        return json.load(file)


def _save_all_books(books):
    with open(books_file, 'w') as file:
        json.dump(books, file)


def mark_book_as_read(name):
    books = get_books()
    for book in books:
        if book["name"] == name:
            book["read"] = True
    _save_all_books(books)


def delete_book(book_name):
    books = get_books()
    books = [book for book in books if book['name'] != book_name]
    _save_all_books(books)
