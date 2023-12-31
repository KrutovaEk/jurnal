

class Student:
    def __init__(self, name, surname, gender):
        self.name = name      
        self.surname = surname  
        self.gender = gender                 #пол
        self.finished_courses = []           #законченые курсы
        self.courses_in_progress = []        #курсы в программе
        self.grades = {}                     #оценки
        self.col_grades = 0                  #количество оценок
        self.average_grades=0                #средняя оценка

    def rate_hw_lecturer(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            lecturer.col_grades += 1
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'
        
    def average_grade(self): 
        grades=self.grades 
        values=0
        for key, value in grades.items():
            values+=sum(value)
        self.average_grades =values/(self.col_grades)
    
    def __str__(self):
        courses_in_progress=', '.join(self.courses_in_progress)
        finished_courses=', '.join(self.finished_courses)
        red=f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания: {self.average_grades}\nКурсы в процессе изучения: {courses_in_progress}\nЗавершенные курсы: {finished_courses}\n' 
        return red
    
    def __lt__(self, student_2):
        self.average_grades>student_2.average_grades
        if self.average_grades > student_2.average_grades:
            return f'Средняя оценка за домашние задания студента {self.name} {self.surname} выше, чем cредняя оценка за домашние задания студента {student_2.name} {student_2.surname}.\n'
        elif self.average_grades < student_2.average_grades:
            return f'Средняя оценка за домашние задания студента {student_2.name} {student_2.surname} выше, чем cредняя за домашние задания студента {self.name} {self.surname}.\n'
        elif self.average_grades == student_2.average_grades:
            return f'Средняя оценка за домашние задания студента {student_2.name} {student_2.surname} и студента {self.name} {self.surname} равны {self.average_grades}.\n'

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []          # закрепленный курс


class Reviewer(Mentor):     
    def rate_hw(self, students, course, grade):
        if isinstance(students, Student) and course in self.courses_attached and course in students.courses_in_progress:
            students.col_grades += 1
            if course in students.grades:
                students.grades[course] += [grade]
            else:
                students.grades[course] = [grade]
        else:
            return 'Ошибка'


    def __str__(self):
        red=f'Имя: {self.name}\nФамилия: {self.surname}\n' 
        return red


class Lecturer(Mentor):
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = [] # закрепленный курс
        self.grades = {}
        self.col_grades = 0
        self.average_grades=0

    def average_grade(self): 
        grades=self.grades 
        values=0
        for key, value in grades.items():
            values+=sum(value)
        self.average_grades =values/(self.col_grades)

    def __str__(self):
        red=f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.average_grades}\n' 
        return red
    
    def __lt__(self, lecturer_2):
        self.average_grades>lecturer_2.average_grades
        if self.average_grades > lecturer_2.average_grades:
            return f'Средняя оценка за лекции лектора {self.name} {self.surname} выше, чем cредняя оценка за лекции лектора {lecturer_2.name} {lecturer_2.surname}.\n'
        elif self.average_grades < lecturer_2.average_grades:
            return f'Средняя оценка за лекции лектора {lecturer_2.name} {lecturer_2.surname} выше, чем cредняя оценка за лекции лектора {self.name} {self.surname}.\n'
        elif self.average_grades == lecturer_2.average_grades:
            return f'Средняя оценка за лекции лектора {lecturer_2.name} {lecturer_2.surname} и лектора {self.name} {self.surname} равны {self.average_grades}.\n'

best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python']
best_student.courses_in_progress += ['Git']

cool_mentor = Reviewer('Some', 'Buddy')
cool_mentor.courses_attached += ['Python']


cool_mentor_2 = Reviewer('Semen', 'Man')
cool_mentor_2.courses_attached += ['Git']

cool_mentor.rate_hw(best_student, 'Python', 10)
cool_mentor.rate_hw(best_student, 'Python', 10)
cool_mentor.rate_hw(best_student, 'Python', 10)
cool_mentor_2.rate_hw(best_student, 'Git', 10)
cool_mentor_2.rate_hw(best_student, 'Git', 10)

best_student.average_grade()


best_student_2 = Student('Olig', 'Grin', 'your_gender')
best_student_2.courses_in_progress += ['Python']
best_student_2.courses_in_progress += ['Git']


cool_mentor.rate_hw(best_student_2, 'Python', 10)
cool_mentor.rate_hw(best_student_2, 'Python', 10)
cool_mentor.rate_hw(best_student_2, 'Python', 10)
cool_mentor_2.rate_hw(best_student_2, 'Git', 10)
cool_mentor_2.rate_hw(best_student_2, 'Git', 9)

best_student_2.average_grade()

cool_lecturer = Lecturer('Nik', 'Zet')
cool_lecturer.courses_attached += ['Python']
cool_lecturer.courses_attached += ['Git']

best_student.rate_hw_lecturer(cool_lecturer, 'Python', 10)
best_student.rate_hw_lecturer(cool_lecturer, 'Python', 8)
best_student.rate_hw_lecturer(cool_lecturer, 'Python', 10)
best_student.rate_hw_lecturer(cool_lecturer, 'Git', 8)
best_student.rate_hw_lecturer(cool_lecturer, 'Git', 8)
best_student.rate_hw_lecturer(cool_lecturer, 'Git', 8)
cool_lecturer.average_grade()



cool_lecturer_2 = Lecturer('Dmitriy', 'Red')
cool_lecturer_2.courses_attached += ['Python']
cool_lecturer_2.courses_attached += ['Git']

best_student.rate_hw_lecturer(cool_lecturer_2, 'Python', 10)
best_student.rate_hw_lecturer(cool_lecturer_2, 'Python', 8)
best_student.rate_hw_lecturer(cool_lecturer_2, 'Python', 7)
best_student.rate_hw_lecturer(cool_lecturer_2, 'Git', 9)
best_student.rate_hw_lecturer(cool_lecturer_2, 'Git', 9)
best_student.rate_hw_lecturer(cool_lecturer_2, 'Git', 8)
cool_lecturer_2.average_grade()


list_student=[best_student, best_student_2]
list_lecturer=[cool_lecturer, cool_lecturer_2]
cours = 'Git'

def average_cours_student(list_student=list_student, cours=cours):
    values=0
    grade = 0
    average_student=0
    for student in list_student:
        s = getattr(student, 'grades')  
        for key, value in s.items():
            if key==cours:
                 values+=sum(value)
                 grade+=len(value)
                 #print(values)
                 #print(grade)
    average_student=f'Средняя оценка студентов за курс {cours} = {values/grade}.'       
    return average_student


def average_cours_lecturer(list_lecturer=list_lecturer, cours=cours):
    values=0
    grade = 0
    average_lecturer=0
    for lecturer in list_lecturer:
        s = getattr(lecturer, 'grades')  
        for key, value in s.items():
            if key==cours:
                 values+=sum(value)
                 grade+=len(value)
                 #print(values)
                 #print(grade)
    average_lecturer=f'Средняя оценка лекторов за курс {cours} = {values/grade}.'       
    return average_lecturer


#print(best_student.average_grades)
#print(best_student.grades)
print(best_student)
print(best_student_2)
print(best_student_2>best_student)

#print(cool_lecturer.grades)
#print(cool_lecturer.average_grades)
print(cool_lecturer)
print(cool_lecturer_2)
print(cool_lecturer>cool_lecturer_2)
print(cool_mentor)
print(cool_mentor_2)



print(average_cours_student())
print(average_cours_lecturer())