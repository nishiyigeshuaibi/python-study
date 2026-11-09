class Student:
    def __init__(self, name, score):
        self.name = name
        self.score = score


student = Student("小明", 88)
print(student.name, student.score)