class Student:
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def is_passing(self):
        return self.score >= 60

    def update_score(self, new_score):
        if 0 <= new_score <= 100:
            self.score = new_score
            return True
        else:
            return False

    def to_dict(self):
        return {"name": self.name, "score": self.score}

    @classmethod
    def from_dict(cls, record):
        return cls(record["name"], record["score"])

    def __str__(self):
        return f"{self.name} {self.score} 分"


student = Student("小明", 88)
print(student.name, student.score)

student_a = Student("小明", 88)
student_b = Student("小红", 95)

student_a.score = 90

print(student_a.score, student_b.score)

student_a.update_score(58)
print(student_a.is_passing())

print(student_a.update_score(101), student_a.score)

students = [student_a, student_b]

student_records = [student.to_dict() for student in students]

restored_students = [Student(record["name"], record["score"]) for record in student_records]

print(restored_students[0].is_passing())

restored_students = [Student.from_dict(record) for record in student_records]

print(restored_students[0].name)

print("==========")

for student in restored_students:
    if student.is_passing():
        print(student.name)

print(restored_students[0])

print("==========")

restored_students[0].update_score(60)

for student in restored_students:
    if student.is_passing():
        print(student)