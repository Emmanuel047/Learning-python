#We want a function that:

#Takes the inventory (list of book dicts) as a parameter

#Takes the filename you want to save as a parameter

#Saves the inventory to that file as JSON

import json

print("Welcome to the book inventory system")
def new_book(inventory, filename):
    try:
        with open(filename, "w") as file:
            json.dump(inventory, file, indent=4)
            print(f"Inventory successfully saved to {filename}")
    except Exception as e:
        print("Error saving file")
    else:
        print("Success")
        
def file_opener(filename):
    with open(filename, "r") as file:
        content = file.read()
        print(content)
        
        
book_inv = [
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
filename = input("Enter the filename of the inventory you want to add: ")
new_book(book_inv, filename)
file_opener(filename)