student_list = []
course_list = []

class Student:
    def __init__(self, student_id, student_name):
        self.student_id = student_id
        self.student_name = student_name

class Subject:
    def __init__(self, subject_id, subject_name, section, credit, teacher):
        self.subject_id = subject_id
        self.subject_name = subject_name
        self.section = section
        self.credit = credit
        self.teacher = teacher
        self.student_list = []
    
    def enroll(self, student: Student):
        self.student_list.append(student)
        
class Teacher:
    def __init__(self, teacher_id, teacher_name):
        self.teacher_id = teacher_id
        self.teacher_name = teacher_name

def get_enrolled_course_by_student_id(student_id):
    all_enrolled_subject = []
    for subject in course_list:
        for student in subject.student_list:
            if student.student_id == student_id:
                all_enrolled_subject.append(subject.subject_name)
    return all_enrolled_subject

def get_student_by_teacher_id(teacher_id):
    all_student = []
    for subject in course_list:
        if teacher_id in [teacher.teacher_id for teacher in subject.teacher]:
            for student in subject.student_list:
                if student.student_name not in all_student:
                    all_student.append(student.student_name)    
    return all_student

# Create student's instance
stu1 = Student('0001', 'John')
stu2 = Student('0002', 'Jane')
stu3 = Student('0003', 'Jack')
stu4 = Student('0004', 'Jill')
stu5 = Student('0005', 'James')
student_list.extend([stu1, stu2, stu3, stu4, stu5])

# Create teacher's instance
teacher1 = Teacher('0001', 'Thana Hongsuwan')
teacher2 = Teacher('0002', 'Orachat Chitsobhu')
teacher3 = Teacher('0003', 'Sakchai Thipchasurat')
teacher4 = Teacher('0004', 'Sakda Thipchasurat')

object_oriented_programming_1 = Subject('261361', 'Object Oriented Programming 01', '01', 3, [teacher1])
object_oriented_programming_2 = Subject('261362', 'Object Oriented Programming 02', '02', 3, [teacher2])
calculus1 = Subject('261101', 'Calculus 01', '01', 3, [teacher3])
calculus2 = Subject('261102', 'Calculus 02', '01', 3, [teacher4, teacher2])
course_list.extend([object_oriented_programming_1, object_oriented_programming_2, calculus1, calculus2])

# John 0001
object_oriented_programming_1.enroll(stu1)
calculus1.enroll(stu1)

# Jane 0002
object_oriented_programming_1.enroll(stu2)
calculus1.enroll(stu2)


# Jack 0003
object_oriented_programming_2.enroll(stu3)
calculus2.enroll(stu3)

# Jill 0004
object_oriented_programming_2.enroll(stu4)

# James 0005
object_oriented_programming_2.enroll(stu5)


print(get_enrolled_course_by_student_id('0004'))
print(get_student_by_teacher_id('0002'))
