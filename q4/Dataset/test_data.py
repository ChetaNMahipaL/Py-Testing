'''
    This module contains the dataset of students to test
'''
import pickle
import os

students = [
    {'name': 'John Kirkman', 'scores': [95, 85, 94]},
    {'name': 'Emily Rhodes', 'scores': [90, 87, 100]},
    {'name': 'Aaron Shore', 'scores': [95, 88, 98]},
    {'name': 'Ray Atwood', 'scores': [74, 89, 90]},
    {'name': 'Penny Wells', 'scores': [79, 75, 82]},
    {'name': 'Mark Richmond', 'scores': [90, 65, 82]},
    {'name': 'Seth Wright', 'scores': [94, 89, 91]}
]

try:
    # Setting path of dataset file
    script_directory = os.path.dirname(os.path.abspath(__file__))
    pickle_file_path = os.path.join(script_directory, 'students_data.pkl')
    with open(pickle_file_path, 'wb') as file:
        pickle.dump(students, file)
except Exception as e:
    print("An error occurred while saving student data:", e)
