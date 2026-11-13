students = [
    {"name": "小明", "score": 88},
    {"name": "小红", "score": 95},
    {"name": "小刚", "score": 60},
]

# scores = [student["score"] for student in students]
# high_scores = [score for score in scores if score >= 90]
# lower_scores = [score for score in scores if score < 90]
#
# print(high_scores)
# print(lower_scores)
#
# top_students = [student for student in students if student["score"] >= 80]
# top_scores = [student["score"] for student in top_students]
# scores_at_least_80 = [student["score"] for student in students if student["score"] >= 80]
#
# print(top_students)
# print(top_scores)
# print(scores_at_least_80)

# scores_by_name = {student["name"]: student["score"] for student in students}
# print(scores_by_name)
# print(scores_by_name["小红"])

high_scores_by_name = {student["name"]: student["score"] for student in students if student["score"] >= 80}
print(high_scores_by_name)

same_name_students = [
    {"name": "小明", "score": 88},
    {"name": "小明", "score": 96},
]

scores_by_name = {
    student["name"]: student["score"] for student in same_name_students
}
print(scores_by_name)

same_name_students.append({"name": "小红", "score": 90})

unique_names = {student["name"] for student in same_name_students}
print(unique_names)
print(len(unique_names))