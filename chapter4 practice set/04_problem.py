#Write a program to sum a list with 4 numbers. 

a=[]
a1=int(input("enter the value :"))
a.append(a1)
a2=int(input("enter the value :"))
a.append(a2)
a3=int(input("enter the value :"))
a.append(a3)
a4=int(input("enter the value :"))
a.append(a4)

b=(a1+a2+a3+a4)
print(b)

print(sum(a))  #here sum is  function , upper and this both are correct but this is more efficient to use

# output
# enter the value :3
# enter the value :3
# enter the value :3
# enter the value :3
# 12
# 12