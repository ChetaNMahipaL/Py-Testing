"""
    This module is to test attached question
"""
import pytest
import sys
import pickle
sys.path.append("../Code/")

from dataop import cal_average

try:
    with open('../Dataset/students_data.pkl', 'rb') as file:
        loaded_students = pickle.load(file)
except pickle.PickleError as e:
    print("An error occurred while saving student data:", e)

def test_mod_1():
    """
        Testcase-1 to check normal ans
    """
    assert cal_average(loaded_students[0]) == {'John Kirkman': 91.33, 'Emily Rhodes': 92.33, 'Aaron Shore': 93.67, 'Ray Atwood': 84.33, 'Penny Wells': 78.67, 'Mark Richmond': 79.0, 'Seth Wright': 91.33}

def test_mod_2():
    """
        Testcase-1 to check normal ans
    """
    assert cal_average(loaded_students[1]) == {'John Kirkman': 91.33, 'Emily Rhodes': 89.67, 'Aaron Shore': 90.33, 'Ray Atwood': 84.33, 'Penny Wells': 78.67, 'Mark Richmond': 79.0, 'Seth Wright': 91.33}

def test_mod_3():
    """
        Testcase-3 to check with negative  score
    """
    assert cal_average(loaded_students[2]) == "Incorrect score detected."

def test_mod_4():
    """
        Testcase-4 to check with score beyond max score
    """
    assert cal_average(loaded_students[3]) == "Incorrect score detected."

def test_mod_5():
    """
        Testcase-5 to check with score entry  zero
    """
    assert cal_average(loaded_students[4]) == {'John Kirkman': 91.33, 'Emily Rhodes': 89.0, 'Aaron Shore': 90.33, 'Ray Atwood': 84.33, 'Penny Wells': 78.67, 'Mark Richmond': 79.0, 'Seth Wright': 61.0}

def test_mod_6():
    """
        Testcase-6 to check with missing score for subject
    """
    assert cal_average(loaded_students[5]) == "Incorrect number of scores detected."