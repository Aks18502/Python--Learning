class school:
    def __init__(self, name, location, students):
        self.name = name
        self.location = location
        self._students = students
    def display(self):
        print(f"School Name: {self.name}\nLocation: {self.location}\nStudents: {self._students}")
class course(school):
    def __init__(self, name, location, students, course_name, duration):
        super().__init__(name, location, students)
        self.course_name = course_name
        self.duration = duration
    def display_course(self):
        super().display()
        print(f" {self.name} this Course Name is: {self.course_name}\nDuration: {self.duration}")
class student(school):
    def __init__(self, name, location, students, student_name, age):
        super().__init__(name, location, students)
        self.student_name = student_name
        self.age = age
    def display_student(self):
        super().display()
        print(f"Hii, {self.student_name}\nyour Age is: {self.age}")

stu=student("Kanishka School", "Myd", 100, "Kanishka", 17)
stu.display_student()
cou=course("Kanishka School", "Myd", 100, "Python Programming", "3 months")
cou.display_course()
print(stu.name, stu.location, stu._students, stu.student_name, stu.age)
print(cou.name, cou.location, cou._students, cou.course_name, cou.duration)
