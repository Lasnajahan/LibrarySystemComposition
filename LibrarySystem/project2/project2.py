class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price

    @staticmethod
    def is_expensive(price):
        if price > 500:
            return True
        
class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)


    @classmethod  
    def from_list(cls, book_list):
        library = cls()

        for data in book_list:
            book = Book(data["title"], data["author"], data["price"])
            library.add_book(book)
            return library

    def show_expensive_books(self):
        print("expensive books (price>500) : ")
        for book in self.books:
            if Book.is_expensive(book.price):
                print(f" {book.title} by {book.author} at {book.price}")

if __name__ == "__main__":
    books_data = [
        {"title": "python", "author": "john", "price": 800},
        {"title": "css", "author": "maria", "price": 450},
        {"title": "html", "author": "roy", "price": 200}
    ]

    library = Library.from_list(books_data)
    library.show_expensive_books()                



