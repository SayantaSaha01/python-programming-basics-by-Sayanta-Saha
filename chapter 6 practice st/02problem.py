# Write a program to find out whether a student has passed or failed if it requires a 
# total of 40% and at least 33% in each subject to pass. Assume 3 subjects and 
# take marks as an input from the user

subject1=int(input("enter the marks1 : "))
subject2=int(input("enter the marks2 : "))
subject3=int(input("enter the marks3 : "))
total_percentage= (subject1+subject2+subject3)/300 *(100)

if (total_percentage>=40 and subject1>=33 and subject2>=33 and subject3>=33):
    print("you are pass now",total_percentage)
else:
    print("you are failed now",total_percentage)