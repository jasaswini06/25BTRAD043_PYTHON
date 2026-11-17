class Library:

    def __init__(self, book_list):
        self.books = {book: True for book in book_list}

    def display_books(self):
        print("\nAvailable Books:")
        for book, available in self.books.items():
            status = "Available" if available else "Issued"
            print(f"- {book} [{status}]")

    def issue_book(self, book):
        if self.books.get(book) is True:
            self.books[book] = False
            print(f"Success: '{book}' has been issued.")
        elif self.books.get(book) is False:
            print(f"Sorry, '{book}' is already issued to someone else.")
        else:
            print("Book not found in library.")

    def return_book(self, book):
        if self.books.get(book) is False:
            self.books[book] = True
            print(f"Success: '{book}' has been returned.")
        elif self.books.get(book) is True:
            print(f"'{book}' was not issued.")
        else:
            print("Book does not belong to this library.")


lib = Library(["Python Basics", "Data Structures", "AI Fundamentals"])

while True:
    print("\n1. View Books  2. Issue Book  3. Return Book  4. Exit")
    choice = input("Enter choice: ").strip()

    if choice == "1":
        lib.display_books()
    elif choice == "2":
        lib.issue_book(input("Enter book name to issue: ").strip())
    elif choice == "3":
        lib.return_book(input("Enter book name to return: ").strip())
    elif choice == "4":
        break
    else:
        print("Invalid choice.")