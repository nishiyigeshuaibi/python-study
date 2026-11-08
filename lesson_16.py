from student_storage import load_students, save_students
from student_service import add_student, delete_student, update_score, find_student, get_top_students



def read_integer(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("请输入整数")


def show_students(students):
    if not students:
        print("暂无学生记录")
    else:
        for number, student in enumerate(students, start=1):
            print(number, student["name"], student["score"])


def show_menu():
    print("===欢迎使用学生管理系统===")
    print("1. 查询学生")
    print("2. 删除学生")
    print("3. 修改成绩")
    print("4. 查看所有学生")
    print("5. 添加学生")
    print("6. 查看前几名")
    print("q. 退出")
    choice = input("请输入您的选择：").strip().lower()
    return choice


def main():
    students = load_students()

    while True:
        choice = show_menu()
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
            new_score = read_integer("请输入要修改成多少分：")
            success = update_score(students, name, new_score)
            if success:
                save_students(students)
                print("修改成功")
            else:
                print("修改失败，请检查姓名和分数")
        elif choice == "4":
            show_students(students)
        elif choice == "5":
            name = input("请输入你要添加的学生姓名：").strip()
            score = read_integer("请输入该学生的分数:")
            success = add_student(students, name, score)
            if success:
                save_students(students)
                print("添加成功")
            else:
                print("添加失败，请检查姓名和分数")
        elif choice == "6":
            while True:
                count = read_integer("要查看前多少位学生：")
                if count <= 0:
                    print("人数必须大于 0")
                    continue
        else:
            print("无效选择")


if __name__ == "__main__":
    main()