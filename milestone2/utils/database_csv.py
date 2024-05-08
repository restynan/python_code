# storing  and retrieving books from a csv
import csv


def create_book_table():
    with open("books.csv", 'w'):
        pass


def add_book(name, author):
    with open("books.csv", 'a') as books_file:
        book_writer = csv.DictWriter(books_file, fieldnames=["name", "author", "read"])
        if len(get_books()) == 0:
            book_writer.writeheader()
        book_writer.writerow({'name': name, 'author': author, 'read': '0'})


def get_books():
    with open("books.csv", 'r') as books_file:
        reader = csv.DictReader(books_file)  # returns a dictionary
        return list(reader)


def _save_all_books(books):
    with open("books.csv", 'w') as books_file:
        book_writer = csv.DictWriter(books_file, fieldnames=["name", "author", "read"])
        book_writer.writeheader()
        book_writer.writerows(books)


def mark_book_as_read(name):
    books = get_books()
    for book in books:
        if book["name"] == name:
            book["read"] = "1"
    _save_all_books(books)


def delete_book(book_name):
    books = get_books()
    books = [book for book in books if book['name'] != book_name]
    _save_all_books(books)
