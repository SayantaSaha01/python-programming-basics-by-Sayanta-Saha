# A file contains a word “Donkey” multiple times. You need to write a program 
# which replace this word with ##### by updating the same file.  

with open("chapter 9 practice set/poems.txt") as f:
    content=f.read()
newcontent=content.replace("Donkey","genious")

with open("chapter 9 practice set/poems.txt","w") as f:
    f.write(newcontent)

