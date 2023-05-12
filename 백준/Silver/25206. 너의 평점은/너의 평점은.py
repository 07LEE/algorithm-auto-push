grade_to_point = {'A+': 4.5, 'A0': 4.0, 'B+': 3.5, 'B0': 3.0, 'C+': 2.5, 'C0': 2.0, 'D+': 1.5, 'D0': 1.0, 'F': 0.0}

total_credit = 0
total_weighted_grade = 0

for i in range(20):
    subject, credit, grade = input().split()
    credit = float(credit)
    if grade == 'P':
        continue
    total_credit += credit
    total_weighted_grade += credit * grade_to_point[grade]

gpa = total_weighted_grade / total_credit
print('%.4f' % gpa)