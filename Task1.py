class Student:
    all_students = []

    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        Student.all_students.append(self)

    def rate_lecture(self, lecture, course, grade):
        self.lecture = lecture
        self.course = course
        self.grade = grade
        if (
            isinstance(lecture, Lecture)
            and (
                self.course in self.courses_in_progress
                or self.course in self.finished_courses
            )
            and self.course in lecture.courses_attached
            and 0 <= grade <= 10
        ):
            lecture.grades.setdefault(course, []).append(grade)
        else:
            return "Ошибка"

    def __str__(self):
        self.list_grade = []
        for key, value in self.grades.items():
            for grade in value:
                self.list_grade.append(grade)
        self.avg_grade = round(sum(self.list_grade) / len(self.list_grade), 1)
        return f"Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания: {self.avg_grade}\nКурсы в процессе изучения: {', '.join(self.courses_in_progress)}\nЗавершенные курсы: {', '.join(self.finished_courses)}"

    def __le__(self, other):
        return self.avg_grade <= other.avg_grade

    def __ge__(self, other):
        return self.avg_grade >= other.avg_grade

    def __eq__(self, other):
        return self.avg_grade == other.avg_grade

    def find_avg_lectures_by_course(self, all_lectures, course):
        lectures_list_avg_grade = []
        if course in self.courses_in_progress or course in self.finished_courses:
            for lecture in all_lectures:
                if course in lecture.grades:
                    grades_for_course = lecture.grades[course]
                    lectures_list_avg_grade.extend(grades_for_course)
        else:
            print("Error")
        return round(sum(lectures_list_avg_grade) / len(lectures_list_avg_grade), 1)


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecture(Mentor):
    all_lectures = []

    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}
        Lecture.all_lectures.append(self)

    def __str__(self):
        self.list_grade_lections = []
        for key, value in self.grades.items():
            for grade in value:
                self.list_grade_lections.append(grade)
        self.avg_grade_lections = round(
            sum(self.list_grade_lections) / len(self.list_grade_lections), 1
        )
        return f"Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.avg_grade_lections}"

    def __le__(self, other):
        return self.avg_grade_lections <= other.avg_grade_lections

    def __ge__(self, other):
        return self.avg_grade_lections >= other.avg_grade_lections

    def __eq__(self, other):
        return self.avg_grade_lections == other.avg_grade_lections


class Reviewer(Mentor):

    def __init__(self, name, surname):
        super().__init__(name, surname)

    def rate_hw(self, student, course, grade):
        if (
            isinstance(student, Student)
            and course in self.courses_attached
            and course in student.courses_in_progress
        ):
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return "Ошибка"

    def __str__(self):
        return f"Имя: {self.name}\nФамилия: {self.surname}"

    def find_avg_by_course(self, all_students, course):
        list_avg_grade = []
        if course in self.courses_attached:
            for student in all_students:
                if course in student.grades:
                    grades_for_this_course = student.grades[course]
                    list_avg_grade.extend(grades_for_this_course)
        else:
            print("Error")
        return round(sum(list_avg_grade) / len(list_avg_grade), 1)


# Вызываем методы для Студентов
student_1 = Student("Ruoy", "Eman", "man")
student_1.courses_in_progress += ["Python"]
student_1.courses_in_progress += ["Git"]
student_1.finished_courses += ["Введение в программирование"]
student_1.finished_courses += ["Маркетинг"]

student_2 = Student("Oleg", "Zaytzev", "man")
student_2.courses_in_progress += ["Java"]
student_2.courses_in_progress += ["Agile"]
student_2.finished_courses += ["Git"]

student_3 = Student("Ronny", "Smith", "man")
student_3.courses_in_progress += ["Python"]


# Вызываем методы для ревьеров
rev_1 = Reviewer("Anna", "Ivanova")
rev_1.courses_attached += ["Python"]
rev_1.courses_attached += ["Java"]

rev_1.rate_hw(student_1, "Python", 5)
rev_1.rate_hw(student_1, "Python", 7)
rev_1.rate_hw(student_1, "Python", 10)

rev_1.rate_hw(student_2, "Java", 5)
rev_1.rate_hw(student_2, "Java", 9)


rev_2 = Reviewer("Andrey", "Novikov")
rev_2.courses_attached += ["Python"]
rev_2.courses_attached += ["Agile"]

rev_2.rate_hw(student_1, "Python", 7)
rev_2.rate_hw(student_1, "Python", 8)
rev_2.rate_hw(student_1, "Python", 9)

rev_2.rate_hw(student_2, "Agile", 1)
rev_2.rate_hw(student_2, "Agile", 4)
rev_2.rate_hw(student_2, "Agile", 8)

rev_1_find_avg = rev_1.find_avg_by_course(Student.all_students, "Python")
rev_2_find_avg = rev_2.find_avg_by_course(Student.all_students, "Python")

print(rev_1_find_avg)
print(rev_2_find_avg)

# Вызываем методы для лекторов
lecture_1 = Lecture("Elena", "Antonova")
lecture_1.courses_attached += ["Python"]
lecture_1.courses_attached += ["Java"]
student_2.rate_lecture(lecture_1, "Java", 8)
student_1.rate_lecture(lecture_1, "Python", 8)
student_1.rate_lecture(lecture_1, "Git", 3)

lecture_2 = Lecture("Petr", "Gudkov")
lecture_2.courses_attached += ["Git"]
student_2.rate_lecture(lecture_2, "Git", 4)
student_1.rate_lecture(lecture_2, "Git", 7)
student_1.rate_lecture(lecture_2, "Git", 10)


student_1_find_avg = student_1.find_avg_lectures_by_course(Lecture.all_lectures, "Git")
student_2_find_avg = student_2.find_avg_lectures_by_course(Lecture.all_lectures, "Git")
student_2_find_avg_2 = student_2.find_avg_lectures_by_course(
    Lecture.all_lectures, "Java"
)

print(student_1_find_avg)
print(student_2_find_avg)
print(student_2_find_avg_2)

# Выводим на экран экземпляры классов
print(student_1)
print()
print(student_2)
print()
print(rev_1)
print()
print(rev_2)
print()
print(lecture_1)
print()
print(lecture_2)

# Результаты реализации методов сравнения лекторов и студентов

print(student_1 <= student_2)
print(lecture_1 <= lecture_2)

print(student_1 >= student_2)
print(lecture_1 >= lecture_2)

print(student_1 == student_2)
print(lecture_1 == lecture_2)
