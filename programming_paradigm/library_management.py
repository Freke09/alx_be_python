class Book:
    def __init__(self, title, author, checked_out):
        self.title = title
        self.author = author
        self._is_checked_out = checked_out


class Library:
    def __init__(self):
        if books is None:
            books = []
        self._books = books
    
    def add_book(self, books):
        self._books.append(book)

    def check_out_book(self, tittle):
        for book in self._books:
            if book.tittle == tittle and book in self.books:
            self.books -= book
        else:
            return f"{book} not available"
    
    def return_book(self, book):
        self.books += book
        return self.books
    
    def list_available_books(self):
        return self.books