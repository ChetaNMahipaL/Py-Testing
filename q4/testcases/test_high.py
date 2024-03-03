"""
    This module is to test attached question
"""
import pytest
import sys
import pickle
sys.path.append("../Code/")

from dataop import find_highest_scorer

try:
    with open('../Dataset/students_data.pkl', 'rb') as file:
        loaded_students = pickle.load(file)
except pickle.PickleError as e:
    print("An error occurred while saving student data:", e)

def test_mod_1():
    """
        Testcase-1 to check normal ans
    """
    assert find_highest_scorer(loaded_students[0]) == ("Aaron Shore", ['Aaron Shore', 'Ray Atwood', 'Emily Rhodes'])

def test_mod_2():
    """
        Testcase-1 to check lexo graphic order for tie breaking for avg
    """
    assert find_highest_scorer(loaded_students[1]) == ("John Kirkman", ['John Kirkman', 'Emily Rhodes', 'Emily Rhodes'])

def test_mod_3():
    """
        Testcase-3 to check with negative  score
    """
    assert find_highest_scorer(loaded_students[2]) == (None, None)

def test_mod_4():
    """
        Testcase-4 to check with score beyond max score
    """
    assert find_highest_scorer(loaded_students[3]) == (None, None)

def test_mod_5():
    """
        Testcase-1 to check lexo graphic order for tie breaking for highest subject scorer
    """
    assert find_highest_scorer(loaded_students[4]) == ("John Kirkman", ['John Kirkman', 'Ray Atwood', 'Emily Rhodes'])

def test_mod_6():
    """
        Testcase-6 to check with missing score for subject
    """
    assert find_highest_scorer(loaded_students[5]) == (None, None)