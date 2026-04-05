import unittest
from lab1 import sorted_squares

class TestLab1(unittest.TestCase):
    
    def test_basic_cases(self):
        self.assertEqual(sorted_squares([-4, -2, 0, 1, 3]), [0, 1, 4, 9, 16])
        self.assertEqual(sorted_squares([1, 2, 3, 4, 5]), [1, 4, 9, 16, 25])

    def test_single_element(self):

        self.assertEqual(sorted_squares([-5]), [25])

    def test_zeros(self):
        self.assertEqual(sorted_squares([0, 0]), [0, 0])

if __name__ == '__main__':
    unittest.main()