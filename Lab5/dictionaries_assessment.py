# This program stores information about books (title, author, year, genre) in dictionaries
# Creates a library (list of book dictionaries)
# Allows searching books by different criteria
# Demonstrates all major dictionary operations
# Shows nested data structures

# Library is a list of dictionaries
library = [
    {
        "title": "The Hobbit",
        "author": "J.R.R. Tolkien",
        "year": 1937,
        "genre": "Fantasy"
    },
    {
        "title": "The Hunger Games",
        "author": "Suzanne Collins",
        "year": 2008,
        "genre": "Dystopian"
    },
    {
        "title": "Ender's Game",
        "author": "Orson Scott Card",
        "year": 1985,
        "genre": "Science fiction"
    }
]

# Function to add a book
def add_book(title, author, year, genre):
    book = {
        "title": title,
        "author": author,
        "year": year,
        "genre": genre
    }
    library.append(book)
    return book

# Function to search by title
def search_by_title(keyword):
    matches = []
    for book in library:
        if keyword.lower() in book["title"].lower():
            matches.append(book)
    return matches

# Function to search by author
def search_by_author(author_name):
    matches = []
    for book in library:
        if author_name.lower() in book["author"].lower():
            matches.append(book)
    return matches

# Function to search by genre
def search_by_genre(genre):
    matches = []
    for book in library:
        if genre.lower() in book["genre"].lower():
            matches.append(book)
    return matches

# Display all books
def display_library():
    for book in library:
        print(book)

# Example usage
print("Library:")
display_library()

print("\nSearch by title: 'the'")
print(search_by_title("the"))

print("\nSearch by author: 'collins'")
print(search_by_author("collins"))

print("\nSearch by genre: 'fantasy'")
print(search_by_genre("fantasy"))

print("\nAdd a new book")
new_book = add_book("The Help", "Kathryn Stockett", 2009, "Historical fiction")
print(new_book)
