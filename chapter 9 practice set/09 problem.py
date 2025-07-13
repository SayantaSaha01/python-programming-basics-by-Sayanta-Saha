# Write a program to find out whether a file is identical & matches the content of 
# another file. 

                         #EX-1
with open("chapter 9 practice set/log.txt") as f:
    content1=f.read()

with open("chapter 9 practice set/this_1.txt") as f:
    content2=f.read()

if(content1==content2):
    print("yes both file is identical")
else:
    print("no both file is not identical")

                       #EX-2

with open("chapter 9 practice set/this.txt") as f:
    content1=f.read()

with open("chapter 9 practice set/this_1.txt") as f:
    content2=f.read()

if(content1==content2):
    print("yes both file is identical")
else:
    print("no both file is not identical")

    

    