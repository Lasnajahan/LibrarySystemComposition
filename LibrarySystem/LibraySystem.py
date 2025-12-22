class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price

    @staticmethod
    def is_expensive(price):
        return price > 500


class Library:
    def __init__(self):
        self.books = []   

    def add_book(self, book):
        self.books.append(book)

    def show_expensive_books(self):
        print("Expensive Books:")
        for book in self.books:
            if Book.is_expensive(book.price):
                print(f"{book.title} - {book.author} - {book.price}")

    @classmethod
    def from_list(cls, book_list):
        lib = cls()
        for b in book_list:
            lib.add_book(Book(b["title"], b["author"], b["price"]))
        return lib




books_data = [
    {"title": "AI Guide", "author": "Sara", "price": 700},
    {"title": "Python Basics", "author": "John", "price": 350},
    {"title": "Machine Learning", "author": "Mike", "price": 900}
]

library = Library.from_list(books_data)
library.show_expensive_books()
