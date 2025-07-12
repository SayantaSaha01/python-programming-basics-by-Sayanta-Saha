# Write a program using functions to find greatest of three numbers.

#              EX-1
# a=[]
# a1=int(input("enter the number :"))
# a.append(a1)
# a2=int(input("enter the number :"))
# a.append(a2)
# a3=int(input("enter the number :"))
# a.append(a3)
# def gn():
#     a.sort()
#     greatest=a[2]
#     print(f"the greaters number of{a}is : {greatest}")

# gn()

#                     ex-2

a= int(input("enter the number : "))
b= int(input("enter the number : "))
c= int(input("enter the number : "))


def GN():
    if(a>b and a>c):
        return a
    elif(b>a and b>c):
        return b
    elif(c>b and c>a):
        return c
   

d=GN()
print(f"the greatest number is : {d}")


