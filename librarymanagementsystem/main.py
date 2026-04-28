import datetime

FILENAME = "library_records.txt"

def add_book(book_name):
    with open(FILENAME, "a") as file:
        file.write(f"BOOK: {book_name}\n")
    print(f'Book "{book_name}" added successfully!')

def show_books():
    try:
        with open(FILENAME, "r") as file:
            books = [line.strip() for line in file if line.startswith("BOOK:")]
            if books:
                print("\n--- Books in Library ---")
                for idx, book in enumerate(books, start=1):
                    print(f"{idx}. {book.replace('BOOK: ', '')}")
            else:
                print("No books available.")
    except FileNotFoundError:
        print("No records found.")

def issue_book(book_name):
    with open(FILENAME, "a") as file:
        file.write(f"ISSUED: {book_name} - {datetime.datetime.now()}\n")
    print(f'Book "{book_name}" issued successfully!')

def return_book(book_name):
    with open(FILENAME, "a") as file:
        file.write(f"RETURNED: {book_name} - {datetime.datetime.now()}\n")
    print(f'Book "{book_name}" returned successfully!')

def search_book(book_name):
    try:
        with open(FILENAME, "r") as file:
            records = file.readlines()
            found = [record.strip() for record in records if book_name in record]
            if found:
                print("\n--- Search Results ---")
                for record in found:
                    print(record)
            else:
                print(f'No records found for "{book_name}".')
    except FileNotFoundError:
        print("No records found.")

def menu():
    print("\n--- Library Management System ---")
    print("1. Add Book")
    print("2. Show Books")
    print("3. Issue Book")
    print("4. Return Book")
    print("5. Search Book")
    print("6. Exit")

if __name__ == "__main__":
    while True:   # Infinite loop for menu-driven system
        menu()
        choice = input("Enter choice: ")
        if choice == "1":
            name = input("Enter book name: ")
            add_book(name)
        elif choice == "2":
            show_books()
        elif choice == "3":
            name = input("Enter book name to issue: ")
            issue_book(name)
        elif choice == "4":
            name = input("Enter book name to return: ")
            return_book(name)
        elif choice == "5":
            name = input("Enter book name to search: ")
            search_book(name)
        elif choice == "6":
            print("Exiting system... Goodbye!")
            break
        else:
            print("Invalid choice, try again.")
