# storing  and retrieving books from a list
books = []


def add_book(name, author):
    books.append({'name': name, 'author': author, 'read': False})


def get_books():
    return books


def mark_book_as_read(name):
    for book in books:
        if book["name"] == name:
            book['read'] = True
            break


def delete_book(book_name):
    global books
    books = [book for book in books if book['name'] != book_name]

