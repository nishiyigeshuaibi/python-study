from student_service import update_score


def test_update_score_zero():
    students = [{"name": "小明", "score": 88}]
    success = update_score(students, "小明", 0)

    assert success is True
    assert students[0]["score"] == 0


def test_update_score_too_high():
    students = [{"name": "小明", "score": 88}]
    success = update_score(students, "小明", 120)

    assert success is False
    assert students[0]["score"] == 88


def test_update_score_student_not_found():
    students = [{"name": "小明", "score": 88}]
    success = update_score(students, "小李", 95)

    assert success is False
    assert students == [{"name": "小明", "score": 88}]


def test_update_score_hundred():
    students = [{"name": "小明", "score": 88}]
    success = update_score(students, "小明", 100)

    assert success is True
    assert students[0]["score"] == 100


def test_update_score_negative():
    students = [{"name": "小明", "score": 88}]
    success = update_score(students, "小明", -1)

    assert success is False
    assert students[0]["score"] == 88


test_update_score_zero()
test_update_score_too_high()
test_update_score_student_not_found()
test_update_score_hundred()
test_update_score_negative()
print("全部检查通过")