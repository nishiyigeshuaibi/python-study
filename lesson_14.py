import json

# students = [{"name": "小丽", "score": 26}]
#
# text = json.dumps(students, ensure_ascii=False)
#
# print(text)
#
# with open("students.json", "w", encoding="utf-8") as f:
#     f.write(text)


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


students = load_students()

while True:
    print("1. 查询学生")
    print("2. 删除学生")
    print("3. 修改成绩")
    print("4. 查看所有学生")
    print("5. 添加学生")
    print("q. 退出")
    choice = input("请输入您的选择：").strip().lower()
    if choice == "q":
        save_students(students)
        break
    elif choice == "1":
        name = input("请输入您要查询的学生姓名：").strip()
        student = find_student(students, name)
        if student is not None:
            print(student["name"], student["score"])
        else:
            print("未找到该学生")
    elif choice == "2":
        name = input("请输入您要删除的学生姓名：").strip()
        success = delete_student(students, name)
        if success:
            save_students(students)
            print("删除成功")
        else:
            print("未找到该学生")
    elif choice == "3":
        name = input("请输入您要修改分数的学生姓名：").strip()
        while True:
            try:
                new_score = int(input("请输入要修改成多少分："))
                success = update_score(students, name, new_score)
                if success:
                    save_students(students)
                    print("修改成功")
                else:
                    print("修改失败，请检查姓名和分数")
                break
            except ValueError:
                print("请输入整数")
    elif choice == "4":
        if not students:
            print("暂无学生记录")
        else:
            for number, student in enumerate(students, start=1):
                print(number, student["name"], student["score"])
    elif choice == "5":
        name = input("请输入你要添加的学生姓名：").strip()
        while True:
            try:
                new_score = int(input("请输入该学生的分数："))
                success = add_student(students, name, new_score)
                if success:
                    save_students(students)
                    print("添加成功")
                else:
                    print("添加失败，请检查姓名和分数")
                break
            except ValueError:
                print("请输入整数")
    else:
        print("无效选择")
