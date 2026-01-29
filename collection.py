from books import Book

class Collection():
    def __init__(self, books_collection = []):
        self.books_collection = books_collection

    def add_book(self, new_book):
       if len(self.books_collection) == 10:
           print('The shelf is full.')
       else:
            self.books_collection.append(new_book)

    def search_book_by_title(self, title):
        print()
        print(f"The books with the title {title} are:")
        for book in self.books_collection:
            if title.lower() == book.title.lower():
                print(book)

    def search_book_by_genre(self, genre):
        print()
        print(f"The books with the genre {genre} are:")
        for book in self.books_collection:
            if genre.lower() == book.genre.lower():
                print(book)

    def search_book_by_author(self, author):
        print()
        print(f"The books with the author {author} are:")
        for book in self.books_collection:
            if author.lower() == book.author.lower():
                print(book)

    def update_book_title(self, index, title):
        if index >= len(self.books_collection):
            print("Index out of bounds.")
        else:
            self.books_collection[index].title = title

    def update_book_price(self, index, price):
        if index >= len(self.books_collection):
            print("Index out of bounds.")
        else:
            self.books_collection[index].price = price

    def display_collection(self):
        print()
        print("The books collection contains: ")
        for book in self.books_collection:
            print(book)


book1 = Book("Crima din Orient Express", "Agatha Christie", 1934, "Crime", 35)
book2 = Book("Factfullness", "Hans Rosling", 2018, "Self-help", 50)
book3 = Book("factfullness", "Hans Rosling", 2021, "Self-help", 60)
book4 = Book("Libraria din Teheran", "Marjan Kamali", 2022, "Beletristica", 45)

collection = Collection()
collection.add_book(book1)
collection.add_book(book2)
collection.add_book(book3)
collection.add_book(book4)
collection.display_collection()

collection.search_book_by_author("Hans Rosling")
collection.search_book_by_title("Factfullness")
collection.search_book_by_genre("Beletristica")

collection.update_book_title(2, "Ana")
collection.update_book_price(2, 30)
collection.update_book_price(5, 40)
collection.display_collection()
