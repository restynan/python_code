from utils import database

USER_CHOICE = """
Enter:
- 'a' to add a new book
- 'l' to list all books
- 'r' to mark a book as read
- 'd' to delete a book
- 'q' to quit

Your choice: """


def prompt_add_book():
    book_name = input("Enter book name: ")
    book_author = input("Enter book author: ")
    database.add_book(book_name, book_author)


def prompt_list_books():
    books = database.get_books()
    print(books)
    for book in books:
        read = 'YES' if book['read'] else 'NO'
        print(f"name: {book['name']}, author: {book['author']}, read: {read}")


def prompt_read_book():
    read_book = input("Enter the book name you have read: ")
    database.mark_book_as_read(read_book)


def prompt_delete_book():
    book_name = input("Enter the name of the book you want to delete: ")
    database.delete_book(book_name)


operations = {
    'a': prompt_add_book,
    'l': prompt_list_books,
    'r': prompt_read_book,
    'd': prompt_delete_book
}


def user_input():
    database.create_book_table()  # helps create csv if it doesn't exist
    user_choice = input(USER_CHOICE)
    while user_choice != 'q':
        if user_choice in operations:
            user_operation = operations[user_choice]
            user_operation()
        else:
            print("unknown command. Please try again ")
        user_choice = input(USER_CHOICE)


user_input()
