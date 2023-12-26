student_list = []

class Student:
    def __init__(self, student_id: str, student_name, peerahat = None):
        self.student_id = student_id
        self.student_name = student_name
        self.year = 67 - int(student_id[:2]) # Convert student_id to year
        self.student_mentor = peerahat if peerahat else None

def show_sairahat(student_id):
    for student in student_list:
        if student.student_id == student_id:
            if student.student_mentor == 0:
                print("No more sairahat")
                return 
            if student.student_mentor != None:
                print(student.student_mentor.student_id, student.student_mentor.student_name)
                show_sairahat(student.student_mentor.student_id)

def is_sairahat(student_id1, student_id2):
    # Swap student_id1 and student_id2 if student_id1 is greater than student_id2
    if int(student_id1) < int(student_id2):
        student_id1, student_id2 = student_id2, student_id1

    for student in student_list:
        if student.student_id == student_id1:
            if student.student_mentor == 0:
                return False
            if student.student_mentor.student_id == student_id2:
                return True
            return is_sairahat(student.student_mentor.student_id, student_id2)
    return False

# Create student's instance
stu1 = Student('63000001', 'James')
stu2 = Student('64000001', 'Jill')
stu3 = Student('64000002', 'Jack', stu1)
stu4 = Student('65000001', 'Jane', stu3)
stu5 = Student('66000001', 'John', stu4)

stu6 = Student('63000002', 'Wiroj')
stu7 = Student('63000003', 'Wichai')
stu8 = Student('64000003', 'Wichit', stu6)
stu9 = Student('64000004', 'Wichian')
stu10 = Student('65000002', 'Wicharn', stu8)
stu11 = Student('66000002', 'Wirat', stu10)
student_list.extend([stu1, stu2, stu3, stu4, stu5, stu6, stu7, stu8, stu9, stu10, stu11])

'''

John        ->      Jane        ->      Jack        ->      James
66000001    ->      65000001    ->      64000002    ->      63000001


Wirat       ->      Wicharn        ->   Wichit      ->      Wiroj
66000002    ->      65000002    ->      64000003    ->      63000002

'''

show_sairahat('65000001')
print(is_sairahat('64000003', '66000002'))
