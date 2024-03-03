'''
    This module is used to make calculation related to students dataset
'''
import pickle

def cal_average(data):
    '''
    This function calculates the average score of each student and returns dict.
    '''
    try:
        average_scores = {}
        num_subjects = len(data[0]['scores'])
        for student in data:
            name = student['name']
            scores = student['scores']
            if any(score < 0 or score > 100 for score in scores):
                return ("Incorrect score detected.")
            if len(scores) != num_subjects:
                return "Incorrect number of scores detected."
            average_score = round(sum(scores) / len(scores),2)
            average_scores[name] = average_score
        return average_scores
    except Exception as e:
        print("An error occurred while calculating average scores:", e)
        return {}

def find_highest_scorer(dataset):
    '''
    This function finds the student with the highest average score
    and the highest scorer for each subject.
    '''
    try:
        average_scores = cal_average(dataset)

        highest_average_score = max(average_scores.values())
        highest_average_scorer = sorted([name for name, score in average_scores.items() if score == highest_average_score])[0]

        highest_subject_scorers = []
        num_subjects = len(dataset[0]['scores'])
        for i in range(num_subjects):
            highest_score_subject_i = max(student['scores'][i] for student in dataset)
            highest_scorers_subject_i = sorted([student['name'] for student in dataset if student['scores'][i] == highest_score_subject_i])[0]
            highest_subject_scorers.append(highest_scorers_subject_i)

        return highest_average_scorer, highest_subject_scorers
    except Exception as e:
        print("An error occurred while finding the highest scorer:", e)
        return None, None

def main():
    '''
        This is menu based user input
    '''
    students = []
    try:
        num_students = int(input("Enter number of students: "))
        num_subjects = int(input("Enter number of subjects: "))
    except ValueError:
        print("Please enter valid integer values for number of students and subjects.")
        exit()

    for i in range(num_students):
        name = input(f"Enter name of student {i+1}: ")
        scores = []
        for j in range(num_subjects):
            try:
                score = int(input(f"Enter score for subject {j+1}: "))
            except ValueError:
                print("Please enter valid integer values for number of students and subjects.")
                exit()
            scores.append(score)
        student = {'name': name, 'scores': scores}
        students.append(student)
    print(cal_average(students))
    avg, list_st = find_highest_scorer(students)
    print(avg)
    print(list_st)

if __name__ == "__main__":
    main()

# try:
#     with open('../Dataset/students_data.pkl', 'rb') as file:
#         loaded_students = pickle.load(file)
# except pickle.PickleError as e:
#     print("An error occurred while saving student data:", e)
# i=0
# for load in loaded_students:
#     print(i)
#     print(cal_average(load))
#     avg, list_st = find_highest_scorer(load)
#     print(avg)
#     print(list_st)
#     i += 1