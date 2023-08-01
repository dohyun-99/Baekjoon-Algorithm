total_grade, total_credit = 0, 0
grade_credit={'A+': 4.5 ,'A0':4,'B+':3.5,'B0':3,'C+':2.5,'C0':2.0,'D+':1.5,'D0':1,'F':0}

for i in range(20):
    subject, credit, grade = map(str,input().split())
    if grade == 'P':
        pass
    else:
        total_grade += float(credit) * grade_credit[grade]
        total_credit+= float(credit)

print(total_grade/total_credit)