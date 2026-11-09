record = ("小明", 88)
name, score = record

print(name, score)

records = [("小明", 88), ("小红", 95)]

for name, score in records:
    print(name, score)

def get_score_range(scores):
    return min(scores), max(scores)


lowest, highest = get_score_range([88, 95, 60])
print(lowest, highest)

scores_by_name = {"小明": 88, "小红": 95}

for name, score in scores_by_name.items():
    print(name, score)

names = ["小明", "小红", "小刚"]
scores = [95, 88]

for name, score in zip(names, scores):
    print(name, score)

print(list(zip(names, scores)))

if len(names) == len(scores):
    scores_by_name = dict(zip(names, scores))
    print(scores_by_name)
else:
    print("姓名和分数的数量不一致")

single_score = (95)
print(type(single_score))

record = ("小明", 88)
record = ("小明", 90)