# Week 1.7, Session 1: Task 2 - unit test for process_data() 

# Write test functions for the values you have chosen in the equivalence classes
# for testing the functions

# Hint: you should test for empty list, list with a single value, list with multiple values
# and for positive and negative integers


from process_data import process_data
import unittest

def test_empty_list():
    assert process_data( [] ) == "None"
    
def test_one_int_list():
    assert process_data( [9] ) == "9"

def test_multiple_int_list():
    assert process_data( [1,2,-1,-3,2] ) == "1"

class test_list_methods(unittest.TestCase):
    def test_empty_list(self):
        self.assertTrue(process_data([])==None)

    def test_one_int_list(self):
        self.assertEqual(process_data([9]),9)

    def test_multiple_int_list(self):
        self.assertEqual(process_data([1,2,-1,-3,2]),1)

if __name__ == '__main__':
    unittest.main()
    


    
    
