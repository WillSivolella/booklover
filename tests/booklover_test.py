import unittest
from booklover import BookLover

class BookLoverTestSuite(unittest.TestCase):
    
    def test_1_add_book(self): 
        # add a book and test if it is in `book_list`.
        test_object1 = BookLover("Han Solo", "hsolo@millenniumfalcon.com", "scifi")
        test_object1.add_book("War of the Worlds" , 4)
        print(test_object1.name)
        print(test_object1.book_list)
        self.assertTrue("War of the Worlds" in list(test_object1.book_list['book_name']))
        
    def test_2_add_book(self):
        # add the same book twice. Test if it's in `book_list` only once.
        test_object2 = BookLover("Han Solo", "hsolo@millenniumfalcon.com", "scifi")
        test_object2.add_book("War of the Worlds" , 4)
        test_object2.add_book("War of the Worlds" , 4)
        print(test_object2.name)
        print(test_object2.book_list)
        
        expected = 1
        self.assertEqual(len(test_object2.book_list['book_name']), expected)
        
    def test_3_has_read(self): 
        # pass a book in the list and test if the answer is `True`.
        test_object3 = BookLover("Han Solo", "hsolo@millenniumfalcon.com", "scifi")
        test_object3.add_book("War of the Worlds" , 4)
        print(test_object3.name)
        print(test_object3.book_list)
        self.assertTrue(test_object3.has_read("War of the Worlds"))
        
        
    def test_4_has_read(self): 
        # pass a book NOT in the list and use `assert False` to test the answer is `True`
        test_object4 = BookLover("Han Solo", "hsolo@millenniumfalcon.com", "scifi")
        test_object4.add_book("War of the Worlds" , 4)
        print(test_object4.name)
        print(test_object4.book_list)
        self.assertFalse(test_object4.has_read("The Bible"))
        
    def test_5_num_books_read(self): 
        # add some books to the list, and test num_books matches expected.
        test_object5 = BookLover("Han Solo", "hsolo@millenniumfalcon.com", "scifi")
        test_object5.add_book("War of the Worlds" , 4)
        test_object5.add_book("The Bible" , 4)
        test_object5.add_book("Magic Tree House" , 4)
        test_object5.add_book("Harry Potter" , 4)
        print(test_object5.name)
        print(test_object5.book_list)
        expected = 4
        self.assertEqual(test_object5.num_books_read(), expected) 

    def test_6_fav_books(self):
        # add some books with ratings to the list, making sure some of them have rating > 3. 
        # Your test should check that the returned books have rating  > 3
        test_object6 = BookLover("Han Solo", "hsolo@millenniumfalcon.com", "scifi")
        test_object6.add_book("War of the Worlds" , 4)
        test_object6.add_book("The Bible" , 3)
        test_object6.add_book("Magic Tree House" , 5)
        test_object6.add_book("Harry Potter" , 2)
        print(test_object6.name)
        print(test_object6.fav_books())
        expected = 2
        self.assertEqual(len(test_object6.fav_books()), expected)
        
        
                
if __name__ == '__main__':
    
    unittest.main(verbosity=3)