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
        for student in data:
            name = student['name']
            scores = student['scores']
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
        return '', [[]] * len(dataset[0]['scores'])


try:
    with open('../Dataset/random_data.pkl', 'rb') as file:
        loaded_students = pickle.load(file)
except pickle.PickleError as e:
    print("An error occurred while saving student data:", e)

print(cal_average(loaded_students))
avg, list_st = find_highest_scorer(loaded_students)
print(avg)
print(list_st)