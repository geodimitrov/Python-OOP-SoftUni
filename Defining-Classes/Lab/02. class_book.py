
class Book:
    def __init__(self, name, author, pages):
        self.name = name
        self.author = author
        self.pages = pages

#Examples to test the code
book = Book("The Name of the Rose", "Umberto Eco", 700)
print(book.name)
print(book.author)
print(book.pages)