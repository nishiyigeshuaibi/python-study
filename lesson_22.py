class Student:
    def __init__(self, name, score):
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


student = Student("小明", 60)
print(student.score)

student.score = 90
print(student.score)

try:
    student.score = 101
except ValueError as e:
    print(e)

print(student.score)

Student("小明", 101)