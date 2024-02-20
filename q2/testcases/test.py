"""
    This module is to inlcude tescases for q2
"""
import unittest
import sys
sys.path.append("../Code/")
from kaprekarroutine import main

class TestRoutine(unittest.TestCase):
    """
        This class includes all testcases
    """
    def test_case_1(self):
        """
        This test case checks normal 4 digit with all unique
        """
        result = main(4136)
        self.assertEqual(result, 6174)
    def test_case_2(self):
        """
        This test case checks normal 4 digit with 3 unique digits
        """
        result = main(6136)
        self.assertEqual(result, 6174)
    def test_case_3(self):
        """
        This test case checks normal 4 digit with 2 unique digits
        """
        result = main(6336)
        self.assertEqual(result, 6174)
    def test_case_4(self):
        """
        This test case checks normal 4 digit with 1 unique digits
        """
        result = main(6666)
        self.assertEqual(result, "Enter a valid 4-digit number")
    def test_case_5(self):
        """
        This test case checks normal number with leading zeros
        """
        result = main(98)
        self.assertEqual(result, 6174)
    def test_case_6(self):
        """
        This test case checks normal number with first difference a three digit number
        """
        result = main(5444)
        self.assertEqual(result, 6174)
    def test_case_7(self):
        """
        This test case checks normal number is a three digit number
        """
        result = main(444)
        self.assertEqual(result, 6174)
    def test_case_8(self):
        """
        This test case checks for neagative number
        """
        result = main(-6689)
        self.assertEqual(result, "Enter a valid 4-digit number")
    def test_case_9(self):
        """
        This test case checks for string input
        """
        result = main("6689")
        self.assertEqual(result, "Enter a valid 4-digit number")
    def test_case_10(self):
        """
        This test case checks number on reversing forms three digit number
        """
        result = main(4440)
        self.assertEqual(result, 6174)
    def test_case_11(self):
        """
        This test case checks number on reversing forms two digit number
        """
        result = main(4400)
        self.assertEqual(result, 6174)
    def test_case_12(self):
        """
        This test case checks number on reversing forms one digit number
        """
        result = main(4000)
        self.assertEqual(result, 6174)
    def test_case_13(self):
        """
        This test case checks for string input
        """
        result = main("fsdghsdgh")
        self.assertEqual(result, "Enter a valid 4-digit number")

if __name__ == '__main__':
    unittest.main()
