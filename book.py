#Book Inventory Management System
import os

book_inventory = [
    {
    "Title": "1984",
    "Author": "George Orwell",
    "Year Published": "1949",
    "Genres": ["Dystopian", "Political Fiction", "Science Fiction"]
    },
    {
        "Title": "To Kill a MockingBird",
        "Author": "Harper Lee",
        "Year Published": "1910",
        "Genres": ["Southern Gothic", ]
    },
    {
        "Title": "The Great Gatsby",
        "Author": "F. Scott Fitzgerald",
        "Year Published": "1925",
        "Genres": ["Tragedy", "Realism"]
    },
    {
        "Title": "Fahrenheit 451",
        "Author": "Ray Bradbury",
        "Year Published": 1953,
        "Genres": ["Dystopian", "Science Fiction"]
    }
]

print("Hi welcome to the Book Inventory Management System")
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')
    
clear_screen()
print("Screen cleared")
while True:
    action = input("Would you like to \n"\
    "1.Add \n" \
    "2.Remove.\n" \
    "3.Update\n" \
    "4.View\n"
    "5.Exit\n").strip()
    
    if action not in {"1", "2", "3", "4", "5"}:
        print("Enter a valid choice")
        continue

    if action == "1":
        title = input("Enter book title: ")
        author = input("Enter book author: ")
        year_published = input("Enter year of publication: ")
        genres = input("Enter book genres comma separated: ").split()

        new_book = {
            "Title": title,
            "Author": author,
            "Year Published": year_published,
            "Genres": genres
        }
        book_inventory.append(new_book)
        print(f"the book {title} has been added to the inventory.")

    elif action == "2":
        title = input("Enter the title of the book to remove: ")
        book_found = False
        for book in book_inventory:
            if book["Title"].lower() == title.lower():
                book_inventory.remove(book)
                book_found = True
                print(f"The book {title} has been removed from the inventory.")
                break
        if not book_found:
            print("The book doesn't exist")
    elif action == "3":
        choice = input("What you the book you want to update: ").lower()
        book_found = False
        for book in book_inventory:
            if book["Title"].lower() == choice.lower():
                new_title = input("Enter the new title (leave blank to keep current): ")
                new_author = input("Enter the new author (leave blank for current): ")
                new_year = input("Enter the new year published (leave blank for current): ")
                new_genre = input("Enter the new genres comma separated (leave blank for current): ").split()
                if new_title:
                    book["Title"] = new_title
                if new_author:
                    book["Title"] = new_author
                if new_year:
                    try:
                        book["Year published"] = int(new_year)
                    except ValueError:
                        print("Invalid year format")
                if new_genre:
                    book["Genres"] = new_genre
                book_found = True
                print(f"The book {choice} has been updated.")
                break
        if not book_found:
            print("The book doesn't exist")
    elif action == "4":
        print("Current book inventory: ")
        for book in book_inventory:
            for key, value in book.items():
                print(f"{key}: {value}")
            print("\n")
    elif action == "5":
        print("Exiting program.")
        break
    elif action == "5":
        print("Exiting Program")
        break
    else:
        print("Invalid action. Please choose 1, 2, 3, or 4.")