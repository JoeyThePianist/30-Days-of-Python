# For this project the application needs to have the following functionality:
# Users should be able to add a book to their reading list by providing a book
# title, an author's name, and a year of publication.
# The program should store information about all of these books in a Python list.
# Users should be able to display all the books in their reading list, and these
# books should be printed out in a user-friendly format.
# Users should be able to select these options from a text menu, and they should
# be able to perform multiple operations without restarting the program. You can
# see an example of a working menu in the post on while loops (day 8).
reading_list = []
title = None
author = None
year_published = None

while True:
    book_buddy = input("Hi again! Would you like to 'ADD' a book to your reading list or 'VIEW' what you currently have in your list? To quit, enter 'QUIT': ")

    if book_buddy == "ADD":
        print("You chose to 'ADD' a new book!")
        title = input("What is the title of your new book? ")
        author = input("Who is the author of your new book? ")
        year_published = input("What year was this book published? ")
        book_to_add = (title, author, year_published)
        reading_list.append(book_to_add)
        print(f"Awesome! {title} ({year_published}) by {author} has been added to your reading list!")
        print("Book Buddy loops so that you can view your list! Going back to the beginning...")
    elif book_buddy == "VIEW":
        print("Looks like you want to 'VIEW' your book list!")
        for book in reading_list:
            print(f"{book[0]} ({book[2]}), by {book[1]}")
        print("Book Buddy loops so that you can add to your list! Going back to the beginning...")
    elif book_buddy == "QUIT":
        print("You chose to 'QUIT' and so we shall! Quitting Book Buddy...")
        break
    else:
        print("You selected an invalid option.")