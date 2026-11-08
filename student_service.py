
def find_student(students, target_name):
    for student in students:
        if student["name"] == target_name:
            return student
    return None


def update_score(students, target_name, new_score):

    if 0 <= new_score <= 100:
        student = find_student(students, target_name)
        if student is None:
            return False
        else:
            student["score"] = new_score
            return True
    else:
        return False


def delete_student(students, target_name):
    student = find_student(students, target_name)
    if student is None:
        return False
    else:
        students.remove(student)
        return True


def add_student(students, name, score):
    name = name.strip()
    if 0 <= score <= 100 and name:
        students.append({"name": name, "score": score})
        return True
    else:
        return False


def get_score(student):
    return student["score"]


def get_top_students(students, count):
    if count <= 0:
        return []
    ranked_students = sorted(students, key=get_score, reverse=True)
    return ranked_students[:count]