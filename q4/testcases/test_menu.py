"""
    This module is to test attached question
"""
import pytest
import sys
import pickle
sys.path.append("../Code/")

from dataop import main

def test_main_1(monkeypatch):
    '''
        Testcase-1: Checks normal working
    '''
    inputs = ["3", "3", "John", "90", "80", "70", "Emily", "85", "95", "75", "Aaron", "92", "88", "90"]
    outputs = [{'John': 80.0, 'Emily': 85.0, 'Aaron': 90.0},
               "Aaron",
               ['Aaron', 'Emily', 'Aaron']]

    def mock_input(prompt):
        print(prompt)
        return inputs.pop(0)

    monkeypatch.setattr('builtins.input', mock_input)

    main_output = main()

    for expected_output in outputs:
        assert expected_output in main_output

def test_main_2(monkeypatch):
    '''
        Testcase-2: Checks invalid number of students
    '''
    inputs = ["0", "-1", "John", "90", "80", "70", "Emily", "85", "95", "75", "Aaron", "92", "88", "90"]
    outputs = "Please enter valid integer values for number of students and subjects."
    def mock_input(prompt):
        print(prompt)
        return inputs.pop(0)

    monkeypatch.setattr('builtins.input', mock_input)

    main_output = main()

    for expected_output in outputs:
        assert expected_output in main_output

def test_main_3(monkeypatch):
    '''
        Testcase-3: Checks invalid number of subjects
    '''
    inputs = ["3", "-1", "John", "90", "80", "70", "Emily", "85", "95", "75", "Aaron", "92", "88", "90"]
    outputs = "Please enter valid integer values for number of students and subjects."
    def mock_input(prompt):
        print(prompt)
        return inputs.pop(0)

    monkeypatch.setattr('builtins.input', mock_input)

    main_output = main()

    for expected_output in outputs:
        assert expected_output in main_output

def test_main_4(monkeypatch):
    '''
        Testcase-4: Check for negative scores
    '''
    inputs = ["3", "3", "John", "-90", "80", "70", "Emily", "85", "95", "75", "Aaron", "92", "88", "90"]
    outputs = "Incorrect Score Entered"
    def mock_input(prompt):
        print(prompt)
        return inputs.pop(0)

    monkeypatch.setattr('builtins.input', mock_input)

    main_output = main()

    for expected_output in outputs:
        assert expected_output in main_output

def test_main_5(monkeypatch):
    '''
        Testcase-5: Check for random string in place of score
    '''
    inputs = ["3", "3", "John", "zfhd", "80", "70", "Emily", "85", "95", "75", "Aaron", "92", "88", "90"]
    outputs = "Please enter valid integer values for scores"
    def mock_input(prompt):
        print(prompt)
        return inputs.pop(0)

    monkeypatch.setattr('builtins.input', mock_input)

    main_output = main()

    for expected_output in outputs:
        assert expected_output in main_output

if __name__ == "__main__":
    pytest.main([__file__])