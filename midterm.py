import json

with open('sample-data.json', 'r', encoding='utf-8') as file:
    data = json.load(file) 

## filter ##
filtered_data = list(filter(lambda x: x['department_code'] == 2110, data))


## Map ##
mapped_data = list(map(lambda x: (x['student_id'], x['grade_point']), filtered_data))

##reduce##
students = {}
for student_id, grade in mapped_data:
    if student_id not in students:
        students[student_id] = []
    students[student_id].append(grade)

average_grades = {}
for student, grades in students.items():
    total = 0
    for grade in grades:
        total += grade
    average_grades[student] = total / len(grades)

print('Answers ===>',average_grades)
