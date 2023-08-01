from booklover import booklover

object1 = booklover.BookLover('Will', 'wjs3jc@virginia.edu', 'Fiction')
object1.add_book('Magic Tree House', 5)
object1.add_book('Winnie the Poo', 5)
object1.add_book('Percy Jackson', 5)
print("Number of books read", object1.num_books_read())