class Student:
    def __init__(self, name: str, score: int) -> None:
        self.name = name
        self.score = score

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, new_score):
        if not 0 <= new_score <= 100:
            raise ValueError("分数必须在 0 到 100 之间")
        self._score = new_score


class StudentGroup:
    def __init__(self):
        self.students: list[Student] = []

    def add_student(self, student: Student) -> None:
        self.students.append(student)

    def average_score(self):
        total_score = 0
        for student in self.students:
            total_score += student.score
        if len(self.students) == 0:
            return None
        return total_score / len(self.students)

    def find_student(self, target_name):
        for student in self.students:
            if student.name == target_name:
                return student
        return None

    def remove_student(self, target_name):
        student = self.find_student(target_name)
        if student is not None:
            self.students.remove(student)
            return True
        return False


group = StudentGroup()
group.add_student(Student("小明", 88))
group.add_student(Student("小红", 95))

print(group.students[1].name)
print(group.average_score())

student = group.find_student("小明")

if student is not None:
    student.score = 90

print(group.average_score())

print(group.remove_student("小明"))
print(group.remove_student("小明"))

empty_group = StudentGroup()
print(group.average_score(), empty_group.average_score())