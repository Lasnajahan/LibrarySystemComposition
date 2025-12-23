class Book:
    def __init__(self,title,author,price):
        self.title = title
        self.author = author
        self.price = price 

    @staticmethod
    def is_expensive(price):
        return price > 500

class Library:
    def __init__(self):
        self.books = [] 

    def add_book(self,book):
        self.books.append(book)

    def show_expensive_books(self):
        print("\nExpensive Books (price > 500):")
        for b in self.books:
            if Book.is_expensive(b.price):
                print(f"- {b.title} by {b.author} → ₹{b.price}")
    
    @classmethod
    def from_list(cls, book_list):
        lib = cls()
        for item in book_list :
            book_obj = Book(item["title"],item["author"],item["price"])
            lib.add_book(book_obj)
        return lib


b1 = Book("Python Basics", "John Deo", 450)
b2 = Book("Machine Learning", "Andrew Ng", 900)
b3 = Book("Data Structures", "Narasimha", 650)


library = Library()
library.add_book(b1)
library.add_book(b2)
library.add_book(b3)

library.show_expensive_books()

book_list = [
    {"title": "AI Revolution", "author": "Mark Z", "price": 1200},
    {"title": "HTML Guide", "author": "Sam R", "price": 300}
]


lib2 = Library.from_list(book_list)
lib2.show_expensive_books()

