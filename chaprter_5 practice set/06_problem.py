# Create an empty dictionary. Allow 4 friends to enter their favorite language as 
# value and use key as their names. Assume that the names are unique. 

a = {}

name= input("enter the friend's name : ")
lang=input("enter the language : ")
a.update({name:lang})                   # its a syntax of taking value  in key and value in dictionary

name= input("enter the friend's name : ")
lang=input("enter the language : ")
a.update({name:lang})

name= input("enter the friend's name : ")
lang=input("enter the language : ")
a.update({name:lang})

name= input("enter the friend's name : ")
lang=input("enter the language : ")
a.update({name:lang})
print(a)

# output
# enter the friend's name : sayanta
# enter the language : python
# enter the friend's name : arka
# enter the language : java
# enter the friend's name : arindam
# enter the language : c
# enter the friend's name : puspendu
# enter the language : java
# {'sayanta': 'python', 'arka': 'java', 'arindam': 'c', 'puspendu': 'java'}
