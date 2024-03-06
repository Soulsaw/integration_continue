import unittest
import app

class TestAddition(unittest.TestCase):
    def test_valid_addition(self):
        self.assertTrue(app.Additionner(10,30)==40)
        self.assertTrue(app.Additionner(-10,10)==0)

    def test_invalid_password(self):
        self.assertFalse(app.Additionner(0,1)==0)
        self.assertFalse(app.Additionner(0,-5)==5)
        self.assertFalse(app.Additionner(4,5)==4)

if __name__ == '__main__':
    unittest.main()