# Write a program to find out whether a given post is talking about “Harry” or not. 

post = input("enter the post: ")

if("Harry".lower() in post.lower()):
    print("its talking about 'Harry'")
else:
    print("its not talking about 'Harry'")