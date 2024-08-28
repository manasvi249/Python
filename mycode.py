library_inventory={}
def add_book(isbn, title, author, genre, availability):
    if isbn in library_inventory:
        print(f"Book with ISBN {isbn} already exists.")
        return
    
    library_inventory[isbn] = {
        'title': title,
        'author': author,
        'genre': genre,
        'availability': availability
    }
    print(f"Book '{title}' added successfully.")

def update_book_details(isbn, title=None, author=None, genre=None, availability=None):
    if isbn not in library_inventory:
        print(f"Book with ISBN {isbn} does not exist.")
        return
    
    if title is not None:
        library_inventory[isbn]['title'] = title
    if author is not None:
        library_inventory[isbn]['author'] = author
    if genre is not None:
        library_inventory[isbn]['genre'] = genre
    if availability is not None:
        library_inventory[isbn]['availability'] = availability
    
    print(f"Book with ISBN {isbn} updated successfully.")

def search_by_isbn(isbn):
    
    book = library_inventory.get(isbn, None)
    if book:
        print(f"Book found: ISBN {isbn}")
        print(f"Title: {book['title']}")
        print(f"Author: {book['author']}")
        print(f"Genre: {book['genre']}")
        print(f"Availability: {'Available' if book['availability'] else 'Not Available'}")
    else:
        print(f"Book with ISBN {isbn} not found.")


def generate_genre_report():
    genre_report = {}
    for book in library_inventory.values():
        if book['availability']:
            genre = book['genre']
            if genre not in genre_report:
                genre_report[genre] = []
            genre_report[genre].append(book['title'])
    
    print("Available Books by Genre:")
    for genre, titles in genre_report.items():
        print(f"{genre}:")
        for title in titles:
            print(f"  - {title}")

add_book("121-02","Mystery","James","fiction","True")
add_book("122-03","My School Days","Anne Frank","real","False")

searchisbn=input("Enter isbn to search ")
search_by_isbn(searchisbn)

isbn=input("Enter isbn to add ")
title=input("Enter title ")
author=input("Enter author ")
genre=input("Enter genre ")
availability=input("Enter availability ")
add_book(isbn,title,author,genre,availability)
searchisbn1=input("Enter isbn to search to update ")
update_book_details(searchisbn1,availability=True)
search_by_isbn(searchisbn)
                    

generate_genre_report()






    
