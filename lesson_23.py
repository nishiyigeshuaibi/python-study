from typing import Optional
import json

class Student:
    def __init__(self, name: str, score: int) -> None:
        self.name = name
        self.score = score

    def to_dict(self) -> dict:
        return {"name": self.name, "score": self.score}

    @property
    def score(self) -> int:
        return self._score

    @score.setter
    def score(self, new_score) -> None:
        if not 0 <= new_score <= 100:
            raise ValueError("分数必须在 0 到 100 之间")
        self._score = new_score


class StudentGroup:
    def __init__(self):
        self.students: list[Student] = []

    def add_student(self, student: Student) -> None:
        self.students.append(student)

    def average_score(self) -> Optional[float]:
        total_score = 0
        for student in self.students:
            total_score += student.score
        if len(self.students) == 0:
            return None
        return total_score / len(self.students)

    def find_student(self, target_name: str) -> Optional[Student]:
        for student in self.students:
            if student.name == target_name:
                return student
        return None

    def remove_student(self, target_name) -> bool:
        student = self.find_student(target_name)
        if student is not None:
            self.students.remove(student)
            return True
        return False

    def get_passing_students(self) -> list[Student]:
        return [student for student in self.students if student.score >= 60]

    def passing_rate(self) -> Optional[float]:
        if not self.students:
            return None

        return len(self.get_passing_students()) / len(self.students)

    def to_records(self) -> list[dict]:
        return [student.to_dict() for student in self.students]

def test_passing_rate_half():
    group = StudentGroup()
    group.add_student(Student("小明", 40))
    group.add_student(Student("小红", 80))

    assert group.passing_rate() == 0.5

def show_passing_rate(group: StudentGroup) -> None:
    rate = group.passing_rate()

    if rate is not None:
        print(f"及格率：{rate:.2%}")
    else:
        print("暂无成绩")

def test_passing_rate_empty():
    empty_group = StudentGroup()
    assert empty_group.passing_rate() is None

def test_passing_rate_zero() -> None:
    group = StudentGroup()

    group.add_student(Student("小明", 40))
    group.add_student(Student("小红", 50))

    assert group.passing_rate() == 0.0

def test_passing_rate_all() -> None:
    group = StudentGroup()

    group.add_student(Student("小明", 60))
    group.add_student(Student("小红", 100))

    assert group.passing_rate() == 1.0, "全部学生及格时，及格率应为 1.0"

def test_passing_rate_after_update() -> None:
    group = StudentGroup()
    student = Student("小红", 50)
    group.add_student(student)

    assert group.passing_rate() == 0.0

    student.score = 80
    assert group.passing_rate() == 1.0

def save_group(group: StudentGroup) -> None:
    records = group.to_records()
    text = json.dumps(records, ensure_ascii=False)

    with open("student_group.json", "w", encoding="utf-8") as f:
        f.write(text)

with open("student_group.json", "r", encoding="utf-8") as f:
    text = f.read()

records = json.loads(text)
print(records[0]["name"])
