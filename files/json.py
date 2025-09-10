import json
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

book = json.loads(book_inventory)
print(book)