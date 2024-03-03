'''
    This script makes a dataset with student details and marks randomly
'''
import random
import pickle
import os

def generate_names(num_stu):
    '''
        This function generate names of students
    '''
    names = []
    for _ in range(num_stu):
        name = ''.join(random.choices('abcdefghijklmnopqrstuvwxyz', k=random.randint(5, 10)))
        names.append(name.capitalize())
    return names

def generate_scores(num_sub, num_student):
    '''
        This function generates marks of students
    '''
    scores = []
    for _ in range(num_student):
        student_scores = [random.randint(60, 100) for _ in range(num_sub)]
        scores.append(student_scores)
    return scores

def create_students(num_st, num_subject):
    '''
        This function generates data structure of dictionary
    '''
    names = generate_names(num_st)
    scores = generate_scores(num_subject, num_st)
    students = [{'name': name, 'scores': score} for name, score in zip(names, scores)]
    return students

try:
    num_students = int(input("Enter number of students: "))
    num_subjects = int(input("Enter number of subjects: "))
    students_list = create_students(num_students, num_subjects)
except ValueError:
    print("Please enter valid integer values for number of students and subjects.")
    exit()

try:
    # Setting path of dataset file
    script_directory = os.path.dirname(os.path.abspath(__file__))
    pickle_file_path = os.path.join(script_directory, 'random_data.pkl')
    with open(pickle_file_path, 'wb') as file:
        pickle.dump(students_list, file)
except Exception as e:
    print("An error occurred while saving student data:", e)

try:
    with open(pickle_file_path, 'rb') as file:
        loaded_students = pickle.load(file)
except pickle.PickleError as e:
    print("An error occurred while saving student data:", e)

for student in loaded_students:
    print(student)
