
#                        ex-1
# def factorial1(n):
#     if(n==1 or n==0):
#         return 1
#     else:
#         return n*factorial1(n-1)
# n=int(input("enter the value: "))
# print(f"the factorial of {n} is : {factorial1(n)}")

#                         ex-2

n=int(input("enter the value: "))

def factorial1(n):   # (n) parenthesis ke andar n diya because recursion me har bar n ki value alag hai isliye ye yha pe dena zarori hai.
    if(n==1 or n==0):
        return 1
    else:
        return n*factorial1(n-1)
print(f"the factorial of {n} is : {factorial1(n)}")


a= factorial1(n)






