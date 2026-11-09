students = [
    {"name": "小明", "score": 88},
    {"name": "小红", "score": 95},
    {"name": "小刚", "score": 60},
]

# 列表推导式：提取和筛选
scores = [student["score"] for student in students]
high_scores = [score for score in scores if score >= 90]
lower_scores = [score for score in scores if score < 90]

high_score_names = [
    student["name"] for student in students if student["score"] >= 90
]
top_students = [student for student in students if student["score"] >= 80]
top_scores = [student["score"] for student in top_students]
scores_at_least_80 = [
    student["score"] for student in students if student["score"] >= 80
]

print("全部分数", scores)
print("90 分及以上", high_scores)
print("低于 90 分", lower_scores)
print("高分学生姓名", high_score_names)
print("80 分及以上的学生记录", top_students)
print("筛选后提取分数", top_scores)
print("直接筛选并提取分数", scores_at_least_80)

# 字典推导式：用姓名作键，分数作值
scores_by_name = {
    student["name"]: student["score"] for student in students
}
high_scores_by_name = {
    student["name"]: student["score"]
    for student in students
    if student["score"] >= 80
}

print("小红的分数", scores_by_name["小红"])
print("80 分及以上的姓名和分数", high_scores_by_name)

# 同名记录：后写入的分数覆盖先写入的分数
same_name_students = [
    {"name": "小明", "score": 96},
    {"name": "小明", "score": 88},
]

same_name_scores = {
    student["name"]: student["score"] for student in same_name_students
}
print("同名记录转成字典", same_name_scores)

# 集合推导式：收集不同的姓名
unique_names = {student["name"] for student in same_name_students}
print("添加小红前的姓名数量", len(unique_names))

same_name_students.append({"name": "小红", "score": 90})
unique_names = {student["name"] for student in same_name_students}
print("添加小红后的姓名数量", len(unique_names))
print("小刚是否在成绩记录中", "小刚" in unique_names)

unique_names.add("小明")
print("再次添加小明后的姓名数量", len(unique_names))

# 交集、差集和并集
registered_names = {"小红", "小刚"}

print("报名且有成绩的姓名", unique_names & registered_names)
print("报名但没有成绩的姓名", registered_names - unique_names)

all_names = registered_names | unique_names
print("两份名单合并去重后的姓名数量", len(all_names))

print("已有成绩、却没有报名的人", unique_names - registered_names)

print(unique_names ^ registered_names)