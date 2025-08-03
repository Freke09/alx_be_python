class Book:
    def __init__(self, title, author, checked_out=False):
        self.title = title
        self.author = author
        self._is_checked_out = checked_out


class Library:
    def __init__(self):
        self.books = []
    
    def add_book(self, book):
        self.books.append(book)

    def check_out_book(self, title):
        for book in self.books:
            if book.title == title and book._is_checked_out:
                self.books.remove(book)
    
    def return_book(self, title):
        for book in self.books:
            if book.title == title and book._is_checked_out:
                book._is_checked_out = False
                self.books.append(book)
    
    def list_available_books(self):
        return self.books