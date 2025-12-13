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
        self.books = []   # Library has Book objects

    def add_book(self, book):
        self.books.append(book)

    def show_expensive_books(self):
        print("Expensive Books:")
        for b in self.books:
            if Book.is_expensive(b.price):
                print(b.title, "-", b.author, "-", b.price)

    @classmethod
    def from_list(cls, book_list):
        lib = cls()
        for title, author, price in book_list:
            lib.add_book(Book(title, author, price))
        return lib


# -------------------
# Example testing
# -------------------

# Method 1: Add books manually
b1 = Book("Python Basics", "John", 400)
b2 = Book("AI Guide", "Sara", 700)

lib = Library()
lib.add_book(b1)
lib.add_book(b2)

lib.show_expensive_books()

print()

# Method 2: Add books using class method
data = [
    ("Machine Learning", "Mike", 900),
    ("HTML Basics", "Anna", 300)
]

lib2 = Library.from_list(data)
lib2.show_expensive_books()
