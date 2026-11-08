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

students = [
    {"name": "小明", "score": 55},
    {"name": "小红", "score": 90},
    {"name": "小刚", "score": 60},
]

# print(students[0]["name"])

# print(students[1]["score"])

# students[0]["score"] = 65

# for student in students:
#     if student["score"] >= 60:
#         print(student["name"], student["score"])

# students.append({"name": "小华", "score": 72})
#
# for student in students:
#     if student["name"] == "小华":
#         print(student["name"], student["score"])
#         break
#
# result = find_student(students, "小华")
#
# if result is None:
#     print("未找到该学生")
# else:
#     result["score"] = 85
#     print(result["name"], result["score"])
#
# result_again = find_student(students, "小华")
# print(result_again["score"])
#
# students = [{"name": "小华", "score": 88}]
#
# target_name = input("请输入要修改成绩的学生姓名：").strip()
#
# while True:
#     try:
#         new_score = int(input("请输入要修改成多少分："))
#         break
#     except ValueError:
#         print("请输入整数")
#
# success = update_score(students, target_name, new_score)
#
# if success:
#     print("修改成功")
# else:
#     print("修改失败，请检查姓名和分数")
#
# student = find_student(students, target_name)
# if student is not None:
#     print(student["name"], student["score"])
students.append({"name": "小华", "score": 72})

while True:
    print("1. 查询学生")
    print("2. 删除学生")
    print("3. 修改成绩")
    print("4. 查看所有学生")
    print("5. 添加学生")
    print("q. 退出")
    choice = input("请输入您的选择：").strip().lower()
    if choice == "q":
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
            for number,student in enumerate(students,start=1):
                print(number, student["name"], student["score"])
    elif choice == "5":
        name = input("请输入你要添加的学生姓名：").strip()
        while True:
            try:
                new_score = int(input("请输入该学生的分数："))
                success = add_student(students, name, new_score)
                if success:
                    print("添加成功")
                else:
                    print("添加失败，请检查姓名和分数")
                break
            except ValueError:
                print("请输入整数")
    else:
        print("无效选择")