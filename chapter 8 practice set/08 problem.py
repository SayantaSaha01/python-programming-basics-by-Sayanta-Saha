# Write a python function to print multiplication table of a given number.


                    #   EX-1
n= int(input("enter the number : "))
def multipicationtable():
    for i in range(1,11):
        print(f"{n}X{i} is : {(n*i)}")

multipicationtable()


                            #EX-2


def multipicationtable(n):
    for i in range(1,11):
        print(f"{n}X{i} is : {(n*i)}")

multipicationtable(5)








