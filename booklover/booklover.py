import pandas as pd
import numpy as np

class BookLover:
    '''init functions'''
    def __init__(self, name, email, fav_genre, num_books = 0, book_list = pd.DataFrame({'book_name':[], 'book_rating':[]})):
        self.name = name 
        self.email = email 
        self.fav_genre = fav_genre 
        self.num_books = num_books 
        self.book_list = book_list
    
    def add_book(self, book_name, book_rating):
        "Adds a book to the list if it is not already in there"
        if book_name in list(self.book_list['book_name']):
            print("The book already exists in this list.")
        else:
            new_book = pd.DataFrame({
            'book_name': [book_name], 
            'book_rating': [book_rating]
            })
            self.book_list = pd.concat([self.book_list, new_book], ignore_index=True)
            self.num_books += 1
            
    def has_read(self, book_name):
        "Returns 'True' if the person has ready the book"
        if book_name in list(self.book_list['book_name']):
            return True
        else:
            return False
        
    def num_books_read(self):
        "Returns the number of books the person has read"
        return self.num_books
    
    def fav_books(self):
        "Returns a dataframe of all books with the "
        return self.book_list[self.book_list['book_rating'] > 3] 
    
