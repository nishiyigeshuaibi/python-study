import json

def load_students():
    try:
        with open("students.json", "r", encoding="utf-8") as f:
            text = f.read()
        students = json.loads(text)
        return students
    except FileNotFoundError:
        return []


def save_students(students):
    json_str = json.dumps(students, ensure_ascii=False)
    with open("students.json", "w", encoding="utf-8") as f:
        f.write(json_str)
