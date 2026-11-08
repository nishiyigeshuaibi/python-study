# try:
#     score = int(input("请输入整数分数："))
#     print("分数", score)
# except ValueError:
#     print("输入有误，请输入整数")

def read_score(student_number):
    while True:
        try:
            score = int(input(f"请输入第 {student_number} 位学生的整数分数："))
            if 0 <= score <= 100:
                break
            print(f"第 {student_number} 名学生的分数必须在 0 到 100 之间")
        except ValueError:
            print("输入有误，请输入整数")
    return score


def is_passing(score):
    return score >= 60


def count_passing(scores):
    count = 0

    for score in scores:
        if is_passing(score):
            count += 1
    return count


def calculate_sum(scores):
    total = 0
    for score in scores:
        total += score
    return total


def show_report(scores):

    if len(scores) == 0:
        print("暂无成绩")
        return

    print("成绩统计")
    print(f"学生人数：{len(scores)}")

    passing_count = count_passing(scores)
    average = calculate_sum(scores) / len(scores)

    print(f"及格人数：{passing_count} 人")
    print(f"平均分：{average:.2f}")

    highest_score = max(scores)

    print(f"最高分：{highest_score}")

    lowest_score = min(scores)

    print(f"最低分：{lowest_score}")

    pass_rate = passing_count / len(scores)

    print(f"及格率：{pass_rate:.2%}")


def read_student_count():
    while True:
        try:
            input_count = int(input("请输入您要录入的学生人数:"))
            if input_count > 0:
                return input_count
            print("学生人数必须大于 0")
        except ValueError:
            print("输入有误，请输入整数")


# score = read_score()
# print("分数", score)

scores = []
student_count = read_student_count()

for index in range(student_count):
    score = read_score(index + 1)
    scores.append(score)

show_report(scores)

