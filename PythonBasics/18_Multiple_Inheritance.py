"""
Real Life Example :

Create multiple inheritance on teacher,student and youtuber.
Q. if we have created teacher and now one student joins master degree 
with becoming teacher then what??

Ans :  just make subclass from  teacher so that student will become teacher
Now student is teacher as well as youtuber then what???
-just use multiple inheritance for these three relations

"""

class teacher():
    def __init__(self):
        self.role = 'Teacher'

    def teacher_skills(self):
        print('Teacher teaches students')

class youtuber():
    def __init__(self):
        self.role = 'Youtuber'
    
    def youtuber_skills(self):
        print('Youtuber Makes content')

class student():
    def __init__(self):
        self.role = 'Student'
    
    def student_skills(self):
        print("Student learns to become a teacher")

class person(student,teacher,youtuber):
    pass


p = person()
p.teacher_skills()
p.youtuber_skills()
p.student_skills()