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
    }
]

with open('emma.json', "w") as file:
    json.dump(book_inventory, file, indent = 4)
    print("File saved succesfully")
    
def file_opener(filename):
    with open(filename, "r") as file:
        content = json.load(file)
        print(content)
        
file_opener('emma.json')