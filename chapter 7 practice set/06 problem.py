# Write a program to calculate the factorial of a given number using for loop.

n = int(input("enter the number : "))

i=1
product=1
for i in range(i,n+1):
    # product=product*i
    product*=i
    i+=1
print(f"the factorial of{n} is : {product}")