#  Write a program to find whether a given username contains less than 10 
# characters or not.

username=input("enter your user name: ")
# length_username=len(username)
# if(length_username<10):
if(len(username)<10):
    print("not valid")
else:
    print("its valid")
