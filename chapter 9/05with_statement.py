f = open("chapter 9/file4.txt")
print(f.read())
f.close()

#The same thing is done without close fuction using with statement

with open("chapter 9/file4.txt")as f:
    print(f.read())  # when you step out of  with indentation its automatically close the file


