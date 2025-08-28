
# Base class for any book
class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year


class HarryPotterBook(Book):
    def __init__(self, title, year, house):
        super().__init__(title, "J.K. Rowling", year)
        self.house = house

hp_book = HarryPotterBook("Harry Potter and the Goblet of Fire", 2000, "Gryffindor")

# Showing book info
print("Book Info")
print("Title:", hp_book.title)
print("Author:", hp_book.author)
print("Year:", hp_book.year)
print(hp_book.title + " is full of magic from " + hp_book.house + " house!")
