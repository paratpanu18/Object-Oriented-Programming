subject_score = {}

def add_score(subject_score, student, subject, score):
    if student not in subject_score:
        subject_score[student] = {}

    subject_score[student][subject] = score
    # print(subject_score)

def calc_average_score(subject_score):
        return {student: '%.2f' % ((sum(scores.values())) / len(scores)) for student, scores in subject_score.items()}
        # return {student: '%.2f' % (sum([score for score in subject_score[student].values()]) / len(subject_score[student].values()))} if student in subject_score else "No student in the list"

add_score(subject_score=subject_score, student='66010542', subject="ICE", score=100)
add_score(subject_score=subject_score, student='66010542',subject="Calculus", score=60)
add_score(subject_score=subject_score, student='66010542',subject="ProFund", score=70)
add_score(subject_score=subject_score, student='66010542',subject="OOP", score=100)
print(subject_score)
print(calc_average_score(subject_score))

