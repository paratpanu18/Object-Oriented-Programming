subject_score = {}

def add_score(subject_score, subject, score):
    subject_score[subject] = score
    print(subject_score)

def calc_average_score(subject_score):
    return str('%.2f' % float(sum([int(subject_score[num]) for num in subject_score]) / len(subject_score)))
  
add_score(subject_score=subject_score, subject="ICE", score=100)
add_score(subject_score=subject_score, subject="Calculus", score=60)
add_score(subject_score=subject_score, subject="ProFund", score=70)
print(calc_average_score(subject_score))
