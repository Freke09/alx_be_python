class Book:
    def __init__(self, title, author, checked_out=False):
        self.title = title
        self.author = author
        self._is_checked_out = checked_out
    
    def __repr__(self):
        return f"{self.title} by {self.author}"


class Library:
    def __init__(self):
        self._books = []
    
    def add_book(self, book):
        self._books.append(book)

    def check_out_book(self, title):
        for book in self._books:
            if book.title == title and not book._is_checked_out:
                book._is_checked_out = True
    
    def return_book(self):
        for book in self._books:
            if book._is_checked_out == True:
                book._is_checked_out = False
    
    def list_available_books(self):
        for book in self._books:
            if not book._is_checked_out:
                print(f"{book}")