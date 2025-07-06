# Write a program to print multiplication table of a given number using for loop.

t= int(input("enter the number: "))
for i in range(1,11):
    print(f"{t}x{i}={t*i}")

          #both are correct 

v= int(input("enter the number: "))
i=1
while(i<11):
    print(f"{v}x{i}={v*i}")
    i+=1

    
