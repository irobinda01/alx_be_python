class Book:
  def __init__(self, title, author):
    self.title = title
    self.author = author
    self._is_checked_out = False

  def check_out(self):
    if not self._is_checked_out:
      self._is_checked_out = True

  def return_book(self):
    self._is_checked_out = False

  def is_available(self):
    if not self._is_checked_out:
      return True
    return False


class Library:
  def __init__(self):
    self._books = []

  def add_book(self, book):
    if isinstance(book, Book):
      self._books.append(book)

  def check_out_book(self, title):
    for book in self._books:
      if book.title == title:
        book.check_out()
  
  def return_book(self, title):
    for book in self._books:
      if book.title == title:
        book.return_book()

  def list_available_books(self):
    available_books = [f"{book.title} by {book.author}" for book in self._books if book.is_available()]
    for book in available_books:
      print(book)
