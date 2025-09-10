# a= open("chapter 9/file4.txt")    #readlines function
# lines=a.readlines()
# print(lines,type(lines))
# a.close()


# a= open("chapter 9/file4.txt")      #readline function
# line1=a.readline()
# print(line1,type(line1))

# line2=a.readline()
# print(line2,type(line2))

# line3=a.readline()
# print(line3,type(line3))

# line4=a.readline()
# print(line4=="")

# a.close()


a= open("chapter 9/file4.txt")      #readline function using while loop
line=a.readline()
while(line!=""):
    print(line)
    line=a.readline()
a.close()



