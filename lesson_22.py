class Student:
    def __init__(self, name, score):
        self.name = name
        self._score = score

    @property
    def score(self):
        return self._score


student = Student("小明", 60)
print(student.score)

