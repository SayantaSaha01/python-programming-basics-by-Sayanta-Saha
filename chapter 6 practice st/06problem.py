# Write a program to calculate the grade of a student from his marks from the 
# following scheme: 
# 90 – 100 => Ex 
# 80 – 90 => A 
# 70 – 80 => B 
# 60 – 70  =>C 
# 50 – 60 => D 
# <50        
# => F 

marks1= int(input("enter the marks: "))

if(marks1<=100 and marks1>=90):
    grade = "Ex"
elif(marks1<90 and marks1>=80):
    grade = "a"
elif(marks1<80 and marks1>=70):
    grade = "b"
elif(marks1<=0 and marks1>=60):
    grade = "c"
elif(marks1<60 and marks1>=50):
    grade = "d"
elif(marks1<50):
    grade = "F"

print("your grade is: " ,grade)

