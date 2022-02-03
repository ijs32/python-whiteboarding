# Given a list of books provided in this format:

books = [
    {"title": "The Lord of the Rings", "author": "J. R. R. Tolkien", "year": 1954},
    {"title": "To Kill a Mockingbird", "author": "Harper Lee", "year": 1960},
    {"title": "1984", "author": "George Orwell", "year": 1949},
    {"title": "Go Set a Watchman", "author": "Harper Lee", "year": 2015},
    {"title": "The Hobbit", "author": "J. R. R. Tolkien", "year": 1937},
    {"title": "The Great Gatsby", "author": "F. Scott Fitzgerald", "year": 1925},
    {"title": "The Two Towers", "author": "J. R. R. Tolkien", "year": 1954}
]

# return the data in this new author-centric format:

# { "J. R. R. Tolkien" => [
# {title: "The Lord of the Rings", year: 1954 },
# {title: "The Hobbit", year: 1937 },
# {title: "The Two Towers", year: 1954 }
# ],
# "Harper Lee" => [
# {title: "To Kill a Mockingbird", year: 1960 },
# {title: "Go Set a Watchman", year: 2015 }
# ],
# "George Orwell" => [
# {title: "1984", year: 1949 }
# ],
# "F. Scott Fitzgerald" => [
# {title: "The Great Gatsby", year: 1925 }
# ]
# }


def book_organizer(books):
    authors = {}
    for book in books:
        authors[book["author"]] = [] # creates an array for each author
    for book in books:
        if book["author"] in authors: # if author matches hash author do following
            temp = {"title": book["title"], "year": book["year"]}
            authors[book["author"]].append(temp)
    return authors


print(book_organizer(books))
