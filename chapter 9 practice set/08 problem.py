# Write a program to make a copy of a text file “this. txt”

with open("chapter 9 practice set/this.txt") as f:
    content=f.read()
    content=(content)

with open("chapter 9 practice set/this_1.txt","w") as f:
    f.write(content)
    