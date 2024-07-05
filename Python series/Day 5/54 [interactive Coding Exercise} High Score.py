student_scores=input("Enter Numbers ").split()
for n in range(0,len(student_scores)):
    student_scores[n]=int(student_scores[n])

hight_score=0
for score in student_scores:
    if score>hight_score:
       hight_score=score    
print(f"The highest score in the class is : {hight_score}")