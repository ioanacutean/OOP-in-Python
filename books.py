from datetime import datetime

class Book:

    def __init__(self, title, author, publication_year, genre, price):
        self.title = title
        self.author = author
        self.publication_year = publication_year
        self.genre = genre
        self.price = price

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        if len(value) == 0:
            print("The title cannot be empty")
        else:
            self._title = value

    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, value):
        if len(value) == 0:
            print("The author cannot be empty")
        else:
            self._author = value

    @property
    def publication_year(self):
        return self._publication_year

    @publication_year.setter
    def publication_year(self, value):
        current_year = datetime.now().year
        if type(value) != int or value < 0 or value > current_year:
            print(f"The publication year must be a positive integer less than or equal to {current_year}.")
        else:
            self._publication_year = value

    @property
    def genre(self):
        return self._genre

    @genre.setter
    def genre(self, value):
        if len(value) == 0:
            print("The genre cannot be empty")
        else:
            self._genre = value

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if value < 0:
            print("The price cannot be negative")
        else:
            self._price = value

    def __str__(self):
        return f"The {self.genre} book {self.title} by {self.author} published in {self.publication_year} costs {self.price} lei."
