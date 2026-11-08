students = [
    {"name": "小明", "score": 88},
    {"name": "小红", "score": 95},
    {"name": "小刚", "score": 60},
]


def get_score(student):
    return student["score"]


def get_top_students(students, count):
    if count <= 0:
        return []
    ranked_students = sorted(students, key=get_score, reverse=True)
    return ranked_students[:count]

top_students = get_top_students(students, 1)

assert top_students == [{"name": "小红", "score": 95}]
assert get_top_students([], 2) == []
assert get_top_students(students, -1) == []

print("检查通过")
