students_height=input().split()
for n in range(0,len(students_height)):
    students_height[n]=int(students_height[n])
total_height=0
for height in students_height:
    total_height +=height
print(f"total height = {total_height} ")

number_students=0
for student in students_height:
    number_students +=1
print(f"total student = {number_students} ")
   
average_height=round(total_height/number_students)
print(f" average height = {average_height}")
   