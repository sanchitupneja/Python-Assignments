from library_manager.inventory import LibraryInventory
from library_manager.book import Book

def main():
    inventory = LibraryInventory()

    while True:
        print("\n===== Library Menu =====")
        print("1. Add Book")
        print("2. Issue Book")
        print("3. Return Book")
        print("4. View All Books")
        print("5. Search Book")
        print("6. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            title = input("Enter title: ")
            author = input("Enter author: ")
            isbn = input("Enter ISBN: ")
            book = Book(title, author, isbn)
            inventory.add_book(book)
            print("Book added successfully!")

        elif choice == "2":
            isbn = input("Enter ISBN to issue: ")
            book = inventory.search_by_isbn(isbn)
            if book and book.issue():
                inventory.save_data()
                print("Book issued!")
            else:
                print("Book not available.")

        elif choice == "3":
            isbn = input("Enter ISBN to return: ")
            book = inventory.search_by_isbn(isbn)
            if book:
                book.return_book()
                inventory.save_data()
                print("Book returned!")
            else:
                print("Book not found.")

        elif choice == "4":
            inventory.display_all()

        elif choice == "5":
            name = input("Enter title to search: ")
            results = inventory.search_by_title(name)
            if results:
                for b in results:
                    print(b)
            else:
                print("No book found.")

        elif choice == "6":
            print("Exiting...")
            break

        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
