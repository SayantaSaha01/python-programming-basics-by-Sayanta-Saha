# 3. Write a program to detect double space in a string.
a="sayanta is  a boss"
print(a.find("  "))  # its a method which use to search data by giving starting index value

b="sayanta is a boss"
print(b.find("  "))  # if funtion does not find any data which we ask , then it give -1 value

#bonous example
c="sayanta is a boss"
print(c.find("bo")) 

#output
# 10
# -1
# 13

