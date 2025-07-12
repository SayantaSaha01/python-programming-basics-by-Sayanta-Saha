# Write a program to read the text from a given file ‘poems.txt’ and find out 
# whether it contains the word ‘twinkle’. 

f=open("chapter 9 practice set/poems.txt")
words=f.read()
if("twinkle" in words):
    print("twinkle is present")
else:
    print("twinkle is not present")

f.close()
