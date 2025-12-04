import json
from pathlib import Path
from .book import Book

class LibraryInventory:
    def __init__(self):
        self.books = []
        self.file_path = Path("library_data.json")
        self.load_data()

    def add_book(self, book):
        self.books.append(book)
        self.save_data()

    def search_by_title(self, title):
        return [book for book in self.books if title.lower() in book.title.lower()]

    def search_by_isbn(self, isbn):
        for book in self.books:
            if book.isbn == isbn:
                return book
        return None

    def display_all(self):
        if not self.books:
            print("\nNo books found!")
        for book in self.books:
            print(book)

    def save_data(self):
        data = [book.to_dict() for book in self.books]
        with open(self.file_path, "w") as f:
            json.dump(data, f, indent=4)

    def load_data(self):
        if not self.file_path.exists():
            return
        try:
            with open(self.file_path, "r") as f:
                data = json.load(f)
                for item in data:
                    self.books.append(Book(item["title"], item["author"], item["isbn"], item["status"]))
        except:
            print("Error loading file, starting fresh.")
