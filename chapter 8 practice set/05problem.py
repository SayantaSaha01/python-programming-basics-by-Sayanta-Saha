# Write a python function to print first n lines of the following pattern: 
# *** 
# **               
# * 

# n= int(input("enter the value : "))
# def pattern(n):
#     if n==0:
#         return ("")
#     else:
#          print(n*"*")
#          pattern(n-1)  #its recursive call

# pattern(n)

n= int(input("enter the value : "))

for i in range(n,0,-1):
    print (i*"*")
