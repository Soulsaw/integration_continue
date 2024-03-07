import unittest
from app import *

class TestAddition(unittest.TestCase):
    def test_valid_addition(self):
        self.assertTrue(additionner(10,30)==40)
        self.assertTrue(additionner(-10,10)==0)

    def test_invalid_password(self):
        self.assertFalse(additionner(0,1)==0)
        self.assertFalse(additionner(0,-5)==5)
        self.assertFalse(additionner(4,5)==4)
        
    def test_multiplication(self):
        self.assertEqual(25, multiplication(5, 5))
        self.assertEqual(25, multiplication(-5, -5))
        self.assertFalse(multiplication(-5, 5)==350)

if __name__ == '__main__':
    unittest.main()