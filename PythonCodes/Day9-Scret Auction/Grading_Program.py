student_scores = {
    'Harry': 88,
    'Ron': 78,
    'Hermione': 95,
    'Draco': 75,
    'Neville': 60
}

student_grades ={
    
}
#print(student_scores["Harry"])
for name in student_scores:
    #print(name)
    #print(student_scores[name])
    if student_scores[name]>=91:
        student_grades[name]= "Outstanding" 
    elif student_scores[name]>=81 and student_scores[name]<=90:
        student_grades[name]= "Exceeds Expectations" 
    elif student_scores[name]>=71 and student_scores[name]<=80:
        student_grades[name]= "Acceptable" 
    elif student_scores[name]<=70:
        student_grades[name]= "Fail" 

    #student_grades[name]= student_scores[name]
print(student_grades)