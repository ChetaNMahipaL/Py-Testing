"""
    This module is to test attached question
"""
import pytest
import sys
sys.path.append("../Code/")

from palindrome import main

def testing_module_1():
    """
        Testcase-1 to check output with palindrome year
    """
    assert main("2020") == "02-02-2020"

def testing_module_2():
    """
        Testcase-2 to check with non-palindrome year
    """
    assert main("2044") == "No Palindrome days available in the given year"

def testing_module_3():
    """
        Testcase-3 to check with negative year
    """
    assert main("-2020") == "Enter a valid year"

def testing_module_4():
    """
        Testcase-4 to check with  year as 0
    """
    assert main("0") == "Enter a valid year"

def testing_module_5():
    """
        Testcase-5 to check year without leading zero
    """
    assert main("111") == "11-10-0111"

def testing_module_6():
    """
        Testcase-6 to check with  year given a random string
    """
    assert main("clfg") == "Enter a valid year"

def testing_module_7():
    """
        Testcase-7 to check year with leading zero
    """
    assert main("0111") == "11-10-0111"

def testing_module_8():
    """
        Testcase-8 to check with float
    """
    assert main("0.33") == "Enter a valid year"
