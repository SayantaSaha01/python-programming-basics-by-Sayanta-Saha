# Write a python program to rename a file to “renamed_by_ python.txt. 
with open("chapter 9 practice set/old.txt") as f:
    content=f.read()
with open("chapter 9 practice set/new.txt","w") as f:
    f.write(content)
   