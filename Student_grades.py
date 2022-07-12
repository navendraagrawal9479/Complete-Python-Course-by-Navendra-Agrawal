student_marks = {
    "name1": 89,
    "name2": 76,
    "name3": 65,
    "name4":90
}
# 90-100 - A
# 80-89 - B
# 70-79 - C
# below 70 - Fail
student_grades = {}
for name in student_marks:
    marks = student_marks[name]
    if marks>=90:
        student_grades[name] = "A"
    elif marks>=80:
        student_grades[name] = "B"
    elif marks>=70:
        student_grades[name] = "C"
    else:
        student_grades[name] = "FAIL"

print(student_grades)