#Learning About Dictionaries in Python
#Mini-project: Contact list manager using dictionaries and lists.
student = {
    "name": "Emma",
    "age": "24",
    "location": "Kenya",
}

book = {
    "Title": "1984",
    "Author": "George Orwell",
    "Year Published": "1949",
    "Genres": ["Dystopian", "Political Fiction", "Science Fiction"]
}
book["Publisher"] = "Secker & Warburg"
book["Year Published"] = 1951
publisher = book.pop("Publisher")
print("Removed Publisher:", publisher)
del book["Genres"]

for key, value in book.items():
    print(f"Key: {key}: Value: {value}")

#print(student["name"], student["age"], student["location"])

