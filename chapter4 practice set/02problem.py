#Write a program to accept marks of 6 students and display them in a sorted manner

marks =[]

f1=int(input("enter your marks ="))
marks.append(f1)
f2=int(input("enter your marks ="))
marks.append(f2)
f3=int(input("enter your marks ="))
marks.append(f3)
f4=int(input("enter your marks ="))
marks.append(f4)
f5=int(input("enter your marks ="))
marks.append(f5)
f6=int(input("enter your marks ="))
marks.append(f6)
f7=int(input("enter your marks ="))
marks.append(f7)

marks.sort()

print(marks)

# output
# enter your marks =12
# enter your marks =43
# enter your marks =54
# enter your marks =32
# enter your marks =65
# enter your marks =67
# enter your marks =90
# [12, 32, 43, 54, 65, 67, 90]
