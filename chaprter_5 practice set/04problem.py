# What will be the length of following set s: 
# s = set() 
# s.add(20) 
# s.add(20.0) 
# s.add('20')  , length of s after these operations? 
s= set() 
s.add(20) 
s.add(20.0) # here in python 20 and 20.0 is equal so 
s.add('20')

b=len(s)
print(b)

# output
# 2