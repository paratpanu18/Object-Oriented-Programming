subject_score = {}

def add_score(subject_score, student, subject, score):
    if student not in subject_score:
        subject_score[student] = {}

    subject_score[student][subject] = score
    # print(subject_score)

def calc_average_score(student, subject_score):
    if student in subject_score:
        sum_score = 0
        subject_count = 0
        for i in subject_score[student].items():
            sum_score += i[1]
            subject_count += 1
        return '{:.2f}'.format(sum_score / subject_count)

    else:
        return "Student not in the list"

add_score(subject_score=subject_score, student='66010542', subject="ICE", score=100)
add_score(subject_score=subject_score, student='66010542',subject="Calculus", score=60)
add_score(subject_score=subject_score, student='66010542',subject="ProFund", score=70)
print(calc_average_score('66010542', subject_score))

